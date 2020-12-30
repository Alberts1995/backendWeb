import requests
import dateparser
import datetime
from  bd_segmentaciya import SQLite
import pandas as pd
import time
from datetime import  timedelta




bd = SQLite()
key_api = "key_api"

sourse = {
                155: "Схемы", 186: "Схемы", 333: "Схемы", 36: "Схемы", 140: "Схемы", 219: "Схемы", 311: "Схемы",
                237: "Схемы", 176: "Схемы", 161: "Схемы", 
                521: "Схемы", 190: "Схемы", 338: "Схемы", 47: "Схемы", 191: "Схемы", 466: "Схемы", 25: "Схемы",
                38: "Схемы", 269: "Схемы", 45: "Схемы",
                187: "Схемы", 188: "Схемы", 177: "Схемы", 309: "Схемы", 249: "Схемы", 317: "Схемы",
                400: "Схемы", 401: "Схемы", 438: "Схемы",
                231: "Схемы", 149: "Схемы", 26: "Схемы", 194: "Схемы", 315: "Схемы", 611: "Схемы", 615: "Схемы",
                618: "Схемы", 181: "Схемы", 222: "Схемы",
                276: "Схемы", 364: "Схемы", 412: "Схемы", 451: "Схемы", 270: "Схемы", 277: "Схемы",
                471: "Схемы", 637: "Схемы", 517: "Схемы", 596: "Схемы",
                598: "Схемы", 538: "Схемы", 594: "Схемы", 627: "Схемы", 198: "Fb бк", 133: "Fb бк",
                193: "Fb бк", 119: "Fb бк", 271: "Fb бк",
                371: "Fb бк", 372: "Fb бк", 117: "Fb бк", 125: "Fb бк", 329: "Fb бк", 231: "Fb бк",
                195: "Fb бк", 273: "Fb бк", 96: "Fb бк",
                157: "Fb бк", 160: "Fb бк", 192: "Fb бк", 132: "Fb бк", 275: "Fb бк", 367: "Fb бк",
                127: "Fb бк", 322: "Fb бк", 206: "Fb бк",
                373: "Fb бк", 514: "Fb бк", 272: "Fb бк", 515: "Fb бк", 477: "Fb бк", 369: "Fb бк",
                660: "Fb бк", 649: "Fb бк", 531: "Fb бк",
                13: "FB казино", 81: "FB казино", 421: "FB казино", 134: "FB казино", 182: "FB казино",
                117: "FB казино", 30: "FB казино",
                135: "FB казино", 108: "FB казино", 45: "FB казино", 330: "FB казино", 27: "FB казино",
                381: "FB казино", 297: "FB казино",
                137: "FB казино", 121: "FB казино", 79: "FB казино", 34: "FB казино", 189: "FB казино",
                181: "FB казино", 422: "FB казино",
                518: "FB казино", 551: "FB казино", 418: "FB казино", 173: "FB казино", 491: "FB казино",
                183: "FB казино", 212: "FB казино",
                280: "FB казино", 199: "FB казино", 294: "FB казино", 367: "FB казино", 128: "FB казино",
                106: "FB казино",
                484: "FB казино", 457: "FB казино", 284: "FB казино", 439: "FB казино", 490: "FB казино",
                420: "FB казино", 511: "FB казино",
                526: "FB казино", 667: "FB казино", 640: "FB казино", 118: "FB казино"
                }



