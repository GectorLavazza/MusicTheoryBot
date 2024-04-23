from PIL import Image, ImageDraw, ImageFont

# Define constants for the original image size and key sizes
ORIGINAL_IMAGE_WIDTH = 1120
ORIGINAL_IMAGE_HEIGHT = 200
WHITE_KEY_WIDTH = 80
WHITE_KEY_HEIGHT = ORIGINAL_IMAGE_HEIGHT
BLACK_KEY_WIDTH = 40
BLACK_KEY_HEIGHT = ORIGINAL_IMAGE_HEIGHT * 0.6


def draw_keyboard(notes_list):
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
    keys = {'C': 1, 'C#': 2, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6,
            'G': 7, 'G#': 8, 'A': 9, 'A#': 10,
            'B': 11}  # Map key positions to note letters

    font_size = 30
    font = ImageFont.truetype("data/arial.ttf", font_size)

    previous_note = notes_list[0]

    for note in notes_list:

        key_pos = keys[note]

        if keys[note] < keys[previous_note]:
            key_pos += 12

        if '#' in note:
            x_center = key_pos // 2 * WHITE_KEY_WIDTH * 2 + BLACK_KEY_WIDTH * 4
            y_center = ORIGINAL_IMAGE_HEIGHT * 0.25 * 2
            circle_radius = 30
            draw.ellipse([x_center - circle_radius, y_center - circle_radius,
                          x_center + circle_radius, y_center + circle_radius],
                         outline="red", fill="red")
            draw.text((x_center - 17, y_center - 16), note, fill="white",
                      font=font)
        else:
            x_center = (
                                   key_pos + 1) // 2 * WHITE_KEY_WIDTH * 2 + WHITE_KEY_WIDTH
            y_center = ORIGINAL_IMAGE_HEIGHT * 0.75 * 2
            circle_radius = 30
            draw.ellipse([x_center - circle_radius, y_center - circle_radius,
                          x_center + circle_radius, y_center + circle_radius],
                         outline="red", fill="red")
            draw.text((x_center - 11, y_center - 16), note, fill="white",
                      font=font)

    # Save the image
    image.save("piano_keyboard.jpg")
    image.show()


if __name__ == "__main__":
    draw_keyboard(['F', 'D#'])
