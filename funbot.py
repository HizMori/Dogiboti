def start():
    start = "Dogiboti поможет вам создать своего бота. " \
            "С помощью Dogiboti вы сможете рассылать сообщения пользователям бота, " \
            "создавать свои команды и красивые меню." \
            "\n\nЧтобы добавить своего первого бота, используйте команду /addbot."
    return start

def addbot():
    addbot = "1⃣ Перейдите к @BotFather. Для этого нажмите на его имя, а потом 'Запустить', если это потребуется.\n\n" \
             "2⃣ Создайте нового бота у него. Для этого внутри @BotFather используйте команду '/newbot' " \
             "(сначала вам нужно будет придумать название, оно может быть на русском; " \
             "потом нужно придумать ссылку на вашего бота, она должна быть на английском и " \
             "обязательно заканчиваться на 'bot').\n\n3⃣ Скопируйте API токен, который вам выдаст @BotFather\n\n" \
             "4⃣ Возвращайтесь обратно в @Dogiboti_bot и пришлите скопированный API токен в ответ на это сообщение."
    return addbot

def help():
    help = "🚀 Создание и просмотр ботов\n/addbot - создать нового бота\n/mybot - просмотр существующих ботов\n\n" \
           "📢 Рассылка\n/newpost - отправить сообщение своим подписчика\n/subscribers - посмотреть сколько у вас подписчиков\n\n" \
           "🔧 Настройки бота\n/setdescription - редактировать описание вашего бота\n" \
           "/autoposting - включить автопостинг из VK, Twitter, YouTube и других соцсетей\n" \
           "/admins - управление администраторами ваших ботов\n\n💢 Прочее\n/deletebot - удалить бота\n/help - вызвать это меню"
    return help

def manual():
    manual = "❓ Как создать своего бота?\n\n🔹 Откройте @Dogiboti_bot, используйте команду /addbot и следуйте инструкциям.\n\n" \
             "❓ Как настроить аватарку и описание бота?\n\n🔹 Откройте @BotFather и используйте следующие команды:\n" \
             "/setuserpic - чтобы изменить аватарку бота\n/setdescription - чтобы изменить текст, " \
             "который пользователи видят перед тем как нажать на start.\n/setabouttext - чтобы изменить текст внутри профиля бота\n" \
             "/setname - чтобы изменить имя бота\n\nПерейдите в @Dogiboti_bot и используйте команду " \
             "/setdescription чтобы изменить описание бота (также используется в качестве приветствия).\n\n" \
             "❓ Как создать свою команду?\n\n🔹 Откройте своего бота и используйте команду /commands, " \
             "чтобы создать свои команды и настроить меню бота.\n\n❓ Как настроить внешний вид меню?\n\n" \
             "🔹 Перейдите в своего бота, используйте команду /commands, а потом выберите 'Настроить меню' и следуйте инструкциям.\n\n" \
             "и т.д."
    return manual

def cancel():
    cancel = "Отменено"
    return cancel

#Сообщения, которые отправляет бот на ответ на определённые команды