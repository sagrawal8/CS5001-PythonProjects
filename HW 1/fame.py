'''
 CS5001
 Spring 2020
 HW1
 Shashank Agrawal
'''

def main():

    fame_minutes = int(input("How many minutes of fame do you want? "))     #input from user

    fame_hours = fame_minutes / 60    #hours = minutes/60
    formatted_hours = "{:.3f}".format(fame_hours)   #format upto 3 decimal places
    
    fame_days = fame_hours / 24   #days = hours/24
    formatted_days = "{:.3f}".format(fame_days)     #format upto 3 decimal places
    
    print("Solid! You'll be in the spotlight for: ")
    print(fame_minutes, " minutes(s), which is")
    print(">> ", fame_minutes*60, " seconds(s), which is ")     #seconds = minutes*60
    print(">>>> ", formatted_hours, " hour(s), which is ")
    print(">>>>>> ", formatted_days, " day(s) ")    


main()
