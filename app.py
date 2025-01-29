from flask import Flask
from flask import render_template
import book_manager
from PIL import Image
import io
import os
app = Flask(__name__)

@app.route("/")
def book():

    book = book_manager.extract_book_content()
    
    return render_template("index.html", content=book)