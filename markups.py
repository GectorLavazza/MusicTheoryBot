from telebot.util import quick_markup

start_markup = quick_markup({
    'Main menu 🏠': {'callback_data': 'Main'}
}, row_width=1)

intervals_exercise_markup = quick_markup({
    'Exercise more 💪': {'callback_data': 'Intervals hearing'},
    'Main menu 🏠': {'callback_data': 'Main'}
}, row_width=1)

instrument_markup = quick_markup({
    'Piano 🎹': {'callback_data': 'piano'},
    'Guitar 🎸': {'callback_data': 'guitar'},
    'Main menu 🏠': {'callback_data': 'Main'}
}, row_width=2)

notes_exercise_markup = quick_markup({
    'Exercise more 💪': {'callback_data': 'Notes hearing'},
    'Main menu 🏠': {'callback_data': 'Main'}
}, row_width=1)

main_markup = quick_markup({
    'Build a scale 🎼': {'callback_data': 'Scale'},
    'Build an interval 🎵': {'callback_data': 'Intervals'},
    'Build a chord 🎶': {'callback_data': 'Chords'},
    'Ear training 🎧': {'callback_data': 'Training'}
}, row_width=2)

notes_markup = quick_markup({
    'C': {'callback_data': 'C'},
    'C#\Db': {'callback_data': 'C#\Db'},
    'D': {'callback_data': 'D'},
    'D#\Eb': {'callback_data': 'D#\Eb'},
    'E': {'callback_data': 'E'},
    'F': {'callback_data': 'F'},
    'F#\Gb': {'callback_data': 'F#\Gb'},
    'G': {'callback_data': 'G'},
    'G#\Ab': {'callback_data': 'G#\Ab'},
    'A': {'callback_data': 'A'},
    'A#\Bb': {'callback_data': 'A#\Bb'},
    'B\Cb': {'callback_data': 'B\Cb'},
    'Back ↩️': {'callback_data': 'Back'}
}, row_width=4)

scale_markup = quick_markup({
    'Major': {'callback_data': 'Major'},
    'Minor': {'callback_data': 'Minor'},
    'Major Pentatonic': {'callback_data': 'Major Pentatonic'},
    'Minor Pentatonic': {'callback_data': 'Minor Pentatonic'},
    'Blues': {'callback_data': 'Blues'},
    'Dorian': {'callback_data': 'Dorian'},
    'Back ↩️': {'callback_data': 'Back'}
}, row_width=2)

finish_markup = quick_markup({
    'Back ↩️': {'callback_data': 'Back'},
    'Main menu 🏠': {'callback_data': 'Main'},
}, row_width=2)

scale_finish_markup = quick_markup({
    'Back ↩️': {'callback_data': 'Back'},
    'Main menu 🏠': {'callback_data': 'Main'},
    'More songs ➕': {'callback_data': 'More'}
}, row_width=2)

intervals_markup = quick_markup({
    'Minor 2nd': {'callback_data': 'Minor 2nd'},
    'Major 2nd': {'callback_data': 'Major 2nd'},
    'Minor 3rd': {'callback_data': 'Minor 3rd'},
    'Major 3rd': {'callback_data': 'Major 3rd'},
    '4th': {'callback_data': '4th'},
    '5th': {'callback_data': '5th'},
    'Minor 6th': {'callback_data': 'Minor 6th'},
    'Major 6th': {'callback_data': 'Major 6th'},
    'Minor 7th': {'callback_data': 'Minor 7th'},
    'Major 7th': {'callback_data': 'Major 7th'},
    'Tritone': {'callback_data': 'Tritone'},
    'Back ↩️': {'callback_data': 'Back'}
}, row_width=2)

chords_markup = quick_markup({
    'Major': {'callback_data': 'maj'},
    'Minor': {'callback_data': 'min'},
    'Diminished': {'callback_data': 'dim'},
    'Augmented': {'callback_data': 'aug'},
    'Back ↩️': {'callback_data': 'Back'}
}, row_width=2)

chords_additions_markup = quick_markup({
    '...6': {'callback_data': '6'},
    '...maj6': {'callback_data': 'maj6'},
    '...7': {'callback_data': '7'},
    '...maj7': {'callback_data': 'maj7'},
    'No additions': {'callback_data': 'None'},
    'Back ↩️': {'callback_data': 'Back'}
}, row_width=2)

training_markup = quick_markup({
    'Notes': {'callback_data': 'Notes hearing'},
    'Intervals': {'callback_data': 'Intervals hearing'},
    'Back ↩️': {'callback_data': 'Back'}
}, row_width=2)
