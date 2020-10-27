from flask import Flask, render_template, request, redirect, url_for, jsonify
from bson.json_util import dumps, loads
from flask_pymongo import PyMongo
import os

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
mongo = PyMongo(app)


@app.route('/')
def homepage():
    books = list(mongo.db.books.find().limit(3))
    return render_template('home.template.html', books=books)


@app.route('/livesearch', methods=["POST", "GET"])
def livesearch():
    query = request.form.get('text')
    print(query)
    # data = mongo.db.books.find({"book_category": {"$regex": query}})
    data = mongo.db.books.find({'$text': {'$search': query}})
    # print(data)
    json_data = dumps(data)
    print(json_data)
    return json_data

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
