'''
Name: Shashank Agrawal
Class: CS 5001
Program: color_square helper file
'''


'''
Function: check_valid_row
Parameters: row (int): row of chessboard
Returns: True/False
Does: Checks whether row lies between 1 and 8
'''
def check_valid_row(row):
    if(row < 1 or row > 8):
        return False
    else:
        return True

'''
Function: check_valid_column
Parameters: column (String): String of chessboard
Returns: True/False
Does: Checks whether column lies between ASCII values for a to h or A to H
'''
def check_valid_column(column):
    if(len(column) > 1):
       return False
    elif(ord(column) >= 65 and ord(column) <= 72):
        return True
    elif(ord(column) >=97 and ord(column) <= 104):
        return True
    else:
        return False
