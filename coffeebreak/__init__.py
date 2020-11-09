from pathlib import Path
from flask import Flask

app = Flask(__name__)

root_path = Path(__file__).parent

from . import routes
