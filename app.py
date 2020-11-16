from flask import Flask, render_template, request, redirect, url_for, flash, session
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


def loggedIn():
    if not session.get("user") is None:
        logged_name = session.get("user").get('user_name')
        return logged_name


@app.route('/')
def homepage():
    books = list(db.books.find().sort("reviews", -1))
    new_books = list(db.books.find().sort("release_date", -1))
    new = new_books[:3]
    top = books[:6]
    search_list = searchList()
    logged = loggedIn()

    return render_template('home.template.html', new=new, logged=logged,
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


@app.route('/login', methods=["POST", "GET"])
def show_login():
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    logged = loggedIn()
    users = list(db.users.find())
    # print(users)
    # for x in users:
    #     print(x.get('email'))
    #     print(x.get('_id'))

    if request.method == "POST":
        session.pop('user', None)
        userEmail = request.form.get("userEmail")
        userPassword = request.form.get("userPassword")

        for user in users:
            if user.get('email') == userEmail:
                if user.get('password') == userPassword:
                    new_session = {
                        "user_id": str(user.get('_id')),
                        "user_name": user.get('name')
                    }
                    # session['user_id'] = str(user.get('_id'))
                    # session['user_name'] = (user.get('name'))
                    session['user'] = new_session
                    print(session)
                    flash('Successfully Logged In!')
                    return redirect(url_for('homepage'))
                else:
                    flash('Invalid User Email/Password! Try again!', 'error')
                    return redirect(url_for('show_login'))

    return render_template("login.template.html", books=books,
                           search_list=search_list, logged=logged)


@app.route('/logout')
def show_logout():
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    logged = loggedIn()
    return render_template("logout.template.html", search_list=search_list,
                           books=books, logged=logged)


@app.route('/logout', methods=["POST"])
def process_logout():
    session.pop('user', None)
    return redirect(url_for('homepage'))


@app.route('/register')
def show_register():
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    logged = loggedIn()
    return render_template('registration.template.html', books=books,
                           search_list=search_list, logged=logged)


@app.route('/register', methods=["POST"])
def process_register():
    user_name = request.form.get('userName')
    user_email = request.form.get('userEmail')
    user_password = request.form.get('userPassword')
    TNC, mailing = False, False
    if request.form.getlist("TNC"):
        TNC = True
    if request.form.getlist("mailingList"):
        mailing = True

        new_mailing = {
            "name": user_name,
            "email": user_email
        }

        db.mailing_list.insert_one(new_mailing)

    new_user = {
        "name": user_name,
        "email": user_email,
        "password": user_password,
        "TNC": TNC,
        "mailing": mailing
    }

    db.users.insert_one(new_user)
    return redirect(url_for('show_login'))


@app.route('/category/<book_category>')
def show_books_in_category(book_category):
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    logged = loggedIn()
    category = list(db.category.aggregate([{
        '$lookup': {
            'from': 'books',
            'localField': 'name',
            'foreignField': 'category',
            'as': 'books'
        }}, {
        '$match': {
            "name": book_category
        }}]))
    return render_template('show_category_books.template.html', books=books,
                           category=category, search_list=search_list,
                           logged=logged)


@app.route('/info/<book_id>')
def show_book_info(book_id):
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    logged = loggedIn()
    book = db.books.find_one({
        '_id': ObjectId(book_id)
    })
    return render_template('book_info.template.html', book=book,
                           search_list=search_list, books=books,
                           logged=logged)


@app.route('/create')
def show_create_form():
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    logged = loggedIn()
    category_list = db.category.find()
    return render_template("create.template.html", books=books,
                           search_list=search_list, logged=logged,
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
    flash(f"New book review {new_book['name']} has been ADDED successfully!",
          "success")
    return redirect(url_for('show_books_in_category', book_category=category))


@app.route('/category/create')
def show_create_category():
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    logged = loggedIn()
    return render_template("create_category.template.html",
                           books=books, search_list=search_list,
                           logged=logged)


@app.route('/category')
def show_category():
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    logged = loggedIn()
    return render_template("show_category.template.html", books=books,
                           search_list=search_list, logged=logged)


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
    flash(f"New Series {new_cat['name']} has been ADDED successfully!",
          "success")
    return redirect(url_for('show_create_form'))


@app.route('/edit/<book_id>')
def show_edit_book(book_id):
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    logged = loggedIn()
    category_list = db.category.find()
    book = db.books.find_one({
        '_id': ObjectId(book_id)
    })
    return render_template('edit_book.template.html', books=books,
                           book=book, search_list=search_list,
                           category_list=category_list, logged=logged)


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

    flash(f"{name}'s review has been UPDATED successfully!",
          "success")

    return redirect(url_for('show_book_info', book_id=ObjectId(book_id)))


@app.route('/delete/<book_id>')
def show_delete_book(book_id):
    search_list = searchList()
    books = list(db.books.find().sort("reviews", -1))
    logged = loggedIn()
    book_to_delete = db.books.find_one({
        '_id': ObjectId(book_id)
    })

    return render_template('show_delete_book.template.html', books=books,
                           book=book_to_delete, search_list=search_list,
                           logged=logged)


@app.route('/delete/<book_id>', methods=["POST"])
def confirm_delete_book(book_id):
    db.books.remove({
        '_id': ObjectId(book_id)
    })

    flash("Book Review has been DELETED successfully!", "success")

    return redirect(url_for("homepage"))


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
