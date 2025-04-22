import telebot
import json
import os
from telebot import types

# Ініціалізація бота
API_TOKEN = '8016620618:AAH6W4hJ-Jmy6qhqQrDCdQDUjbKEhSIhQYg'
bot = telebot.TeleBot(API_TOKEN)

# Вбудована база даних
database = {
    "users": {}
}

# Функція для завантаження бази даних з файлу
def load_database():
    global database
    if os.path.exists('database.json'):
        with open('database.json', 'r') as file:
            database = json.load(file)
    else:
        database = {"users": {}}  # Якщо файл не знайдено, створюємо порожню базу

# Функція для збереження бази даних у файл
def save_database():
    with open('database.json', 'w') as file:
        json.dump(database, file, indent=4)

# Функція для перевірки статусу користувача
def check_user_status(username, checker_username):
    if username not in database["users"]:
        # Перевіряємо, чи має користувач статус "стажёр"
        if database["users"].get(checker_username, None) == "стажёр":
            database["users"][username] = "скаммер"
            save_database()
            return {
                "text": f"👤 {username} (https://ibb.co/RTvnJv5s)\n"
                        f"🛑 Статус: скаммер | ⚠️ 1 | ✅ 0\n\n"
                        f"❤️ Страна не задана\n\n"
                        f"🔥 Скаммеров слито: 1\n\n"
                        f"👍 Всегда идите через гарантов MENTAS, чтобы сделки проходили безопасно\n\n"
                        f"🗓 Скоро будет | 🔍 0\n"
                        f"🔍 Занёс: {checker_username}",
                "status": "скаммер"
            }
        else:
            return {
                "text": f"👤 {username} (https://ibb.co/Q77XJCjW)\n"
                        f"🛑 Статус: нет в базе. Вероятность скама: 30%\n\n"
                        f"❤️ Страна не задана\n\n"
                        f"🔥 Скаммеров слито: 0\n\n"
                        f"👍 Всегда идите через гарантов MENTAS, чтобы сделки проходили безопасно\n\n"
                        f"🗓 Скоро будет | 🔍 0\n"
                        f"🔍 Проверено: {checker_username}",
                "status": "нет в базе"
            }
    
    user_status = database["users"][username]
    
    # Перевірка, чи статус є рядком
    if isinstance(user_status, str) and user_status in status_texts:
        return {
            "text": status_texts[user_status]["text"].format(username=username),
            "status": user_status
        }
    else:
        return {
            "text": f"👤 {username} має невідомий статус.",
            "status": "невідомий"
        }

# Тексти для статусів
status_texts = {
    "нет в базе": {
        "text": "👤 Користувач {username} не знайдений. Вероятність скама: 30%\n\n"
                "❤️ Страна не задана\n\n"
                "🔥 Скаммеров слито: 0\n\n"
                "👍 Всегда идите через гарантов MENTAS, чтобы сделки проходили безопасно\n\n"
                "🗓 Скоро будет| 🔍 0",
    },
    "гарант": {
        "text": "👤 {username} (https://ibb.co/CsH16HQ2) #id5399940308\n\n"
                "💙 Репутація: Гарант ✅ | ⚠️ 0\n"
                "❓ Кто такой гарант? (https://telegra.ph/Kto-takoj-GARANT-05-29)\n\n"
                "🌎 Страна: Не задана 💸\n"
                "🔥 Скаммеров слито: 0\n\n"
                "👍 Всегда идите через гарантов MENTAS, чтобы сделки проходили безопасно\n\n"
                "🗓 Скоро будет | 🔍 0",
    },
    "стажёр": {
        "text": "👤 {username} (https://ibb.co/qSjs5Lh) #id7213082439\n\n"
                "💙 Репутація: Стажёр | ⚠️ 0 | ✅ 0\n"
                "💙 Персонал [MENTAS]\n\n"
                "🌎 Страна: Не задана 🦦\n\n"
                "🗓 Скоро будет | 🔍 0",
    },
    "владелец": {
        "text": "👤 {username} (https://ibb.co/Rpm4gsRR) #id496974176\n\n"
                "💙 Репутація: Владелец | ⚠️ 0 | ✅ 0\n"
                "💙 Персонал [MENTAS]\n\n"
                "🌎 Страна: Не задана 🦛\n\n"
                "🗓 Скоро будет | 🔍 0",
    },
    "проверен гарантом": {
        "text": "👤 {username} (https://ibb.co/kszwJMGW) #id7460423631\n\n"
                "💙 Репутація: Проверен гарантом: {username}\n"
                "💙 Персонал [MENTAS](https://t.me/Mentas_Report)\n\n"
                "🌎 Страна: нету\n\n"
                "🗓 Скоро будет | 🔍 0",
    },
    "скаммер": {
        "text": "👤 {username} (https://ibb.co/RTvnJv5s) #id7213082439\n\n"
                "🛑 Статус: Скаммер ⚠️\n"
                "💙 Репутація: Скаммер | ⚠️ 0 | ✅ 0\n\n"
                "🌎 Страна: Не задана 🦦\n\n"
                "🗓 Скоро будет | 🔍 0",
    },
    "петух": {
        "text": "👤 {username} (https://ibb.co/Rpm4gsRR) #id496974176\n\n"
                "🛑 Статус: Петух 🐓\n"
                "💙 Репутація: Петух | ⚠️ 0 | ✅ 0\n\n"
                "🌎 Страна: Не задана 🦛\n\n"
                "🗓 Скоро будет | 🔍 0",
    },
}

