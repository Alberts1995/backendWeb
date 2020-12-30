import pymysql.cursors
import time
import datetime
import requests
from pymysql.constants import CLIENT



class SQLite(object):
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
            
    def del_segmentaciya(self, date):
        sql = f"""DELETE FROM Segmentaciya WHERE date = '{date}' """
        self.cursor.execute(sql)


    def insert_segmentaciya(self, affilate, category, offer, advertiser, country, confirmed, pending, hold,  scheme, date):
        sql = """INSERT INTO Segmentaciya (affilate, category, offer, advertiser, country, confirmed, pending, hold,  scheme, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (affilate, category, offer, advertiser, country, confirmed, pending, hold,  scheme, date)
        self.cursor.execute(sql, values)

    def select_information(self, date_from, data_to):
        sql = f"""SELECT affilate, category, offer, advertiser, country, revenue, scheme, date FROM Segmentaciya WHERE date between '{date_from}' and '{data_to}'"""
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        row = [i for i in rows]
        return row


