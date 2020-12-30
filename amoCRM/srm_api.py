from datetime import datetime
from itertools import count
from pprint import pprint
import json
import arrow
import requests
import time

amo_domain = 'amo_domain'
# логин AmoCRM
amo_user = 'amo_user'
# ключ API
amo_key = "amo_key"

today = arrow.now().format('YYYY-MM-DD')
state = {
    'cookies': None
}


# #добавить  сделку
def new_partner():
    partner = 0
    while True:
        try:
            url = "http://api.cpanomer1.affise.com/3.0/admin/partners?page=1&limit=1"
            headers = {
            'API-Key': 'API-Key',
            'Cookie': 'PHPSESSID=er7qv5r09qg5ms9hl038turnp0'
            }
            try:
                response = requests.request("GET", url, headers=headers)
                page = response.json()['pagination']['total_count']
            except:
                print(1)
            url_par = f"http://api.cpanomer1.affise.com/3.0/admin/partners?page={page}&limit=1"
            headers = {
            'API-Key': 'API-Key',
            'Cookie': 'PHPSESSID=er7qv5r09qg5ms9hl038turnp0'
            }
            try:
                response = requests.request("GET", url_par, headers=headers)
                id_partner = response.json()
            except:
                print(2)
            if id_partner['partners'][0]['manager'] == None and partner != id_partner['partners'][0]['id']:
                partner = 0
                partner += id_partner['partners'][0]['id']
                auth(amo_user, amo_key, id_partner['partners'][0])
            else:
                pass
        except IndexError as b:
            print(b)

    
def auth(user, user_hash, info_partner):
    id_p = info_partner["id"]
    mail = info_partner["email"] 
    telega = info_partner["customFields"][0]['value']
    info = info_partner["customFields"][1]['value']
    vk = info_partner["customFields"][2]['value']
    obem = info_partner["customFields"][3]['value']
    mess = info_partner["customFields"][4]['value']
    opit = info_partner["customFields"][5]['value']

    url = amo_domain + '/private/api/auth.php'
    data = {
        'USER_LOGIN': user, 
        'USER_HASH': user_hash
    }
    res = requests.post(url, data=data, params={'type':'json'})
    print('status code', res.status_code)
    if res.status_code == 200:
        state['cookies'] = res.cookies
        pprint(res.json())
    else:
        pprint(res.json())

    json = [{"name": f"{id_p, mail, telega, info, vk, obem, mess, opit}"}]

    res1 = requests.post(amo_domain + '/api/v4/leads',  json= json, cookies=state['cookies'], verify=False)
    print(res1.status_code)
    if res1.status_code == 200:
        data = res1.json()
        pprint(data)
    else:
        data = res1.json()
        pprint(data)

new_partner()

#Менять сделку
def auth(user, user_hash):
    while True:
        url = amo_domain + '/private/api/auth.php'
        data = {
            'USER_LOGIN': user, 
            'USER_HASH': user_hash
        }
        res = requests.post(url, data=data, params={'type':'json'})
        print('status code', res.status_code)

        if res.status_code == 200:
            state['cookies'] = res.cookies

        res1 = requests.get(amo_domain + '/api/v4/leads', cookies=state['cookies'])
        id_partner = res1.json()
        for x in id_partner["_embedded"]["leads"]:
            if x['status_id'] == 36295270:
                id_par = x["id"]
                aff = x['name'].split(",")[0].split("(")[-1]
                url_aff = f"http://api.cpanomer1.affise.com/3.0/admin/partners?id[]={aff}"
                headers = {
                'API-Key': 'API-Key',
                'Cookie': 'PHPSESSID=er7qv5r09qg5ms9hl038turnp0'
                }
                try:
                    response = requests.request("GET", url_aff, headers=headers)
                    aff_info = response.json()
                except :
                    pass
                rub = (aff_info['partners'][0]['balance']["RUB"]["balance"]+ aff_info['partners'][0]['balance']["RUB"]["hold"])
                usd = ((aff_info['partners'][0]['balance']["USD"]["balance"]+ aff_info['partners'][0]['balance']["USD"]["hold"])  * 70)
                eur = ((aff_info['partners'][0]['balance']["EUR"]["balance"]+ aff_info['partners'][0]['balance']["EUR"]["hold"]) * 90)
                btc = (aff_info['partners'][0]['balance']["BTC"]["balance"]+ aff_info['partners'][0]['balance']["BTC"]["hold"])
                total_count = rub + usd + eur + btc
                total_count = str(total_count)
                count = total_count.split(".")[0]
                count = int(count)
                json = [{"id": id_par, "price": count}]
                res2 = requests.patch(amo_domain + f'/api/v4/leads', json= json, cookies=state['cookies'])
                if res2.status_code == 200:
                    data = res2.json()
                    pprint(data)
                else:
                    data = res2.json()
                    pprint(data)
        time.sleep(600)

auth(amo_user, amo_key)


# #посмотреть все сделки сделка
def auth_select(user, user_hash):
    url = amo_domain + '/private/api/auth.php'
    data = {
        'USER_LOGIN': user, 
        'USER_HASH': user_hash
    }
    res = requests.post(url, data=data, params={'type':'json'})
    print('status code', res.status_code)

    if res.status_code == 200:
        state['cookies'] = res.cookies
        pprint(res.json())
    else:
        pprint(res.json())

    res1 = requests.get(amo_domain + '/api/v4/leads?catalog_elements',  cookies=state['cookies'])
    if res1.status_code == 200:
        data = res1.json()
        pprint(data)
    else:
        data = res1.json()
        pprint(data)
auth_select(amo_user, amo_key)
