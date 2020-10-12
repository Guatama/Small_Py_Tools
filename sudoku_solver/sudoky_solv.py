board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def print_board(board):
    counter_h = 0
    for line in board:
        if counter_h == 3:
            print('- - - + - - - + - - - ')
            counter_h = 0

        counter_v = 0
        for item in line:
            if counter_v == 3:
                print('|', end=' ')
                counter_v = 0

            print(item, end=' ')
            counter_v += 1

        counter_h += 1
        print()


def check_if_empty(board):
    for row_ind in range(len(board)):
        for col_ind in range(len(board[0])):
            if board[row_ind][col_ind] == 0:
                return row_ind, col_ind


def valid(board, num, pos):
    # Checking row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Checking box
    box_row = pos[1] // 3
    box_col = pos[0] // 3

    for i in range(box_col * 3, box_col * 3 + 3):
        for j in range(box_row * 3, box_row * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    check = check_if_empty(board)
    if not check:
        return True
    else:
        row, col = check

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


if __name__ == "__main__":
    print_board(board)
    solve(board)
    print('\n', '-' * 30, '\n')
    print_board(board)
