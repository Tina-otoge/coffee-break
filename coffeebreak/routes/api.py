import io
import json
import os

from flask import abort, send_file, request, url_for
from coffeebreak import app, image, params, root_path

def filter_data(data=None):
    data = data or request.args
    return {k: data.get(k, params.ARGUMENTS[k]) for k in params.ARGUMENTS}

@app.route('/api/card.html')
def generate_html(data=None):
    return image.get_html(filter_data(data))

@app.route('/api/generate')
def generate(data=None):
    html = generate_html(data)
    result = image.from_html(html)
    return send_file(io.BytesIO(result), mimetype='image/jpeg')

@app.route('/api/register')
def register():
    return generate()

def get_data_from_example(name):
    try:
        path = root_path / '../examples/requests/{}.json'.format(name)
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        abort(404)
    return data

@app.route('/api/examples/<name>.html')
def example_html(name):
    return generate_html(get_data_from_example(name))

@app.route('/api/examples/<name>')
def example_card(name):
    return generate(get_data_from_example(name))
