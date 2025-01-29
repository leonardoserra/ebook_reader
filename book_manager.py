import ebooklib
from ebooklib import epub
from collections import OrderedDict
from bs4 import BeautifulSoup


def extract_book_content() -> OrderedDict:
    book = epub.read_epub('ebooks/algoritmi_e_strutture_dati.epub')
    
    items = OrderedDict([])

    for item in book.get_items():

        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            item_name = item.get_name()
            item_data:str = item.get_content()
            # soup:str = BeautifulSoup(item_data, 'html.parser')
            items[item_name]= item_data

        if item.get_type() == ebooklib.ITEM_IMAGE:
            image_name:str = item.get_name()
            image_data:bytes = item.get_content()
            
            items[image_name] = image_data
    print(items)
    return items
