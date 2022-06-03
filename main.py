import cv2 as cv
import numpy as np
import PIL
import pytesseract
import streamlit as st


def load_image():
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    uploaded_file = st.file_uploader("Choose a image file", type=["jpg", 'png', 'jpeg'])
    sel_lang = st.radio('Select language, please', ['English', 'Russian'])
    lang = ''
    if sel_lang == 'Russian':
        lang = 'rus'
    else:
        lang = 'eng'
    if uploaded_file is not None:
        # Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv.imdecode(file_bytes, 1)
        config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'
        text = pytesseract.image_to_string(opencv_image, config=config, lang=lang)
        st.write(text)
    else:
        st.write("No image...")


if __name__ == '__main__':
    load_image()


