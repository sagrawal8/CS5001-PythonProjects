'''
Name: Shashank Agrawal
Class: CS 5001
Program: Fontastic - helper
'''
import traceback

def create_dict():
    '''
    Function: create_dict
    Parameters: None
    Returns: dictionary (nested list):
                contains keys (English) and
                value (Morse, Phonetic, etc.)
                pairs
    Does: reads fonts.txt and assigns keys and values
        depending on how they are ordered in the text file.
        First line is read and the indexes of columns for different
        fonts are stored. Remaining lines are read and keys and values
        are stored based on the pre-determined indexes
    '''
    try:
        f = open("fonts.txt",'r')
        line = f.readline()
        split = line.split()
        #used to find index of column containing english fonts
        english_index = -1

        #checks if the word METADATA is present
        if split[0] == "METADATA":
            for x in range(1, len(split), 1):                
                if(split[x].lower() == "english"):
                    english_index = x - 1
        else:
            print("First word is not METADATA; Font file incorrect")
            return()
               
        lines = f.readlines()
        length_lines = len(lines)
        keys = []
        values = [[] for _ in range(length_lines)]
        
        for x in range(0, len(lines), 1):
            fontss = lines[x]            
            fontss_split = fontss.split()
            keys.append(fontss_split[english_index])
            del fontss_split[english_index]            
            for y in range(0, len(fontss_split), 1):
                values[x].append(fontss_split[y])

        f.close()                          
        return dict(zip(keys, values))                
        
    except OSError as err:
        print("OS error: {0}".format(err))

    except:
        print("Error: {0}".format(err))


def create_font_order():
    '''
    Function: create_font_order
    Parameters: None
    Returns: fonts(list)
                list containing the different fonts
                stored at similar indexes as mentioned
                in fonts.txt. 
    Does: reads the first line in fonts.txt and returns the
        same line without the word METADATA and English in it.
        This is required to find the order of values assigned to
        each key in the dictionary.
    '''
    try:
        f = open("fonts.txt",'r')
        line = f.readline()
        split = line.split()
        fonts = []
        if split[0] == "METADATA":
                for x in range(1, len(split), 1):
                    if(split[x].lower() == "english"):
                        continue
                    fonts.append(split[x].upper())

        f.close()
        return fonts

    except OSError as err:
        print("OS error: {0}".format(err))

    except:
        print("Error: {0}".format(err))

def read_file_from(file_from):
    '''
    Function: read_file_from
    Parameters: file_from (string):
                    String containing name of file
                    to be read from.
    Returns: line_from (string):
                String containing text in english
                to be translated to a different font
    Does: reads a file and returns the text in it as a string
    '''
    try:
        f = open(file_from, 'r')
        lines = f.readlines()
        line_from = ""
        for x in lines:
            line_from = line_from + x
        f.close()
        return line_from
    except OSError as err:
        print("OS error: {0}".format(err))
    except Exception as e:
        traceback.print_exc()

def convert(dictionary, fonts, line_from, font_from, font_to):
    '''
    Function: convert
    Parameters: dictionary (dict):
                    contains the key value pairs
                fonts (list):
                    contains the type of fonts each key
                    is associated with
                line_from (string):
                    line to be translated
                front_from (string):
                     font of line_from
                font_to (string):
                    font line_from is converted to
    Returns: line_to (string):
                translated string to be written in output file
    Does: converts each letter in line_from to font 'font_to'
        Since there are multiple values associated with a single
        key, the right value is determined using the fonts list.
        In order to meet column width requirements, a new line
        characted is added every 3 words.
    
    '''
    try:
        font_to_index = fonts.index(font_to.upper())
        line_to = ""
        count = 0
                    
        for letter in line_from:
            if letter == " ":
                line_to = line_to[:-1]
                line_to += "/"
                count += 1
                flag = False
            elif letter == "\n":
                continue

            else:                
                translated_letter = dictionary[letter.upper()]                
                if translated_letter == None:                
                    raise Exception("Letter to be translated ", letter, " not found in dictionary.")
                if count % 3 == 0 and count > 0 and flag == False:
                    line_to += "\n"
                    flag = True
                line_to += translated_letter[font_to_index] + " "               
        
        return line_to.strip()
    
    
    except OSError as err:
        print("OS error: {0}".format(err))
    except Exception as e:
        traceback.print_exc()
        
def write_file_to(file_to, line_to):
    '''
    Function: write_file_to
    Parameters: file_to (string):
                    String containing name of file
                    to be written to.
                line_to (string):
                    line to be written in new file
    Returns: None
    Does: writes into a file
    '''
    f = open(file_to, 'w')
    f.write(line_to)
    f.close()
    
def read_directive():
    '''
    Function: read_directive
    Parameters: None
    Returns: None
    Does: reads directives.txt to find out what line has to be
    converted from which font to which font. Converts the line
    and writes it into output file
    '''
    try:
        f = open("directives.txt", 'r')
        lines = f.readlines()
        dictionary = create_dict()

        if dictionary == None:
            raise Exception ("Dictionary was unable to be made")
        fonts = create_font_order()

        for x in range(0, len(lines), 1):
            lines_split = lines[x].split()
            font_from = lines_split[0]
            font_to = lines_split[1]
            file_from = lines_split[2]
            file_to = lines_split[3]            

            if font_to.upper() in fonts:
                line_from = read_file_from(file_from)                
                line_to = convert(dictionary, fonts, line_from, font_from, font_to)
                write_file_to(file_to, line_to)
                print("Writing into file has completed successfully")
            else:
                raise Exception("Font to be converted from or font to be converted to metadata missing")                

        f.close()       

    except OSError as err:
        print("OS error: {0}".format(err))

    except Exception as e:
        traceback.print_exc()
        


