from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv
from bson.objectid import ObjectId
from bson.json_util import dumps, loads
import pymongo
import os

load_dotenv()
# print(os.environ.get("MONGO_URL")) #double check connection to MongoDB
MONGO_URL = os.environ.get('MONGO_URL')
DB_NAME = "tabletop_shop"

# create the MongoClient first
# Global Variables
client = pymongo.MongoClient(MONGO_URL)
db = client[DB_NAME]

app = Flask(__name__)


@app.route('/')
def homepage():
    books = list(db.books.find().limit(3))
    return render_template('home.template.html', books=books)


@app.route('/livesearch', methods=["POST", "GET"])
def livesearch():
    query = request.form.get('text')
    # print(query)
    # data = db.books.find({"book_category": {"$regex": query}})
    data = db.books.find({'$text': {'$search': query}})
    # print(data)
    json_data = dumps(data)
    # print(json_data)
    return json_data

@app.route('/create')
def show_create_form():
    return render_template("create.template.html")

@app.route('/create', methods=["POST"])
def process_create_form():
    return redirect(url_for('homepage'))

# def query():
#     try:
        
#         data = list(mongo.db.books.find())
#         print(data)
#         query = request.form.get("text")
#         print(query)
#         # doc = mongo.db.books.find({"$text": {"$search": "/.*boo.*/"}})
#         # doc = mongo.db.books.find({"book_name":/.*boo.*/}).pretty()
#         doc = mongo.db.books.find({"book_name": {"$regex": ".*bo.*"}})
#         print(doc)
#         lis_doc = list(doc)
#         print(lis_doc)
#     except:
#         print("Error Connecting to Server")

# query()

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
