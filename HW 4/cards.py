'''
Name: Shashank Agrawal
Class: CS 5001
Program: cards 
'''
from cards_helper import *
'''
Function: main
Parameters:
    None
Returns:
    None
Does:
    Runs Program; Main function included in here
    as when included in helper it runs when imported
''' 
def main():
    print("Original deck is: \n", create_deck())
    x = shuffle(create_deck())
    print("Shuffled deck is: \n", x)
    hands = deal(10, 2, x)
    format_output(hands)
main()
