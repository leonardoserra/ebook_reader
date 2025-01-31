import io
import os
import ebooklib
from ebooklib import epub

from PIL import Image


def extract_and_convert_images(epub_path, output_folder="static", extension="JPEG"):
    book = epub.read_epub(epub_path)

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_IMAGE:

            # if the name is a path, i will split
            # it and take just the last element, the filename.

            image_path = item.get_name()
            image_filename = item.get_name().split("/")[-1]
            name = image_filename.split(".")[0]
            extension = image_filename.split(".")[-1]

            if extension.upper() == "JPG":
                extension = "JPEG"

            print(
                ":\nimage_path: ",
                image_path,
                ":\nimage_filename: ",
                image_filename,
                ":\nname: ",
                name,
                ":\nextension: ",
                extension.upper(),
            )

            image_data: bytes = item.get_content()

            # Convert image format (e.g., to JPG)
            try:
                image = Image.open(io.BytesIO(image_data), formats=[extension])
                output_buffer = io.BytesIO(image_data)
                image.save(output_buffer, format=extension)
                converted_data = output_buffer.getvalue()

            except Exception as e:
                print(f"Error converting {image_filename}: {e}")
                continue

            # Update the file extension
            new_image_path = f"{name}.{extension.lower()}"

            # Save the converted image
            full_output_path = os.path.join(output_folder, new_image_path)
            os.makedirs(os.path.dirname(full_output_path), exist_ok=True)

            with open(full_output_path, "wb") as f:
                f.write(converted_data)
            print(f"Saved converted image: {full_output_path}")



# Run the script
if __name__ == "__main__":
    extract_and_convert_images("ebooks/book.epub")