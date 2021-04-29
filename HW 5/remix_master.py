'''
Name: Shashank Agrawal
Class: CS 5001
Program: remix_master
'''

from music import *
from remix_master_helper import *
# Stores imported playlist from music.py
playlist = PLAYLIST
# Stores imported songs from music.py
songs = SONGS


def main():
    '''
    Function: main
    Parameters: None
    Returns: None
    Does: Runs the menu used to work the program
    '''
    
    print("Welcome to Remix Master where",
          "you can remix greatest hits!")
    # index of song in playlist
    title_choice = song_menu(playlist, songs)
    #copy of song used for edits
    remix_song = songs[title_choice]
    menu_choice = ''                            
    while menu_choice.upper() != 'Q':

        menu_choice = program_menu()
        
        if(menu_choice.upper() == 'L'):
            title_choice = song_menu(playlist, songs)
            remix_song = songs[title_choice]

        elif(menu_choice.upper() == 'T'):
            print("Title of song is", playlist[title_choice])

        elif(menu_choice.upper() == 'S'):
            remix_song = subs_word(remix_song)

        elif(menu_choice.upper() == 'P'):
            playback_song(remix_song)
        
        elif(menu_choice.upper() == 'R'):
             remix_song = reverse_song(remix_song)

        elif(menu_choice.upper() == 'X'):
             remix_song = songs[title_choice]

        else:
            print("Enter a valid menu option. ")
            continue
        

main()
    
    
