import telebot
from funbot import *
from keyboardbot import *
bot = telebot.TeleBot("1763935068:AAEw63baPA3mul-18P5SzkE7tUxfqEWSjT4")

@bot.message_handler(commands=["start"])
def satart_message(message):
    bot.send_message(message.chat.id, f"Здравствуй {message.from_user.first_name}!\n\n{start()}",
                     reply_markup=keyboard1())
#Обрабатывает команду /start

@bot.message_handler(commands=["addbot"])
def addbot_message(message):
    adbot = bot.send_message(message.chat.id, addbot(), reply_markup=keyboard2())
    bot.register_next_step_handler(adbot, ready_made_bot)
#Обрабатывает команду /addbot

@bot.message_handler(commands=["help"])
def help_message(message):
    bot.send_message(message.chat.id, help())
#Обрабатывает команду /help

@bot.message_handler(commands=["manual"])
def manual_message(message):
    bot.send_message(message.chat.id, manual())
#Обрабатывает команду /manual

@bot.message_handler(commands=["cancel"])
def cancel_message(message):
    bot.send_message(message.chat.id, cancel(), reply_markup=keyboard1())
#Обрабатывает команду /cancel

@bot.message_handler(content_types=["text"])
def answer_message(message):
    if message.text == "Добавить нового бота":
        adbot = bot.send_message(message.chat.id, addbot(), reply_markup=keyboard2())
        bot.register_next_step_handler(adbot, ready_made_bot)
    elif message.text == "Отменить":
        bot.send_message(message.chat.id, "Отменено", reply_markup=keyboard1())
    elif message.text == "Инструкции":
        bot.send_message(message.chat.id, manual())
    elif message.text == "Помощь":
        bot.send_message(message.chat.id, help())
    elif message.text == "Привет":
        bot.send_message(message.chat.id, f"Здравствуй {message.from_user.first_name}!\n\n{start()}",
                         reply_markup=keyboard1())
#Обрабатывает текстовые сообщения присланные пользователем и кнопки



print("Бот запущен!!!")

if __name__ == "__main__":
    bot.polling(none_stop=True)
#Запускаем бота