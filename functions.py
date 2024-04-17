import csv
import random
from pprint import pprint

from variables import *


def add_roman(scale):
    res = []

    for note in scale:
        roman = ROMAN[scale.index(note) + 1]
        res.append(f'{roman} *{note}*')

    return res


def get_scale(key, scale, notes=NOTES * 2, scales=SCALES):
    res = [key]
    current_index = notes.index(key)
    scale_formula = scales[scale]

    for step in scale_formula[:-1]:
        next_note_index = current_index + step
        res.append(notes[next_note_index])
        current_index += step

    res = add_roman(res)

    return res


def get_interval(note, interval, notes=NOTES * 2, intervals=INTERVALS):
    current_index = notes.index(note)
    interval_lenght = intervals[interval]

    res = notes[current_index + interval_lenght]

    return res


def get_chord(root, chord, addition=0, notes=NOTES * 2,
              chords=CHORDS, chord_additions=CHORD_ADDITIONS):
    res = [root]
    if addition and addition != 'None':
        chord_formula = chords[chord] + chord_additions[addition]
    else:
        chord_formula = chords[chord]

    current_index = notes.index(root)

    for step in chord_formula:
        next_note_index = current_index + step
        res.append(notes[next_note_index])
        current_index += step

    res = ' – '.join(res)

    return res


def get_songs(filename='dataset.csv', amount=1, key='0', mode='0'):
    with open(filename, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        data = sorted(reader, key=lambda el: el[5])[:-1][::-1]

        possible_songs = [f'_{row[2]}_ – _{row[4]}_' for row in data if row[10] == key and row[12] == mode]

        res = random.choices(possible_songs, k=amount)

        return res
