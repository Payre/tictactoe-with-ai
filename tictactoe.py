#necessary modules
import numpy as np
import random as rad



#creating a game board

'''initializing an empty board with an order of 3x3'''
def tboard():
    board = np.array([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
    print(board)
    print(board)
    return board


def ps():
    #player choose - completed
    while True:
        inpu = input("Enter X or O: ").lower() #fucking dumb, forgot to take input again inside the loop.
        print(inpu)

        if inpu == 'x' or inpu == 'o':
            print(f"Player one is {inpu}")
            break
        print("Please enter a valid input, only 'X' and 'O'.")
    return ps


#position selector

#main function
def main(board, inpu):
    tboard()
    print(board)
    ps()
    for x in range(9):
        r = int(input("Enter the row: "))
        c = int(input("Enter the column: "))
        r -= 1
        c -= 1
    print("ok xa ta")
    npc1 = rad.randint(0,9)
    npc2= rad.randint(0,9)
    if r == npc1 and c == npc2:
        pass
    board[r,c]=inpu
    print(board)

print("hello!")


#taking input from the user.
#choose position - make infinite; switch player; declare winner.
#once the game is functional, release beta 0.0 on github
#try to implement function for alpha release.
#make more user friendly 1.5
#add graphics 2.0
#end project

#libraries infomration
'''random: https://docs.python.org/3/library/random.html'''

#creating ai is aaukat bahira.