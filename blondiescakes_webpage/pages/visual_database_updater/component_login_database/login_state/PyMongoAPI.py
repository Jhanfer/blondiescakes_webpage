from pymongo import MongoClient
from pymongo.server_api import ServerApi
import dotenv
import os


"""dotenv.load_dotenv()
URL:str=os.environ.get("MONGO_URL")"""

def get_mongo():
    dotenv.load_dotenv()
    URL:str=os.environ.get("MONGO_URL")
    if URL:
        mongo=MongoClient(URL, server_api=ServerApi('1')) 
        return mongo
    else:
        return MongoClient("keys")

mongo_client=get_mongo()

"""mongo_client=mongo=MongoClient(MONGO_URL, server_api=ServerApi('1')) 


# Create a new client and connect to the server

# Send a ping to confirm a successful connection
try:
    mongo_client.users.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
"""

