from flask import Flask
from flask import abort
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
    try:
        parsed_ebook= ebook_manager.extract_book_content(ebook_name)
    except page_not_found as e:
        abort(e)

    ctx = {
        "page_title": ebook_name,
        "ebook":parsed_ebook,
    }
    
    return render_template("read.html",**ctx)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', error=error), 404


@app.errorhandler(500)
def page_not_found(error):
    return render_template('errors/404.html', error=error), 500
