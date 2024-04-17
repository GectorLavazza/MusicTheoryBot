from markups import scale_markup, intervals_markup, chords_markup

API_TOKEN = '7161683104:AAHqONitwtt3N4x2Wx-2MFMxC55f-d0ShVU'

NOTES = ['C', 'C#\Db', 'D', 'D#\Eb', 'E', 'F',
         'F#\Gb', 'G', 'G#\Ab', 'A', 'A#\Bb', 'B\Cb']

SCALES = {
    'Major': [2, 2, 1, 2, 2, 2, 1],
    'Minor': [2, 1, 2, 2, 1, 2, 2],
    'Major Pentatonic': [2, 2, 3, 2, 3],
    'Minor Pentatonic': [3, 2, 2, 3, 2],
    'Blues': [3, 2, 1, 1, 3, 2],
    'Dorian': [2, 1, 2, 2, 2, 1, 2]
}

INTERVALS = {
    'Minor 2nd': 1,
    'Major 2nd': 2,
    'Minor 3rd': 3,
    'Major 3rd': 4,
    '4th': 5,
    'Tritone': 6,
    '5th': 7,
    'Minor 6th': 8,
    'Major 6th': 9,
    'Minor 7th': 10,
    'Major 7th': 11
}

CHORDS = {
    'maj': [4, 3],
    'min': [3, 4],
    'dim': [3, 3],
    'aug': [4, 4]
}

CHORD_ADDITIONS = {
    '6': [1],
    'maj6': [2],
    '7': [3],
    'maj7': [4],
    'None': ''
}

ROMAN = {
    1: 'Ⅰ.',
    2: 'Ⅱ.',
    3: 'Ⅲ.',
    4: 'Ⅳ.',
    5: 'Ⅴ.',
    6: 'Ⅵ.',
    7: 'Ⅶ.'
}

NOTES_TO_NUMBERS = {
    'C': '0',
    'C#\Db': '1',
    'D': '2',
    'D#\Eb': '3',
    'E': '4',
    'F': '5',
    'F#\Gb': '6',
    'G': '7',
    'G#\Ab': '8',
    'A': '9',
    'A#\Bb': '10',
    'B\Cb': '11'
}

SCALES_TO_NUMBERS = {
    'Major': '1',
    'Minor': '0'
}

last_messages = []
destination = ''
current_note = ''
current_scale = ''
current_interval = ''
current_chord = ''
current_addition = ''

destinations = {
    'Scale': {'text': 'OK. In which mode?', 'markup': scale_markup},
    'Intervals': {'text': 'OK. What interval?', 'markup': intervals_markup},
    'Chords': {'text': 'OK. What chord?', 'markup': chords_markup}
}

callback_queries_types = {
    'main': ['Main', 'Back'],
    'home': ['Basics', 'Scale', 'Intervals', 'Chords']
}
