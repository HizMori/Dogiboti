from telebot import types


def keyboard1():
    keyboard1 = types.ReplyKeyboardMarkup(row_width=2)
    button1 = types.KeyboardButton("Добавить нового бота")
    button2 = types.KeyboardButton("Инструкции")
    button3 = types.KeyboardButton("Помощь")
    keyboard1.add(button1, button2, button3)
    return keyboard1


def keyboard2():
    keyboard2 = types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton("Отменить")
    keyboard2.add(button1)
    return keyboard2