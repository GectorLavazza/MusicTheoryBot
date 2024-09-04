from PIL import Image, ImageDraw, ImageFont
import roman


def draw_isntrument(user_id, notes_list, instrument):
    if instrument == 'piano':
        draw_piano(user_id, notes_list)
    elif instrument == 'guitar':
        draw_guitar(user_id, notes_list)


def draw_piano(user_id, notes_list):
    image_width = 1120
    image_height = 200
    white_key_width = 80
    white_key_height = image_height
    black_key_width = 40
    black_key_height = image_height * 0.6

    image = Image.new("RGB",
                      (image_width * 2, image_height * 2),
                      "white")
    draw = ImageDraw.Draw(image)

    for i in range(0, image_width * 2, white_key_width * 2):
        draw.rectangle(
            [i, 0, i + white_key_width * 2, image_height * 2],
            fill="white", outline="black")

    black_key_positions = [60, 140, 300, 380, 460, 620, 700, 860, 940, 1020]
    for pos in black_key_positions:
        draw.rectangle(
            [pos * 2, 0, (pos + black_key_width) * 2, black_key_height * 2],
            fill="black", outline="black")

    keys = {'C': 0, 'C#\\Db': 1, 'D': 2, 'D#\\Eb': 3, 'E': 4, 'F': 5,
            'F#\\Gb': 6,
            'G': 7, 'G#\\Ab': 8, 'A': 9, 'A#\\Bb': 10,
            'B\\Cb': 11}

    font_size = 30
    font = ImageFont.truetype("data/arial.ttf", font_size)

    previous_note = notes_list[0]
    current_octave = 1

    for note in notes_list:

        key_pos = keys[note]
        letter = note.split('\\')[0]

        if keys[note] < keys[previous_note] or current_octave == 2:
            current_octave = 2
            key_pos += 14

        if '#' in note:
            x_center = key_pos // 2 * white_key_width * 2 + black_key_width * 4
            y_center = image_height * 0.25 * 2
            circle_radius = 30
            draw.ellipse([x_center - circle_radius, y_center - circle_radius,
                          x_center + circle_radius, y_center + circle_radius],
                         fill="red")
            draw.text((x_center - 17, y_center - 16), letter, fill="white",
                      font=font)
        else:
            x_center = ((key_pos + 1) // 2 *
                        white_key_width * 2 + white_key_width)
            y_center = image_height * 0.75 * 2
            circle_radius = 30
            draw.ellipse([x_center - circle_radius, y_center - circle_radius,
                          x_center + circle_radius, y_center + circle_radius],
                         fill="red")
            draw.text((x_center - 11, y_center - 16), letter, fill="white",
                      font=font)

        previous_note = note

    image.save(f"{user_id}_instrument.jpg")


def draw_guitar(user_id, notes_list):
    image_width = 1600
    image_height = 400

    strings = 6
    frets = 11

    string_color = 'black'
    fret_color = 'gray'
    background_color = 'white'

    note_positions = {
        'E': [0, 5, 9, 2, 7, 0],
        'F': [1, 6, 10, 3, 8, 1],
        'F#\\Gb': [2, 7, 11, 4, 9, 2],
        'G': [3, 8, 0, 5, 10, 3],
        'G#\\Ab': [4, 9, 1, 6, 11, 4],
        'A': [5, 10, 2, 7, 0, 5],
        'A#\\Bb': [6, 11, 3, 8, 1, 6],
        'B\\Cb': [7, 0, 4, 9, 2, 7],
        'C': [8, 1, 5, 10, 3, 8],
        'C#\\Db': [9, 2, 6, 11, 4, 9],
        'D': [10, 3, 7, 0, 5, 10],
        'D#\\Eb': [11, 4, 8, 1, 6, 11]
    }

    fret_spacing = image_width / (frets + 1)
    string_spacing = image_height // (strings + 1)

    img = Image.new('RGB', (image_width, image_height), color=background_color)

    draw = ImageDraw.Draw(img)

    for i in range(frets):
        x = (i + 1) * fret_spacing
        draw.line([(x, 0), (x, image_height)], fill=fret_color, width=2)
        font_fret = ImageFont.truetype("data/arial.ttf", 16)
        draw.text((x - fret_spacing / 2 - 3, 10), roman.toRoman(i),
                  fill='black', font=font_fret)
        if i == frets - 1:
            x = (i + 2) * fret_spacing
            draw.text((x - fret_spacing / 2 - 3, 10), roman.toRoman(i + 1),
                      fill='black', font=font_fret)

    font = ImageFont.truetype("data/arial.ttf", 30)

    for string_num in range(strings):

        y = (string_num + 1) * string_spacing
        draw.line([(0, y), (image_width, y)], fill=string_color, width=10)

        for note in notes_list:
            note_position = note_positions[note][string_num]
            note_to_draw = note.split('\\')[0]

            if notes_list.index(note) == 0:
                circle_color = 'red'
            else:
                circle_color = 'black'

            x = (note_position + 0.5) * fret_spacing

            circle_radius = 26
            draw.ellipse([(x - circle_radius, y - circle_radius),
                          (x + circle_radius, y + circle_radius)],
                         fill=circle_color)
            if '#' in note:
                x_offset = 32
            else:
                x_offset = 20
            draw.text((x - x_offset / 2, y - 32 / 2), note_to_draw,
                      fill='white',
                      font=font)

    img.save(f'{user_id}_instrument.jpg')
