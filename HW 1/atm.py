'''
 CS5001
 Spring 2020
 HW1
 Shashank Agrawal
'''


def main():

    total_money = int(input("How much to withdraw? "))      #ask user for input

    fifties = int(total_money / 50)     #calculate number of fifties
    remainder = total_money % 50        #find remainder money
    
    twenties = int(remainder / 20)      #calculate number of twenties
    remainder = int(remainder % 20)     #find remainder money

    tens = int(remainder / 10)          #calculate number of tens
    remainder = int(remainder % 10)     #find remainder money

    fives = int(remainder / 5)          #calculate number of fives
    remainder = int(remainder % 5)      #find remainder money

    ones = int(remainder / 1)           #rest of money is ones
    
    print("You asked for $", total_money)
    print("That breaks down to ")
    print(fifties, " fifties")
    print(twenties, " twenties")
    print(tens, " tens")
    print(fives, " fives")
    print(ones, " ones")    
            


main()
