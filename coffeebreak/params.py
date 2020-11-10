ARGUMENTS = {
    # player
    'avatar': 'Must be an URL',
    'game': None,
    'username': None,
    'player_code': 'Used in some games to add to a friendlist',
    'rank': 'The dan rank or skill level of a player',
    'playstyle': 'Precision on the playstyle, such as controller or keyboard',
    'profile_extras': 'Extra infos, arcade, global rank, country...',

    # song
    'title': None,
    'subtitle': None,
    'artist': None,
    'subartist': None,
    'genre': None,
    'bpm': None,
    'jacket': 'Must be an URL',

    # chart
    'mode': 'Useful for games with SP and DP modes',
    'difficulty': 'The name of the chart difficulty',
    'level': 'The level of the chart difficulty',
    'creator': 'The creator of the chart/map',
    'notes_count': 'Amount of notes',
    'mods': 'List of mods, use shortnames/acronyms if possible',

    # score
    'grade': 'The grade or rank, such as A, AA+, S, etc',
    'clear_type': 'The clear type of medal, such as CLEARED, FAILED, HARD CLEAR, FULLCOMBO, etc',
    'score': None, # actual score
    'accuracy': None,
    'hp': 'Must be an integer from 0 to 100',
    'max_combo': 'Maximum combo reached by the player',
    'max_chart_combo': 'Maximum combo reachable on the chart',
    'breaks': 'Combo breaks',
    'pp': 'Performance points',

    # judges
    'judges': 'Dictionary of judges mapping to their respective amounts',

    # footer
    'date': 'The date on which the score was achieved',
    'copy': 'A custom copyright notice',

    # customization
    'class': 'Apply custom styles to certain elements',
    'settings': None,
}

DEFAULTS = {
    'class': {},
    'settings': {},
    'mods': [],

    # score
    'judges': {},

    'copy': 'scorecard generated with coffee break ☕'
}

OBJECTS = ['class', 'settings', 'mods', 'judges']
