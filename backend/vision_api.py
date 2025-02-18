from google.cloud import vision
import io

def detect_text_in_image(image_path):
    """Mendeteksi teks dalam gambar menggunakan Google Vision API"""
    client = vision.ImageAnnotatorClient()
    
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    if texts:
        return texts[0].description.strip()  # Ambil teks utama
    return None
