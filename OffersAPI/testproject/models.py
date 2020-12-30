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

class SQLite():
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

    def insert_segmentaciya(self, affilate, category, offer, advertiser, country, revenue, scheme, date):
        sql = """INSERT INTO Segmentaciya (affilate, category, offer, advertiser, country, revenue, scheme, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
        values = (affilate, category, offer, advertiser, country, revenue, scheme, date)
        self.cursor.execute(sql, values)


    def select_information(self, date_from, data_to):
        sql = f"""SELECT affilate, category, offer, advertiser, country, confirmed, pending, hold,  scheme, date FROM Segmentaciya WHERE date between '{date_from}' and '{data_to}'"""
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        row = [i for i in rows]
        return row




# if  __name__ == "__main__":
#     SQLite().select_information("2020-04-04", "2020-04-05")
        


 
