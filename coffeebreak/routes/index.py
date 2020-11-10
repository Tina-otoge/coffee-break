from flask import render_template

from coffeebreak import app, params

@app.route('/')
def index():
    return render_template('index.html', inputs=params.ARGUMENTS)
