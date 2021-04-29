'''
Name: Shashank Agrawal
Class: CS 5001
Program: runlength_decoder
'''

'''
Function: decode
Parameters:
    a (array): array to be decoded
Returns:
    b(array): decoded array
Does:
    Uses the first value of every two values
    as the letter to be repeated and the second value
    as the number of times to be repeated.
    
'''
def decode(a):
    b = []
    for x in a:
        if(isinstance(x,str) == True):
            letter = x
            continue
        if(isinstance(x,int) == True):
            digit = x
        count = 0
        while(count < digit):
            b.append(letter)
            count += 1
    return b

'''
Function: arrToString
Parameters:
    a (array): decoded array
Returns:
    None
Does:
    Prints the decoded array as a string    
'''
def arrToString(a):
    str1 = ''.join(a)
    print(str1)
        
            
        
