import io
import json
import os

from flask import abort, current_app, send_file, request, url_for, jsonify
from coffeebreak import app, image, params, root_path, storage

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

@app.route('/api/cards/<int:id>.jpg')
def get_card(id):
    db = storage.JSONStorage()
    return generate(db.get(id))

@app.route('/api/register', methods=['GET', 'POST'])
def register():
    data = json.dumps(filter_data())
    db = storage.JSONStorage()
    index = db.insert(data)
    db.commit()
    return jsonify({
        'id': index,
        'url': current_app.config.get('PUBLIC_URI') + url_for('get_card', id=index)
    })

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
