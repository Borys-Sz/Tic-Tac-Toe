# write your code here
cells = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
cells = list(cells)

import sys

board = [
    [cells[0], cells[1], cells[2]],
    [cells[3], cells[4], cells[5]],
    [cells[6], cells[7], cells[8]],
]

def board_display():
    print("---------")
    print("|", board[0][0], board[0][1], board[0][2], "|")
    print("|", board[1][0], board[1][1], board[1][2], "|")
    print("|", board[2][0], board[2][1], board[2][2], "|")
    print("---------")

def game_state_check():
    X = 0
    O = 0
    for i in board:
        for c in i:
            if c == "X":
                X += 1
            elif c == "O":
                O += 1
    xwins = 0
    owins = 0
    if board[0][0] == board[1][1] == board[2][2] == "X" or board[0][2] == board[1][1] == board[2][0] == "X":
        xwins += 1
    if board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O":
        owins += 1
    if board[0][0] == board[0][1] == board[0][2] == "X" or board[1][0] == board[1][1] == board[1][2] == "X" or board[2][0] ==\
        board[2][1] == board[2][2] == "X":
        xwins += 1
    if board[0][0] == board[0][1] == board[0][2] == "O" or board[1][0] == board[1][1] == board[1][2] == "O" or board[2][0] ==\
        board[2][1] == board[2][2] == "O":
        owins += 1
    if board[0][0] == board[1][0] == board[2][0] == "X" or board[0][1] == board[1][1] == board[2][1] == "X" or board[0][2] ==\
        board[1][2] == board[2][2] == "X":
        xwins += 1
    if board[0][0] == board[1][0] == board[2][0] == "O" or board[0][1] == board[1][1] == board[2][1] == "O" or board[0][2] ==\
        board[1][2] == board[2][2] == "O":
        owins += 1
    if xwins:
        print("X wins")
        sys.exit()
    elif owins:
        print("O wins")
        sys.exit()
    elif not xwins and not owins and X + O == 9:
        print("Draw")
        sys.exit()
    elif not xwins and not owins and X + O < 9:
        print("Game not finished")

player = "X"

while True:
    game_state_check()
    if player == "X":
        board_display()
        move = input("Enter the coordinates")
        coords = move.split(" ")
        if coords[0].isalpha() or coords[1].isalpha():
            print("You should enter numbers!")
            continue
        elif int(coords[0]) < 1 or int(coords[0]) > 3 or int(coords[1]) < 1 or int(coords[1]) > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        elif board[int(coords[0]) - 1][int(coords[1]) - 1] in "XO":
            print("This cell is occupied! Chose another one!")
            continue
        else:
            if int(coords[0]) == 1 and int(coords[1]) == 1:
                board[0][0] = "X"
            if int(coords[0]) == 1 and int(coords[1]) == 2:
                board[0][1] = "X"
            if int(coords[0]) == 1 and int(coords[1]) == 3:
                board[0][2] = "X"
            if int(coords[0]) == 2 and int(coords[1]) == 1:
                board[1][0] = "X"
            if int(coords[0]) == 2 and int(coords[1]) == 2:
                board[1][1] = "X"
            if int(coords[0]) == 2 and int(coords[1]) == 3:
                board[1][2] = "X"
            if int(coords[0]) == 3 and int(coords[1]) == 1:
                board[2][0] = "X"
            if int(coords[0]) == 3 and int(coords[1]) == 2:
                board[2][1] = "X"
            if int(coords[0]) == 3 and int(coords[1]) == 3:
                board[2][2] = "X"
        board_display()
        player = "O"
    elif player == "O":
        board_display()
        move = input("Enter the coordinates")
        coords = move.split(" ")
        if coords[0].isalpha() or coords[1].isalpha():
            print("You should enter numbers!")
            continue
        elif int(coords[0]) < 1 or int(coords[0]) > 3 or int(coords[1]) < 1 or int(coords[1]) > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        elif board[int(coords[0]) - 1][int(coords[1]) - 1] in "XO":
            print("This cell is occupied! Chose another one!")
            continue
        else:
            if int(coords[0]) == 1 and int(coords[1]) == 1:
                board[0][0] = "O"
            if int(coords[0]) == 1 and int(coords[1]) == 2:
                board[0][1] = "O"
            if int(coords[0]) == 1 and int(coords[1]) == 3:
                board[0][2] = "O"
            if int(coords[0]) == 2 and int(coords[1]) == 1:
                board[1][0] = "O"
            if int(coords[0]) == 2 and int(coords[1]) == 2:
                board[1][1] = "O"
            if int(coords[0]) == 2 and int(coords[1]) == 3:
                board[1][2] = "O"
            if int(coords[0]) == 3 and int(coords[1]) == 1:
                board[2][0] = "O"
            if int(coords[0]) == 3 and int(coords[1]) == 2:
                board[2][1] = "O"
            if int(coords[0]) == 3 and int(coords[1]) == 3:
                board[2][2] = "O"
        board_display()
        player = "X"


