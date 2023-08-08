#сначала создаю и распечатываю игровое поле.
pole = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"],
]

for j in pole:
    print(j)
#У игрока 1 крестик, у игрока 2 нолик
player1_symbol = 'X'
player2_symbol = '0'
current_player = 1 #начинает первый игрок

def winner(board, symbol): #функция проверки на победу
    for row in board: #вертикаль
        if all(cell == symbol for cell in row):
            return True

    for col in range(3):#горизонталь
        if all(board[row][col] == symbol for row in range(3)):
            return True
    # диагональ
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True

    return False
def move_player(player, hod): #функция хода игрока. Нахожу номер индекса в списке
    index = int(hod) - 1
    row_index = index // 3
    col_index = index % 3

    symbol = player1_symbol if player == 1 else player2_symbol
    #проверяю правильно ли игрок сходил
    if int(hod) >= 1 and int(hod) <= 9 and pole[row_index][col_index] != 'X' and pole[row_index][col_index] != '0':
        pole[row_index][col_index] = symbol
    else:
        print("Ошибка ввода. Повторите свой ход")
        return False
    #распечатываю новое игровое поле
    for k in pole:
        print(k)

    return True


for _ in range(9):
    player = 1 if current_player == 1 else 2
    hod = input(f"Ход игрока №{player} - введите номер ячейки, ваш ход закрасится {'X' if player == 1 else '0'}: ")

    while not move_player(player, hod):
        hod = input("Недопустимый ход. Введите номер ячейки снова: ")

    if winner(pole, player1_symbol):
        print("Игрок №1 выиграл!")
        break
    elif winner(pole, player2_symbol):
        print("Игрок №2 выиграл!")
        break
    elif _ == 8:
        print("Ничья.")

    current_player = 2 if current_player == 1 else 1
