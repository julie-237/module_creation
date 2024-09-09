import os
import ast
import random
import time

file_name = "flash_card.txt"
def collect_card_list_from_file():
    card_list = []
    if os.path.exists(file_name):
       with open(file_name, "r") as f:
           card_list = ast.literal_eval(f.read())
           return card_list
           
def guess_cards(card_list:list):
    while len(card_list) > 0:
        index = random.randint(0, len(card_list) - 1)
        word_en = card_list[index][0]
        word_fr = card_list[index][1]
        answer = input(word_en + " ? ")
        if answer == word_fr:
            print("correct")
            del card_list[index]
        else:
            print("Not correct. Will try later")
    
           
     
if not os.path.exists("flash_card.txt"):
    print("No cards available yet. please create new ones first ")
    exit
card_list = collect_card_list_from_file()
print("you have " + str(len(card_list)) + " cards to guess.")
input("Ready ? press enter to start ")
time_start = time.time()
guess_cards(card_list)
time_stop = time.time()
duration = int(time_stop - time_start)
print("you guessed all cards in " + str(duration) + " seconds")
print("End of program")