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


def searchList():
    books = list(db.books.find().sort("reviews", -1))

    search_list = list()
    items_set = set()

    for book in books:
        if not book['category'] in items_set:
            items_set.add(book['category'])
            search_list.append(book)

    return search_list


@app.route('/')
def homepage():
    books = list(db.books.find().sort("reviews", -1))
    top = books[:3]
    search_list = searchList()
    # print(search_list)
    return render_template('home.template.html',
                           books=books, search_list=search_list, top=top)


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


@app.route('/catsearch', methods=["POST", "GET"])
def catsearch():
    query = request.form.get('text')
    # print(query)
    # data = db.books.find({"book_category": {"$regex": query}})
    data = db.category.find({'$text': {'$search': query}})
    # print(data)
    json_data = dumps(data)
    # print(json_data)
    return json_data


@app.route('/category/<book_category>')
def show_books_in_category(book_category):
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
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
    return render_template('show_category_books.template.html', books=books,
                           cat=category, search_list=search_list)


@app.route('/info/<book_id>')
def show_book_info(book_id):
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    book = db.books.find_one({
        '_id': ObjectId(book_id)
    })
    return render_template('book_info.template.html', book=book,
                           search_list=search_list, books=books)


@app.route('/create')
def show_create_form():
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    category_list = db.category.find()
    return render_template("create.template.html", books=books,
                           search_list=search_list,
                           category_list=category_list)


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

    new_book = {
        "category": category,
        "name": name,
        "author": author,
        "release_date": release_date,
        "price": price,
        "reviews": reviews,
        "comments": comments,
        "image": image
    }
    db.books.insert_one(new_book)
    flash("New book review is created successfully!", "success")
    return redirect(url_for('show_books_in_category', book_category=category))


@app.route('/category/create')
def show_create_category():
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    return render_template("create_category.template.html",
                           books=books, search_list=search_list)


@app.route('/category/create', methods=["POST"])
def process_create_category():
    name = request.form.get('catName')
    publisher = request.form.get('catPublisher')
    comments = request.form.get('catComments')

    new_cat = {
        "name": name,
        "publisher": publisher,
        "comments": comments,
    }

    db.category.insert_one(new_cat)
    flash("New book category is created successfully!", "success")
    return redirect(url_for('show_create_form'))


@app.route('/edit/<book_id>')
def show_edit_book(book_id):
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    book = db.books.find_one({
        '_id': ObjectId(book_id)
    })
    return render_template('edit_book.template.html', books=books,
                           book=book, search_list=search_list)


@app.route('/edit/<book_id>', methods=["POST"])
def process_edit_book(book_id):
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
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
    return redirect(url_for('homepage'), search_list=search_list,
                    books=books)


@app.route('/delete/<book_id>')
def show_delete_book(book_id):
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    book_to_delete = db.books.find_one({
        '_id': ObjectId(book_id)
    })

    return render_template('show_delete_book.template.html', books=books,
                           book=book_to_delete, search_list=search_list)


@app.route('/delete/<book_id>', methods=["POST"])
def confirm_delete_book(book_id):
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    db.books.remove({
        '_id': ObjectId(book_id)
    })
    return redirect(url_for("homepage"), search_list=search_list,
                    books=books)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
