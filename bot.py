import telebot
from funbot import *
from keyboardbot import *
bot = telebot.TeleBot("1763935068:AAEw63baPA3mul-18P5SzkE7tUxfqEWSjT4")


@bot.message_handler(commands=["start"])
def satart_message(message):
    bot.send_message(message.chat.id, f"Здравствуй {message.from_user.first_name}!\n\n{start()}",
                     reply_markup=keyboard1())


@bot.message_handler(commands=["addbot"])
def addbot_message(message):
    bot.send_message(message.chat.id, addbot())


@bot.message_handler(commands=["help"])
def help_message(message):
    bot.send_message(message.chat.id, help())


@bot.message_handler(commands=["manual"])
def manual_message(message):
    bot.send_message(message.chat.id, manual())


@bot.message_handler(commands=["cancel"])
def cancel_message(message):
    bot.send_message(message.chat.id, cancel(), reply_markup=keyboard1())


@bot.message_handler(content_types=["text"])
def answer_start_message(message):
    if message.text == "Добавить нового бота":
        bot.send_message(message.chat.id, addbot(), reply_markup=keyboard2())
    elif message.text == "Отменить":
        bot.send_message(message.chat.id, "Отменено", reply_markup=keyboard1())
    elif message.text == "Инструкции":
        bot.send_message(message.chat.id, manual())
    elif message.text == "Помощь":
        bot.send_message(message.chat.id, help())
    elif message.text == "Привет":
        bot.send_message(message.chat.id, f"Здравствуй {message.from_user.first_name}!\n\n{start()}",
                         reply_markup=keyboard1())
    else:
        bot.send_message(message.chat.id, "Я не знаю таких команд. Пропешите /help, "
                                          "чтобы посмотреть существующие команды.")


print("Бот запущен!!!")


if __name__ == "__main__":
    bot.polling(none_stop=True)