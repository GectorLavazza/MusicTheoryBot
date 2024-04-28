import os
import json
import asyncio

from telebot import *
from telebot.async_telebot import AsyncTeleBot

from functions import *
from variables import *
from markups import *
from pitch_shift import *
from image_draw import *

bot = AsyncTeleBot(API_TOKEN)

with open('users.json') as users_data:
    users = json.load(users_data)


# Handle '/start'
@bot.message_handler(commands=['start'])
async def send_welcome(message):
    chat_id = message.chat.id
    user_id = str(message.from_user.id)

    users[user_id] = {'last_messages': [],
                      'last_message': [],
                      'destination': '',
                      'current_note': '',
                      'current_scale': '',
                      'current_interval': '',
                      'current_chord': '',
                      'current_addition': '',
                      'last_songs': [],
                      'notes_shifts': [],
                      'responded': False,
                      'note_answer': '',
                      'last_note': '',
                      'results': [],
                      'intervals': [],
                      'last_interval': '',
                      'interval_answer': '',
                      'exercising': False,
                      'instrument': 'piano'}

    await bot.send_message(chat_id, """\
Hi there, I am MusicTheoryBot 🎶
I am here to help you with music theory!
Maybe you want me to build a scale or give you some basic information. 
Whatever you want!\n\nCheck news about the bot here: https://t.me/music_theory_helper_bot_news
""", reply_markup=start_markup)


# Handle '/home'
@bot.message_handler(commands=['home'])
async def send_welcome(message):
    chat_id = message.chat.id
    user_id = str(message.from_user.id)

    users[user_id]['exercising'] = False
    await bot.send_message(chat_id, "*Choose from the menu:*",
                           reply_markup=main_markup,
                           parse_mode="Markdown")


@bot.message_handler(commands=['instrument'])
async def send_welcome(message):
    chat_id = message.chat.id
    user_id = str(message.from_user.id)

    users[user_id]['exercising'] = False

    await bot.send_message(chat_id,
                           f"_Instrument_ affects audio and pictures.\n\n"
                           f"Your instrument is now "
                           f"*{users[user_id]['instrument']}*.\nWant to change it?",
                           reply_markup=instrument_markup,
                           parse_mode="Markdown")


# Handle non-command messages
@bot.message_handler(func=lambda message: not message.text.startswith('/'))
async def handle_non_command_messages(message):
    # Handle non-command messages here
    if message.text == '@pav1en5kiy':
        await bot.send_message(message.chat.id,
                               "Oh boi, u got me.\n"
                               "Did ya now I'm an artist too?\n"
                               "Here: https://t.me/pav1en5kiyMusic")
    else:
        await bot.send_message(message.chat.id, "Please, send commands only.")


@bot.callback_query_handler(func=lambda call: call.data == 'Main')
async def main_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)
    users[user_id]['exercising'] = False

    if call.data == "Main":
        await bot.answer_callback_query(call.id, "Main menu")
        message = await bot.send_message(chat_id,
                                         "*Choose from the menu:*",
                                         reply_markup=main_markup,
                                         parse_mode="Markdown")
        users[user_id]['last_message'] = [message.message_id]

        users[user_id]['last_messages'].append(users[user_id]['last_message'])


@bot.callback_query_handler(func=lambda call: call.data == 'Back')
async def back_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)
    users[user_id]['exercising'] = False

    if call.message.id not in users[user_id]['last_message']:
        await bot.answer_callback_query(call.id, "Can't go back")
    else:
        await bot.answer_callback_query(call.id, "Back")

        for message in users[user_id]['last_message']:
            await bot.delete_message(chat_id, message)

        users[user_id]['last_messages'].pop(-1)
        users[user_id]['last_message'] = (
            users)[user_id]['last_messages'][-1]


@bot.callback_query_handler(func=lambda call: call.data == 'Scale')
async def scale_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)
    users[user_id]['exercising'] = False

    users[user_id]['last_songs'] = []

    await bot.answer_callback_query(call.id, "Build a scale")
    users[user_id]['destination'] = call.data
    message = await bot.send_message(chat_id,
                                     "Let's build a scale. In what key?",
                                     reply_markup=notes_markup,
                                     parse_mode="Markdown")
    users[user_id]['last_message'] = [message.message_id]

    users[user_id]['last_messages'].append(users[user_id]['last_message'])


