
import random

#These are all my lists I made in'Magic_8_Ball_Response_List'
from Magic_8_Ball_Response_List import Response_Type_List, Affirmative_Answers_List, Non_committal_Answers_List, Negative_Answers_Lists

#-------------------------------------------------------------- GAME START LOOP
while True:
    user_input = input("Welcome to your personal Magic 8 Ball!\
                       \nWould you like to play? (Yes/No): ").lower()
    # Check if input is no (Not no = true)
    if not user_input == 'no':
        # Check if input is yes, else asks you to respond with yes or no
        if user_input == 'yes':
            print('Great! Ask me a question.')
            #breaks the loop and moves to next stage
            break
        else:
            print('Please type \'yes or no\'')
    else:
        print('That\'s too bad. Goodbye!')
        quit()

#--------------------------------------------------------------- MAIN GAME LOOP
#Ask a question loop
while True:
    question = input('Ask me a question.').lower()
    # Check if input is not a number (Not a number = true)
    if len(question.split()) > 2:
            #if all these conditions are met we move on to the radomizer

            #gives an equal chance for yes no or maybe responses
            Chosen_list = random.choice(Response_Type_List)
            #this choses an answer from the chosen list
            Chosen_response_type = random.choice(Response_Type_List)
            
            if Chosen_response_type == 'Affirmative_Answers_List':
                    Chosen_Phrase = random.choice(Affirmative_Answers_List)
                    print(Chosen_Phrase)
            elif Chosen_response_type == 'Non_committal_Answers_List':
                    Chosen_Phrase = random.choice(Non_committal_Answers_List)
                    print(Chosen_Phrase)
            elif Chosen_response_type == 'Negative_Answers_Lists':
                    Chosen_Phrase = random.choice(Negative_Answers_Lists)
                    print(Chosen_Phrase)

            #This sets the user up to ask a new question and restarts this loop
            ask_again = input("Would you like to ask another question?\
                        \n(Yes/No): ").lower()
            if ask_again != 'yes':
                    print('Thanks for playing!')
                    quit()
    else:
         print('Please type a complete question')      
        
