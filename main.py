import telebot

bot = telebot.TeleBot('6440121870:AAGHtv7J_9M4G5EWSC7ZIZ9DmfWmkD1ehQE')

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id,  f'Привет, {message.from_user.first_name}')

@bot.message_handler(commands = ['help'])
def money(message):
    bot.send_message(message.chat.id, 'Команды\n /start начать работу с ботом')

# Запуск бота
bot.polling(none_stop=True)
