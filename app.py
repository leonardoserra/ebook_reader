from flask import Flask

from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import flash
from flask import abort

import random

import ebook_manager

app = Flask(__name__)
app.secret_key = random.randbytes(8)


@app.route("/")
def index():
    ebooks = ebook_manager.choose_book()

    ctx = {
        "origin": request.path,
        "page_title": "Collection",
        "ebooks": ebooks,
        "theme": ebook_manager.get_theme(),
    }
    flash("test")
    return render_template("index.html", **ctx)


@app.route("/read/<ebook_name>/<int:page_index>")
def read_ebook(ebook_name="book.epub", page_index=0):
    try:
        page_content, page_count = ebook_manager.extract_page(ebook_name, page_index)

        ebook_manager.set_ebook_state(ebook_name, page_index)

    except Exception as e:
        abort(e)

    ctx = {
        "origin": request.path,
        "theme": ebook_manager.get_theme(),
        "page_index": page_index,
        "page_title": ebook_name,
        "page_count": page_count,
        "page_content": page_content,
        "limits": ebook_manager.pages_range(page_index, page_count),
    }

    return render_template("read.html", **ctx)


@app.route("/toggle-theme")
def toggle_theme():

    ebook_manager.toggle_theme()

    origin = request.args.get("origin", url_for('index'))

    return redirect(origin)


@app.errorhandler(500)
@app.errorhandler(404)
def error_page(error):
    return render_template("error.html", error=error)
