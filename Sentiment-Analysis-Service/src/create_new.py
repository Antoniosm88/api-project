from src.app import app
from flask import json
import pymongo 
from src.config import DBURL, DB_NAME
from flask import request
from src.check import *

client = pymongo.MongoClient()
db = client[ "databaseapi" ] 
col = db[ "users" ] 

@app.route("/user/create/<username>")#, methods=['POST'])
def create_user(username): 
    print("Request to create user with username: ", username)
    if check_user(username) == True:
        col.insert_one( {"name" : f"{username}" })
        response= f"yeeeehaaa we have create {username}"
    else:
        print(f"It seems {username}, already exists in our database ")                   
    return response

