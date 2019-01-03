from flask import Flask, render_template
import random, logging

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.INFO)

images_path = 'config/images.txt'
try:
    with open(images_path,'r') as images_file:
        images = images_file.read().splitlines()
except:
    app.logger.warning('Unable to load {images} - falling back to default list'.format(images=images_path))
    # Default list of cat images courtesy of buzzfeed

@app.route('/')
def index():
#    url = random.choice(images)
#    return render_template('index.html', url=url)
    return render_template('index.html')

@app.route('/list')
def list():
    return render_template('index2.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
