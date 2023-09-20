
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
    Kasaragod_button = KeyboardButton("Kasaragod")
    Kannur_button = KeyboardButton("Kannur")
    Wayanad_button = KeyboardButton("Wayanad")
    Kozhikode_button = KeyboardButton("Kozhikode")
    Malappuram_button = KeyboardButton(" Malappuram")
    Palakkad_button = KeyboardButton("Palakkad")
    Thrissur_button = KeyboardButton(" Thrissur")
    Ernakulam_button = KeyboardButton("Ernakulam")
    Idukki_button = KeyboardButton("Idukki")
    Kottayam_button = KeyboardButton("Kottayam")
    Alappuzha_button = KeyboardButton("Alappuzha")
    Pathanamthitta_button = KeyboardButton("Pathanamthitta")
    Kollam_button = KeyboardButton("kollom")
    Thiruvananthapuram_button = KeyboardButton("Thiruvananthapuram")

      # Add "Back" and "Main Menu" buttons to the nested keyboard
    back_button = KeyboardButton("Back")
    main_menu_button = KeyboardButton("Main Menu")

    nested_keyboard.row(Kasaragod_button)
    nested_keyboard.row(Kannur_button)   
    nested_keyboard.row(Wayanad_button)      
    nested_keyboard.row(Kozhikode_button)   
    nested_keyboard.row(Malappuram_button)   
    nested_keyboard.row(Palakkad_button)   
    nested_keyboard.row(Thrissur_button)   
    nested_keyboard.row(Ernakulam_button)   
    nested_keyboard.row(Idukki_button)   
    nested_keyboard.row(Kottayam_button)
    nested_keyboard.row(Alappuzha_button)   
    nested_keyboard.row(Pathanamthitta_button)   
    nested_keyboard.row(Kollam_button)   
    nested_keyboard.row(Thiruvananthapuram_button)   
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

#we will add the rest of the district code copy and pasted into here                        - 
if __name__ == "__main__":
    bot.polling()
