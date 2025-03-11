from flask import Flask

from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask import flash
from flask import abort

import json

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
        scroll_y = request.args.get('scroll_y', 0)
        ebook_manager.set_state(ebook_name, page_index, scroll_y=scroll_y)

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

    origin = request.args.get("origin", url_for("index"))

    return redirect(origin)


@app.route("/load-state")
def load_json():
    with open("./static/state.json", "r") as file:
        return file.readlines()


@app.route("/save-state")
def save_state():
    state = request.form.get("state")
    if state:
        with open("./static/state.json", "w") as file:
            file.write(json.dumps(state))


@app.route("/set-y-axis", methods=["POST"])
def set_y_axis():
    """
    api to expose a way to set the y scroll position  
    """
    ebook_name = request.json.get('ebookName', '')
    scroll_y = request.json.get('scrollY', 0)

    ebook_manager.set_state(ebook_name, scroll_y=scroll_y)
    r = json.dumps({'status': 201})
    return r


@app.route("/get-y-axis/<ebook_name>", methods=["GET"])
def get_y_axis(ebook_name):
    """
    api to expose a way to get the y scroll position of a given book
    """
    state = ebook_manager.load_state(ebook_name)
    r = json.dumps({**state})
    return r



@app.errorhandler(500)
@app.errorhandler(404)
def error_page(error):
    return render_template("error.html", error=error)
