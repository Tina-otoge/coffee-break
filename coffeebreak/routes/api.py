import io
import json
import os

from flask import abort, send_file, request, url_for
from coffeebreak import app, image, params, root_path

def handle_settings(data):
    if 'settings' not in data:
        return data
    if data['settings'].get('auto_combo'):
        data['max_chart_combo'] = sum(data.get('judges', {}).values())
    return data

def filter_data(data=None):
    data = data or dict(request.values)
    data = handle_settings(data)
    return {k: data.get(k, params.DEFAULTS.get(k)) for k in params.ARGUMENTS}

@app.route('/api/card.html', methods=['GET', 'POST'])
def generate_html(data=None):
    data = data or filter_data(data)
    return image.get_html(data)

@app.route('/api/generate', methods=['GET', 'POST'])
def generate(data=None):
    html = generate_html(data)
    result = image.from_html(html)
    return send_file(io.BytesIO(result), mimetype='image/jpeg')

@app.route('/api/register', methods=['GET', 'POST'])
def register():
    data = filter_data()
    return generate()

def get_data_from_example(name):
    try:
        path = root_path / '../examples/requests/{}.json'.format(name)
        with open(path) as f:
            data = json.load(f)
    except FileNotFoundError:
        abort(404)
    except:
        abort(403)
    return data

@app.route('/api/examples/<name>.html')
def example_html(name):
    return generate_html(get_data_from_example(name))

@app.route('/api/examples/<name>')
def example_card(name):
    return generate(get_data_from_example(name))
