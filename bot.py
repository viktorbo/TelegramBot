import telebot
import json

with open('bot_config.json', 'r', encoding='utf-8') as bot_config:
    config = json.load(bot_config)

bot = telebot.TeleBot(token=config['token'])


@bot.message_handler(commands=['start', 'help'])
def start_help_info(message):
    msg = f"Hi, {message.from_user.first_name}{' '+message.from_user.last_name if  message.from_user.last_name else ''}! \n" \
        if 'start' in message.text \
        else 'Command list: \n'
    for command in config['commands'].keys():
        msg += f"/{command}  -  {config['commands'][command]} \n"
    bot.send_message(message.chat.id, msg, parse_mode='html')


@bot.message_handler(commands=['id'])
@bot.channel_post_handler(commands=['id'])
def get_id(message):
    bot.send_message(message.chat.id, f"{message.chat.type} ID: {message.chat.id}")


bot.polling(none_stop=True)


