# Richard Waltiere rcw232@nau.edu
# Joshua Walsh jpw273@nau.edu

from lab5_supportfile import *

# Takes a string input and transforms it into a horizontal or vertical banner.
# Input string must be 31 characters or less.


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

    if len(banner_letters) > 31:
        print("Banner must be 31 characters or less.")
        return None

    horiz_or_vert = choose_orientation()

    print()

    if horiz_or_vert == 'V':
        display_banner_vertical(banner_letters)

    if horiz_or_vert == 'H':
        display_banner_horizontal(banner_letters)


# Receives string input from user. Banner will be created from this input.
def choose_banner():
    choice = input("Please enter the banner word or phrase (letters only): ")
    print()

    return choice


# Detects whether the chosen banner is a valid input.
def valid_choice(banner_letters):
    alphabet = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' '
    ]

    for letter in banner_letters:
        if letter not in alphabet:
            return False

    return True


# User chooses orientation--horizontal or vertical.


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


# Banner is broken into a list comprised of the
# individual characters in the banner.


def transform_to_list(banner_choice):
    banner_choice = banner_choice.upper()

    transform_to_list = list(banner_choice)

    return transform_to_list


# Displays one full letter of the banner


def display_letter(banner_letter):
    for row in banner_letter:
        print(row)
    print()


# Displays a single line of a horizontally written banner.
# When six lines have been printed, the entire
# horizontal banner will be displayed.


def display_line_of_banner(banner_letters, line_to_display):
    for letter in banner_letters:
        current_letter_banner = letter_to_banner[letter]
        print(current_letter_banner[line_to_display], end='  ')


# Displays the vertical banner one letter at a time.
# Only one verical column allowed in the banner; vertical banners cannot
# be printed side-by-side.


def display_banner_vertical(banner_letters):
    for letter in banner_letters:
        display_letter(letter_to_banner[letter])


# Displays the horizontal banner. Only 15 letters can be printed before
# letters begin to overlap. The banner is broken up into two horizontal lines
# if the length of the banner exceeds 15 characters.


def display_banner_horizontal(banner_letters):
    if len(banner_letters) > 15:
        banner_words_line1 = banner_letters[:15]
        banner_words_line2 = banner_letters[15:]

        for line in range(6):
            display_line_of_banner(banner_words_line1, line)
            print()

        print()

        for line in range(6):
            display_line_of_banner(banner_words_line2, line)
            print()

    else:
        for line in range(6):
            display_line_of_banner(banner_letters, line)
            print()


if __name__ == '__main__':
    main()
