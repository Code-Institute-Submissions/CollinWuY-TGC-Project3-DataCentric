from flask import Flask, render_template, request, redirect, url_for
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
    books = list(mongo.db.books.find())
    return render_template('home.template.html', books = books)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
