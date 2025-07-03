from flask import Flask, send_file, render_template
import os
from PIL import np
import numpy as np


app = Flask(__name__)

IMAGE_PATH = "static/image.bmp"

@app.route('/')
def home():
    # Проверяем, существует ли файл
    if not os.path.exists(IMAGE_PATH):
        return "Изображение не найдено!", 404
    return render_template("index.html")

@app.route('/image')
def get_image():
    # Отправляем BMP-файл как статический
    return send_file(IMAGE_PATH, mimetype='image/bmp')

if __name__ == '__main__':
    # Создаём папку static, если её нет
    os.makedirs("static", exist_ok=True)
    app.run(debug=True)

    def replace_image_bytes(source_path, target_path, output_path):

        try:
            with Image.open(source_path) as img:
                width, height = img.size
                mode = img.mode
                img_format = img.format

                # Преобразуем в numpy array
                source_array = np.array(img)
                source_bytes = source_array.tobytes()

            with open(target_path, 'rb') as f:
                target_bytes = f.read()

            required_bytes = len(source_bytes)
            if len(target_bytes) < required_bytes:
                print(f"Ошибка: В целевом файле недостаточно байтов ({len(target_bytes)}), нужно {required_bytes}")
                return

            replacement_bytes = target_bytes[:required_bytes]

            new_array = np.frombuffer(replacement_bytes, dtype=source_array.dtype)

            if len(source_array.shape) == 3:
                new_array = new_array.reshape(height, width, source_array.shape[2])
            else:
                new_array = new_array.reshape(height, width)

            result_img = Image.fromarray(new_array)

            result_img.save(output_path, format=img_format)
            print(f"Изображение успешно сохранено в {output_path}")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

        source_image = "image.bmp"  # Исходное изображение
        target_file = "image2.bmp"  # Файл с байтами для замены (может быть любым файлом)
        output_image = "output.jpg"  # Результат

        replace_image_bytes(source_image, target_file, output_image)