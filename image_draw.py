from PIL import Image, ImageDraw, ImageFont

# Define constants for the original image size and key sizes
ORIGINAL_IMAGE_WIDTH = 1120
ORIGINAL_IMAGE_HEIGHT = 200
WHITE_KEY_WIDTH = 80
WHITE_KEY_HEIGHT = ORIGINAL_IMAGE_HEIGHT
BLACK_KEY_WIDTH = 40
BLACK_KEY_HEIGHT = ORIGINAL_IMAGE_HEIGHT * 0.6


def draw_keyboard(user_id, notes_list):
    # Create a new image with white background
    image = Image.new("RGB",
                      (ORIGINAL_IMAGE_WIDTH * 2, ORIGINAL_IMAGE_HEIGHT * 2),
                      "white")
    draw = ImageDraw.Draw(image)

    # Draw white keys
    for i in range(0, ORIGINAL_IMAGE_WIDTH * 2, WHITE_KEY_WIDTH * 2):
        draw.rectangle(
            [i, 0, i + WHITE_KEY_WIDTH * 2, ORIGINAL_IMAGE_HEIGHT * 2],
            fill="white", outline="black")

    # Draw black keys
    black_key_positions = [60, 140, 300, 380, 460, 620, 700, 860, 940, 1020]
    for pos in black_key_positions:
        draw.rectangle(
            [pos * 2, 0, (pos + BLACK_KEY_WIDTH) * 2, BLACK_KEY_HEIGHT * 2],
            fill="black", outline="black")

    # Draw circles with note letters above the keys you choose
    keys = {'C': 0, 'C#\\Db': 1, 'D': 2, 'D#\\Eb': 3, 'E': 4, 'F': 5, 'F#\\Gb': 6,
            'G': 7, 'G#\\Ab': 8, 'A': 9, 'A#\\Bb': 10,
            'B\\Cb': 11}  # Map key positions to note letters

    font_size = 30
    font = ImageFont.truetype("data/arial.ttf", font_size)

    previous_note = notes_list[0]
    current_octave = 1

    for note in notes_list:

        key_pos = keys[note]
        letter = note.split('\\')[0]

        # if keys[previous_note] + keys[note] > 12:
        #     current_octave = 2

        if keys[note] < keys[previous_note] or current_octave == 2:
            current_octave = 2
            key_pos += 14

        if '#' in note:
            x_center = key_pos // 2 * WHITE_KEY_WIDTH * 2 + BLACK_KEY_WIDTH * 4
            y_center = ORIGINAL_IMAGE_HEIGHT * 0.25 * 2
            circle_radius = 30
            draw.ellipse([x_center - circle_radius, y_center - circle_radius,
                          x_center + circle_radius, y_center + circle_radius],
                         outline="red", fill="red")
            draw.text((x_center - 17, y_center - 16), letter, fill="white",
                      font=font)
        else:
            x_center = (
                               key_pos + 1) // 2 * WHITE_KEY_WIDTH * 2 + WHITE_KEY_WIDTH
            y_center = ORIGINAL_IMAGE_HEIGHT * 0.75 * 2
            circle_radius = 30
            draw.ellipse([x_center - circle_radius, y_center - circle_radius,
                          x_center + circle_radius, y_center + circle_radius],
                         outline="red", fill="red")
            draw.text((x_center - 11, y_center - 16), letter, fill="white",
                      font=font)

        previous_note = note

    # Save the image
    image.save(f"{user_id}_keyboard.jpg")
    # image.show()

# if __name__ == "__main__":
#     draw_keyboard(user_id, ['B', 'C#', 'D', 'E', 'F#', 'G', 'A'])
