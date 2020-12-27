from pathlib import Path
from flask import Flask

app = Flask(__name__)
app.config['PUBLIC_URI'] = 'http://localhost:5000'

@app.template_filter()
def idify(s: str):
    return s.replace('_', '-').replace(' ', '-').lower()

root_path = Path(__file__).parent

from . import routes
