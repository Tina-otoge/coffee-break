from datetime import datetime

ARGUMENTS = {
    # customization
    'class': {},
    'background': None,

    # player
    'avatar': None,
    'game': None,
    'username': None,
    'player_code': None,
    'rank': None, # dan

    # song
    'title': None,
    'subtitle': None,
    'artist': None,
    'subartist': None,
    'genre': None,
    'bpm': None,
    'jacket': None, # URL

    # chart
    'mode': None,
    'difficulty_name': None,
    'difficulty_level': None,
    'notes_count': None,

    # score
    'playstyle': None, # input type (controller, keyboard)
    'grade': None,
    'clear_type': None,
    'total': None, # actual score
    'hp': None, # from 0 to 100
    'max_combo': None,
    'max_chart_combo': None,

    # judges
    'judges': [], # {"judge_name": "score"}

    # footer
    'date': datetime.now().replace(microsecond=0),
    'copy': 'scorecard generated with coffee break ☕'
}
