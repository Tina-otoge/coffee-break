import json

from flask import abort, render_template

from coffeebreak import app, idify, params, root_path

class Input:
    def __init__(self, name, params={}):
        self.name = name
        self.id = idify(name)
        self.label = params.get('label') or (self.name[0].upper() + self.name[1:].replace('_', ' '))
        self.params = params

    @classmethod
    def from_params(self):
        result = []
        for i in params.ARGUMENTS:
            added_params = {}
            if i in params.TYPES:
                if isinstance(params.TYPES[i], str):
                    added_params['type'] = params.TYPES[i]
                else:
                    added_params.update(params.TYPES[i])
                if 'radio' in added_params:
                    added_params['type'] = 'radio'
            else:
                added_params['type'] = 'text'
            added_params['description'] = params.ARGUMENTS[i]
            result.append(Input(i, params=added_params))
        return result


@app.route('/')
def index():
    return render_template('index.html', inputs=Input.from_params())

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
    return render_template('index.html', inputs=Input.from_params(), prefilled=data)
