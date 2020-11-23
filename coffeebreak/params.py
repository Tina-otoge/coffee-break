ARGUMENTS = {
    'username': None,
    'player_code': 'Used in some games to add to a friendlist',
    'rank': 'The dan rank or skill level of a player',
    'avatar': 'Must be an URL',
    'playstyle': 'Precision on the playstyle, such as controller or keyboard',
    'profile_extras': 'Extra infos, arcade, global rank, country...',

    'game': None,
    'title': None,
    'subtitle': None,
    'artist': None,
    'subartist': None,
    'genre': None,
    'bpm': None,
    'jacket': 'Must be an URL',

    'mode': 'Useful for games with SP and DP modes',
    'level': 'The level of the chart difficulty',
    'difficulty': 'The name of the chart difficulty',
    'notes_count': 'Amount of notes',
    'max_chart_combo': 'Maximum combo reachable on the chart',
    'creator': 'The creator of the chart/map',
    'mods': 'List of mods, use shortnames/acronyms if possible<br>JSON formatted, ie: ["EZ", "FL"]',

    'clear_type': 'The clear type of medal, such as CLEARED, FAILED, HARD CLEAR, FULLCOMBO, etc',
    'score': None, # actual score
    'grade': 'The grade or rank, such as A, AA+, S, etc',
    'accuracy': None,
    'hp': 'Must be an integer from 0 to 100',
    'max_combo': 'Maximum combo reached by the player',
    'breaks': 'Combo breaks',
    'pp': 'Performance points',

    'judges': 'Dictionary of judges mapping to their respective amounts<br>JSON formatted, ie: {"GREAT": 100, "GOOD": 10, "MISS": 2}',

    'date': 'The date on which the score was achieved',
    'copyright': 'A custom copyright notice',

    'class': 'Apply custom styles to certain elements',
    'settings': None,
}

DEFAULTS = {
    'class': {},
    'settings': {},
    'mods': [],

    # score
    'judges': {},

    'copyright': 'scorecard generated with coffee break ☕'
}

OBJECTS = ['class', 'settings', 'mods', 'judges']

TYPES = {
    'avatar': 'url',
    'jacket': 'url',
    'playstyle': {'radio': ['controller', 'keyboard', 'arcade']},
    'profile_extras': 'textarea',
    'bpm': {'label': 'BPM'},
    'mode': {'radio': ['SP', 'DP']},
    'notes_count': 'number',
    'clear_type': {'radio': ['FULLCOMBO', 'EXHARD CLEAR', 'HARD CLEAR', 'CLEARED', 'FAILED']},
    'hp': {'type': 'number', 'min': '0', 'max': '100', 'label': 'HP'},
    'max_combo': 'number',
    'max_chart_combo': 'number',
    'breaks': 'number',
    'pp': {'label': 'pp'},
    'date': 'date',
}
