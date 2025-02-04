import base64
from os import walk
# from os import path # con questo potresti prendere la dimensione dei file e mostrarla.
import ebooklib
from ebooklib import epub
EBOOKS_PATH = "./ebooks"

def choose_book():

    ebooks = []
    for (dirpath, dirnames, filenames) in walk(EBOOKS_PATH):

        ebooks.extend(filenames)
        break
    
    ebooks = [e for e in ebooks if e.endswith('.epub')]

    return ebooks


def extract_book_content(ebook_name: str = "book.epub") -> list[dict]:
    """
    Given a epub name it opens, loads and pass the value to the main route.

    :param ebook_name: the name of the epub you wanna read.

    """

    ebook = epub.read_epub(f"{EBOOKS_PATH}/{ebook_name}")

    documents = []

    images = {}

    for item in ebook.get_items():

        if item.get_type() == ebooklib.ITEM_DOCUMENT:

            html = item.get_body_content().decode('utf-8')
            documents.append(html)

        if item.get_type() in (ebooklib.ITEM_IMAGE, ebooklib.ITEM_COVER):

            name = item.get_name()
            file_extension = name.split(".")[-1]

            data = item.get_content()
            converted_base64 = base64.b64encode(data).decode("utf-8")

            src = f"data:image/{file_extension};base64,{converted_base64}"
            images[name] = src
    
    full_content = ''.join(list(documents))

    for k,v in images.items():
        if k in full_content:
            full_content = full_content.replace(k, v)

    return full_content
