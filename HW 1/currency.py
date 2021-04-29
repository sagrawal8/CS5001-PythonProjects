'''
 CS5001
 Spring 2020
 HW1
 Shashank Agrawal
'''

'''
Test case #1:
Input: $250
Total fee: $12.00

Test case #2:
Input: $80
Total fee: $6.90

Test case #3:
Input: $110.34
Total fee: $7.81

'''

def main():

    user_money = float(input("How much to convert?: "))     #ask for input

    fee = float(0.03 * user_money + 4.50)                   #calculate fee using algo given
    formatted_fee = "{:.2f}".format(fee)                    #format fee to 2 decimal places
    
    print("The fee you are being charged is $", formatted_fee)   #print fee


main()
