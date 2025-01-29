from flask import Flask
from flask import render_template
import book_manager

app = Flask(__name__)

@app.route("/")
def index():

    book = book_manager.extract_book_content()
    
    return render_template("index.html", book=book)
