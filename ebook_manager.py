import base64

from os import walk
from functools import cache

from bs4 import BeautifulSoup

# from os import path # con questo potresti prendere la dimensione dei file e mostrarla.
import ebooklib
from ebooklib import epub

EBOOKS_PATH = "./ebooks"


def choose_book():

    ebooks = []
    for _, __, filenames in walk(EBOOKS_PATH):

        ebooks.extend(filenames)
        break

    ebooks = [e for e in ebooks if e.endswith(".epub")]

    return ebooks


@cache
def extract_book_content(ebook_name: str) -> str:
    """
    Given a epub name it opens, loads and pass the value to the main route.

    :param ebook_name: the name of the epub you wanna read.

    """

    raw_ebook = epub.read_epub(f"{EBOOKS_PATH}/{ebook_name}")

    documents = []

    images = {}

    for item in raw_ebook.get_items():

        if item.get_type() == ebooklib.ITEM_DOCUMENT:

            html = item.get_body_content().decode("utf-8")
            documents.append(html)

        if item.get_type() in (ebooklib.ITEM_IMAGE, ebooklib.ITEM_COVER):

            name = item.get_name()
            file_extension = name.split(".")[-1]

            data = item.get_content()
            converted_base64 = base64.b64encode(data).decode("utf-8")

            src = f"data:image/{file_extension};base64,{converted_base64}"
            images[name] = src

    parsed_ebook = "".join(list(documents))

    for k, v in images.items():
        if k in parsed_ebook:
            parsed_ebook = parsed_ebook.replace(k, v)

    return parsed_ebook


@cache
def extract_page(ebook_name: str, page_index: int) -> tuple[str, int]:

    parsed_ebook = extract_book_content(ebook_name)

    pages = [
        p.strip().strip("&#13;")
        for p in parsed_ebook.split("</div>")
        if p.strip().strip("&#13;")
    ]
    page_count = len(pages)

    page_content = BeautifulSoup(pages[page_index].strip(), "html.parser")

    return page_content, page_count


def pages_range(page_index, page_count) -> tuple[int, int]:

    prev = page_index - 3
    post = page_index + 3

    limits = (prev if prev >= 0 else 0, post if post < page_count else 0)

    return limits
