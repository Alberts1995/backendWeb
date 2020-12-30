from flask import Flask
import requests
from watermark import create_watermark

app = Flask(__name__)

@app.route('/sendMessage/<chat_id>/<text>/<filename>')
def hello_world(chat_id, filename, text):
    filename = filename.replace('/', '')
    f_type = filename.split('_')[-1]
    f_name = "_".join(filename.split('_')[0:-1])+ '.'+f_type
    with open(f_name, 'wb') as fi:
        fi.write(requests.get(f'http://127.0.0.1/media/{f_name}').content)
    create_watermark(text, f_name, chat_id)
    with open(f"{chat_id}.mp4", 'rb') as f:
        params = {'chat_id':chat_id}
        files = {'video':f}
        r = requests.post(f'https://api.telegram.org/bot{Token}/sendVideo', files=files, params=params)
    if r.status_code==200:
        return {'status':'ok'}
    else:
        return {'status':'error', 'code':r.status_code}
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
