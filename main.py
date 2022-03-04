import os
import telebot
from telebot import types

imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)
imageSelect.add('Mickey', 'Minnie')
hideBoard = types.ReplyKeyboardRemove()

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['xama'])
def xama(message):
    cid = message.chat.id
    bot.send_audio(cid,open('xama.ogg','rb'), reply_markup=hideBoard)
    bot.send_message(cid,"FAÇA O PRÉ-SAVE:"
                +" https://ada.lnk.to/toquederecolher. ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ @sophiamoraesc :)")
    bot.send_chat_action(cid, 'typing') 
    bot.send_message(cid, "Veja o clipe abaixo:")
    bot.send_video(cid, open('toque_de_recolher.mp4', 'rb'), reply_markup=hideBoard)
    
@bot.message_handler(commands=['netflix'])
def netflix(message):
    cid = message.chat.id
    bot.reply_to(message,"Explicação do termo netflix")
    bot.send_audio(cid,open('porqueNetflix.flac','rb'), reply_markup=hideBoard)
  
@bot.message_handler(commands=['wallpaperds'])  
def wlpp(message):
    cid = message.chat.id
    bot.send_photo(cid,open('quartomaisorganizadodeSolutions.png','rb'), reply_markup=hideBoard)
  
bot.polling()