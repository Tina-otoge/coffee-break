import io
import json
import os
from datetime import datetime

from flask import abort, current_app, send_file, request, url_for, jsonify
from coffeebreak import app, image, params, root_path, storage

def fill_presets(data):
    with open(root_path / 'presets.json') as f:
        presets = json.load(f).get(data['settings']['preset'])
    if not presets:
        print('Could not find preset for {}'.format(preset_name))
        return data
    presets['class'] = presets.get('class', {})
    presets['presets'] = presets.get('presets', {})
    for key, value in presets['presets'].items():
        if key == 'level':
            actual_level = data.get('level')
            if not actual_level:
                continue
            actual_level = float(actual_level)
            levels = list(value.keys())
            levels.sort(reverse=True)
            for level in levels:
                if actual_level > float(level):
                    presets[key] = value[level]
                    break
            continue
        if key == 'judge':
            presets['class'][key] = data.get(key, value)
            continue
        presets['class'][key] = value.get(data.get(key))
    del presets['presets']
    for key, value in presets.items():
        if isinstance(value, dict):
            for k2, v2 in value.items():
                data[key] = data.get(key, {})
                data[key][k2] = data[key].get(k2, v2)
        else:
            data[key] = data.get(key, value)
    return data

def handle_settings(data):
    if 'settings' not in data:
        return data
    if data['settings'].get('preset'):
        data = fill_presets(data)
    if data['settings'].get('auto_combo'):
        data['max_chart_combo'] = sum(data.get('judges', {}).values())
    if data['settings'].get('auto_date'):
        data['date'] = data.get('date') or '{} UTC'.format(datetime.utcnow().replace(microsecond=0))
    if data['settings'].get('auto_fc') and not data.get('clear_type'):
        if data.get('breaks'):
            fc = data['breaks'] == '0'
        else:
            fc = data.get('judges', {}).get(data['settings']['auto_fc'].get('miss', 'MISS')) == 0
        if fc:
            data['clear_type'] = data['settings']['auto_fc'].get('fc', 'FULLCOMBO')
        else:
            data['clear_type'] = data['settings']['auto_fc'].get('not_fc', 'CLEARED')
    return data

def filter_data(data=None):
    data = data or dict(request.values)
    return {k: v for k, v in data.items() if k in params.ARGUMENTS and v != ''}

@app.route('/api/card.html', methods=['GET', 'POST'])
def generate_html(data=None):
    data = data or filter_data(data)
    for k in params.OBJECTS:
        if isinstance(data.get(k), str):
            try:
                data[k] = json.loads(data[k])
            except json.JSONDecodeError:
                del data[k]
    data = handle_settings(data)
    for k in params.DEFAULTS:
        if k not in data:
            data[k] = params.DEFAULTS[k]
    return image.get_html(data)

@app.route('/api/card.jpg', methods=['GET', 'POST'])
@app.route('/api/generate', methods=['GET', 'POST'])
def generate_image(data=None):
    html = generate_html(data)
    result = image.from_html(html)
    return send_file(io.BytesIO(result), mimetype='image/jpeg')

@app.route('/api/cards/<int:id>.jpg')
def get_card(id):
    db = storage.JSONStorage()
    try:
        return generate_image(db.get(id))
    except IndexError:
        abort(404)

@app.route('/api/register', methods=['GET', 'POST'])
def register():
    data = filter_data()
    db = storage.JSONStorage()
    index = db.insert(data)
    db.commit()
    return jsonify({
        'id': index,
        'url': current_app.config.get('PUBLIC_URI') + url_for('get_card', id=index)
    })

def get_data_from_example(name):
    path = root_path / '../examples/requests/{}.json'.format(name)
    try:
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
    return generate_image(get_data_from_example(name))
