import telebot
from my_env.tg import config
import random

from telebot import types
TOKEN = '1287545960:AAHVcVh8yxnVfAkP9B-tsf5WLbJKNcQvUJQ'
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('D:\stick_fire.jpg', 'rb')#здесь замени путь до файлов на соответсвующий 
    bot.send_sticker(message.chat.id, sti)



    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число")
    item2 = types.KeyboardButton("Как дела?")
    item3 = types.KeyboardButton("Анекдот")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - {1.first_name}, бот созданный чтобы быть подопытным кроликом.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])

def lalala(message):
    sti3 = open('D:\stick_margo.jpg', 'rb')#здесь замени путь до файлов на соответсвующий
    sti4 = open('D:\stick_anek.jpg', 'rb')

    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)

        elif message.text == 'Анекдот':
            bot.send_message(message.chat.id, 'Идут два моряка по пристани. Один говорит:"А я не моряк"')
            bot.send_sticker(message.chat.id, sti4)

        else:
            bot.send_sticker(message.chat.id, sti3)




@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Это хорошо')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает')



    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)