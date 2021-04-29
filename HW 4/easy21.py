'''
Name: Shashank Agrawal
Class: CS 5001
Program: cards main function
'''

from cards_helper import *

'''
Function: winner
Parameters:
    hands(array): array containing hands dealt
Returns:
    b(array):
        array containg the sum of the hand
        with the maximum value provided this
        value is less than 21 and the index of
        the winning hand + 1.        
Does:
    Adds up the cards of each hand to find
    the total. If the total is <21 and is
    greater than the previous max, it becomes
    the new max. Otherwise, nothing happens.
    Also assigns cards like jack, queen, king
    and ace with values.

'''
def winner(hands):
    b =[]
    maxx = 0
    win_hand = -1
    index = 0
    for hand in hands:
        total = 0                
        for card in hand:
            value = card[0]
            if(value == 'A'):
                total += 1
            elif(value == 'K'):
                total += 13
            elif(value == 'Q'):
                total += 12
            elif(value == 'J'):
                total += 11
            elif(value == 'T'):
                total += 10
            else:
                total += int(value)
        if(total > maxx and total <= 21):
            maxx = total
            win_hand = index + 1        
        index += 1
    b.append(maxx)
    b.append(win_hand)
    return b
    
'''
Function: program
Parameters:
    None
Returns:
    None      
Does:
    Runs a program asking users to draw, stand,
    show remaining cards in deck, or quit.

'''

def program():
    # shuffled deck of cards is created
    shuffled = shuffle(create_deck())
    print("Welcome to Easy 21!")
    # boolean counter for invalid number of hands input
    flag = False

    while(flag == False):
        number_of_hands = int(input("How many "
                                    "hands to deal (1-4)? "))
        if(number_of_hands >= 1 and number_of_hands <= 4):
            flag = True
            
    hands = deal(number_of_hands, 2, shuffled)
    format_output(hands)
    # holds the choice of the user
    choice = ''              

    while(choice != 'q' and choice != 'Q'):        
        choice = input("Select:\n\tD to draw:\n\tS to Stand:"
                       "\n\tW to show hands:\n\tC to show "
                       "remaining cards:\n\tQ to quit: ")

        # choice is d or D
        if choice == 'd' or choice == 'D':

            # does not allow user to draw if hands are busted
           bust = winner(hands)
           if bust[0] == 0:
                print("Both hands busted")
                break;
           draw_for_hand = int(input("Draw for which hand? "))

            # checks for valid hand number input
           if draw_for_hand < 1 or draw_for_hand > number_of_hands:
               print("Not a valid hand number")
               continue                        
            # card is drawn
           else:
                card_drawn = shuffled.pop()
                hands[draw_for_hand - 1].append(card_drawn)
                print("Card drawn for Hand", draw_for_hand, "was",
                      card_drawn)
                print("Hands are now:\n")
                format_output(hands)
                continue           

        # choice is q, Q, S or cards in deck are over
        elif (len(shuffled) == 0 or choice == 'q' or
              choice == 'Q' or choice == 's' or choice == 'S'):            
            win = winner(hands)
            if win[0] != 0:
                print("Hand", win[1], "won by", win[0], "points")
            else:
                print("Both hands busted. ")
            if len(shuffled) == 0:
                choice = 'q'

        elif choice == 'w':
            print("Current hands are:\n")
            format_output(hands)

        elif choice == 'c':
            print("Cards left in deck are:\n", shuffled)

        else:
            print("Invalid choice; choose again. ")
            continue            
        

def main():
    program()

main()

                    
               
                       
