import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

bot = telebot.TeleBot('6101444089:AAF17UIY8KKz5XPDGEzwZT9Vopsj7jtGNoo')

# Define a dictionary to keep track of user states
user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    # Create a custom keyboard with a "Category" button and a "Student" button
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    
    travel_brochure_button = KeyboardButton("travel brochure")
    district_button = KeyboardButton("district")
    
    keyboard.row(travel_brochure_button, district_button)
    
    # Add "Back" and "Main Menu" buttons
    back_button = KeyboardButton("Back")
    main_menu_button = KeyboardButton("Main Menu")
    
    #keyboard.row(back_button, main_menu_button)
    
    bot.send_message(message.chat.id, 'Welcome to my bot!', reply_markup=keyboard)

    # Set the user's initial state to the main menu
    user_states[message.chat.id] = "main_menu"

@bot.message_handler(func=lambda message: message.text == "Back")
def back_button_clicked(message):
    chat_id = message.chat.id
    
    if chat_id in user_states:
        current_state = user_states[chat_id]
        
        # Handle "Back" button based on the user's current state
        if current_state == "category_selected":
            # User was in the "travel brochure" section, go back to the main menu
            start(message)
        # Add more cases for other states as needed
        
        # Update the user's current state
        user_states[chat_id] = current_state

@bot.message_handler(func=lambda message: message.text == "Main Menu")
def main_menu_button_clicked(message):
    # Handle the "Main Menu" button click by sending the main menu again
    start(message)
@bot.message_handler(func=lambda message: message.text == "travel brochure")
def travel_brochure_button_selected(message):
    # Create a nested keyboard when the user selects the "travel brochure" button
    nested_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    two_day_button = KeyboardButton("two day")
    three_day_button = KeyboardButton("three day")
    
    # Add "Back" and "Main Menu" buttons to the nested keyboard
    back_button = KeyboardButton("Back")
    main_menu_button = KeyboardButton("Main Menu")
    
    # Create two separate rows for buttons
    nested_keyboard.row(two_day_button)
    nested_keyboard.row(three_day_button)

    nested_keyboard.row(back_button, main_menu_button)

    # Respond with a message when the user selects the "travel brochure" button and include the nested keyboard
    bot.send_message(message.chat.id, 'Hello! Welcome to the "travel brochure" section.', reply_markup=nested_keyboard)

    # Update the user's current state to reflect the current menu
    user_states[message.chat.id] = "category_selected"
@bot.message_handler(func=lambda message: message.text == "district")
def district_button_selected(message):
    # Create a nested keyboard when the user selects the "district" button
    nested_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
   
    Kozhikode_button = KeyboardButton("Kozhikode")
    main_menu_button = KeyboardButton("Main Menu")  
    back_button = KeyboardButton("Back")
    main_menu_button = KeyboardButton("Main Menu")


    nested_keyboard.row(Kozhikode_button)   
    nested_keyboard.row(back_button)   
    nested_keyboard.row(main_menu_button)   
    
    # Respond with a message when the user selects the "district" button and include the nested keyboard
    bot.send_message(message.chat.id, 'Welcome to the "district" section.', reply_markup=nested_keyboard)

    # Update the user's current state to reflect the current menu
    user_states[message.chat.id] = "district_selected"
@bot.message_handler(func=lambda message: message.text == "Back")
def district_back_button_clicked(message):

    chat_id = message.chat.id
    
    if chat_id in user_states:
        current_state = user_states[chat_id]
        
        # Handle "Back" button based on the user's current state
        if current_state == "district_selected":
            # User was in the "district" section, go back to the main menu
            start(message)  # Call the start function to return to the main menu
        # Add more cases for other states as needed
        
        # Update the user's current state
        user_states[chat_id] = current_state
@bot.message_handler(func=lambda message: message.text =="Kozhikode")
def kozhikode_button_selected(message):
  nest_nested_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
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

    #nest_nest_nested_keyboard.row(kozhikode_beach_button)
    nest_nest_nested_keyboard.row(kappad_beach_button)
    nest_nest_nested_keyboard.row(back_button)
    nest_nest_nested_keyboard.row(main_menu_button)
    bot.send_message(message.chat.id, 'Welcome to Kozhikode! W', reply_markup=nest_nest_nested_keyboard)
    user_states[message.chat.id] = "Kozhikode_selected"

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

if __name__ == "__main__":
    bot.polling()

    