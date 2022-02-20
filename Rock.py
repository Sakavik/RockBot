import telebot;
import random
from telebot import types
bot = telebot.TeleBot('5163682639:AAHFnSTJvnAdqYgs-DT6-pt7eAzTGDyTFuI')
name=''
@bot.message_handler( commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message(message.from_user.id, "Как зовут тебя?")
messages = ['всё будет хорошо!','ты со всем справишься!','ты свернёшь горы!','поверь в себя,ведь','если нужно-отдохни,а потом возьмёшься за дела с новыми силами.', 'чёрная полоса в жизни когда-нибудь закончится и начнётся белая.']
@bot.message_handler(content_types=['text'])
def handle_start_help(message):
    voice = open('Rock.ogg', 'rb')
    photo = open('{}.jpg'.format(random.randint(1,5)), 'rb')
    name = message.text
    bot.send_message(message.from_user.id,message.chat.id, '{}'.format(name.title())+', '+messages[random.randint(0,len(messages)-1)] + ' Скала верит в тебя!')
    bot.send_photo(message.from_user.id,message.chat.id,photo)
    bot.send_voice(message.from_user.id,message.chat.id,voice)
   
        
    
bot.polling(none_stop=True, interval=0)