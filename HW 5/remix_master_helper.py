'''
Name: Shashank Agrawal
Class: CS 5001
Program: remix_master
'''



def song_menu(playlist, songs):
    '''
    Function: song_menu
    Parameters:
            playlist (list):
                contains titles of songs
            songs (list):
                contains the lyrics of songs        
    Returns: choice - 1 (int)
                index of song chosen in playlist list
    Does: Displays menu to user to choose song from
        available options. Checks if user input is numeric
        and within sepcified range. It then displays the
        lyrics of the song chosen    
'''

    # counter to test conditions
    flag = True
    while(flag == True):
        print("Please choose a song you would" +
              " like to remix:")
        for i in range(0, len(playlist), 1):
            print(str(i+1) + ":", playlist[i])
        choice = input("Your choice: ")

    # check if input is numeric
        if(choice.isnumeric() == False):
            print("Enter valid choice.")
            continue
        choice = int(choice)

    # check if input is within specified range
        if choice >= 1 and choice <= len(playlist):
            flag = False

        else:
            print("Enter a valid choice.")
            continue

    # print lyrics of chosen song
    print("\nYour chosen song is: ")
    song = songs[choice - 1]
    string = ""
    for i in range(0, len(song), 1):
        string = string + song[i]+ "\n"
    print(string)

    return (choice - 1)


def program_menu():
    '''
    Function: program_menu
    Parameters: None        
    Returns: string: Choice of user
    Does: Displays available options for user to remix song
        Returns user choice
    '''
    print("\nChoose from the following menu options")
    print("L: Load a different song\nT: Title of current"
          " song\nS: Substitute a word\nP: Playback your song"
          "\nR: Reverse it!\nX: Reset to original song\n"
          "Q: Quit")
    return(input("Your choice: "))



def subs_word(remix_song):
    '''
    Function: subs_word
    Parameters:
            remix_song (list):
                list containing lyrics of song to be edited              
    Returns: edited_song (list):
                list containing lyrics of song w subbed word
    Does: Asks user for words to find and replace. Finds word
        in remix_song and replaces it. If word isn't found,
        'word to replace not found' is displayed.
    '''

    find = input("What word would you like to replace? ")
    find = find.lower()
    replace = input("What word would you like to replace " +
                    find + " with? ")

    # counter to check if word to be replaced is found
    found = False
    edited_song = []
    for i in range(0, len(remix_song), 1):
        line = remix_song[i]
        line = line.lower()
        if(find in line):
            found = True
        edited_line = line.replace(find, replace)
        edited_song.append(edited_line)

    if(found == False):
        print("Word to replace not found.")
    return edited_song
        

def playback_song(remix_song):
    '''
    Function: playback_song
    Parameters:
            remix_song (list):
                list containing lyrics of song to be played back             
    Returns: None
    Does: Plays back remixed song containing/not-containing edits
        from user
    '''

    string = ""
    for i in range(0, len(remix_song), 1):
        string = string + remix_song[i]+ "\n"
    print(string)


def reverse_song(remix_song):
    '''
    Function: reversed_song
    Parameters:
            remix_song (list):
                list containing lyrics of song to be edited              
    Returns: reversed_song (list):
                list containing lyrics of song in reverse
    Does: Reverses the words of the song but not the letters.
        Uses " " as a delimitter and appends each word in
        each line (remix_song[i]) to a new string called rev_line.
        This new string is appended to a new list called reversed_song
        Goes through each line of remix_song.
        reversed_song is then reversed itself as the lyrics are
        appended in reverse order ie. last line is at index 0. 
    '''
    reversed_song = []
    for i in range(len(remix_song) - 1, -1, -1):
        rev_line = " ".join(reversed(remix_song[i].split(" ")))
        reversed_song.append(rev_line)

    reversed_song = reversed_song[::-1]
    return reversed_song