class Offers():
    def off(self):

            bd.del_segmentaciya(datetime.date.today())
            date_from = f"{datetime.date.today()}"
            date_to = f"{datetime.date.today()}"


            All = []
            OfferCategoryID = []

            url = "http://api.cpanomer1.affise.com/3.0/offer/categories"

            headers = {
            'API-Key': f'{key_api}',
            'Cookie': 'PHPSESSID=2fqbh4akb83drv9iv721lriu6p'
            } 
            try:
                response = requests.get(url, headers=headers)
                json_response = response.json()
                for i in json_response['categories']:
                    OfferCategoryID.append(i)
            except:
                Offers().off()

            for categ in OfferCategoryID:
            # Get запрос с определенным offer and countries
                offers = []
                for num in range(1, 7):
                    url = f"http://api.cpanomer1.affise.com/3.0/offers?status[]=stopped&categories[]={categ['id']}&page={num}"
            
                    headers = {
                    'API-Key': f'{key_api}',
                    'Cookie': 'PHPSESSID=iojid6ella10h5tl19ibm19nrt'
                    }
                    try:
                        response = requests.request("GET", url, headers=headers)
                        json_response = response.json()
                        # Save ID offer
                        if json_response['offers'] != []:
                            off = [offer["id"] for offer in json_response['offers']]
                            offers.append(off)
                        else:
                            continue
                    # for offer in json_response['offers']:
                    #     offers.append(offer["id"])
                    except:
                        Offers().off()

                for num in range(1, 7):
                    url1 = f"http://api.cpanomer1.affise.com/3.0/offers?status[]=suspended&categories[]={categ['id']}&page={num}"
                    headers = {
                    'API-Key': f'{key_api}',
                    'Cookie': 'PHPSESSID=iojid6ella10h5tl19ibm19nrt'
                    }
                    try:    
                        response = requests.request("GET", url1, headers=headers)
                        json_response = response.json()
                        # Save ID offer
                        if json_response['offers'] != []:
                            off = [offer["id"] for offer in json_response['offers']]
                            offers.append(off)
                        else:
                            continue
                    # for offer in json_response['offers']:
                    #     offers.append(offer["id"])
                    except:
                        Offers().off()
                
                for num in range(1, 7):
                    url2 = f"http://api.cpanomer1.affise.com/3.0/offers?categories[]={categ['id']}&page={num}"
                    headers = {
                    'API-Key': f'{key_api}',
                    'Cookie': 'PHPSESSID=iojid6ella10h5tl19ibm19nrt'
                    }
                    try:
                        response = requests.request("GET", url2, headers=headers)
                        json_response = response.json()
                        # Save ID offer
                        if json_response['offers'] != []:
                            off = [offer["id"] for offer in json_response['offers']]
                            offers.append(off)
                        else:
                            continue
                        # for offer in json_response['offers']:
                        #     offers.append()
                    except:
                        Offers().off()

                for of in offers:
                    for x in of:
                        url = f"http://api.cpanomer1.affise.com/3.0/stats/custom?slice[]=year&slice[]=month&slice[]=day&slice[]=affiliate&slice[]=country&filter[nonzero]=1&filter[date_from]={date_from}&filter[date_to]={date_to}&limit=10000&order[]=pending_revenue&slice[]=offer&slice[]=advertiser&filter[offer][]={x}"
                    # for x in offers:
                    #     url = url+f"&filter[offer][]={x}"
                        headers = {
                        'API-Key': f'{key_api}',
                        'Cookie': 'PHPSESSID=t8m3cmea1i1n0e92ht1vm2f5v4'
                        }
                        try:
                            response = requests.request("GET", url, headers=headers, timeout=123)
                            json_response = response.json()

                            print([categ['title']][0])
                            stats = json_response['stats']
                            for stat in stats:
                                Category=[]
                                Confirmed = []
                                Pending = []
                                Hold = []
                                if stat["actions"]["confirmed"]["charge"] > 0 or stat["actions"]["pending"]["charge"] > 0 or stat["actions"]["hold"]["charge"] > 0 or stat["actions"]["confirmed"]["charge"] < 0 or stat["actions"]["pending"]["charge"] < 0 or stat["actions"]["hold"]["charge"] < 0:  
                                    day = stat["slice"]["day"]
                                    month = stat["slice"]["month"]
                                    year = stat["slice"]["year"]
                                    date_p = dateparser.parse(f'{year}-{month}-{day}') 
                                    Category.append([stat["slice"]["affiliate"]["id"]])
                                    Category.append([categ['title']])
                                    Category.append([stat["slice"]["offer"]["id"]])               
                                    Category.append([stat["slice"]["advertiser"]["title"]])   
                                    Category.append([stat["slice"]["country"]])
                                    Confirmed.append([stat["actions"]["confirmed"]["charge"]])
                                    Confirmed.append([stat["actions"]["confirmed"]["revenue"]])
                                    Confirmed.append([stat["actions"]["confirmed"]["earning"]])
                                    Pending.append([stat["actions"]["pending"]["charge"]])
                                    Pending.append([stat["actions"]["pending"]["revenue"]])
                                    Pending.append([stat["actions"]["pending"]["earning"]])
                                    Hold.append([stat["actions"]["hold"]["charge"]])
                                    Hold.append([stat["actions"]["hold"]["revenue"]])
                                    Hold.append([stat["actions"]["hold"]["earning"]])
                                    offer_s = [sourse[i] for i in sourse if i==stat["slice"]["offer"]["id"]]
                                    Category.append(Confirmed)
                                    Category.append(Pending)
                                    Category.append(Hold)
                                    Category.append(offer_s)
                                    Category.append(date_p)
                                    All.append(Category)
                        except:
                            Offers().off()


            print(6)
            for x in All:
                if x[8] == []:
                    c = ", ".join(str(x) for x in x[5])
                    p = ", ".join(str(x) for x in x[6])
                    h = ", ".join(str(x) for x in x[7])
                    bd.insert_segmentaciya(x[0][0], x[1][0], x[2][0], x[3][0], x[4][0], c, p, h, "", str(x[9]))

                else:
                    c = ", ".join(str(x) for x in x[5])
                    p = ", ".join(str(x) for x in x[6])
                    h = ", ".join(str(x) for x in x[7])
                    bd.insert_segmentaciya(x[0][0], x[1][0], x[2][0], x[3][0], x[4][0], c, p, h, x[8][0], str(x[9]))

    
    # def sel(self):
    #     date_to = f"{datetime.date.today()}"
    #     #series = pd.Series(bd.select_information("2019-01-01", "2019-12-31")) 
    #     series = pd.Series(bd.select_information("2020-01-01", f"{date_to}")) 
    #     df = pd.DataFrame(series)
    #     df.to_excel('2020-now.xls')

Offers().off()