@bot.callback_query_handler(func=lambda call: call.data == 'Intervals')
async def intervals_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)
    users[user_id]['exercising'] = False

    await bot.answer_callback_query(call.id, "Build an interval")
    users[user_id]['destination'] = call.data
    message = await bot.send_message(chat_id,
                                     "Let's build an interval. From what note?",
                                     reply_markup=notes_markup,
                                     parse_mode="Markdown")
    users[user_id]['last_message'] = [message.message_id]

    users[user_id]['last_messages'].append(users[user_id]['last_message'])


@bot.callback_query_handler(func=lambda call: call.data == 'Chords')
async def chords_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)
    users[user_id]['exercising'] = False

    await bot.answer_callback_query(call.id, "Build a chord")
    users[user_id]['destination'] = call.data
    message = await bot.send_message(chat_id,
                                     "Let's build a chord. From what note?",
                                     reply_markup=notes_markup,
                                     parse_mode="Markdown")
    users[user_id]['last_message'] = [message.message_id]

    users[user_id]['last_messages'].append(users[user_id]['last_message'])


@bot.callback_query_handler(func=lambda call: call.data == 'Training')
async def training_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)
    users[user_id]['exercising'] = False

    await bot.answer_callback_query(call.id, "Ear training")
    message = await bot.send_message(chat_id,
                                     "Let's complete some exercises. "
                                     "What do you want to train?",
                                     reply_markup=training_markup,
                                     parse_mode="Markdown")

    users[user_id]['last_message'] = [message.message_id]

    users[user_id]['last_messages'].append(users[user_id]['last_message'])


@bot.callback_query_handler(func=lambda call: call.data == 'piano')
async def main_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)
    users[user_id]['exercising'] = False

    users[user_id]['instrument'] = 'piano'

    await bot.answer_callback_query(call.id, "Piano")
    message = await bot.send_message(chat_id,
                                     'Your instrument is now *piano*.',
                                     reply_markup=start_markup,
                                     parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data == 'guitar')
async def main_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)
    users[user_id]['exercising'] = False

    users[user_id]['instrument'] = 'guitar'

    await bot.answer_callback_query(call.id, "Guitar")
    message = await bot.send_message(chat_id,
                                     'Your instrument is now *guitar*.',
                                     reply_markup=start_markup,
                                     parse_mode='Markdown')


@bot.callback_query_handler(func=lambda call: call.data in NOTES)
async def notes_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)

    users[user_id]["current_note"] = call.data

    await bot.answer_callback_query(call.id, users[user_id]["current_note"])

    if users[user_id]['destination'] != 'notes hearing':

        users[user_id]['exercising'] = False

        message = await bot.send_message(chat_id,
                                         destinations[
                                             users[user_id][
                                                 'destination']][
                                             'text'],
                                         reply_markup=
                                         destinations[
                                             users[user_id][
                                                 'destination']][
                                             'markup'],
                                         parse_mode="Markdown")
        users[user_id]['last_message'] = [message.message_id]

        users[user_id]['last_messages'].append(users[user_id]['last_message'])

    else:
        if call.data == users[user_id]['note_answer']:
            caption = f'*Correct!* The answer is _{users[user_id]["note_answer"]}_.'
            users[user_id]['results'].append(1)
        else:
            caption = f"*Sorry, you're wrong.* The answer is _{users[user_id]['note_answer']}_."
            users[user_id]['results'].append(0)

        await bot.edit_message_caption(caption, chat_id,
                                       users[user_id]['last_note'],
                                       parse_mode='Markdown')

        users[user_id]['responded'] = True


