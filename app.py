from flask import Flask, send_file, render_template
import os

app = Flask(__name__)

# Путь к BMP-файлу (создайте его заранее или сгенерируйте программно)
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