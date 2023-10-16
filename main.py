print("КРЕСТИКИ-НОЛИКИ")
print("---------------")
board = [[" " for _ in range(3)] for _ in range(3)]
def display_board():
    print("  0 1 2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print()

def is_valid_move(row, col):
    if 0 <= row < 3 and 0 <= col < 3:
        if board[row][col] == " ":
            return True
    return False


def has_won(symbol):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol:
            return True
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False

move_count = 0
first_player_turn = True
while move_count < 9:
    display_board()
    if first_player_turn:
        print("Ход первого игрока (X)")
    else:
        print("Ход второго игрока (O)")

    row = int(input("Введите номер строки: "))
    col = int(input("Введите номер столбца: "))

    if is_valid_move(row, col):
        if first_player_turn:
            board[row][col] = "X"
            if has_won("X"):
                display_board()
                print("Первый игрок выиграл!")
                break
        else:
            board[row][col] = "O"
            if has_won("O"):
                display_board()
                print("Второй игрок выиграл!")
                break
        first_player_turn = not first_player_turn
        move_count += 1
    else:
        print("Неверный ход. Попробуйте еще раз.")

if move_count == 9:
    display_board()
    print("Ничья!")
