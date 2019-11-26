import imgkit
from jinja2 import Template

test_full = {
    'avatar': 'https://tina.moe/img/magileine.png',
    'username': 'N.TINA',
    'player_code': '0573-0573',
    'rank': 'SL10',
    'game': 'SOUND VOLTEX',

    'title': 'Brain Power',
    'subtitle': 'ooooooo-',
    'artist': 'NOMA',
    'subartist': 'The Brain Power man',
    'genre': 'osu! song',
    'bpm': '170-173',
    'jacket': 'https://remywiki.com/images/thumb/e/e7/Brain_Power.png/200px-Brain_Power.png',

    'mode': 'DP',
    'difficulty_name': 'EXHAUST',
    'difficulty_level': 16,
    'max_chart_combo': 1597,
    'max_chart_notes': 'idk lol',

    'playstyle': 'controller',
    'medal': 'AAA',
    'clear_type': 'HARD CLEAR',
    'hp': 94.45,
    'total': 9874123,
    'max_combo': 1573,
    'scores': {'CRITICAL': 1000, 'NEAR': 573, 'ERROR': 24},

    'date': '2019-11-25 4:24PM',
    'copy': 'cool stuff',

    'class': {
        'difficulty_name': 'red',
        'medal': 'gold',
        'clear_type': 'red',
        'CRITICAL': 'yellow',
    }
}
test_normal = {
    'avatar': 'https://tina.moe/img/magileine.png',
    'username': 'N.TINA',
    'game': 'SOUND VOLTEX',

    'title': 'Brain Power',
    'artist': 'NOMA',
    'bpm': '170-173',
    'jacket': 'https://remywiki.com/images/thumb/e/e7/Brain_Power.png/200px-Brain_Power.png',

    'difficulty_name': 'EXHAUST',
    'difficulty_level': 16,

    'medal': 'AAA',
    'clear_type': 'HARD CLEAR',
    'hp': 94.45,
    'total': 9874123,
    'max_combo': 1573,
    'scores': {'CRITICAL': 1000, 'NEAR': 573, 'ERROR': 24},

    'date': '2019-11-25 4:24PM',
    'copy': 'cool stuff',

    'class': {
        'difficulty_name': 'red',
        'medal': 'gold',
        'clear_type': 'red',
        'CRITICAL': 'yellow',
    }
}
test_mini = {
    'username': 'N.TINA',

    'title': 'Brain Power',
    'artist': 'NOMA',

    'difficulty_level': 16,

    'total': 9874123,
    'scores': {'CRITICAL': 1000, 'NEAR': 573, 'ERROR': 24},

    'class': {
        'difficulty_name': 'red',
        'medal': 'gold',
        'clear_type': 'red',
        'CRITICAL': 'yellow',
    }
}

def batch_test():
    template = get_template()
    html = generate_html(test_mini, template=template)
    with open('test/mini.html', 'w') as f:
        f.write(html)
    imgkit.from_string(html, 'test/mini.png', options={'width': 380})
    html = generate_html(test_normal, template=template)
    with open('test/normal.html', 'w') as f:
        f.write(html)
    imgkit.from_string(html, 'test/normal.png', options={'width': 380})
    html = generate_html(test_full, template=template)
    with open('test/full.html', 'w') as f:
        f.write(html)
    imgkit.from_string(html,'test/full.png', options={'width': 380})

def get_template():
    with open('template.html') as f:
        template = f.read()
    return Template(template)

def generate_html(data={}, template=None):
    data['class'] = data.get('class', {})
    data['scores'] = data.get('scores', {})
    if template is None:
        template = get_template()
    return template.render(data)

def generate_picture(data={}, template=None, out=None):
    html = generate_html(data, template)
    return imgkit.from_string(html, out, options={'width': 380})
