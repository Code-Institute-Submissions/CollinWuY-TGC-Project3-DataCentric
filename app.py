from flask import Flask, render_template, request, redirect, url_for, flash
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
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def homepage():
    books = list(db.books.find().sort("reviews", -1))
    top4 = books[:4]

    search_list = list()
    items_set = set()

    for book in books:
        if not book['category'] in items_set:
            items_set.add(book['category'])
            search_list.append(book)
    # print(search_list)
    return render_template('home.template.html',
                           books=books, search_list=search_list, top4=top4)


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


@app.route('/category/<book_category>')
def show_books_in_category(book_category):
    category = db.category.aggregate([{
        '$lookup': {
            'from': 'books',
            'localField': 'name',
            'foreignField': 'category',
            'as': 'books'
        }}, {
        '$match': {
            "name": book_category
        }}])

    print(category)

    return render_template('show_category_books.template.html', cat=category)


@app.route('/create')
def show_create_form():
    return render_template("create.template.html")


@app.route('/create', methods=["POST"])
def process_create_form():
    name = request.form.get('bookName')
    category = request.form.get('bookCategory')
    author = request.form.get('bookAuthor')
    release_date = request.form.get('bookRelease_Date')
    price = request.form.get('bookPrice')
    comments = request.form.get('bookComments')
    image = request.form.get('bookImage')
    reviews = request.form.getlist('rate')
    reviews = int(reviews[0])

    new_record = {
        "category": category,
        "name": name,
        "author": author,
        "release_date": release_date,
        "price": price,
        "reviews": reviews,
        "comments": comments,
        "image": image
    }

    print(new_record)
    db.books.insert_one(new_record)
    flash("New book review is created successfully!", "success")

    return redirect(url_for('homepage'))


@app.route('/edit/<book_id>')
def show_edit_book(book_id):
    book = db.books.find_one({
        '_id': ObjectId(book_id)
    })
    print(book)
    return render_template('edit_book.template.html', book=book)


@app.route('/edit/<book_id>', methods=["POST"])
def process_edit_book(book_id):
    name = request.form.get('bookName')
    category = request.form.get('bookCategory')
    author = request.form.get('bookAuthor')
    release_date = request.form.get('bookRelease_Date')
    price = request.form.get('bookPrice')
    comments = request.form.get('bookComments')
    image = request.form.get('bookImage')
    reviews = request.form.getlist('rate')
    reviews = int(reviews[0])

    db.books.update_one({
        "_id": ObjectId(book_id)
    }, {
        '$set': {
            "category": category,
            "name": name,
            "author": author,
            "release_date": release_date,
            "price": price,
            "reviews": reviews,
            "comments": comments,
            "image": image
        }
    })
    return redirect(url_for('homepage'))


@app.route('/delete/<book_id>')
def show_delete_book(book_id):
    book_to_delete = db.books.find_one({
        '_id': ObjectId(book_id)
    })

    return render_template('show_delete_book.template.html',
                           book=book_to_delete)


@app.route('/delete/<book_id>', methods=["POST"])
def confirm_delete_book(book_id):
    db.books.remove({
        '_id': ObjectId(book_id)
    })
    return redirect(url_for("homepage"))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
