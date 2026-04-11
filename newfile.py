import telebot
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

# BotFather берган Tokenни шу ерга қўйинг
API_TOKEN = '8757770526:AAGQi-o5bHMfOeL-BWHrpp8kKxa6moHg1Bc'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # Тугма яратамиз
    markup = InlineKeyboardMarkup()
    
    # Веб-илова манзили (намуна сифатида менинг сайтим, кейин ўзингникига алмаштирамиз)
    web_info = WebAppInfo(url="https://behhruz.github.io/wedding/")
    
    btn = InlineKeyboardButton(text="Таклифномани очиш 💌", web_app=web_info)
    markup.add(btn)
    
    bot.send_message(message.chat.id, 
                     f"Ассалому алайкум, {message.from_user.first_name}!\n\n"
                     "Сизни тўйимизга таклиф этамиз. Таклифномани кўриш учун пастдаги тугмани босинг:", 
                     reply_markup=markup)

print("Бот ишга тушди...")
bot.polling()
