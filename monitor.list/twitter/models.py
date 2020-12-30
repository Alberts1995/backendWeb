from django.contrib.auth.models import User
from django.db import models
import pymysql.cursors
from pymysql.constants import CLIENT
import time
import pymysql


class Message(models.Model):
    text = models.CharField(max_length=64, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)



class SQLite(models.Model):
    def __init__(self):
        self.connect()
    def connect(self):
        try:
            self.connection = pymysql.connect(host='127.0.0.1',
                                                      port=8000,
                                                      user='user',
                                                      password='password',
                                                      db='db', 
                                                      autocommit=True, 
                                                      client_flag = CLIENT.MULTI_STATEMENTS)
            self.cursor = self.connection.cursor()
        except Exception as e:
            print("WARNING\n", e)
            time.sleep(5)
            self.connect()

    def insert_day(self, new, reckl, offer, plan_day, gross, morja, scheme):
        sql = """INSERT INTO Day (new, reckl, offer, plan_day, gross, morja, scheme) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        values = (new, reckl, offer, plan_day, gross, morja, scheme)
        self.cursor.execute(sql, values)
        

    def insert_month(self, new, reckl, offer, plan_month, gross, morja, scheme):
        sql = """INSERT INTO Month (new, reckl, offer, plan_month, gross, morja, scheme) VALUES (?, ?, ?, ?, ?, ?, ?)"""
        values = (new, reckl, offer, plan_month, gross, morja, scheme)
        self.cursor.execute(sql, values)
        

    def plan_month(self, Month_Plan_FB, Month_Total_Merjinalnost_FB, Month_Total_Gross_FB, Month_Plan_sxema, Month_Total_Merjinalnost_sxema, Month_Total_Gross_sxema, month_Plan_prochee, Month_Total_Merjinalnost_prochee, Month_Total_Gross_prochee):
        sql = """INSERT INTO Month_total (Month_Plan_FB, Month_Total_Merjinalnost_FB, Month_Total_Gross_FB, 
            Month_Plan_sxema, Month_Total_Merjinalnost_sxema, Month_Total_Gross_sxema, month_Plan_prochee, 
            Month_Total_Merjinalnost_prochee, Month_Total_Gross_prochee) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        values = (Month_Plan_FB, Month_Total_Merjinalnost_FB, Month_Total_Gross_FB, Month_Plan_sxema, Month_Total_Merjinalnost_sxema, Month_Total_Gross_sxema, month_Plan_prochee, Month_Total_Merjinalnost_prochee, Month_Total_Gross_prochee)
        self.cursor.execute(sql, values)
        

    def plan_day(self, Day_Plan_prochee, Day_Total_Merjinalnost_FB, Day_Total_Gross_FB, Day_Plan_FB, Day_Total_Merjinalnost_Sxema, Day_Total_Gross_Sxema, Day_Plan_sxema, Day_Total_Merjinalnost_prochee, Day_Total_Gross_prochee):
        sql = """INSERT INTO Day_total (Day_Plan_prochee, Day_Total_Merjinalnost_FB, Day_Total_Gross_FB, 
        Day_Plan_FB, Day_Total_Merjinalnost_Sxema, Day_Total_Gross_Sxema, Day_Plan_sxema, Day_Total_Merjinalnost_prochee,
        Day_Total_Gross_prochee) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        values = (Day_Plan_prochee, Day_Total_Merjinalnost_FB, Day_Total_Gross_FB, Day_Plan_FB, Day_Total_Merjinalnost_Sxema, Day_Total_Gross_Sxema, Day_Plan_sxema, Day_Total_Merjinalnost_prochee, Day_Total_Gross_prochee)
        self.cursor.execute(sql, values)
        

    def update_table(self, reckl, gross, morja, table, scheme):
        sql = """UPDATE {3} SET gross = '{1:s}', morja = '{2:s}' WHERE reckl='{0:s}' AND scheme = '{4:s}'
               """.format(reckl,  gross, morja, table, scheme)
        self.cursor.execute(sql)


    def update_month(self, Month_Plan_FB, Month_Total_Merjinalnost_FB, Month_Total_Gross_FB, Month_Plan_sxema, Month_Total_Merjinalnost_sxema, Month_Total_Gross_sxema, month_Plan_prochee, Month_Total_Merjinalnost_prochee, Month_Total_Gross_prochee):
        sql = """UPDATE Month_total SET Month_Plan_FB = '{0:s}', Month_Total_Merjinalnost_FB = '{1:s}', Month_Total_Gross_FB = '{2:s}', 
        Month_Plan_sxema = '{3:s}', Month_Total_Merjinalnost_sxema = '{4:s}', Month_Total_Gross_sxema = '{5:s}', month_Plan_prochee = '{6:s}', 
        Month_Total_Merjinalnost_prochee = '{7:s}', Month_Total_Gross_prochee = '{8:s}' WHERE id=12
            """.format(str(Month_Plan_FB), str(Month_Total_Merjinalnost_FB), str(Month_Total_Gross_FB), str(Month_Plan_sxema), str(Month_Total_Merjinalnost_sxema), str(Month_Total_Gross_sxema), str(month_Plan_prochee), str(Month_Total_Merjinalnost_prochee), str(Month_Total_Gross_prochee))
        self.cursor.execute(sql)


    def update_day(self, Day_Plan_prochee, Day_Total_Merjinalnost_FB, Day_Total_Gross_FB, Day_Plan_FB, Day_Total_Merjinalnost_Sxema, Day_Total_Gross_Sxema, Day_Plan_sxema, Day_Total_Merjinalnost_prochee, Day_Total_Gross_prochee):
        sql = """UPDATE Day_total SET Day_Plan_prochee = '{0:s}', Day_Total_Merjinalnost_FB = '{1:s}', Day_Total_Gross_FB = '{2:s}', 
        Day_Plan_FB = '{3:s}', Day_Total_Merjinalnost_Sxema = '{4:s}', Day_Total_Gross_Sxema = '{5:s}', Day_Plan_sxema = '{6:s}', 
        Day_Total_Merjinalnost_prochee = '{7:s}', Day_Total_Gross_prochee = '{8:s}' WHERE id=4
               """.format(str(Day_Plan_prochee), str(Day_Total_Merjinalnost_FB), str(Day_Total_Gross_FB), str(Day_Plan_FB), str(Day_Total_Merjinalnost_Sxema), str(Day_Total_Gross_Sxema), str(Day_Plan_sxema), str(Day_Total_Merjinalnost_prochee), str(Day_Total_Gross_prochee))
        self.cursor.execute(sql)



    def check_day(self):
        sql = """SELECT new, reckl, offer, plan_day, morja, gross   FROM Day WHERE scheme='FB'"""
        sql2 = """SELECT new, reckl, offer, plan_day, morja, gross FROM Day WHERE scheme='scheme'"""
        sql_total = """SELECT Day_Plan_FB, Day_Total_Merjinalnost_FB, Day_Total_Gross_FB, 
                        Day_Plan_sxema, Day_Total_Merjinalnost_Sxema, Day_Total_Gross_Sxema, 
                        Day_Plan_prochee, Day_Total_Merjinalnost_prochee, Day_Total_Gross_prochee FROM Day_total """
        sql_total_month = """SELECT Month_Plan_FB, Month_Total_Merjinalnost_FB, Month_Total_Gross_FB, 
                        Month_Plan_sxema, Month_Total_Merjinalnost_sxema, Month_Total_Gross_sxema, 
                        month_Plan_prochee, Month_Total_Merjinalnost_prochee, Month_Total_Gross_prochee FROM Month_total """
        sql3 = """SELECT new, reckl, offer, plan_month, morja, gross FROM Month WHERE scheme='FB'"""
        sql4 = """SELECT new, reckl, offer, plan_month, morja, gross FROM Month WHERE scheme='scheme'"""
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        Total_Day = {}
        day = {'FB': [], 'scheme':[], "other": "0", "Total": []}
        Month = {'FB': [], 'scheme':[], "other": "0", "Total": []}
        
        indexs_total = ["Day_Plan_FB", "Day_Total_Merjinalnost_FB", "Day_Total_Gross_FB", 
                        "Day_Plan_sxema", "Day_Total_Merjinalnost_Sxema", "Day_Total_Gross_Sxema", 
                        "Day_Plan_prochee", "Day_Total_Merjinalnost_prochee","Day_Total_Gross_prochee"]
        indexs_total_month = ["Month_Plan_FB", "Month_Total_Merjinalnost_FB", "Month_Total_Gross_FB", 
                        "Month_Plan_sxema", "Month_Total_Merjinalnost_sxema", "Month_Total_Gross_sxema", 
                        "month_Plan_prochee", "Month_Total_Merjinalnost_prochee","Month_Total_Gross_prochee"]
                        
        indexs = ["new", "reckl", "offer", "plan_day", "morja", "gross"]
        indexs_month = ["new", "reckl", "offer", "plan_month", "morja", "gross"]
        Total_fb = {}
        Total_sxema = {}
        Total_prochee = {}
        Total_month_fb = {}
        Total_month_sxema = {}
        Total_month_prochee = {}

        for row in rows:
            day["FB"].append({indexs[i]:y for i, y in enumerate(row)})
        self.cursor.execute(sql2)
        rows = self.cursor.fetchall()

        for row in rows:
            day["scheme"].append({indexs[i]:y for i, y in enumerate(row)})
        self.cursor.execute(sql_total)
        rows = self.cursor.fetchall()

        for row in rows:
            for i, y in enumerate(row[0:3]):
                Total_fb[indexs_total[i]]=y
            for i, y in enumerate(row[3:6], 3):
                Total_sxema[indexs_total[i]]=y
            for i, y in enumerate(row[6:9], 6):
                Total_prochee[indexs_total[i]]=y
            day["Total"].append(Total_fb)
            day["Total"].append(Total_sxema)
            day["Total"].append(Total_prochee)

        self.cursor.execute(sql_total_month)
        rows = self.cursor.fetchall()

        for row in rows:
            for i, y in enumerate(row[0:3]):
                Total_month_fb[indexs_total_month[i]]=y
            for i, y in enumerate(row[3:6], 3):
                Total_month_sxema[indexs_total_month[i]]=y
            for i, y in enumerate(row[6:9], 6):
                Total_month_prochee[indexs_total_month[i]]=y
            Month["Total"].append(Total_month_fb)
            Month["Total"].append(Total_month_sxema)
            Month["Total"].append(Total_month_prochee)


        self.cursor.execute(sql3)
        rows = self.cursor.fetchall()
        for row in rows:
            Month["FB"].append({indexs_month[i]:y for i, y in enumerate(row)})
            
        self.cursor.execute(sql4)
        rows = self.cursor.fetchall()
        
        for row in rows:
            Month["scheme"].append({indexs_month[i]:y for i, y in enumerate(row)})

        Total_Day["TotalInformation_month"] = Month
        Total_Day["Total_Day"] = day
        Al = ["Total_Day", "TotalInformation_month"]
        FB = ["FB", "scheme"]
        for z in Al:
            for i in FB:
                for y in Total_Day[z][i]:
                    ad = y["offer"].split(", ")
                    if len(ad) > 1:
                        ad = [int(x) for x in ad]
                    else:
                        ad = int(ad[0])
                    y["offer"] = ad
        return Total_Day
        
