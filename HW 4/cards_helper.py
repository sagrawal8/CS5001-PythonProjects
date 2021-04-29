'''
Name: Shashank Agrawal
Class: CS 5001
Program: cards
'''

import random

'''
Function: create_deck
Parameters: none
Returns: array of unshuffledcards in a
         normal sized deck (len: 52)
Does: nested for loop that cycles through each
      value and suite in order to pair them
'''

def create_deck():
    # suites of cards
    suite = ['s', 'h', 'c', 'd']
    # values of cards
    value = ['2', '3', '4', '5', '6', '7', '8',
             '9', 'T', 'J', 'Q', 'K', 'A']
    # array to be returned
    cards = []
    
    for x in value:
        for y in suite:
            card = x + y
            cards.append(card)   
    return cards

'''
Function: shuffle
Parameters: cards: array of string type
Returns: array of shuffled cards in a
         normal sized deck (len: 52)
Does: uses random.shuffle() to shuffle deck
'''

def shuffle(cards):
    shuffled = cards.copy()
    random.shuffle(shuffled)    
    return shuffled

'''
Function: deal
Parameters:
    number_of_hands (int): number of hands to deal
    number_of_cards (int): number of cards per hand
    cards(array): shuffled deck of cards
Returns:
    all_hands(array): nested array/list
                      containing hands
Does:
    Uses .pop() to deal hands from cards array.
    Cards are appended to current_hand and
    current_hand is appended to all_hands.
'''
def deal(number_of_hands, number_of_cards,
         cards):
    all_hands = []    
    # counts number of hands dealt
    count = 0
    

    while(count < number_of_hands):
        # counts number of cards dealt per hand
        given_cards = 0
        current_hand = []
        
        while(given_cards < number_of_cards):
            current_hand.append(cards.pop())  
            given_cards += 1
            
        count += 1
        all_hands.append(current_hand)
    
    return all_hands

'''
Function: format_output
Parameters: hands: array of string type
Returns: None
Does:
    Prints hands array in a easy to read
    format.
    
'''
def format_output(hands):
    total_hands = len(hands)
    count = 0
    while(count < total_hands):
        print("Hand", count + 1, ":", hands[count])
        count += 1
        


            
        
