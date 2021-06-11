import telebot
from telebot import types
bot = telebot.TeleBot("1763935068:AAEw63baPA3mul-18P5SzkE7tUxfqEWSjT4")


@bot.message_handler(commands=["start"])
def satart_message(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("Добавить нового бота")
    button2 = types.KeyboardButton("Инструкции")
    button3 = types.KeyboardButton("Помощь")
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Manybot поможет вам создать своего бота. С помощью Manybot вы сможете рассылать\
    сообщения пользователям бота, создавать свои команды и красивые меню.", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def answer_start_message(message):
    if message.text == "Добавить нового бота":
        bot.send_message(message.chat.id, "Для начала создай бота в BotFather.")
    elif message.text == "Инструкции":
        bot.send_message(message.chat.id, "1. Как создать бота\n Ответ: BotFather в помощь.")
    elif message.text == "Помощь":
        bot.send_message(message.chat.id, "Тут я вам помогу)")


print("Бот запущен!!!")


if __name__ == "__main__":
    bot.polling(none_stop=True)