import random

def build_board(dims):
    return [['^' for count in range(dims)] for count in range(dims)]

def print_board(board):
    for b in board:
        print(*b)

# board = build_board(8)
# print_board(board)

def build_ship(dims):
    len_ship = random.randint(2, dims)
    orientation = random.randint(0, 1)

    if orientation == 0:
        row_ship = [random.randint(0, dims - 1)] * len_ship
        col = [random.randint(0, dims - len_ship)]
        col_ship = list(range(col, col + len_ship))
        coords = tuple(zip(row_ship, col_ship))
    else:
        # Same as above except switch column and row
        col_ship = [random.randint(0, dims - 1)] * len_ship
        row = random.randint(0, dims - len_ship)
        row_ship = list(range(row, row + len_ship))
        coords = tuple(zip(row_ship, col_ship))
    return list(coords)

# ship = build_ship(4)

# print(ship)


def user_guess():
    row = int(input('Row: ')) - 1
    col = int(input('Column: ')) - 1
    return(row, col)

# x = user_guess()
# print(x)


def update_board(guess, board, ship, guesses):
    if guess in guesses:
        print('You already guessed that, silly!')
        return board
    guesses.append(guess)
    if guess in ship:
        print('You hit my battleship!')
        board[guess[0]][guess[1]] = 'X'
        ship.remove(guess)
        return board
    print('LOL miss!')
    return board

# guesses = [] 
# our_guess = user_guess()
# board = update_board(our_guess, board, ship, guesses)
# print_board(board)

def welcome_message():
    print('Welcome to Battleship!')
    print('There is a battleship hidden in this board. Enter your row and column guesses to sink it!')


def main():
    welcome_message()
    board = build_board(8)
    ship = build_ship(5)
    guesses = []
    while len(ship) > 0:
        board = update_board(user_guess(), board, ship, guesses)
        print_board(board)
    print('You sunk my battleship!')
    return


main()
