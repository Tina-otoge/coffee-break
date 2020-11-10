import json

from flask import abort, render_template

from coffeebreak import app, params, root_path

@app.route('/')
def index():
    return render_template('index.html', inputs=params.ARGUMENTS)

@app.route('/prefilled/<name>')
def prefilled(name):
    path = root_path / '../examples/requests/{}.json'.format(name)
    try:
        with open(path) as f:
            data = json.load(f)
    except FileNotFoundError:
        abort(404)
    for k in params.OBJECTS:
        data[k] = json.dumps(data.get(k, params.DEFAULTS.get(k)))
    return render_template('index.html', inputs=params.ARGUMENTS, prefilled=data)
