from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.template.html')


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), # or '0.0.0.0'
            port=int(os.environ.get('PORT')), #or 8080
            debug=True)
