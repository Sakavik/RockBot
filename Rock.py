import telebot;
import random
from telebot import types
bot = telebot.TeleBot('TOKEN')
name=''
@bot.message_handler( commands=['start', 'help'])
def handle_start_help(message):
    bot.send_message( message.chat.id, "Как зовут тебя?")
messages = ['всё будет хорошо!','ты со всем справишься!','ты свернёшь горы!','поверь в себя,ведь','если нужно-отдохни,а потом возьмёшься за дела с новыми силами.', 'чёрная полоса в жизни когда-нибудь закончится и начнётся белая.']
@bot.message_handler(content_types=['text'])
def handle_start_help(message):
    voice = open('Rock.ogg', 'rb')
    photo = open('{}.jpg'.format(random.randint(1,5)), 'rb')
    name = message.text
    bot.send_message( message.chat.id, '{}'.format(name.title())+', '+messages[random.randint(0,len(messages)-1)] + ' Скала верит в тебя!')
    bot.send_photo( message.chat.id,photo)
    bot.send_voice( message.chat.id,voice)
   
        
    
bot.polling(none_stop=True, interval=0)
