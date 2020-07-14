import pymongo
from src.config import DBURL
from src.config import DBURL, DB_NAME


client = pymongo.MongoClient()
db = client[ "databaseapi" ]
col = db[ "users" ] 

def check_user(name):
    query = {"name":{"$eq":f"{name}"}}
    cur = db.col.find(query)
    data = list(cur)
    if len(data)==0:
        print(len(data))
        return True
    else:
        print(len(data))
        return False
