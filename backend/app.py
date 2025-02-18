from flask import Flask, request, jsonify
from flask_cors import CORS
from database import search_images_by_number
from drive_api import list_images_from_drive
from vision_api import detect_text_in_image
import os

app = Flask(__name__)
CORS(app)  # Mengizinkan frontend mengakses API

UPLOAD_FOLDER = "static/images/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/search', methods=['GET'])
def search():
    bib_number = request.args.get('number')
    if not bib_number:
        return jsonify({"error": "Nomor dada tidak boleh kosong"}), 400

    results = search_images_by_number(bib_number)
    return jsonify(results)

@app.route('/process_images', methods=['POST'])
def process_images():
    images = list_images_from_drive("id folder google drive ")
    processed_images = []

    for img in images:
        img_path = os.path.join(UPLOAD_FOLDER, img['name'])
        detected_text = detect_text_in_image(img_path)

        if detected_text:
            from database import save_image_data
            save_image_data(img['name'], detected_text, img_path)
            processed_images.append({"image": img_path, "text": detected_text})

    return jsonify({"processed": processed_images})

if __name__ == '__main__':
    app.run(debug=True)
