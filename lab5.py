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

