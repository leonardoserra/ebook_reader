# EBOOK READER (.epub)
| 2025.01.31 - Version 0.0.2 |

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


### Get Started
1. Put a file into the `/ebooks` folder and call it `book.epub`  
2. run into the terminal: `flask run`  
4. Go to the ip address provided by the terminal ( usually is http://127.0.0.1:5000 )  
    
### Changelog:  
> 2025.02.03 - `version 0.0.5`  
- Added 404 and 500 error page.
- Changed font.
- Some style on the ebook list menu.

> 2025.02.03 - `version 0.0.4`  
- Now the landing page is the page where to choose the book from the ebooks folder.  
- Added the `read/<ebook_name>` route to open different books.
- added some style in the `static/css/main.css` file.

> 2025.02.03 - `version 0.0.3`  
- Changed the module names from 'book' to 'ebook'. 
- Added a base64 decoding to directly pass to the template the images loaded, without the necessity to store them locally into the static folder.
- removed `pillow` package.
- removed `beautifulsoup4` and `soupsieve` packages.
- added a todo.md file, with all the features or fix.  
  
> 2025.01.31 - `version 0.0.2`  
- Added an image extractor module to store in local the ebook images.  
- Rendering of the book, currently the images are not in order.  

> 2025.01.29 - `version 0.0.1`  
- Added flask implementation with a single route, to show the content.

> 2025.01.29 - `version 0.0.0`  
- First implementation, just printed the content.  

_______

#### References Docs

- [Flask](https://flask.palletsprojects.com/en/stable/quickstart)  
- [EbookLib](https://docs.sourcefabric.org/projects/ebooklib/en/latest/tutorial.html)  