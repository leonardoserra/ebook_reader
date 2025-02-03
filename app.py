from flask import Flask
from flask import render_template
import ebook_manager

app = Flask(__name__)

@app.route("/")
def index():
    ebook_name = "book.epub"
    parsed_ebook= ebook_manager.extract_book_content(ebook_name)

    ctx = {
        "ebook_name": ebook_name,
        "ebook":parsed_ebook,
    }
    
    return render_template("index.html",**ctx)
