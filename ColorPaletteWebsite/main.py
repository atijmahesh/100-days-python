from flask import Flask, render_template, request, redirect, url_for
import os
from PIL import Image
import numpy as np
from collections import Counter

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No file part', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        top_colors = detect_top_colors(file_path)
        return render_template('results.html', colors=top_colors)

def detect_top_colors(image_path):
    image = Image.open(image_path)
    np_image = np.array(image)
    pixels = np_image.reshape(-1, 3)
    counts = Counter(map(tuple, pixels))
    top_colors = counts.most_common(10)
    top_colors_with_text_color = []
    for color, _ in top_colors:
        color_hex = '#%02x%02x%02x' % color
        # Calculate brightness (simple approximation)
        brightness = (color[0] * 299 + color[1] * 587 + color[2] * 114) / 1000
        text_color = '#000000' if brightness > 125 else '#FFFFFF'
        top_colors_with_text_color.append((color_hex, text_color))
    
    return top_colors_with_text_color


if __name__ == '__main__':
    app.run(debug=True)
