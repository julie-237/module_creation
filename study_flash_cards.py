import os
import ast

file_name = "flash_card.txt"

def collect_card_list_from_file():
    card_list = []
    if os.path.exists(file_name):
       with open(file_name, "r") as f:
           card_list = ast.literal_eval(f.read())
           print(card_list)
           
       
if not os.path.exists("flash_card.txt"):
    print("No cards available yet. please create new ones first ")
    exit
