from django.contrib.auth.models import User
from django.db import models
import pymysql.cursors
from pymysql.constants import CLIENT
import time
import pymysql
from djongo import models
import time
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['Monitor']
series_day = db['Day']
series_month = db['Month']
series_day_total = db['day_total ']
series_month_total = db['month_total']

class Message(models.Model):
    text = models.CharField(max_length=64, null=False, blank=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)



class Posts(models.Model):
    # insert
    def plan_month(self, collection, data):
        """ Function to insert a document into a collection and
        return the document's id.
        """
        return collection.insert_one(data).inserted_id

    def plan_day(self, collection, data):
        """ Function to insert a document into a collection and
        return the document's id.
        """
        return collection.insert_one(data).inserted_id

    def insert_day(self, collection, data):
        """ Function to insert a document into a collection and
        return the document's id.
        """
        return collection.insert_one(data).inserted_id

    def insert_month(self, collection, data):
        """ Function to insert a document into a collection and
        return the document's id.
        """
        return collection.insert_one(data).inserted_id



    #update
    def update_month(self, collection, query_elements, new_values):
        """ Function to update a single document in a collection.
        """
        collection.update_one(query_elements, {'$set': new_values})


    def update_day(self, collection, query_elements, new_values):
        """ Function to update a single document in a collection.
        """
        collection.update_one(query_elements, {'$set': new_values})

    
    def update_table(self, collection, query_elements, new_values):
        """ Function to update a single document in a collection.
        """
        collection.update_one(query_elements, {'$set': new_values})



    # Select
    def find_document_fb_day(self, collection, elements):
        """ Function to retrieve single or multiple documents from a provided
        Collection using a dictionary containing a document's elements.
        """
        results =  collection.find({"scheme": "FB"}, {"_id": 0, "data": 0, "scheme": 0})
        offer = []
        for r in results:
            offer.append({"new": r["new"], "reckl": r["reckl"], "offer": r["offer"], "plan_day": r["plan_day"], "morja": r["morja"], "gross": r["gross"]})
        
        return offer 


    def find_document_sxem_day(self, collection, elements):
        """ Function to retrieve single or multiple documents from a provided
        Collection using a dictionary containing a document's elements.
        """
        results =  collection.find({"scheme": "FB"}, {"_id": 0, "data": 0, "scheme": 0})
        offer = []
        for r in results:
            offer.append({"new": r["new"], "reckl": r["reckl"], "offer": r["offer"], "plan_day": r["plan_day"], "morja": r["morja"], "gross": r["gross"]})
        
        return offer 


    def find_document_fb_month(self, collection, elements):
        """ Function to retrieve single or multiple documents from a provided
        Collection using a dictionary containing a document's elements.
        """
        results =  collection.find({"scheme": "FB"}, {"_id": 0, "data": 0, "scheme": 0})
        offer = []
        for r in results:
            offer.append({"new": r["new"], "reckl": r["reckl"], "offer": r["offer"], "plan_month": r["plan_month"], "morja": r["morja"], "gross": r["gross"]})
        
        return offer 



    def find_document_sxem_month(self, collection, elements):
        """ Function to retrieve single or multiple documents from a provided
        Collection using a dictionary containing a document's elements.
        """
        results =  collection.find({"scheme": "FB"}, {"_id": 0, "data": 0, "scheme": 0})
        offer = []
        for r in results:
            offer.append({"new": r["new"], "reckl": r["reckl"], "offer": r["offer"], "plan_month": r["plan_month"], "morja": r["morja"], "gross": r["gross"]})
        
        return offer 


    def find_document_month(self, collection, elements):
        """ Function to retrieve single or multiple documents from a provided
        Collection using a dictionary containing a document's elements.
        """
        results =  collection.find({}, {"_id": 0})
        info_total = []
        for r in results:
            info_total.append({"Month_Plan_FB": r["Month_Plan_FB"], "Month_Total_Merjinalnost_FB": r["Month_Total_Merjinalnost_FB"], "Month_Total_Gross_FB": r["Month_Total_Gross_FB"]})
            info_total.append({"Month_Plan_Sxema": r["Month_Plan_Sxema"], "Month_Total_Merjinalnost_Sxema": r["Month_Total_Merjinalnost_Sxema"], "Month_Total_Gross_Sxema": r["Month_Total_Gross_Sxema"]})
            info_total.append({"Month_Plan_Prochee":  r["Month_Plan_Prochee"], "Month_Total_Merjinalnost_Prochee": r["Month_Total_Merjinalnost_Prochee"], "Month_Total_Gross_Prochee": r["Month_Total_Gross_Prochee"]})
        return info_total

    def find_document_day(self, collection, elements):
        """ Function to retrieve single or multiple documents from a provided
        Collection using a dictionary containing a document's elements.
        """
        results =  collection.find({}, {"_id": 0})
        info_total = []
        for r in results:
            info_total.append({"Day_plan_FB": r["Day_plan_FB"], "Day_Total_Merjinalnost_FB": r["Day_Total_Merjinalnost_FB"], "Day_Total_Gross_FB": r["Day_Total_Gross_FB"]})
            info_total.append({"Day_plan_sxema": r["Day_plan_sxema"], "Day_Total_Merjinalnost_Sxema": r["Day_Total_Merjinalnost_Sxema"], "Day_Total_Gross_Sxema": r["Day_Total_Gross_Sxema"]})
            info_total.append({"Day_plan_prochee":  r["Day_plan_prochee"], "Day_Total_Merjinalnost_prochee": r["Day_Total_Merjinalnost_prochee"], "Day_Total_Gross_prochee": r["Day_Total_Gross_prochee"]})
        return info_total



