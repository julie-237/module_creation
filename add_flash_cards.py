import mytrans
import os
import ast

file_name = "flash_card.txt"
def collect_card_list_from_file():
    card_list = []
    if os.path.exists(file_name):
       with open(file_name, "r") as f:
           card_list = ast.literal_eval(f.read())
           print(card_list)
           print("The current card_list contains " + str(len(card_list)) + " card")
           for i, card in enumerate(card_list):
                print(str(i+1) + ". " + card[0] + ": " + card[1])

card_list = []
translate_msg = "do you want to translate a word?"
save_msg = "do you want to save this card? (yes/no) "

collect_card_list_from_file()

start = input(translate_msg)
while start == "yes":
    word_en = input("type a word in English to get the French translation ")
    word_fr = mytrans.english_to_french_translator(word_en)
    new_card = (word_en, word_fr)
    print(new_card)
    save = input(save_msg)
    if save == "yes":
        card_list.append(new_card )
    else:
        exit
    start = input(translate_msg)
print(card_list)
save_to_file = input("do you want to save this card_list to file? (yes/no) ")
if save_to_file == "yes":
    with open(file_name, "w") as f:
        f.write(str(card_list))
    
    print("saving...")
else:
    exit
print("End of program")

