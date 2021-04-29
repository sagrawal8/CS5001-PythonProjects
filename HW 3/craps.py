'''
Name: Shashank Agrawal
Class: CS 5001
Program: craps
'''

import random

def main():
    choice = "z"
    Mesg1 = "Tough luck buddy. Try again. "     #random messages displayed by house manager
    Mesg2 = "I guess today isn't your day. Maybe you should blow on the die. "
    Mesg3 = "It must be the air in here. "
    
    while choice != "q":  #checks if choice of user is not q      

        choice = input("Welcome to Craps. Do you want to back out? Type q to do so, otherwise type anything else. ")
        if choice == "q":
            print("You lost!")
            break
    
        die1 = random.randint(1, 6)  #die 1 integer
        die2 = random.randint(1, 6)  #die 2 integer
        total = die1 + die2
        print("You rolled a {} and {}. Your total is {}. ".format(die1, die2, total))
    
        if total == 7 or total == 11:  #winning criteria
            choice = input("Wow you are really good. You win. Enter q to quit or anything else to play again. ")
            if choice == "q":
                print("Thanks for playing!")
    
        elif total == 2 or total == 3 or total == 12:  #losing criteria
            choice = input("You've lost. Wanna try again? Enter q to quit or anything else to play again. ")
            if choice == "q":
                print("Thanks for playing!")
        
        else:               #point criteria
            point = total  
            total = -1
            print("Your point is", point)
            
            while choice != 'q':        #nested while to play point
                while total != 7:

                    choice = input("Do you want to continue? Type q to do so, otherwise type anything else. ")
                    if choice == "q":
                        print("Thanks for playing!")                        
                    
                    die1 = random.randint(1, 6)  #die 1 integer
                    die2 = random.randint(1, 6)  #die 2 integer
                    total = die1 + die2
                    print("You rolled a {} and {}. Your total is {}. ".format(die1, die2, total))
                
                    if total == point:    #winning criteria
                         choice = input("Wow you are really good. You win. Enter q to quit or anything else to play again. ")
                         if choice == "q":
                            print("Thanks for playing!") 

                    elif total == 7:   #losing criteria
                        choice = input("You've lost. Wanna try again? Enter q to quit or anything else to play again. ")
                        if choice == "q":
                            print("Thanks for playing!")

                    else:   #displays random messages from house manager
                        randMesg = random.randint(1,3)
                        if randMesg == 1:
                            print("House Manager:", Mesg1)
                        elif randMesg == 2:
                            print ("House Manager:", Mesg2)
                        else:
                            print("House Manager:", Mesg3)
                    
main()                  


                
                
                
        
        
