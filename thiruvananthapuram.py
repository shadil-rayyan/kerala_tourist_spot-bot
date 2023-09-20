import telebot
from telebot.types import  ReplyKeyboardMarkup, KeyboardButton
user_states={}
#code start from now on will be copy pasted into the main.py (note: that we are not gonna import the district
# file into  main.py but copy paste into it,that seem like less confusing to me )
#since this is not contain all the codes,the bot should have yellow line below it
#if you do not understand the code look at kozhikode.py file i added comments to it 
#at the same time run the example.py file using a bot token from telegram botfather in your phone to udnersand 
#it better

@bot.message_handler(func=lambda message: message.text =="Thiruvananthapuram_button")
def  Thiruvanthapuram_button_selected(message):

  nest_nested_keyboard =ReplyKeyboardMarkup(resize_keyboard=True)
  travel_brochure1_button=KeyboardButton("travel brochure")
  park_button=KeyboardButton("park")
  beach_button=KeyboardButton("beach")
  dam_button=KeyboardButton("dam")
  wildlife_sanctuary_button=KeyboardButton("wildlife_sanctuary")
  Mountain_button=KeyboardButton("Montain")
  hills_button=KeyboardButton("Hills")
  Historical_place_button=KeyboardButton("Historical place")
  jungle_button=KeyboardButton("jungle")
  others_button=KeyboardButton("other")
  back_button = KeyboardButton("Back")
  main_menu_button = KeyboardButton("Main Menu")

  nest_nested_keyboard.row(travel_brochure1_button)
  nest_nested_keyboard.row(park_button)
  nest_nested_keyboard.row(beach_button)
  nest_nested_keyboard.row(dam_button)
  nest_nested_keyboard.row(wildlife_sanctuary_button)
  nest_nested_keyboard.row(Mountain_button)
  nest_nested_keyboard.row(hills_button)
  nest_nested_keyboard.row(Historical_place_button)
  nest_nested_keyboard.row(jungle_button)
  nest_nested_keyboard.row(others_button)
  nest_nested_keyboard.row(back_button)
  nest_nested_keyboard.row(main_menu_button)
 #Respond with a message when the user selects "" and include the nested keyboard
  bot.send_message(message.chat.id, 'Welcome to ! What would you like to explore?', reply_markup=nest_nested_keyboard)
  user_states[message.chat.id] = "Kasaragod_selected"
