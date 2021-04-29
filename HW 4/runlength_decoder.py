'''
Name: Shashank Agrawal
Class: CS 5001
Program: runlength_decoder
'''

from hw4data import *
from runlength_decoder_helper import *
def main():
        
    a = DATA0
    b = DATA1
    c = DATA2
    d = DATA3
    e = DATA4
    f = DATA5
    print("DATA0 decodes to")
    arrToString(decode(a))
    print("DATA1 decodes to")
    arrToString(decode(b))
    print("DATA2 decodes to")
    arrToString(decode(c))
    print("DATA3 decodes to")
    arrToString(decode(d))
    print("DATA4 decodes to")
    arrToString(decode(e))
    print("DATA5 decodes to")
    arrToString(decode(f))

main()
