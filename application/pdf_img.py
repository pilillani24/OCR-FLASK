import os
from pdf2image import convert_from_path
import tempfile

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def prepare_images(pdf_path_url):
    # Output dir
    print("APP_ROOT: " + APP_ROOT)
    # output_dir = os.path.join(APP_ROOT,"/static/pdf_image/")

    # List of directory path of saved img
    tempPathImg_list = []
    page_num = 0

    pages = convert_from_path(pdf_path = pdf_path_url, dpi=220)
    # get saved images from temporary directory
    for page in pages:
        page_num = page_num + 1
        imgPath = f"{APP_ROOT}/static/pdf_image/_page_{page_num}.jpg"
        page.save(imgPath, 'JPEG')
        # This Line of code must be handled differently
        temp_imgPath = f"/static/pdf_image/_page_{page_num}.jpg"

        tempPathImg_list.append(temp_imgPath)

    return tempPathImg_list
