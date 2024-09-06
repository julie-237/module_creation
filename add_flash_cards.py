import mytrans

card_list = []
msg_template = "do you want to translate a word?"
new_card = input(msg_template)
while new_card == "yes":
    word = input("type a word in English to get the French translation ")
    card = mytrans.english_to_french_translator(word)
    save = input("do you want to save this card? (yes/no) ")
    if save == "yes":
        
        card_list.append(card)
    else:
        exit
    new_card = input(msg_template)
print(card_list)
save_to_file = input("do you want to save cards to file? (yes/no) ")
if save_to_file == "yes":
    with open("add_flash_cards.py", "a") as f:
        f.write(str(card_list))
    print("saving...")
else:
    exit
print("End of program")
['amour', 'femme', 'lit']