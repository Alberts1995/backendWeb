from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g, redirect, make_response, session
import sqlite3
import os
from db_flask import FDataBase
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from UserLogin import UserLogin
from forms import LoginForm, RegisterForm
from admin.admin import admin




DATABASE = "flask_tutorial/tutorial_flask.sql"
DEBUG = True
MAX_CONTENT_LENGHT = 1024 * 1024

app = Flask(__name__)
app.config.from_object(__name__) 
app.permanent_session_lifetime = datetime.timedelta(days = 10)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "tutorial_flask.sql")))
app.register_blueprint(admin, url_prefix="/admin")
app.config['SECRET_KEY'] = "SECRET_KEY"

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = "Авторизуйтесь для доступа к закрытым страницам"
login_manager.login_message_category = "success"

#data = [1,2,3,4]


menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}
        ]

#BD
def connect_db():
    conn = sqlite3.connect(app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


def creat_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


dbase = None
@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)


# read Post
@app.route("/post/<alias>")
@login_required
def showPost(alias):
    title, post = dbase.getPost(alias)[0]
    #post = dbase.getPost(id_post)[0][1]
    if not title:
        abort(404)

    return render_template('post.html', menu = dbase.getMenu(), title=title, post = post)


#session
# @app.route("/")
# def index():
#     if "visits" in session:
#         session['visits'] = session.get('visits') +1
#     else:
#         session['visits'] = 1
#     return f"<h1>Main Page </h1><p>Число просмотров: {session['visits']}"


# @app.route('/session')
# def session_data():
#     session.permanent = True
#     if "data" not in session:
#         session['data'] = data
#     else:
#         session["data"][1] += 1
#         session.modified = True

#     return f"<p> session['data']: {session['data']}"


#cookies
# @app.route("/login", methods=["POST", "GET"])
# def login():
#     log = ""
#     if request.cookies.get('logged'):
#         log = request.cookies.get('logged')
#     res = make_response(f"<h1>Форма авторизации</h1><p>logged: {log}")
#     res.set_cookie('logged', "yes", 30*24*3600)
#     return res

# @app.route("/logout")
# def logout():
#     res = make_response(f"<p> Вы больше не авторизованы! </p>")
#     res.set_cookie('logged', "", 0)
#     return res


@app.route("/")
def index():
    return render_template("index.html", menu=dbase.getMenu(), posts = dbase.getPostAnonce())


@app.route("/about")
def about():
    return render_template("about.html", menu=dbase.getMenu(), title = "О сайте")



@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form["username"]) >2:
            flash("Сообщение отправлено", category="success")
        else:
            flash("Ошибка отправки", category="error")
    return render_template("contact.html", menu=menu, title = "Обратная связь")


# avtorization
@login_manager.user_loader
def load_user(user_id):
    return UserLogin().fromDB(user_id, dbase)


@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = dbase.GetUserByEmail(form.email.data)
        if user[0] and check_password_hash(user[0]['psw'], form.psw.data):
            userlogin = UserLogin().creater(user[0])
            rm = form.remember.data
            login_user(userlogin, remember=rm)
            return redirect(request.args.get('next') or url_for('profile'))

        flash('Неверный логин/пароль', "error")
    return render_template('login.html', menu=dbase.getMenu(), title= "Авторизация", form=form)
    
    #     user = dbase.GetUserByEmail(request.form['email'])
    #     if user[0] and check_password_hash(user[0]['psw'], request.form['psw']):
    #         userlogin = UserLogin().creater(user[0])
    #         rm = True if request.form.get('remainme') else False
    #         login_user(userlogin, remember=rm)
    #         return redirect(request.args.get('next') or url_for('index'))

    # return render_template('login.html', title = "Авторизация", menu=dbase.getMenu()) 


# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if 'userLogged' in session:
#         return redirect(url_for('profile', username=session['userLogged']))
#     elif request.method == "POST" and request.form['username'] == 'selfedu' and request.form['psw'] == '123':
#         session['userLogged'] = request.form['username']
#         return redirect(url_for("profile", username = session['userLogged']))

#     return render_template('login.html', title = "Авторизация", menu=dbase.getMenu()) 



# @app.route("/profile/<username>")
# def profile(username):
#     if 'userLogged' not in session or session['userLogged'] != username:
#         abort(401)
#     return render_template("login.html", menu=dbase.getMenu(), title = "Авторизация")


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hash = generate_password_hash(form.psw.data)
        res = dbase.addUser(form.name.data, form.email.data, hash)
        if res:
            flash("Вы успешно зарегистрированы", "success")
            return redirect(url_for('login'))
        else:
            flash("Пользователь с таким данными уже существует", "error")

    return render_template("register.html", menu=dbase.getMenu(), title = "Регистарция", form=form)



#Error
@app.errorhandler(404)
def pegeNotFount(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)

# NEW POST
@app.route("/add_post", methods=["POST", "GET"])
@login_required
def addPost():
    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form["post"]) > 10:
            res = dbase.addPost(request.form["name"], request.form['post'], request.form['url'])
            if not res:
                flash("Ошибка добовления статьи", category='error')
            else:
                flash('Статья добавлена успешно', category='success')
        else:
            flash("Ошибка добовления статьи", category='error')
        return redirect(url_for('index'), 301)
    return render_template('add_post.html', menu = dbase.getMenu(), title = "Добавить статьи")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Вы вышли из аккаунта", "succcess")
    return redirect(url_for('login'))



@app.route("/profile")
@login_required
def profile():
    return render_template('profile.html', menu=dbase.getMenu(), title='Профиль')


@app.route("/userva")
@login_required
def userva():
    img =current_user.getAvatar(app)
    if not img:
        return ""

    h = make_response(img)
    h.headers["Content-Type"] = 'img/png'
    return h

@app.route("/upload", methods=["POST", "GET"])
@login_required
def upload():
    if request.method == "POST":
        files = request.files['file']
        if files and current_user.verifyExt(files.filename):
            try:
                img = files.read()
                res = dbase.updateAvatar(img, current_user.get_id())
                if not res:
                    flash("Ошибка обновления аватарки", "error")
                flash("Аватарка обновлена", "success")
            except FileNotFoundError as e:
                flash("Ошибка чтения файла", "error")
        else:
            flash("Ошибка обновления аватарки", "error")
    return redirect(url_for('profile'))
            


if __name__ == "__main__":
    app.run(debug=True)
