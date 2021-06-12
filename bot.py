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
    bot.send_message(message.chat.id, f"Здравствуй {message.from_user.first_name}!\n\nDogiboti поможет вам создать своего бота. "
                                      f"С помощью Dogiboti вы сможете рассылать сообщения пользователям бота, создавать свои команды и красивые меню.\n\n"
                                      f"Чтобы добавить своего первого бота, используйте команду /addbot.", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def answer_start_message(message):
    if message.text == "Добавить нового бота":
        bot.send_message(message.chat.id, "Для начала создай бота в BotFather.")
    elif message.text == "Инструкции":
        bot.send_message(message.chat.id, "❓Как создать своего бота?\n\n🔹Откройте @Dogiboti_bot, "
                                          "используйте команду /addbot и следуйте инструкциям.\n\n"
                                          "❓Как настроить аватарку и описание бота?\n\n"
                                          "🔹Откройте @BotFather и используйте следующие команды:\n"
                                          "/setuserpic - чтобы изменить аватарку бота\n"
                                          "/setdescription - чтобы изменить текст, "
                                          "который пользователи видят перед тем как нажать на Start.\n"
                                          "/setabouttext - чтобы изменить текст внутри профиля бота\n"
                                          "/setname - чтобы изменить имя бота\n\n"
                                          "Перейдите в @Dogiboti_bot и используйте команду "
                                          "/setdescription чтобы изменить описание бота "
                                          "(также используется в качестве приветствия).\n\n❓Как создать свою команду?\n\n"
                                          "🔹Откройте своего бота и используйте команду /commands, "
                                          "чтобы создать свои команды и настроить меню бота.\n\n"
                                          "❓Как настроить внешний вид меню?\n\n"
                                          "🔹Перейдите в своего бота, используйте команду /commands, "
                                          "а потом выберите 'Настроить меню' и следуйте инструкциям.\n\n"
                                          "и т.д.")
    elif message.text == "Помощь":
        bot.send_message(message.chat.id, "🚀 Создание бота\n\n/addbot - создать нового бота\n\n📢 Рассылка\n\n"
                                          "/newpost - отправить сообщение своим подписчика\n"
                                          "/subscribers - посмотреть сколько у вас подписчиков\n\n🔧 Настройки бота\n\n"
                                          "/setdescription - редактировать описание вашего бота\n"
                                          "/autoposting - включить автопостинг из RSS, VK, Twitter, YouTube\n"
                                          "/admins - управление администраторами ваших ботов\n\n📚 Инструкции\n\n"
                                          "/tutorials - подробные ответы на вопросы по созданию и настройке ботов\n\n"
                                          "💢 Прочее\n\n/deletebot - удалить бота\n"
                                          "/help - вызвать это меню")


print("Бот запущен!!!")


#t.me/Dogiboti_bot (ссылка на бота)


if __name__ == "__main__":
    bot.polling(none_stop=True)