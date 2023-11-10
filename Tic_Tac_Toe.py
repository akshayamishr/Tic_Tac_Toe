def constboard(board):
    print('Current status of the board: \n\n')
    for i in range(0, 9):
        if (i % 3 == 0 and i != 0):
            print("\n")
        if (board[i] == 0):
            print("_  ", end=' ')
        if (board[i] == 1):
            print("O  ", end=' ')
        if (board[i] == -1):
            print("X  ", end=' ')
    print('\n\n')


def User_1_Turn(board):
    pos = input("Enter the position of X [1,2,3,...,9] ")
    pos = int(pos)
    if (board[pos-1] != 0):
        print("Wrong Move")
        exit(0)
     # if(board[pos-1]==0):
    board[pos-1] = -1


def User_2_Turn(board):
    pos = input("Enter the position of O [1,2,3,...,9] ")
    pos = int(pos)
    if (board[pos-1] != 0):
        print("Wrong Move")
        exit(0)
     # if(board[pos-1]==0):
    board[pos-1] = 1


def analyzeboard(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
          [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for i in range(0, 8):
        if (board[cb[i][0]] != 0 and
           board[cb[i][0]] == board[cb[i][1]] and
           board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][0]]

    return 0


def min_max(board, player):
    x = analyzeboard(board)
    if (x != 0):
        return (x*player)
    pos = -1
    value = -2
    for i in range(0, 9):
        if (board[i] == 0):
            board[i] = player
            score = -min_max(board, player*-1)
            board[i] = 0
            if (score > value):
                value = score
                pos = i
    if (pos == -1):
        return 0
    return value


def Comp_Turn(board):
    pos = -1
    value = -2
    for i in range(0, 9):
        if (board[i] == 0):
            board[i] = 1
            score = -min_max(board, -1)
            board[i] = 0
            if (score > value):
                value = score
                pos = i
    board[pos] = 1


def main():
    choice = input("Enter 1 for single player or Enter 2 for multiplayer \n")
    choice = int(choice)
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if (choice == 1):
        print("Computer --> O VS You --> X")
        player = input("Enter 1 for 1st chance Or Enter 2 for 2nd chance \n")
        player = int(player)
        for i in range(0, 9):
            if (analyzeboard(board) != 0):
                break
            if ((i+player) % 2 == 0):
                Comp_Turn(board)
            else:
                constboard(board)
                User_1_Turn(board)
    else:
        for i in range(0, 9):
            if (analyzeboard(board) != 0):
                break
            if (i % 2 == 0):
                constboard(board)
                User_1_Turn(board)
            else:
                constboard(board)
                User_2_Turn(board)

    x = analyzeboard(board)
    if (x == 0):
        constboard(board)
        print("Draw!!!")
    if (x == 1):
        constboard(board)
        print("O Wins!! and X loses!!")
    if (x == -1):
        constboard(board)
        print("O Wins!! and X loses!!")

main()