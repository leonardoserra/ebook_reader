import ebooklib
from PIL import Image
from ebooklib import epub
import io
from bs4 import BeautifulSoup
import os

def extract_book_content() -> list[dict]:
    ebook = epub.read_epub("ebooks/book.epub")

    book = []

    for item in ebook.get_items():

        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            content = BeautifulSoup( item.get_body_content(), 'html.parser')
            item_dict = {"data": content, "is_image": False}

            book.append(item_dict)

        if item.get_type() == ebooklib.ITEM_IMAGE:
            image_dict = {"data": item.get_content(), "is_image": True}

            book.append(image_dict)

    book = convert_images(book)

    return book


def convert_images(book: list[dict]) -> list[dict]:

    book = [{**e} for e in book]

    for i, element in enumerate(book):
        if element["is_image"] and element.get("data"):
            book[i]["data"] = binary_to_base64(element["data"])

    return book


def binary_to_base64(binary: bytes) -> str:
    try:
        image = Image.open(io.BytesIO(binary))
        output_buffer = io.BytesIO()
        image.save(output_buffer, format='JPEG')
        converted_data = output_buffer.getvalue()
        return f'{converted_data}'
    except Exception as e:
        print(f"Error converting image: {e}")
        return ''

