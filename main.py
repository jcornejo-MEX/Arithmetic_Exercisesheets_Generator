import argparse
import Topics_Data
from random import randint as random


#switch-case box
def case1():
    return "case 1"
def case2():
    return "case 2"
def case3():
    return "case 3"
def exit():
    exit_message_roll = random(0,len(Topics_Data.encouragements))
    return f"Thank you for using me \n {Topics_Data.encouragements[exit_message_roll]}"
def default():
    return "no case was selected, try again"
def switch_box(input:str):
    switch_box_cases = {
        "1": case1,
        "2": case2,
        "3": case3,
        "exit": exit,
    }
    selected_function = switch_box_cases.get(input,default)
    return selected_function()
def main():
    index = None
    print("Welcome to AEG (Arirhmetic_Excersices Generator) \n what can i do for you?")
    while (index != "exit"):
        index = input()
        lines= switch_box(index)
        print(lines)

if __name__ == "__main__":
    main()