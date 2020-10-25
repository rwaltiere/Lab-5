<<<<<<< HEAD
banner_N = ['OO     OO', 'OOO    OO', 'OOOO   OO', 'OO OO  OO', 'OO  OO OO', 'OO    OOO']
banner_O = ['OOOOOOOOO', 'O       O', 'O       O', 'O       O', 'O       O', 'OOOOOOOOO']
banner_P = ['OOOOOOOOO', 'OO     OO', 'OOOOOOOOO', 'OO       ', 'OO       ', 'OO       ']
banner_Q = ['OOOOOOOO ', 'OO    OO ', 'OO    OO ', 'OO    OO ', 'OOOOOOOO ', '      OOO']
banner_R = ['OOOOOOOOO', 'OO     OO', 'OOOOOOOOO', 'OOOO     ', 'OO OOO   ', 'OO   OOO ']
banner_S = ['OOOOOOOOO', 'OO       ', 'OOOOOOOOO', '       OO', '       OO', 'OOOOOOOOO']
banner_T = ['OOOOOOOOO', 'OOOOOOOOO', '   OOO   ', '   OOO   ', '   OOO   ', '   OOO   ']
banner_U = ['OO     OO', 'OO     OO', 'OO     OO', 'OO     OO', 'OOOOOOOOO', 'OOOOOOOOO']
banner_V = ['OO     OO', 'OO     OO', 'OO     OO', ' OO   OO ', '  OOOOO  ', '   OOO   ']
banner_W = ['OO  O  OO', 'OO  O  OO', 'OO  O  OO', 'OO  O  OO', 'OO  O  OO', ' OOO OOO ']
banner_X = ['OO     OO', ' OO   OO ', '  OOOOO  ', '  OOOOO  ', ' OO   OO ', 'OO     OO']
banner_Y = ['OO     OO', 'OO     OO', ' OO   OO ', '  OO OO  ', '   OOO   ', '   OOO   ']
banner_Z = ['OOOOOOOOO', '      OOO', '    OOO  ', '  OOO    ', 'OOO      ', 'OOOOOOOOO']

def display_banner_vertical(letter):
    for row in letter:
        print(row)

def display_banner_horizontally(letter1, letter2):
    for row in range(6):
        print(f'{letter1[row]}  {letter2[row]}')

=======
# Richard Waltiere rcw232@nau.edu
# Joshua Walsh jpw273@nau.edu 

from lab5_supportfile import *

def main():
    banner_choice = choose_banner()
    banner_choice = banner_choice.upper()
    
    banner_letters = transform_to_list(banner_choice)
    
    while not valid_choice(banner_letters):
        print()
        print("There is an invalid character in your banner.")
        print("Letters and spaces only. \n")
        
        banner_choice = choose_banner()
        banner_choice = banner_choice.upper()
        
        banner_letters = transform_to_list(banner_choice)

    horiz_or_vert = choose_orientation()
    
    print()

    if horiz_or_vert == 'V':
        display_banner_vertical(banner_letters)

    if horiz_or_vert == 'H':
        display_banner_horizontal(banner_letters)
        

def choose_banner():
    choice = input("Please enter the banner word or phrase (letters only): ")
    print()
    
    return choice

def valid_choice(banner_letters):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
                'Y', 'Z', ' ']

    for letter in banner_letters:
        if letter not in alphabet:
            return False
        
    return True

def choose_orientation():
    print("Would you like your banner to print horizontally or vertically?")
    horiz_or_vert = input("Enter H for horizontal, V for vertical: ")
    horiz_or_vert = horiz_or_vert.upper()
    
    while horiz_or_vert != 'H' and horiz_or_vert != 'V':
        print()
        print("Invalid input. Please enter only H or V.")
        print()

        horiz_or_vert = input("Enter H for horizontal, V for vertical: ")
        horiz_or_vert = horiz_or_vert.upper()

    return horiz_or_vert
        
def transform_to_list(banner_choice):
    banner_choice = banner_choice.upper()
    
    transform_to_list = list(banner_choice)

    return transform_to_list

def display_letter(banner_letter):
    for row in banner_letter:
        print(row)
    print()

def display_line_of_banner(banner_letters, line_to_display):
    for letter in banner_letters:
        current_letter_banner = letter_to_banner[letter]
        print(current_letter_banner[line_to_display], end='  ')

def display_banner_vertical(banner_letters):
    for letter in banner_letters:
        display_letter(letter_to_banner[letter])

def display_banner_horizontal(banner_letters):
    for line in range(6):
        display_line_of_banner(banner_letters, line)
        print()

if __name__ == '__main__':
    main()
>>>>>>> a0c1df04ffe536074c8f41c60e6842797f671363
