import requests
import test
import datetime
from datetime import  date
from datetime import datetime, timedelta
from pymongo import MongoClient
days = datetime.now()


client = MongoClient('127.0.0.0:27017')
db = client['Monitor']
series_day = db['Day']
series_month = db['Month']
bd = test

def get_response_url(url):
    headers = {
    'API-Key': 'API-Key'
    }
    while True:
        responce = requests.get(url, headers=headers, timeout=300)
        if responce.status_code==200:
            return responce.json()
        else:
            continue
            

class Day_merj():
    def get(self):
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "255.94"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "170.63"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "255.94"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "54.84"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "54.84"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "29.25"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "73.13"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "109.69"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "22.75"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "68.25"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "34.13"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "46"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "23"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "29.25"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "34.13"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "29"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "20"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "20"}

        Information = []
        InformationSxema = []
        Total_Day = {}

        FB = {"FB": Welcome, "FB1": Welcome, "FB5": Welcome, "FB8": Welcome, "FB9": Welcome,
            "FB2": Welcome, "FB3": Welcome, "FB4": Welcome, "FB6": Welcome, "FB7": Welcome,
            }

        Sxema = {"sxema10": Welcome, "sxema12": Welcome,

                "sxema13": Welcome, "sxema14": Welcome, "sxema16": Welcome,

                "sxema18": Welcome, "sxema19": Welcome, "sxema11": Welcome,

                }
        
        FB_all = {"FB2": Welcome, "FB3": Welcome, "FB5": Welcome, "FB6": Welcome, "FB7": Welcome}

        Sxema_all = {"sxema16": Welcome, "sxema10": Welcome, "sxema14": Welcome, "sxema19": Welcome,
                    "sxema13": Welcome}

        Day_Total_Merjinalnost_FB = 0
        Day_Total_Gross_Margin_FB = 0
        Day_Total_Merjinalnost_Sxema = 0
        Day_Total_Gross_Margin_Sxema = 0
        total_all_prochee = {"Day_Plan_prochee": "81.25"}
        total_all_FB = {"Day_Plan_FB": "325"}
        total_all_Sexma = {"Day_Plan_sxema": "853.13"}
        today = date.today()
        vulkanbet_partners = offer
        Offers = offer
        
        Welcome = offer
        Welcome = offer
        Welcome = offer
        Welcome = offer
        Welcome = offer

        Welcome = offer
        Welcome = offer
        Welcome = offer
        total = [Welcome, Welcome, Welcome, Welcome, Welcome, Welcome, Welcome,
                Welcome, Welcome]

        for x in Offers:
            url = f"http://api.cpanomer1.affise.com/3.0/stats/custom?slice[]=day&filter[date_from]={today}&filter[date_to]={today}&filter[offer][]={x}"
            json_response = get_response_url(url)

            try:
                for t, y in FB.items():
                    if y["offer"] == x:
                        offerID = json_response['stats'][-1]["actions"]["total"]
                        y["gross"] = str(offerID["charge"])
                        y["morja"] = str(offerID["earning"])
                        Information.append(y)
                        Day_Total_Merjinalnost_FB += offerID["earning"]
                        Day_Total_Gross_Margin_FB += offerID["charge"]

            except:
                if len(y) <= 4:
                    y["gross"] = "0"
                    y["morja"] = "0"
                    Information.append(y)
                    Day_Total_Merjinalnost_FB += 0
                    Day_Total_Gross_Margin_FB += 0

            try:
                for t, p in Sxema.items():
                    if p["offer"] == x:
                        offerID = json_response['stats'][-1]["actions"]["total"]
                        p["gross"] = str(offerID["charge"])
                        p["morja"] = str(offerID["earning"])
                        InformationSxema.append(p)
                        Day_Total_Merjinalnost_Sxema += offerID["earning"]
                        Day_Total_Gross_Margin_Sxema += offerID["charge"]

            except:

                if len(p) <= 4:
                    p["gross"] = "0"
                    p["morja"] = "0"
                    InformationSxema.append(p)
                    Day_Total_Merjinalnost_Sxema += 0
                    Day_Total_Gross_Margin_Sxema += 0

        for q in total:
            url = f"http://api.cpanomer1.affise.com/3.0/stats/custom?slice[]=day&filter[date_from]={today}&filter[date_to]={today}"
            for z in q:
                url = url + f"&filter[offer][]={z}"
            json_response = get_response_url(url)
            try:
                for y, t in FB_all.items():
                    for value in t["offer"]:
                        if value == z:
                            offerID = json_response['stats'][-1]["actions"]["total"]
                            t["gross"] = str(offerID["charge"])
                            t["morja"] = str(offerID["earning"])
                            Day_Total_Merjinalnost_FB += offerID["earning"]
                            Day_Total_Gross_Margin_FB += offerID["charge"]
                            Information.append(t)

            except:
                if len(t) <= 4:
                    t["gross"] = "0"
                    t["morja"] = "0"
                    Day_Total_Merjinalnost_FB += 0
                    Day_Total_Gross_Margin_FB += 0
                    Information.append(t)

            try:
                for y, t in Sxema_all.items():
                    for value in t["offer"]:
                        if value == z:
                            offerID = json_response['stats'][-1]["actions"]["total"]
                            t["gross"] = str(offerID["charge"])
                            t["morja"] = str(offerID["earning"])
                            Day_Total_Merjinalnost_Sxema += offerID["earning"]
                            Day_Total_Gross_Margin_Sxema += offerID["charge"]
                            InformationSxema.append(t)



            except:
                if len(t) <= 4:
                    t["gross"] = "0"
                    t["morja"] = "0"
                    Day_Total_Merjinalnost_Sxema += 0
                    Day_Total_Gross_Margin_Sxema += 0
                    InformationSxema.append(t)

        Morj_Gross = []
        Total_Day["FB"] = Information
        Total_Day["scheme"] = InformationSxema
        Total_Day["other"] = "0"
        Plan_All_FB = Day_Total_Merjinalnost_FB + Day_Total_Gross_Margin_FB
        Plan_All_Sxema = Day_Total_Merjinalnost_Sxema + Day_Total_Gross_Margin_Sxema
        total_all_FB["Day_Total_Merjinalnost_FB"] = Day_Total_Merjinalnost_FB
        total_all_FB["Day_Total_Gross_FB"] = Day_Total_Gross_Margin_FB
        total_all_Sexma["Day_Total_Merjinalnost_Sxema"] = round(Day_Total_Merjinalnost_Sxema, 1)
        total_all_Sexma["Day_Total_Gross_Sxema"] = round(Day_Total_Gross_Margin_Sxema, 1)
        total_all_FB["Plan_All_FB"] = Plan_All_FB
        total_all_Sexma["Plan_All_Sxema"] = round(Plan_All_Sxema, 1)
        total_all_prochee["Day_Total_Merjinalnost_prochee"] = "0"
        total_all_prochee["Day_Total_Gross_prochee"] = "0"
        Morj_Gross.append(total_all_FB)
        Morj_Gross.append(total_all_Sexma)
        Morj_Gross.append(total_all_prochee)
        Total_Day["Total"] = Morj_Gross




        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "255.94"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "170.63"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "255.94"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "54.84"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "54.84"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "29.25"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "73.13"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "109.69"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "22.75"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "68.25"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "34.13"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "46"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "23"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "29.25"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "34.13"}
        Welcome = {"new": "false", "reckl": "Welcome", "offer": offer, "plan_day": "29"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "20"}
        Welcome = {"new": "true", "reckl": "Welcome", "offer": offer, "plan_day": "20"}

        Information = []
        InformationSxema = []
        Total_Day = {}

        FB = {"FB": Welcome, "FB1": Welcome, "FB5": Welcome, "FB8": Welcome, "FB9": Welcome,
            "FB2": Welcome, "FB3": Welcome, "FB4": Welcome, "FB6": Welcome, "FB7": Welcome,
            }

        Sxema = {"sxema10": Welcome, "sxema12": Welcome,

                "sxema13": Welcome, "sxema14": Welcome, "sxema16": Welcome,

                "sxema18": Welcome, "sxema19": Welcome, "sxema11": Welcome,

                }
        
        FB_all = {"FB2": Welcome, "FB3": Welcome, "FB5": Welcome, "FB6": Welcome, "FB7": Welcome}

        Sxema_all = {"sxema16": Welcome, "sxema10": Welcome, "sxema14": Welcome, "sxema19": Welcome,
                    "sxema13": Welcome}

        Day_Total_Merjinalnost_FB = 0
        Day_Total_Gross_Margin_FB = 0
        Day_Total_Merjinalnost_Sxema = 0
        Day_Total_Gross_Margin_Sxema = 0
        total_all_prochee = {"Day_Plan_prochee": "81.25"}
        total_all_FB = {"Day_Plan_FB": "325"}
        total_all_Sexma = {"Day_Plan_sxema": "853.13"}
        today = date.today()
        vulkanbet_partners = offer
        Offers = offer
        
        Welcome = offer
        Welcome = offer
        Welcome = offer
        Welcome = offer
        Welcome = offer

        Welcome = offer
        Welcome = offer
        Welcome = offer
        total = [Welcome, Welcome, Welcome, Welcome, Welcome, Welcome, Welcome,
                Welcome, Welcome]
                
        Month_Merjinalnost = 0
        Month_Gross_Margin = 0
        Total_Merjinalnost = []
        Total_Gross_Margin = []
        Month_Total_Merjinalnost_FB = 0
        Month_Total_Gross_Margin_FB = 0
        Month_Total_Merjinalnost_sxema = 0
        Month_Total_Gross_Margin_sxema = 0
        total_all_month_FB = {"Month_Plan_FB": "9100"}
        total_all_month_sxema = {"Month_Plan_sxema": "23887.5"}
        total_all_month_prochee = {"month_Plan_prochee": "2275"}

        for x in One_Offers:
            Total_Merjinalnost.append(Month_Merjinalnost)
            Total_Gross_Margin.append(Month_Gross_Margin)
            Month_Merjinalnost = 0
            Month_Gross_Margin = 0
            Total_Merjinalnost = []
            Total_Gross_Margin = []

            url = f"http://api.cpanomer1.affise.com/3.0/stats/custom?slice[]=day&filter[date_from]={one_month}&filter[date_to]={today}&filter[offer][]={x}"
            json_response = get_response_url(url)
            try:
                for y, t in FB_month.items():
                    if t["offer"] == x:
                        for f in json_response['stats']:
                            try:
                                Month_Gross_Margin += int((f["actions"]["total"]["charge"]))
                                Month_Merjinalnost += int((f["actions"]["total"]["earning"]))
                            except:
                                Month_Gross_Margin += 0
                                Month_Merjinalnost += 0
                    if x == t["offer"]:
                        t["morja"] = str(Month_Merjinalnost)
                        t["gross"] = str(Month_Gross_Margin)
                        Information_mont.append(t)
                        Month_Total_Merjinalnost_FB += Month_Merjinalnost
                        Month_Total_Gross_Margin_FB += Month_Gross_Margin



            except:
                pass

            try:
                for y, t in Sxema_months.items():
                    if t["offer"] == x:
                        for f in json_response['stats']:
                            try:
                                Month_Gross_Margin += int((f["actions"]["total"]["charge"]))
                                Month_Merjinalnost += int((f["actions"]["total"]["earning"]))
                            except:
                                Month_Merjinalnost += 0
                                Month_Gross_Margin += 0

                    if x == t["offer"]:
                        t["morja"] = str(Month_Merjinalnost)
                        t["gross"] = str(Month_Gross_Margin)
                        InformationSxema_month.append(t)
                        Month_Total_Merjinalnost_sxema += Month_Merjinalnost
                        Month_Total_Gross_Margin_sxema += Month_Gross_Margin
            except:
                pass

        for offers in total_offers:
            Total_Merjinalnost.append(Month_Merjinalnost)
            Total_Gross_Margin.append(Month_Gross_Margin)
            Month_Merjinalnost = 0
            Month_Gross_Margin = 0
            Total_Merjinalnost = []
            Total_Gross_Margin = []
            url = f"http://api.cpanomer1.affise.com/3.0/stats/custom?slice[]=day&filter[date_from]={one_month}&filter[date_to]={today}"
            for offer in offers:
                url = url + f"&filter[offer][]={offer}"
            json_response = get_response_url(url)
            try:
                for y, t in FB_all_month.items():
                    for value in t["offer"]:
                        if value == offer:
                            for q in json_response['stats']:
                                try:
                                    Month_Gross_Margin += int((q["actions"]["total"]["charge"]))
                                    Month_Merjinalnost += int((q["actions"]["total"]["earning"]))
                                except:
                                    Month_Merjinalnost += 0
                                    Month_Gross_Margin += 0
                        if value == offer:
                            t["morja"] = str(Month_Merjinalnost)
                            t["gross"] = str(Month_Gross_Margin)
                            Information_mont.append(t)
                            Month_Total_Merjinalnost_FB += Month_Merjinalnost
                            Month_Total_Gross_Margin_FB += Month_Gross_Margin



            except:
                pass

            try:
                for y, t in Sxema_all_month.items():
                    for value in t["offer"]:
                        if value == offer:
                            for q in json_response['stats']:
                                try:
                                    Month_Gross_Margin += int((q["actions"]["total"]["charge"]))
                                    Month_Merjinalnost += int((q["actions"]["total"]["earning"]))
                                except:
                                    Month_Merjinalnost += 0
                                    Month_Gross_Margin += 0

                        if value == offer:
                            t["morja"] = str(Month_Merjinalnost)
                            t["gross"] = str(Month_Gross_Margin)
                            InformationSxema_month.append(t)
                            Month_Total_Merjinalnost_sxema += Month_Merjinalnost
                            Month_Total_Gross_Margin_sxema += Month_Gross_Margin



            except:
                pass

        Morj_gros_month = []
        TotalInformation["FB"] = Information_mont
        TotalInformation["scheme"] = InformationSxema_month
        TotalInformation["other"] = "0"
        
        total_all_month_FB["Month_Total_Merjinalnost_FB"] = round(Month_Total_Merjinalnost_FB, 1)
        total_all_month_FB["Month_Total_Gross_FB"] = round(Month_Total_Gross_Margin_FB, 1)
        total_all_month_sxema["Month_Total_Merjinalnost_sxema"] = round(Month_Total_Merjinalnost_sxema, 1)
        total_all_month_sxema["Month_Total_Gross_sxema"] = round(Month_Total_Gross_Margin_sxema, 1)
        total_all_month_prochee["Month_Total_Merjinalnost_prochee"] = "0"
        total_all_month_prochee["Month_Total_Gross_prochee"] = "0"
        Morj_gros_month.append(total_all_month_FB)
        Morj_gros_month.append(total_all_month_sxema)
        Morj_gros_month.append(total_all_month_prochee)
        TotalInformation["Total"] = Morj_gros_month
        a = {"TotalInformation_month": TotalInformation, "Total_Day": Total_Day}
        
        day = a["Total_Day"]["Total"]
        month = a["TotalInformation_month"]["Total"]


        # #Update
        # z = (month[0]['Month_Plan_FB'], month[0]["Month_Total_Merjinalnost_FB"],  month[0]["Month_Total_Gross_FB"], 
        # month[1]['Month_Plan_sxema'], month[1]["Month_Total_Merjinalnost_sxema"],  month[1]["Month_Total_Gross_sxema"],
        # month[2]['month_Plan_prochee'], month[2]["Month_Total_Merjinalnost_prochee"],  month[2]["Month_Total_Gross_prochee"])
        # bd.month_totoal_up(z)

        # b = (day[0]['Day_Plan_FB'], day[0]["Day_Total_Merjinalnost_FB"],  day[0]["Day_Total_Gross_FB"], 
        # day[1]['Day_Plan_sxema'], day[1]["Day_Total_Merjinalnost_Sxema"],  day[1]["Day_Total_Gross_Sxema"],
        # day[2]['Day_Plan_prochee'], day[2]["Day_Total_Merjinalnost_prochee"],  day[2]["Day_Total_Gross_prochee"])
        # bd.days_total_up(b)

        # day = a["Total_Day"]
        # month = a["TotalInformation_month"]

        # #Update
        # for key, value in day.items():
        #     if key == "FB":
        #         for i  in value:
        #             dayse = (i["reckl"], i["gross"], i["morja"], series_day, key, days)
        #             bd.update_table_up(dayse)
        #     elif key == "scheme":
        #         for i  in value:
        #             dayse = (i["reckl"], i["gross"], i["morja"], series_day, key, days)
        #             bd.update_table_up(dayse)

        # for key, value in month.items():
        #     if key == "FB":
        #         for i  in value:
        #             months = (i["reckl"], i["gross"], i["morja"], series_month, key, days)
        #             bd.update_table_up(months)
        #     elif key == "scheme":
        #         for i  in value:
        #             months = (i["reckl"], i["gross"], i["morja"], series_month, key, days)
        #             bd.update_table_up(months)

        #insert
        z = (month[0]['Month_Plan_FB'], month[0]["Month_Total_Merjinalnost_FB"],  month[0]["Month_Total_Gross_FB"], 
        month[1]['Month_Plan_sxema'], month[1]["Month_Total_Merjinalnost_sxema"],  month[1]["Month_Total_Gross_sxema"],
        month[2]['month_Plan_prochee'], month[2]["Month_Total_Merjinalnost_prochee"],  month[2]["Month_Total_Gross_prochee"])
        bd.month_totoal(z)
        

        b = (day[0]['Day_Plan_FB'], day[0]["Day_Total_Merjinalnost_FB"],  day[0]["Day_Total_Gross_FB"], 
        day[1]['Day_Plan_sxema'], day[1]["Day_Total_Merjinalnost_Sxema"],  day[1]["Day_Total_Gross_Sxema"],
        day[2]['Day_Plan_prochee'], day[2]["Day_Total_Merjinalnost_prochee"],  day[2]["Day_Total_Gross_prochee"])
        bd.days_total(b)

        day = a["Total_Day"]
        month = a["TotalInformation_month"]

        #insert
        for key, value in day.items():
            if key == "FB":
                for i  in value:
                    p = i["offer"]
                    if type(i["offer"]) is list:
                        p = ", ".join(str(x) for x in i["offer"])
                        day_info = (i["new"] , i["reckl"], p, i["plan_day"], i["gross"], i["morja"], key, days)
                        bd.days(day_info) 
                        continue
                    day_info = (i["new"] , i["reckl"], i["offer"], i["plan_day"], i["gross"], i["morja"], key, days)
                    bd.days(day_info) 
            elif key == "scheme":
                for i  in value:
                    p = i["offer"]
                    if type(i["offer"]) is list:
                        p = ", ".join(str(x) for x in i["offer"])
                        day_info = (i["new"] , i["reckl"], p, i["plan_day"], i["gross"], i["morja"], key, days)
                        bd.days(day_info) 
                        continue
                    day_info = (i["new"] , i["reckl"], i["offer"], i["plan_day"], i["gross"], i["morja"], key, days)
                    bd.days(day_info) 
            elif key == "other":
                day_info = (0, 0, 0, 0, 0, 0, key, days)
                bd.days(day_info) 
            

        for key, value in month.items():
            if key == "FB":
                for i  in value:
                    p = i["offer"]
                    if type(i["offer"]) is list:
                        p = ", ".join(str(x) for x in i["offer"])
                        mont_total = (i["new"] , i["reckl"], p, i["plan_month"], i["gross"], i["morja"], key, days)
                        bd.month(mont_total)
                        continue
                    mont_total = (i["new"] , i["reckl"], i["offer"], i["plan_month"], i["gross"], i["morja"], key, days)
                    bd.month(mont_total)
                    
            elif key == "scheme":
                for i  in value:
                    p = i["offer"]
                    if type(i["offer"]) is list:
                        p = ", ".join(str(x) for x in i["offer"])
                        mont_total = (i["new"] , i["reckl"], p, i["plan_month"], i["gross"], i["morja"], key, days)
                        bd.month(mont_total)
                        continue
                    mont_total = (i["new"] , i["reckl"], i["offer"], i["plan_month"], i["gross"], i["morja"], key, days)
                    bd.month(mont_total)

            elif key == "other":
                mont_total = (0, 0, 0, 0, 0, 0, key, days)
                bd.month(mont_total)
        
    def select_info(self):
        pass



Day_merj().select_info()