@bot.callback_query_handler(func=lambda call: call.data in SCALES)
async def scales_building_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)
    users[user_id]['exercising'] = False

    users[user_id]["current_scale"] = call.data

    scale = get_scale(users[user_id]["current_note"],
                      users[user_id]["current_scale"])
    draw_isntrument(user_id, scale, users[user_id]['instrument'])
    res = '\n'.join(add_roman(scale))

    songs_text = ''
    markup = finish_markup

    if users[user_id]["current_scale"] in ['Major', 'Minor']:
        current_songs = get_songs('dataset.csv', 10,
                                  NOTES_TO_NUMBERS[
                                      users[user_id]["current_note"]],
                                  SCALES_TO_NUMBERS[
                                      users[user_id]["current_scale"]])

        users[user_id]["last_songs"].append(current_songs)

        songs = '\n'.join(current_songs)
        songs_text = (f'\n\nHere are some songs written in '
                      f'_{users[user_id]["current_note"]} {users[user_id]["current_scale"]}_:\n\n{songs}')
        markup = scale_finish_markup

    await bot.answer_callback_query(call.id,
                                    f'{users[user_id]["current_scale"]} mode')

    get_shifted_scale(SCALES_TO_FILES[users[user_id]["current_scale"]],
                      users[user_id]["current_note"], user_id,
                      users[user_id]['instrument'])

    with open(f'{user_id}_scale.mp3', "rb") as audio_file:
        message = await bot.send_audio(chat_id, audio_file,
                                       f'Here is your _{users[user_id]["current_note"]} '
                                       f'{users[user_id]["current_scale"]}_ scale:\n\n{res}' + songs_text,
                                       parse_mode="Markdown",
                                       reply_markup=markup)

    with open(f'{user_id}_instrument.jpg', "rb") as photo_file:
        photo = await bot.send_photo(chat_id, photo_file)

    users[user_id]['last_message'] = [message.message_id, photo.message_id]

    users[user_id]['last_messages'].append(users[user_id]['last_message'])


@bot.callback_query_handler(func=lambda call: call.data in INTERVALS)
async def intervals_building_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)

    users[user_id]["current_interval"] = call.data

    await bot.answer_callback_query(call.id,
                                    users[user_id]["current_interval"])

    if users[user_id]['destination'] != 'intervals hearing':
        users[user_id]['exercising'] = False

        res = get_interval(users[user_id]["current_note"],
                           users[user_id]["current_interval"])
        draw_isntrument(user_id, [users[user_id]["current_note"], res],
                        users[user_id]['instrument'])

        interval_shift(INTERVALS_TO_FILES[users[user_id]["current_interval"]],
                       NOTES.index(users[user_id]["current_note"]), user_id,
                       users[user_id]['instrument'])

        with open(f'{user_id}_interval.mp3', "rb") as audio_file:
            message = await bot.send_audio(chat_id, audio_file,
                                           f'_{users[user_id]["current_interval"]} of {users[user_id]["current_note"]}_ is *{res}*',
                                           parse_mode="Markdown",
                                           reply_markup=finish_markup)

        with open(f'{user_id}_instrument.jpg', "rb") as photo_file:
            photo = await bot.send_photo(chat_id, photo_file)

        users[user_id]['last_message'] = [message.message_id, photo.message_id]

        users[user_id]['last_messages'].append(users[user_id]['last_message'])

    else:
        if call.data == users[user_id]['interval_answer']:
            caption = f'*Correct!* The answer is _{users[user_id]["interval_answer"]}_.'
            users[user_id]['results'].append(1)
        else:
            caption = f"*Sorry, you're wrong.* The answer is _{users[user_id]['interval_answer']}_."
            users[user_id]['results'].append(0)

        await bot.edit_message_caption(caption, chat_id,
                                       users[user_id]['last_interval'],
                                       parse_mode='Markdown')

        users[user_id]['responded'] = True


@bot.callback_query_handler(func=lambda call: call.data in CHORDS)
async def chords_building_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)
    users[user_id]['exercising'] = False

    users[user_id]["current_chord"] = call.data

    await bot.answer_callback_query(call.id, users[user_id]["current_chord"])

    if users[user_id]["current_chord"] == 'maj' or users[user_id][
        "current_chord"] == 'min':
        message = await bot.send_message(chat_id,
                                         f'OK. Any additions?',
                                         parse_mode="Markdown",
                                         reply_markup=chords_additions_markup)
        users[user_id]['last_message'] = [message.message_id]

        users[user_id]['last_messages'].append(users[user_id]['last_message'])

    else:
        chord = get_chord(root=users[user_id]["current_note"],
                          chord=users[user_id]["current_chord"])
        draw_isntrument(user_id, chord, users[user_id]['instrument'])
        res = ' – '.join(chord)

        get_shifted_chord(users[user_id]["current_note"],
                          users[user_id]["current_chord"], user_id,
                          users[user_id]['instrument'])

        with open(f'{user_id}_chord.mp3', "rb") as audio_file:
            message = await bot.send_audio(chat_id, audio_file,
                                           f'Here are notes of your '
                                           f'_{users[user_id]["current_note"]}{users[user_id]["current_chord"]}_'
                                           f' chord:\n*{res}*',
                                           parse_mode="Markdown",
                                           reply_markup=finish_markup)

        with open(f'{user_id}_instrument.jpg', "rb") as photo_file:
            photo = await bot.send_photo(chat_id, photo_file)

    users[user_id]['last_message'] = [message.message_id, photo.message_id]

    users[user_id]['last_messages'].append(users[user_id]['last_message'])


