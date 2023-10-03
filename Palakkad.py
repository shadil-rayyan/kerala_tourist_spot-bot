
#code start from now on will be copy pasted into the main.py (note: that we are not gonna import the district
# file into  main.py but copy paste into it,that seem like less confusing to me )
#since this is not contain all the codes,the bot should have yellow line below it
#if you do not understand the code look at kozhikode.py file i added comments to it 
#at the same time run the example.py file using a bot token from telegram botfather in your phone to udnersand 
#it better
import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

bot = telebot.TeleBot('Bot token')

@bot.message_handler(commands=['start'])
def start(message):
    # Create a custom keyboard with a "Category" button and a "Student" button
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(('Palkkad'))

    bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=keyboard)

    

@bot.message_handler(func=lambda message: message.text =="Palkkad")
def  palkkad_button_selected(message):
  nest1_keyboard =ReplyKeyboardMarkup(resize_keyboard=True)

  nest1_keyboard.row(('travel_brochure'))
  nest1_keyboard.row(('park'))
  nest1_keyboard.row(('beach'))
  nest1_keyboard.row(('dam'))
  nest1_keyboard.row(('wildlife sanctuary'))
  nest1_keyboard.row(('Mountain'))
  nest1_keyboard.row(('hills') )
  nest1_keyboard.row(('Historical place') )
  nest1_keyboard.row(('jungle'))
  nest1_keyboard.row(('others'))
  
  nest1_keyboard.row(('main menu'))
 #Respond with a message when the user selects "" and include the nested keyboard
  bot.send_message(message.chat.id, 'Welcome to ! What would you like to explore?', reply_markup=nest1_keyboard)

@bot.message_handler(func=lambda message: message.text == "beach")
def pkbeach_selected(message):

  nest2_keyboard =ReplyKeyboardMarkup(resize_keyboard=True)
  nest2_keyboard.row(('palkkad beach'))

  bot.send_message(message.chat.id, 'W', reply_markup=nest2_keyboard)

@bot.message_handler(func=lambda message: message.text == "palkkad beach")
def palkkad1_beach_selected(message):
  # remove the comments after adding url to photo and youtube 
   #photo_url = '#' 
   #bot.send_photo(message.chat.id, photo_url)
    
   
   description = '''Palkkad Beach is a beautiful beach located in Palakkad, Kerala, India.
    It is a popular tourist destination, known for its pristine white sands and 
   clear blue waters. The beach is also home to a variety of marine life, including dolphins,
    turtles, and fish'''
   bot.send_message(message.chat.id, description)
    
   #youtube_video_url = ''  # 
   #bot.send_message(message.chat.id, youtube_video_url)
    

bot.polling()
