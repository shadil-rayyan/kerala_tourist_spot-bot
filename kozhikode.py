import telebot
from telebot.types import  ReplyKeyboardMarkup, KeyboardButton
user_states={}
#code start from now on will be copy pasted into the main.py (note: that we are not gonna import the district
# file into  main.py but copy paste into it,that seem like less confusing to me )
#since this is not contain all the codes,the bot should have yellow line below it

#if you do not understand the code look at kozhikode.py file i added comments to it 
#at the same time run the example.py file using a bot token from telegram botfather in your phone to udnersand 
#it better


#used when clicking a button in the bot 
@bot.message_handler(func=lambda message: message.text == "Kozhikode")
def kozhikode_button_selected(bot,message):
#creating a the custom button section under the message box of telegram,in the space of keyboard in phones
  nest_nested_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#making a button that is going to add into custom button section
  travel_brochure1_button = KeyboardButton("travel brochure")
  park_button = KeyboardButton("park")
  beach_button = KeyboardButton("beach")
  dam_button = KeyboardButton("dam")
  wildlife_sanctuary_button = KeyboardButton("wildlife_sanctuary")
  Mountain_button = KeyboardButton("Montain")
  hills_button = KeyboardButton("Hills")
  Historical_place_button = KeyboardButton("Historical place")
  jungle_button = KeyboardButton("jungle")
  others_button = KeyboardButton("other")
  back_button = KeyboardButton("Back")
  main_menu_button = KeyboardButton("Main Menu")
#this code decide where we are going to place the button
#we palce button in a row , asingle row contain a single button
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
  bot.send_message(message.chat.id, 'Welcome to Kozhikode! What would you like to explore?', reply_markup=nest_nested_keyboard)
  user_states[message.chat.id] = "Kozhikode_selected"
#we use this to make nested button inside kozhikode beach 
@bot.message_handler(func=lambda message: message.text == "beach")
def kozhikode_beach_selected(message):
    # Create a nested keyboard for beach attractions in Kozhikode
    nest_nest_nested_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    kozhikode_beach_button = KeyboardButton("kozhikode beach")
    kappad_beach_button = KeyboardButton("kappad")
    beypore_beach_button = KeyboardButton("beypore beach")
    Parapally_Beach_button = KeyboardButton("Parapally Beach ")
    Sand_Banks_Beach_button = KeyboardButton("Sand Banks Beach")
    thikkodi_drive_in_beach_button = KeyboardButton("thikkodi drive in beach") 
    Kamburam_Beach_button = KeyboardButton("Kamburam Beach") 
    Payyoli_Beach_button = KeyboardButton("Payyoli Beach") 
    Maliyakal_Beach_button = KeyboardButton("Maliyakal Beach") 
    #_button = KeyboardButton("") 
    #_button = KeyboardButton("") 
    #_button = KeyboardButton("") 
    back_button = KeyboardButton("Back")
    main_menu_button = KeyboardButton("Main Menu")

    nest_nest_nested_keyboard.row(kozhikode_beach_button)
    nest_nest_nested_keyboard.row(kappad_beach_button)
    nest_nest_nested_keyboard.row(back_button)
    nest_nest_nested_keyboard.row(main_menu_button)

@bot.message_handler(func=lambda message: message.text == "kappad")
def kozhikode_beach_kappad_selected(message):
    # Send an image of Kappad Beach
    photo_url = 'https://th.bing.com/th/id/OIP.wsPAvIpz3wPx0sXTKXqjbgHaEK?w=272&h=180&c=7&r=0&o=5&pid=1.7' 
    bot.send_photo(message.chat.id, photo_url)
    
    # Send a description of Kappad Beach
    description = "Kappad Beach is a historic beach in Kozhikode, Kerala, India. It's known for its natural beauty and historical significance."
    bot.send_message(message.chat.id, description)
    
    # Send a video link (video note) of Kappad Beach (must be in MP4 format)
    #video_url = 'https://www.bing.com/videos/riverview/relatedvideo?&q=kappad+beach&&mid=7BE5F27FC841A273AA747BE5F27FC841A273AA74&&FORM=VRDGAR' 
       # Send a clickable link to the YouTube video
    youtube_video_url = 'https://www.youtube.com/watch?v=a1A32aCLubY&pp=ygUMa2FwcGFkIGJlYWNo'  # Replace with the actual YouTube video URL
    bot.send_message(message.chat.id, youtube_video_url)
    # You can also provide additional information or options for the user here.
    
    # Update the user's current state (optional)
    user_states[message.chat.id] = "Kozhikode_beach_kappad_selected"   