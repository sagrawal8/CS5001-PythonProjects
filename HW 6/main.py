'''
Name: Shashank Agrawal
Class: CS 5001
Program: Fontastic - main
'''
import traceback
from Fontastic import * 
def main():
     '''
    Function: main
    Parameters: None
    Returns: None
    Does: Runs driver function
    '''
     try:
         read_directive()
     except Exception as e:
        traceback.print_exc()

main()
