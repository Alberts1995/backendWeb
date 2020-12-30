from pymongo import MongoClient
# Create the client
client = MongoClient('127.0.0.1:27017')
# Connect to our database
db = client['Monitor']
# Fetch our series collection
series_day = db['Day']
series_month = db['Month']
series_day_total = db['day_total ']
series_month_total = db['month_total']




# insert
def plan_month(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id

def plan_day(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id

def insert_day(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id

def insert_month(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id





#update
def update_month(collection, query_elements, new_values):
    """ Function to update a single document in a collection.
    """
    collection.update_one(query_elements, {'$set': new_values})

#update
def update_day(collection, query_elements, new_values):
    """ Function to update a single document in a collection.
    """
    collection.update_one(query_elements, {'$set': new_values})

#update
def update_table(collection, query_elements, new_values):
    """ Function to update a single document in a collection.
    """
    collection.update_one(query_elements, {'$set': new_values})





# Select
def find_document(collection, elements):
    """ Function to retrieve single or multiple documents from a provided
    Collection using a dictionary containing a document's elements.
    """
    results =  collection.find({}, {"_id": 0})
    return [r for r in results]




print(find_document(series_day, {}))

# def delete_document(collection, query):
#     """ Function to delete a single document from a collection.
#     """
#     collection.delete_one(query)


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

    insert_day(series_day, day)

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
    plan_day(series_day_total, day_total)
    
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
    insert_month(series_month, Month)

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
    plan_month(series_month_total, Month_total) 




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
    update_day(series_day_total, {'_id': "5fd37d58b3b662ad429afd8a"}, day_total)

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
    update_month(series_month_total, {'_id': "5fd37d58b3b662ad429afd89"}, Month_total) 


def update_table_up(info):
    update_table(info[3], {'$and': [{'reckl': f"{info[0]}"}, {"scheme": f"{info[4]}"}]}, {"gross": f'{info[1]}', "morja": f'{info[2]}', "data": f'{info[5]}'})
     




#bd = Mongo()
#bd.insert_day(series_day, days())
#bd.plan_day(series_day, days_total())
#bd.insert_month(series_month, month())
#bd.plan_month(series_month, month_totoal())
#print(bd.find_document(series_collection, {"year": 1994}))
#bd.update_document(series_collection, {'name': "FRIENDS"}, {'name': "bobo"})
#bd.delete_document(series_collection, {"name": "bobo"})
