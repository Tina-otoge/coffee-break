import io

import imgkit
import jinja2

from coffeebreak import root_path

def get_html(data={}, template_path=root_path / 'templates/card.html'):
    with open(template_path) as f:
        jinja_code = f.read()
    template = jinja2.Template(jinja_code)
    return template.render(data)

def from_html(html, out=None, template_path=None, options={}):
    options['width'] = options.get('width', 380)
    return imgkit.from_string(html, out, options)