@bot.callback_query_handler(func=lambda call: call.data in CHORD_ADDITIONS)
async def chord_additions_building_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)
    users[user_id]['exercising'] = False

    users[user_id]["current_addition"] = call.data

    if users[user_id]["current_chord"] == 'maj':
        chord_sign = ''
    else:
        chord_sign = 'm'

    if users[user_id]["current_addition"] == 'None':
        addition_sign = ''
    else:
        addition_sign = users[user_id]["current_addition"]

    await bot.answer_callback_query(call.id,
                                    users[user_id]["current_addition"])

    chord = get_chord(root=users[user_id]['current_note'],
                      chord=users[user_id]['current_chord'],
                      addition=users[user_id]["current_addition"])
    res = ' – '.join(chord)
    draw_isntrument(user_id, chord, users[user_id]['instrument'])

    get_shifted_chord(users[user_id]["current_note"],
                      users[user_id]["current_chord"], user_id,
                      users[user_id]['instrument'],
                      addition_sign)

    with open(f'{user_id}_chord.mp3', "rb") as audio_file:
        message = await bot.send_audio(chat_id, audio_file,
                                       f'Here are notes of your '
                                       f'_{users[user_id]["current_note"]}{chord_sign}'
                                       f'{addition_sign}_ chord:\n*{res}*',
                                       parse_mode="Markdown",
                                       reply_markup=finish_markup)

    with open(f'{user_id}_instrument.jpg', "rb") as photo_file:
        photo = await bot.send_photo(chat_id, photo_file)

    users[user_id]['last_message'] = [message.message_id, photo.message_id]

    users[user_id]['last_messages'].append(users[user_id]['last_message'])


@bot.callback_query_handler(func=lambda call: call.data == 'More')
async def more_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)
    users[user_id]['exercising'] = False

    await bot.answer_callback_query(call.id, 'More songs')

    current_songs = get_songs('dataset.csv', 20,
                              NOTES_TO_NUMBERS[
                                  users[user_id]['current_note']],
                              SCALES_TO_NUMBERS[
                                  users[user_id]["current_scale"]])

    while any(
            map(lambda s: len(set(s).intersection(set(current_songs))) > 4,
                users[user_id]["last_songs"])):
        current_songs = get_songs('dataset.csv', 20,
                                  NOTES_TO_NUMBERS[
                                      users[user_id]['current_note']],
                                  SCALES_TO_NUMBERS[
                                      users[user_id]["current_scale"]])

    users[user_id]["last_songs"].append(current_songs)

    songs = '\n'.join(current_songs)
    songs_text = (f'\n\nHere are some more songs written in '
                  f'_{users[user_id]["current_note"]} {users[user_id]["current_scale"]}_:\n\n{songs}')

    message = await bot.send_message(chat_id, songs_text,
                                     parse_mode="Markdown",
                                     reply_markup=scale_finish_markup)
    users[user_id]['last_message'] = [message.message_id]

    users[user_id]['last_messages'].append(users[user_id]['last_message'])