# insert
def days(day):
    day = {
        "reckl": day[1],
        "offer": day[2],
        "plan_day": day[3],
        "morja": day[5],
        "gross": day[4],
        "scheme": day[6],
        "new": day[0],
        "data": day[7],
    }

    Posts().insert_day(series_day, day)

# insert
def days_total(day_total):
    day_total = {
        "Day_plan_sxema": day_total[3],
        "Day_Total_Merjinalnost_Sxema": day_total[4], 
        "Day_Total_Gross_Sxema": day_total[5],
        "Day_plan_FB": day_total[0],
        "Day_Total_Merjinalnost_FB": day_total[1],
        "Day_Total_Gross_FB": day_total[2],
        "Day_plan_prochee": day_total[6],
        "Day_Total_Merjinalnost_prochee": day_total[7],
        "Day_Total_Gross_prochee": day_total[8],
        }
    Posts().plan_day(series_day_total, day_total)
    
# insert
def month(Month):
    Month = {
        "reckl": Month[1],
        "offer": Month[2],
        "plan_month": Month[3],
        "morja": Month[5],
        "gross": Month[4],
        "scheme": Month[6],
        "new": Month[0],
        "data": Month[7],
    }
    Posts().insert_month(series_month, Month)

# insert
def month_totoal(Month_total):
    Month_total = {
        "Month_Plan_FB": Month_total[0],
        "Month_Plan_Sxema": Month_total[3], 
        "Month_Plan_Prochee": Month_total[6],
        "Month_Total_Gross_FB": Month_total[2],
        "Month_Total_Gross_Sxema": Month_total[5],
        "Month_Total_Gross_Prochee": Month_total[8],
        "Month_Total_Merjinalnost_FB": Month_total[1],
        "Month_Total_Merjinalnost_Sxema": Month_total[4],
        "Month_Total_Merjinalnost_Prochee": Month_total[7],
        }
    Posts().plan_month(series_month_total, Month_total) 




# update
def days_total_up(day_total):
    day_total = {
        "Day_plan_sxema": day_total[0],
        "Day_Total_Merjinalnost_Sxema": day_total[1], 
        "Day_Total_Gross_Sxema": day_total[2],
        "Day_plan_FB": day_total[3],
        "Day_Total_Merjinalnost_FB": day_total[4],
        "Day_Total_Gross_FB": day_total[5],
        "Day_plan_prochee": day_total[6],
        "Day_Total_Merjinalnost_prochee": day_total[7],
        "Day_Total_Gross_prochee": day_total[8],
        }
    Posts().update_day(series_day_total, {'_id': "5fd37d58b3b662ad429afd8a"}, day_total)

# update
def month_totoal_up(Month_total):
    Month_total = {
        "Month_Plan_FB": Month_total[0],
        "Month_Plan_Sxema": Month_total[1], 
        "Month_Plan_Prochee": Month_total[2],
        "Month_Total_Gross_FB": Month_total[3],
        "Month_Total_Gross_Sxema": Month_total[4],
        "Month_Total_Gross_Prochee": Month_total[5],
        "Month_Total_Merjinalnost_FB": Month_total[6],
        "Month_Total_Merjinalnost_Sxema": Month_total[7],
        "Month_Total_Merjinalnost_Prochee": Month_total[8],
        }
    Posts().update_month(series_month_total, {'_id': "5fd37d58b3b662ad429afd89"}, Month_total) 


def update_table_up(info):
    Posts().update_table(info[3], {'$and': [{'reckl': f"{info[0]}"}, {"scheme": f"{info[4]}"}]}, {"gross": f'{info[1]}', "morja": f'{info[2]}', "data": f'{info[5]}'})
     

class Selec(models.Model):
 # Select
    def sel_fb_day(self, x):
        return Posts().find_document_fb_day(x, {})
    # Select
    def sel_sxem_day(self, x):
        return Posts().find_document_sxem_day(x, {})
    # Select
    def sel_sxem_month(self, x):
        return Posts().find_document_fb_month(x, {})

    # Select
    def sel_fb_month(self, x):
        return Posts().find_document_sxem_month(x, {})

    # Select
    def sel_month(self, x):
        return Posts().find_document_month(x, {})
    # Select
    def sel_day(self, x):
        return Posts().find_document_day(x, {})
