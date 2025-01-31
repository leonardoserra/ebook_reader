import ebooklib
from ebooklib import epub

from flask import url_for

from bs4 import BeautifulSoup


def extract_book_content() -> list[dict]:
    ebook = epub.read_epub("ebooks/book.epub")

    book = []

    for item in ebook.get_items():

        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content = BeautifulSoup(item.get_body_content(), "html.parser")
            item_dict = {"data": content, "is_image": False}

            book.append(item_dict)

        if item.get_type() == ebooklib.ITEM_IMAGE:
            name = item.get_name().split("/")[-1]
            filename = item.get_name().replace("jpg", "jpeg").replace("images/", "")
            url = url_for("static", filename=filename)
            image_dict = {"name": name, "is_image": True, "url": url}

            book.append(image_dict)

    return book
