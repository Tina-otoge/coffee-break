from pathlib import Path
from flask import Flask

app = Flask(__name__)
app.config['PUBLIC_URI'] = 'http://localhost:5000'

root_path = Path(__file__).parent

from . import routes
