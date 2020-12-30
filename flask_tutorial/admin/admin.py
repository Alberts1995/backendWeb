from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g, redirect, make_response, session, Blueprint
import sqlite3

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')
menu = [{"url": '.index', 'title': "Панель"},
        {"url": '.listpubs', "title": "Список статей"},
        {"url": '.listusers', "title": "Список пользователей"},
        {"url": '.logout', "title": "Выйти"}]


db = None
@admin.before_request
def before_request():
    global db
    db = g.get('link_db')

@admin.teardown_request
def teardown_request(request):
    global db
    db = None
    return request


def login_admin():
    session['admin_logged'] = 1

def islLogged():
    return True if session.get('admin_logged') else False

def logout_admin():
    session.pop("admin_logged", None)



@admin.route('/')
def index():
    if not islLogged():
        return redirect(url_for('.login'))
    return render_template("admin/index.html", menu=menu, title="Админ-панель")



@admin.route("/login", methods=["POST", "GET"])
def login():
    if islLogged():
        return redirect(url_for('.index'))
        
    if request.method == "POST":
        if request.form['user'] == 'admin' and request.form['psw'] == "admin":
            login_admin()
            return redirect(url_for(".index"))
        else:
            flash('Неверный логин/пароль', "error")
    return render_template('admin/login.html', title="Админ-панель")


@admin.route('/logout', methods=["POST", "GET"])
def logout():
    if not islLogged():
        return redirect(url_for(".login"))

    logout_admin()

    return redirect(url_for('.login'))


@admin.route('/list-pubs')
def listpubs():
    if not islLogged():
        return redirect (url_for('.login'))
    
    lists = []
    if db:
        try:
            cur = db.cursor()
            cur.execute(f"SELECT title, text, url FROM posts")
            lists = cur.fetchall()
           
        except sqlite3.Error as e:
            print ("Ошибка получения статей иб БД " + str(e))
    return render_template("admin/listpubs.html", title='Список статей', mtnu=menu, list=lists)


@admin.route('/list-users')
def listusers():
    if not islLogged():
        return redirect (url_for('.login'))
    
    lists = []
    if db:
        try:
            cur = db.cursor()
            cur.execute(f"SELECT name, email FROM users ORDER BY time DESC")
            lists = cur.fetchall()
           
        except sqlite3.Error as e:
            print ("Ошибка получения пользователей иб БД " + str(e))
    return render_template("admin/listusers.html", title='Список пользователей', mtnu=menu, list=lists)