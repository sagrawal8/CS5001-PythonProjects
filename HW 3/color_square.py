'''
Name: Shashank Agrawal
Class: CS 5001
Program: color_square
'''

from color_square_helper import *

def main():
    flag = False   #counter for whether row/column criteria is satisfied

    while flag == False:

        column = input("Input valid column between a and h or A and H (ends included): ")
        row = int(input("Input valid row between 1 and 8 (ends included): "))

        if(check_valid_row(row) == False or check_valid_column(column) == False):
            print("Row or column is invalid. Check if it is between specified limit and if" +
                  " it is single number/character.")
            continue
        
        flag = True

        '''
        Since we are starting from bottom left corner, if the remainders for columns and
        rows when divided by 2 are similar, the square is dark. 
        '''
        
        if((ord(column) % 2) == (row % 2)):  
            print("The square {0}{1} is Black.".format(column.upper(), row))

        else:
             print("The square {0}{1} is White.".format(column.upper(), row))

main()
                  
                 
