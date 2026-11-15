from flask import Flask,request #lowercase r cus uppercase is a class that doesnt get arguments which is what we are doing with the object id's in the url lowercase r is for that
from flask_restful import Api,Resource
from pymongo import MongoClient
from bson import ObjectId
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
client = MongoClient("localhost", 27017)
db = client["people_arshia"]
users = db["people"] # 127.0.0.1 is just localhost's address id
CORS(app=app,origins=["http://127.0.0.1:5500"]) # what servers are allowed to connect to this #we are using 5500 on the html stuff and 5000 here because its like a big hotel each port is one room and can do one thing at a time. localhost is my pc, and port 5000 is room 5000 in the hotel being used by this python backend and port 5500 is room 5500 in the hotel using the frontend html and javascript. each port can only do one service.
# search up cors security. its like a system that doesnt let two seperate servers talk for security i think.
# its cus my backend is localhost:5000 but my frontend is localhost:5500

#type this into web browser to actually get something localhost:5000/user?user_id=6acba1a68ccbbad556d84feb the thing after = is just the object id of the person in the database
#/user
#argument should be id which is mongodb id of the person
# returns information that is found about that person
class User(Resource):
    def get(self,): #dont put user_id here cus u want it as an argument and dont want to make it a dynamic url
        try: 
            user_id = request.args.get("user_id")#gets the user id
            user = users.find_one({"_id": ObjectId(str(user_id))},{"registered_at":0}) #_id idk why i forgot probably naming conventions the registered at part means it wont show the part of the person that says registered at cus its 0
            if user:
                user["_id"] = str(user["_id"])
                return user
            return {"msg":"user not found"}
        except Exception:
            return {"msg":"id not found"}
        
api.add_resource(User,"/user")#endpoint
app.run(debug=True)