# Обробка команди /скам
@bot.message_handler(commands=['скам'])
def handle_scam_command(message):
    if database["users"].get(message.from_user.username, None) == "стажёр":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        btn_scammer = types.KeyboardButton("Скаммер")
        btn_petuh = types.KeyboardButton("Петух")
        markup.add(btn_scammer, btn_petuh)

        bot.send_message(chat_id=message.chat.id, text="Виберіть статус користувача:", reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def handle_status_selection(message):
            if message.text == "Скаммер":
                username = message.reply_to_message.from_user.username
                database["users"][username] = "скаммер"
                save_database()
                bot.send_message(chat_id=message.chat.id, text=f"Користувач {username} занесений до бази даних як скаммер.")
            elif message.text == "Петух":
                username = message.reply_to_message.from_user.username
                database["users"][username] = "петух"
                save_database()
                bot.send_message(chat_id=message.chat.id, text=f"Користувач {username} занесений до бази даних як петух.")
            else:
                bot.send_message(chat_id=message.chat.id, text="Невірна команда.")
    else:
        bot.reply_to(message, "Вибачте, але ця команда доступна лише для стажерів.")

# Обробка команд для видачі статусів
@bot.message_handler(commands=['гарант', 'создатель', 'стажёр', 'trust', 'президент', 'директор', 'владелец', 'петух'])
def handle_status_command(message):
    status_map = {
        'гарант': "гарант",
        'создатель': "владелец",
        'стажёр': "стажёр",
        'trust': "проверен гарантом",
        'президент': "нет в базе",  # Временный статус
        'директор': "нет в базе",  # Временный статус
        'владелец': "владелец",
        'петух': "петух",
    }

    command = message.text[1:]  # Витягуємо команду без слешу
    if command in status_map and message.reply_to_message:
        status_key = status_map[command]
        response_text = status_texts[status_key]["text"]
        
        # Якщо статус "проверен гарантом", вставляємо ім'я гаранта
        if status_key == "проверен гарантом":
            guardian_name = message.from_user.username  # Ім'я гаранта
            response_text = response_text.format(username=guardian_name)
        else:
            # Зберігаємо статус у базу даних
            username = message.reply_to_message.from_user.username
            database["users"][username] = status_key
            save_database()  # Зберігаєм

        bot.send_message(chat_id=message.chat.id, text=response_text)

# Обробка команд для перевірки статусу користувача
@bot.message_handler(func=lambda message: True)
def handle_commands(message):
    command = message.text.lower()

    # Перевірка статусу власного користувача
    if command in ['чек ми', 'чек я', 'чек мене']:
        username = message.from_user.username
        status_info = check_user_status(username, username)
        bot.reply_to(message, status_info["text"])

    # Перевірка статусу іншого користувача за @ім'ям
    elif command.startswith('чек @'):
        username = command[5:]  # Витягуємо ім'я користувача
        status_info = check_user_status(username, message.from_user.username)
        bot.reply_to(message, status_info["text"])

    # Перевірка статусу іншого користувача за відповіддю на повідомлення
    elif message.reply_to_message:
        username = message.reply_to_message.from_user.username
        status_info = check_user_status(username, message.from_user.username)
        bot.reply_to(message, status_info["text"])

# Завантажуємо базу даних при старті
load_database()

# Запуск бота
bot.polling()