import os
import base64
import json
from functools import cache

from bs4 import BeautifulSoup

# from os import path # con questo potresti prendere la dimensione dei file e mostrarla.
import ebooklib
from ebooklib import epub

EBOOKS_PATH = "static/ebooks/"


def choose_book():

    ebooks = []
    for _, __, filenames in os.walk(EBOOKS_PATH):

        ebooks.extend(filenames)
        break

    init_state()

    ebooks = [
        {"name": e, "size": get_ebook_size(e), "state": load_state(e)}
        for e in ebooks
        if e.endswith(".epub")
    ]

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


def pages_range(page_index: int, page_count: int) -> tuple[int, int]:

    prev: int = page_index - 3
    post: int = page_index + 3

    limits: tuple[int, int] = (
        prev if prev >= 0 else 0,
        post if post < page_count else 0,
    )

    return limits


def init_state() -> None:

    if os.path.isfile(f"static/state.json"):
        return

    with open("static/state.json", "x") as file:
        file.write(json.dumps({"theme": 1}))


def set_ebook_state(ebook_name: str, current_page: int) -> None:

    state = None

    with open("static/state.json", "r") as file:
        state = json.load(file)

        state[ebook_name] = current_page

    with open("static/state.json", "w") as file:

        file.write(json.dumps(state))


def load_state(ebook_name: str) -> int:

    with open("static/state.json", "r") as file:
        state = json.load(file)
        if ebook_name in state:
            return state[ebook_name]
        else:
            return 0


def toggle_theme():

    theme = get_theme()

    with open("static/state.json", "r") as file:
        state = json.load(file)

        state["theme"] = abs(theme - 1)

    with open("static/state.json", "w") as file:

        file.write(json.dumps(state))


def get_theme() -> int:

    with open("static/state.json", "r") as file:
        state = json.load(file)
        return state["theme"]


def get_ebook_size(ebook_path: str) -> str:

    size: int = os.stat(EBOOKS_PATH + ebook_path).st_size
    unit: str = ""

    if size > 1024 * 1000:  # MB
        size /= 1024 * 1000
        unit = "MB"

    elif size > 1024:  # KB
        size /= 1024
        unit = "KB"

    size = str(size.__round__(3)) + unit

    return size


def add_fav_book(ebook_name: str) -> bool: ...  # this will set the fav bool to true.


def remove_fav_book(ebook_name: str) -> bool: ...  # this will set the fav bool to true.


def add_fav_page(
    ebook_name: str, page_index: int
) -> bool: ...  # this will add the index of the fav ebook pages to the state.json file.


def remove_fav_page(
    ebook_name: str, page_index: int
) -> bool: ...  # this will add the index of the fav ebook pages to the state.json file.


def rename_ebook(
    ebook_name: str, new_name: str
) -> bool: ...  # edit the filename in the menu.


def delete_ebook(ebook_name: str) -> bool: ...  # delete an ebook from the folder.

