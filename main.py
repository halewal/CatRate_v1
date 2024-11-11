from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

# Cache to store cat images
cat_image_cache = []


def get_cat_images(count=5):
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=' + str(count))
    data = response.json()
    return [image['url'] for image in data]


@app.route('/')
def index():
    cat_url = get_cat()
    return render_template('index.html', url=cat_url)


@app.route('/get_cat', methods=['GET'])
def get_cat():
    global cat_image_cache

    # If the cache is empty, populate it
    if not cat_image_cache:
        cat_image_cache = get_cat_images()

        # Randomly select a cat image from the cache
    cat_image_url = random.choice(cat_image_cache)

    return cat_image_url


if __name__ == '__main__':
    app.run(debug=True)
