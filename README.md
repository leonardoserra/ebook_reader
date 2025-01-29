# EBOOK READER (.epub)
| 2025.01.29 - Version 0.0.2 |

> This is a webapp to read a epub extension file (Ebook)  
> It's not complete  
> Currently it just returns a raw page of the html content
> if the ebook has a protection like DRM, it will not work.  

### Installation  

1. Create a venv: `python -m venv .ebook_reader_venv`  
2. Activate the venv:
    - Windows: `.\.ebook_reader_venv\Sripts\activate`  
    - Mac/Linux: `source ebook_reader_venv/bin/activate`  
3. Install requirements: `pip install requirements.txt`  
4. Put a file into the `/ebooks` folder and call it `book.epub`  
5. run into the terminal: `flask run`  
6. Go to the ip address provided by the terminal ( usually is http://127.0.0.1:5000 )  
  
  
#### todo:  
-Fix the the image data render, store it (or not) then convert into base64 and show into the html page.
- would be nice if I find a way to divide all the data in chunks, and create a pagination.  
- adding an argument into the command to change the book name making it possible to select the book to read.  

#### References Docs

- [Flask](https://flask.palletsprojects.com/en/stable/quickstart)  
- [EbookLib](https://docs.sourcefabric.org/projects/ebooklib/en/latest/tutorial.html)  
- [Pillow](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html)  