@bot.callback_query_handler(func=lambda call: call.data == 'Notes hearing')
async def notes_training_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)

    users[user_id]['exercising'] = True

    users[user_id]['results'] = []
    users[user_id]['note_answer'] = ''
    users[user_id]['last_note'] = ''
    users[user_id]['notes_shifts'] = []

    users[user_id]['destination'] = 'notes hearing'

    await bot.answer_callback_query(call.id, 'Notes hearing')

    await bot.send_message(chat_id,
                           "You'll hear 5 notes. "
                           "Choose your answer below the audio. "
                           "Good luck!",
                           parse_mode="Markdown")

    users[user_id]['notes_shifts'] = random.sample(range(1, 12), k=5)

    for ns in users[user_id]['notes_shifts']:
        users[user_id]['responded'] = False

        na = note_answers[ns]
        users[user_id]['note_answer'] = na

        note_shift(ns, user_id, users[user_id]['instrument'])

        variants = [x for i, x in enumerate(NOTES) if i != NOTES.index(na)]
        answers = [na] + random.sample(variants, k=3)
        random.shuffle(answers)

        answers_markup = quick_markup({
            answers[0]: {'callback_data': answers[0]},
            answers[1]: {'callback_data': answers[1]},
            answers[2]: {'callback_data': answers[2]},
            answers[3]: {'callback_data': answers[3]},
        }, row_width=2)

        print()
        print(answers)
        print(na)

        with open(f'{user_id}_note.mp3', "rb") as audio_file:
            message = await bot.send_audio(chat_id, audio_file,
                                           reply_markup=answers_markup)
            users[user_id]['last_note'] = message.message_id

        while not users[user_id]['responded']:
            if not users[user_id]['exercising']:
                break
            await asyncio.sleep(1)

        if not users[user_id]['exercising']:
            break

    if users[user_id]['exercising']:
        right = users[user_id]['results'].count(1)
        wrong = users[user_id]['results'].count(0)

        if right > wrong:
            text = "Great job!"
        else:
            text = "Don't give up, try harder!"

        await bot.send_message(chat_id, f"That's all for now.\n"
                                        f"Your result is *{right}\\5*. {text}",
                               parse_mode='Markdown',
                               reply_markup=notes_exercise_markup)

        users[user_id]['exercising'] = False


@bot.callback_query_handler(func=lambda call: call.data == 'Intervals hearing')
async def intervals_training_callback_handler(call):
    chat_id = call.message.chat.id
    user_id = str(call.from_user.id)

    users[user_id]['exercising'] = True

    users[user_id]['results'] = []
    users[user_id]['interval_answer'] = ''
    users[user_id]['last_interval'] = ''
    users[user_id]['intervals'] = []

    users[user_id]['destination'] = 'intervals hearing'

    await bot.answer_callback_query(call.id, 'Intervals hearing')

    await bot.send_message(chat_id,
                           "You'll hear 5 intervals. "
                           "Choose your answer below the audio. "
                           "Good luck!",
                           parse_mode="Markdown")

    users[user_id]['intervals'] = random.sample(intervals_files, k=5)

    for ins in users[user_id]['intervals']:
        users[user_id]['responded'] = False

        ia = FILES_TO_INTERVALS[ins]
        users[user_id]['interval_answer'] = ia

        interval_shift(ins, random.randrange(0, 12), user_id,
                       users[user_id]['instrument'])

        variants = [x for i, x in enumerate(list(FILES_TO_INTERVALS.values()))
                    if i != list(FILES_TO_INTERVALS.values()).index(ia)]
        answers = [ia] + random.sample(variants, k=3)
        random.shuffle(answers)

        answers_markup = quick_markup({
            answers[0]: {'callback_data': answers[0]},
            answers[1]: {'callback_data': answers[1]},
            answers[2]: {'callback_data': answers[2]},
            answers[3]: {'callback_data': answers[3]},
        }, row_width=2)

        print()
        print(answers)
        print(ia)

        with open(f'{user_id}_interval.mp3', "rb") as audio_file:
            message = await bot.send_audio(chat_id, audio_file,
                                           reply_markup=answers_markup)
            users[user_id]['last_interval'] = message.message_id

        while not users[user_id]['responded']:
            if not users[user_id]['exercising']:
                break
            await asyncio.sleep(1)

        if not users[user_id]['exercising']:
            break

    if users[user_id]['exercising']:

        right = users[user_id]['results'].count(1)
        wrong = users[user_id]['results'].count(0)

        if right > wrong:
            text = "Great job!"
        else:
            text = "Don't give up, try harder!"

        await bot.send_message(chat_id, f"That's all for now.\n"
                                        f"Your result is *{right}\\5*. {text}",
                               parse_mode='Markdown',
                               reply_markup=intervals_exercise_markup)

        users[user_id]['exercising'] = False


if __name__ == "__main__":
    try:

        types = ['note', 'scale', 'chord', 'interval', 'instrument']

        for user in users.keys():
            for type in types:

                if types.index(type) <= 3:
                    filename = f'{user}_{type}.mp3'
                else:
                    filename = f'{user}_{type}.jpg'

                if os.path.exists(filename):
                    os.remove(filename)
                    print(f"File '{filename}' deleted successfully.")
                else:
                    print(f"File '{filename}' does not exist.")

        print(users)
        print('Running...')

        asyncio.run(bot.polling())

    except Exception as e:
        print(e)
    finally:
        with open('users.json', 'w') as users_data:
            json.dump(users, users_data)
        print("Data saved to data.json. Exiting...")
