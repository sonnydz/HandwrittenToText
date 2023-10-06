from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import cv2
from PIL import Image
import pytesseract
from spellchecker import SpellChecker
app = Flask(__name__)


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def handwriting_to_text_from_image(image_path):
    frame = cv2.imread(image_path)
    img_rgb = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    text = pytesseract.image_to_string(img_rgb)
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', error='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('index.html', error='No selected file')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        result_text = handwriting_to_text_from_image(filepath)
        def spell_check(text):
            spell = SpellChecker()

    
            words = text.split()

    
            misspelled = spell.unknown(words)

    
            corrected_text = []
            for word in words:
             if word in misspelled:
               corrected_text.append(spell.correction(word))
             else:
               corrected_text.append(word)

            return ' '.join(corrected_text)


        text_to_check = result_text
        corrected_text = spell_check(text_to_check)
        print(f"Original text: {text_to_check}")
        print(f"Corrected text: {corrected_text}")
        return render_template('index.html', result=corrected_text, filename=filename)

    return render_template('index.html', error='File type not allowed')

if __name__ == '__main__':
    app.run(debug=True)
