from flask import Flask
from flask import render_template
import ebook_manager

app = Flask(__name__)

@app.route("/")
def index():
    ebooks= ebook_manager.choose_book()

    ctx = {
        "page_title": "Collection",
        "ebooks":ebooks,
    }

    return render_template("index.html",**ctx)


@app.route("/read/<ebook_name>")
def read_ebook(ebook_name = "book.epub"):
    parsed_ebook= ebook_manager.extract_book_content(ebook_name)
    ctx = {
        "page_title": ebook_name,
        "ebook":parsed_ebook,
    }
    
    return render_template("read.html",**ctx)
