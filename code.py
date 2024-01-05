board = {'a8': 'r', 'b8': 'n', 'c8': 'b', 'd8': 'q', 'e8': 'k', 'f8': 'b', 'g8': 'n', 'h8': 'r',
              'a7': 'p', 'b7': 'p', 'c7': 'p', 'd7': 'p', 'e7': 'p', 'f7': 'p', 'g7': 'p', 'h7': 'p',
              'a6': '.', 'b6': '.', 'c6': '.', 'd6': '.', 'e6': '.', 'f6': '.', 'g6': '.', 'h6': '.',
              'a5': '.', 'b5': '.', 'c5': '.', 'd5': '.', 'e5': '.', 'f5': '.', 'g5': '.', 'h5': '.',
              'a4': '.', 'b4': '.', 'c4': '.', 'd4': '.', 'e4': '.', 'f4': '.', 'g4': '.', 'h4': '.',
              'a3': '.', 'b3': '.', 'c3': '.', 'd3': '.', 'e3': '.', 'f3': '.', 'g3': '.', 'h3': '.',
              'a2': 'P', 'b2': 'P', 'c2': 'P', 'd2': 'P', 'e2': 'P', 'f2': 'P', 'g2': 'P', 'h2': 'P',
              'a1': 'R', 'b1': 'N', 'c1': 'B', 'd1': 'Q', 'e1': 'K', 'f1': 'B', 'g1': 'N', 'h1': 'R'}
player_turn = 0
changes_dict = {}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'boo']
figures_dict = []
moves_list = []
qwe = []

class Chess:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        print('    A B C D E F G H' + '\n')
        array_row = list(board.values())
        array = []
        c = 0
        c_of_c = 8
        for el in range(len(array_row)):
            array.append(array_row[el])
            c += 1
            if c == 8:
                print(c_of_c, ' ', *array, ' ', c_of_c)
                c_of_c -= 1
                array = []
                c = 0
        return '\n    A B C D E F G H\n'

    def valid_move(self, move, player_turn=0, test=0):
        if test == 0:
            changes_dict.clear()
        if len(move) < 2:
            return False
        for key, value in board.items():
            if key == move:  # проверка на базовые ходы пешки
                if board[move[0] + (str(int(move[1]) - 2) if player_turn % 2 == 0 else str(int(move[1]) + 2))] == (
                        'P' if player_turn % 2 == 0 else 'p') and move[1] == ('4' if player_turn % 2 == 0 else '5') and \
                        board[move[0] + (str(int(move[1]) - 1) if player_turn % 2 == 0 else str(int(move[1]) + 1))] == '.':  # проверка первого хода пешки на +2
                    if test == 0:
                        changes_dict[move[0] + (str(int(move[1]) - 2) if player_turn % 2 == 0 else str(int(move[1]) + 2))] = '.'
                        changes_dict[key] = ('P' if player_turn % 2 == 0 else 'p')
                        return True
                    else:
                        return True
                elif board[move] == '.' and board[
                    move[0] + (str(int(move[1]) - 1) if player_turn % 2 == 0 else str(int(move[1]) + 1))] == (
                        'P' if player_turn % 2 == 0 else 'p'):
                    if test == 0:
                        changes_dict[move[0] + (str(int(move[1]) - 1) if player_turn % 2 == 0 else str(
                            int(move[1]) + 1))] = '.'  # если не +2 то пешка на +1
                        changes_dict[key] = ('P' if player_turn % 2 == 0 else 'p')
                        return True
                    else:
                        return True
            if move[0] in 'abcdefgh' and move[1] == 'x' and move[-2:] in board.keys() and board[
                move[-2:]] in ('rnpbqk' if player_turn % 2 == 0 else 'RNPBQK'):  # пешка ест
                if letters.index(move[0]) - letters.index(move[2]) == -1 and board[move[0] + (str(int(move[-1]) - 1) if player_turn % 2 == 0 else str(int(move[-1]) + 1))] == ('P' if player_turn % 2 == 0 else 'p'):
                    if test == 0:  # проверка с какой стороны ест пешка
                        changes_dict[
                            move[0] + (str(int(move[3]) - 1) if player_turn % 2 == 0 else str(int(move[3]) + 1))] = '.'
                        changes_dict[move[2:]] = ('P' if player_turn % 2 == 0 else 'p')
                        return True
                    else:
                        return True
                elif letters.index(move[0]) - letters.index(move[2]) == 1 and board[move[0] + (str(int(move[-1]) - 1) if player_turn % 2 == 0 else str(int(move[-1]) + 1))] == ('P' if player_turn % 2 == 0 else 'p'):
                    if test == 0:
                        changes_dict[letters[letters.index(move[2]) + 1] + (
                            str(int(move[3]) - 1) if player_turn % 2 == 0 else str(int(move[3]) + 1))] = '.'
                        changes_dict[move[2:]] = ('P' if player_turn % 2 == 0 else 'p')
                        return True
                    else:
                        return True
        if move[0] == ('N' if player_turn % 2 == 0 else 'n'):
            if move[-2] in 'abcdefgh' and move[-1] in '12345678':  # обычный ход конём
                for knight in [letters[(letters.index(move[-2]) + 1) if letters.index(move[-2]) + 1 <= 7 else 8] + str(int(move[-1]) + 2),
                               letters[(letters.index(move[-2]) + 2) if letters.index(move[-2]) + 2 <= 7 else 8] + str(int(move[-1]) + 1),
                               letters[(letters.index(move[-2]) + 2) if letters.index(move[-2]) + 2 <= 7 else 8] + str(int(move[-1]) - 1),
                               letters[(letters.index(move[-2]) + 1) if letters.index(move[-2]) + 1 <= 7 else 8] + str(int(move[-1]) - 2),
                               letters[(letters.index(move[-2]) - 1) if letters.index(move[-2]) - 1 <= 7 else 8] + str(int(move[-1]) - 2),
                               letters[(letters.index(move[-2]) - 2) if letters.index(move[-2]) - 2 <= 7 else 8] + str(int(move[-1]) - 1),
                               letters[(letters.index(move[-2]) - 2) if letters.index(move[-2]) - 2 <= 7 else 8] + str(int(move[-1]) + 1),
                               letters[(letters.index(move[-2]) - 1) if letters.index(move[-2]) - 1 <= 7 else 8] + str(int(move[-1]) + 2)]:
                    if knight in board.keys() and board[knight] == ('N' if player_turn % 2 == 0 else 'n') and \
                            (len(move) == 3 and 'x' not in move and board[move[-2:]] == '.' or
                             len(move) == 4 and 'x' in move and board[move[2:]] in (
                                     'rnpbqk' if player_turn % 2 == 0 else 'RNPBQK')):
                        if test == 0:
                            changes_dict[knight] = '.'
                            changes_dict[move[-2:]] = ('N' if player_turn % 2 == 0 else 'n')
                            return True
                        else:
                            return True
                if move[0] == ('N' if player_turn % 2 == 0 else 'n') and move[1] in 'abcdefgh' and move[
                                                                                                   -2:] in board.keys() and \
                        (len(move) == 4 and 'x' not in move or len(move) == 5 and move[2] == 'x'):
                    if move[2] == 'x' and board[move[-2:]] == '.' or 'x' not in move and board[move[-2:]] != '.':
                        return False
                    else:
                        for keys, values in board.items():
                            if move[-2] in keys and board[keys] == ('N' if player_turn % 2 == 0 else 'n') \
                                    and move[-2:] in board.keys():
                                if test == 0:
                                    changes_dict[keys] = '.'
                                    changes_dict[move[-2:]] = ('N' if player_turn % 2 == 0 else 'n')
                                    return True
                                else:
                                    return True
                elif move[0] == ('N' if player_turn % 2 == 0 else 'n') and move[1] in '12345678' and move[
                                                                                                     -2:] in board.keys() and \
                        (len(move) == 4 and 'x' not in move or len(move) == 5 and move[2] == 'x'):
                    if move[1] == 'x' and board[move[-2:]] == '.' or 'x' not in move and board[move[-2:]] != '.':
                        return False
                    else:
                        for keys, values in board.items():
                            if move[1] in keys and board[keys] == ('N' if player_turn % 2 == 0 else 'n') and move[
                                                                                                                  -2:] in board.keys():
                                if test == 0:
                                    changes_dict[keys] = '.'
                                    changes_dict[move[-2:]] = ('N' if player_turn % 2 == 0 else 'n')
                                    return True
                                else:
                                    return True
        if move[0] == ('B' if player_turn % 2 == 0 else 'b'):
            if (len(move) == 3 and 'x' not in move and board[move[-2:]] == '.' or len(move) == 4 and move[1] == 'x' and
                move[-2:] in board.keys() and board[move[-2:]] in (
                        'rnbqkp' if player_turn % 2 == 0 else 'RNBQKP')) and move[-2] in 'abcdefgh' and move[
                -1] in '12345678':
                if move[-2] in 'abcdefgh' and move[-1] in '12345678' and (len(move) == 3 or len(move) == 4):
                    possible_bishops = []
                    for one_move in [letters[letters.index(move[-2]) + 1] + str(int(move[-1]) + 1),
                                     letters[letters.index(move[-2]) + 1] + str(int(move[-1]) - 1),
                                     letters[letters.index(move[-2]) - 1] + str(int(move[-1]) + 1),
                                     letters[letters.index(move[-2]) - 1] + str(int(move[-1]) - 1)]:
                        if one_move in board.items():
                            if board[one_move] == ('B' if player_turn % 2 == 0 else 'b') and 'x' in move and \
                                    board[move[-2:]] != '.':
                                if test == 0:

                                    changes_dict[one_move] = '.'
                                    changes_dict[move[-2:]] = ('B' if player_turn % 2 == 0 else 'b')
                                    return True
                                else:
                                    return True
                            elif board[one_move] == ('B' if player_turn % 2 == 0 else 'b') and 'x' not in move and \
                                    board[
                                        move[-2:]] == '.':
                                # print(2)
                                if test == 0:  # если ход на одну клетку в любую сторону
                                    changes_dict[one_move] = '.'
                                    changes_dict[move[-2:]] = ('B' if player_turn % 2 == 0 else 'b')
                                    return True
                                else:
                                    return True

                    for shift in range(1, 7):
                        for bishop in [
                            letters[letters.index(move[-2]) + shift if letters.index(move[-2]) + shift <= 7 else 8] + str(
                                int(move[-1]) + shift),
                            letters[letters.index(move[-2]) + shift if letters.index(move[-2]) + shift <= 7 else 8] + str(
                                int(move[-1]) - shift),
                            letters[letters.index(move[-2]) - shift if letters.index(move[-2]) - shift >= 0 else 8] + str(
                                int(move[-1]) + shift),
                            letters[letters.index(move[-2]) - shift if letters.index(move[-2]) - shift >= 0 else 8] + str(
                                int(move[-1]) - shift)]:
                            if bishop in board.keys():
                                possible_bishops.append(bishop)
                            else:
                                possible_bishops.append(0)
                    for my_bishop in range(len(possible_bishops)):
                        if possible_bishops[my_bishop] != 0:
                            if board[possible_bishops[my_bishop]] == ('B' if player_turn % 2 == 0 else 'b'):
                                if int(move[-1]) > int(possible_bishops[my_bishop][1]):
                                    for new_bishop in range(len(possible_bishops)):
                                        if possible_bishops[new_bishop] != 0:
                                            if my_bishop % 4 == new_bishop % 4 and int(move[-1]) >= int(
                                                    possible_bishops[new_bishop][1]) > int(possible_bishops[my_bishop][1]):
                                                if board[possible_bishops[new_bishop]] == '.':
                                                    continue
                                                else:
                                                    return False
                                elif int(move[-1]) < int(possible_bishops[my_bishop][1]):
                                    for new_bishop in range(len(possible_bishops)):
                                        if possible_bishops[new_bishop] != 0:
                                            if my_bishop % 4 == new_bishop % 4 and int(move[-1]) <= int(
                                                    possible_bishops[new_bishop][1]) < int(possible_bishops[my_bishop][1]):
                                                if board[possible_bishops[new_bishop]] == '.':
                                                    continue
                                                else:
                                                    return False
                                if test == 0:
                                    changes_dict[possible_bishops[my_bishop]] = '.'
                                    changes_dict[move[-2:]] = ('B' if player_turn % 2 == 0 else 'b')
                                    return True
                                else:
                                    return True
        if move[0] == ('R' if player_turn % 2 == 0 else 'r'):
            if 'x' in move and board[move[-2:]] in (
            'prnbqk' if player_turn % 2 == 0 else 'PRNBQK') or 'x' not in move and board[move[-2:]] == '.':
                rooks_num = 0
                possible_rooks = []
                valid = False
                my_rook = ''
                trigger = 0
                for shift in range(1, 8):
                    for rook in [
                        letters[letters.index(move[-2]) + shift if letters.index(move[-2]) + shift <= 7 else 8] + move[-1],
                        move[-2] + str(int(move[-1]) + shift),
                        letters[letters.index(move[-2]) - shift if letters.index(move[-2]) - shift >= 0 else 8] + move[-1],
                        move[-2] + str(int(move[-1]) - shift)]:
                        if rook in board.keys():
                            possible_rooks.append(rook)
                        else:
                            possible_rooks.append(0)
                for check_num_of_rooks in range(len(possible_rooks)):
                    if possible_rooks[check_num_of_rooks] != 0:
                        if board[possible_rooks[check_num_of_rooks]] == ('R' if player_turn % 2 == 0 else 'r'):
                            valid = True
                            # print(possible_rooks[check_num_of_rooks], 'my possible rook')
                            for valid_rook in range(len(possible_rooks)):
                                if possible_rooks[valid_rook] != 0 and valid_rook % 4 == check_num_of_rooks % 4 and \
                                        valid_rook != check_num_of_rooks:
                                    if possible_rooks[valid_rook][1] > possible_rooks[check_num_of_rooks][1] and move[-1] > \
                                            possible_rooks[check_num_of_rooks][1] or \
                                            possible_rooks[valid_rook][1] < possible_rooks[check_num_of_rooks][1] and move[
                                        -1] < \
                                            possible_rooks[check_num_of_rooks][1] or \
                                            possible_rooks[valid_rook][1] == possible_rooks[check_num_of_rooks][1] == move[
                                        -1] and (letters.index(move[-2]) < letters.index(
                                        possible_rooks[valid_rook][0]) < letters.index(
                                        possible_rooks[check_num_of_rooks][0]) or letters.index(move[-2]) > letters.index(
                                        possible_rooks[valid_rook][0]) > letters.index(
                                        possible_rooks[check_num_of_rooks][0])):
                                        if board[possible_rooks[valid_rook]] == '.':
                                            continue
                                        else:
                                            valid = False
                                            break

                            if valid:
                                rooks_num += 1
                    if valid:
                        my_rook = possible_rooks[check_num_of_rooks]
                        valid = False
                        trigger += 1
                if my_rook != '' and rooks_num == 1 or my_rook != '' and rooks_num == 1 and trigger == 1:
                    if test == 0:
                        changes_dict[my_rook] = '.'
                        changes_dict[move[-2:]] = ('R' if player_turn % 2 == 0 else 'r')
                        return True
                    else:
                        return True
                if rooks_num == 2 and len(move) == 4 or rooks_num == 2 and len(move) == 4 and trigger == 1:
                    if move[0] == ('R' if player_turn % 2 == 0 else 'r') and move[1] in 'abcdefgh' and move[
                                                                                                       -2:] in board.keys() and \
                            (len(move) == 4 and 'x' not in move or len(move) == 5 and move[2] == 'x'):
                        if move[2] == 'x' and board[move[-2:]] == '.' or 'x' not in move and board[
                            move[-2:]] != '.':
                            return False
                        else:
                            for keys, values in board.items():
                                if move[1] in keys and board[keys] == ('R' if player_turn % 2 == 0 else 'r') and move[
                                                                                                                      -2:] in board.keys():
                                    if test == 0:
                                        changes_dict[keys] = '.'
                                        changes_dict[move[-2:]] = ('R' if player_turn % 2 == 0 else 'r')
                                        return True
                                    else:
                                        return True
                    elif move[0] == ('R' if player_turn % 2 == 0 else 'r') and move[1] in '12345678' and move[
                                                                                                         -2:] in board.keys() and \
                            (len(move) == 4 and 'x' not in move or len(move) == 5 and move[2] == 'x'):
                        if move[2] == 'x' and board[move[-2:]] == '.' or 'x' not in move and board[
                            move[-2:]] != '.':
                            return False
                        else:
                            for keys, values in board.items():
                                if move[1] in keys and board[keys] == ('R' if player_turn % 2 == 0 else 'r') and move[
                                                                                                                      -2:] in board.keys():
                                    if test == 0:
                                        changes_dict[keys] = '.'
                                        changes_dict[move[-2:]] = ('R' if player_turn % 2 == 0 else 'r')
                                        return True
                                    else:
                                        return True
        if move[0] == ('Q' if player_turn % 2 == 0 else 'q'):
            possible_queens = []
            if (len(move) == 3 and 'x' not in move and board[move[-2:]] == '.' or len(move) == 4 and move[1] == 'x' and
                board[move[-2:]] in ('prnbqk' if player_turn % 2 == 0 else 'PRNBQK')) and \
                    move[-2] in 'abcdefgh' and move[-1] in '12345678' and move[-2:] in board.keys():
                for one_move in [letters[letters.index(move[-2]) + 1 if letters.index(move[-2]) + 1 <= 7 else 8] + move[-1],
                                 letters[letters.index(move[-2]) - 1 if letters.index(move[-2]) - 1 >= 0 else 8] + move[-1],
                                 move[-2] + str(int(move[-1]) + 1),
                                 move[-2] + str(int(move[-1]) - 1),
                                 letters[letters.index(move[-2]) + 1 if letters.index(move[-2]) + 1 <= 7 else 8] + str(
                                     int(move[-1]) + 1),
                                 letters[letters.index(move[-2]) + 1 if letters.index(move[-2]) + 1 <= 7 else 8] + str(
                                     int(move[-1]) - 1),
                                 letters[letters.index(move[-2]) - 1 if letters.index(move[-2]) - 1 >= 0 else 8] + str(
                                     int(move[-1]) + 1),
                                 letters[letters.index(move[-2]) - 1 if letters.index(move[-2]) - 1 >= 0 else 8] + str(
                                     int(move[-1]) - 1)]:
                    if one_move in board.keys():
                        if board[one_move] == ('Q' if player_turn % 2 == 0 else 'q'):
                            if test == 0:
                                changes_dict[one_move] = '.'
                                changes_dict[move[-2:]] = ('Q' if player_turn % 2 == 0 else 'q')
                                return True
                            else:
                                return True
                for shift in range(1, 8):
                    for queen in [
                        letters[letters.index(move[-2]) + shift if letters.index(move[-2]) + shift <= 7 else 8] + move[-1],
                        letters[letters.index(move[-2]) + shift if letters.index(move[-2]) + shift <= 7 else 8] + str(
                            int(move[-1]) + shift),
                        move[-2] + str(int(move[-1]) + shift),
                        letters[letters.index(move[-2]) - shift if letters.index(move[-2]) - shift >= 0 else 8] + str(
                            int(move[-1]) + shift),
                        letters[letters.index(move[-2]) - shift if letters.index(move[-2]) - shift >= 0 else 8] + move[-1],
                        letters[letters.index(move[-2]) - shift if letters.index(move[-2]) - shift >= 0 else 8] + str(
                            int(move[-1]) - shift),
                        move[-2] + str(int(move[-1]) - shift),
                        letters[letters.index(move[-2]) + shift if letters.index(move[-2]) + shift <= 7 else 8] + str(
                            int(move[-1]) - shift)]:
                        if queen in board.keys():
                            possible_queens.append(queen)
                        else:
                            possible_queens.append(0)
                for my_queen in range(len(possible_queens)):
                    if possible_queens[my_queen] != 0:
                        if board[possible_queens[my_queen]] == ('Q' if player_turn % 2 == 0 else 'q'):
                            valid = True
                            for valid_queen in range(len(possible_queens)):
                                if possible_queens[
                                    valid_queen] != 0 and valid_queen % 8 == my_queen % 8 and valid_queen != my_queen:
                                    if possible_queens[my_queen][1] > possible_queens[valid_queen][1] > move[-1] or \
                                            possible_queens[my_queen][1] < possible_queens[valid_queen][1] < move[-1] or \
                                            (possible_queens[my_queen][0] > possible_queens[valid_queen][0] > move[-2] or
                                             possible_queens[my_queen][0] < possible_queens[valid_queen][0] < move[-2]) and \
                                            possible_queens[my_queen][1] == possible_queens[valid_queen][1] == move[-1]:
                                        if board[possible_queens[valid_queen]] == '.':
                                            continue
                                        else:
                                            valid = False
                                            break
                            if valid:
                                if test == 0:
                                    changes_dict[possible_queens[my_queen]] = '.'
                                    changes_dict[move[-2:]] = ('Q' if player_turn % 2 == 0 else 'q')
                                    return True
                                else:
                                    return True
        if move[0] == ('K' if player_turn % 2 == 0 else 'k'):
            if (len(move) == 3 and move[1] in 'abcdefgh' and move[2] in '12345678' and 'x' not in move and board[move[-2:]] == '.' or len(move) == 4 and move[1] == 'x' and
                board[move[-2:]] in ('prnbqk' if player_turn % 2 == 0 else 'PRNBQK')) and \
                    move[-2] in 'abcdefgh' and move[-1] in '12345678' and move[-2:] in board.keys():
                if letters[letters.index(move[-2]) - 1] + str(int(move[-1]) + 1) and letters[
                    letters.index(move[-2]) + 1] + str(int(move[-1]) + 1) in board.items():
                    if board[letters[letters.index(move[-2]) - 1] + str(int(move[-1]) + 1)] == (
                    'p' if player_turn % 2 == 0 else 'P') \
                            or board[letters[letters.index(move[-2]) + 1] + str(int(move[-1]) + 1)] == (
                    'p' if player_turn % 2 == 0 else 'P'):
                        return False
                for one_move in [letters[letters.index(move[-2]) + 1 if letters.index(move[-2]) + 1 <= 7 else 8] + move[-1],
                                 letters[letters.index(move[-2]) - 1 if letters.index(move[-2]) - 1 >= 0 else 8] + move[-1],
                                 move[-2] + str(int(move[-1]) + 1),
                                 move[-2] + str(int(move[-1]) - 1),
                                 letters[letters.index(move[-2]) + 1 if letters.index(move[-2]) + 1 <= 7 else 8] + str(
                                     int(move[-1]) + 1),
                                 letters[letters.index(move[-2]) + 1 if letters.index(move[-2]) + 1 <= 7 else 8] + str(
                                     int(move[-1]) - 1),
                                 letters[letters.index(move[-2]) - 1 if letters.index(move[-2]) - 1 >= 0 else 8] + str(
                                     int(move[-1]) + 1),
                                 letters[letters.index(move[-2]) - 1 if letters.index(move[-2]) - 1 >= 0 else 8] + str(
                                     int(move[-1]) - 1)]:
                    if one_move in board.keys():
                        if board[one_move] == ('K' if player_turn % 2 == 0 else 'k'):
                            changes_dict[one_move] = '.'
                            changes_dict[move[-2:]] = ('K' if player_turn % 2 == 0 else 'k')
                            return True
        if move == '0-0':
            if board['e1' if player_turn % 2 == 0 else 'e8'] == ('K' if player_turn % 2 == 0 else 'k') and \
               board['h1' if player_turn % 2 == 0 else 'h8'] == ('R' if player_turn % 2 == 0 else 'r') and \
               board['f1' if player_turn % 2 == 0 else 'f8'] == '.' and board['g1' if player_turn % 2 == 0 else 'g8'] == '.':
                if test == 0:
                    changes_dict['f1' if player_turn % 2 == 0 else 'f8'] = ('R' if player_turn % 2 == 0 else 'r')
                    changes_dict['g1' if player_turn % 2 == 0 else 'g8'] = ('K' if player_turn % 2 == 0 else 'k')
                    changes_dict['e1' if player_turn % 2 == 0 else 'e8'] = '.'
                    changes_dict['h1' if player_turn % 2 == 0 else 'h8'] = '.'
                    print(changes_dict)
                    return True
                else:
                    return True
        if move == '0-0-0':
            if board['e1' if player_turn % 2 == 0 else 'e8'] == ('K' if player_turn % 2 == 0 else 'k') and \
               board['a1' if player_turn % 2 == 0 else 'a8'] == ('R' if player_turn % 2 == 0 else 'R') and \
               board['b1' if player_turn % 2 == 0 else 'b8'] == '.' and \
               board['c1' if player_turn % 2 == 0 else 'c8'] == '.' and \
               board['d1' if player_turn % 2 == 0 else 'd8'] == '.':
                if test == 0:
                    changes_dict['c1' if player_turn % 2 == 0 else 'c8'] = ('R' if player_turn % 2 == 0 else 'r')
                    changes_dict['b1' if player_turn % 2 == 0 else 'b8'] = ('K' if player_turn % 2 == 0 else 'k')
                    changes_dict['a1' if player_turn % 2 == 0 else 'a8'] = '.'
                    changes_dict['e1' if player_turn % 2 == 0 else 'e8'] = '.'
                    return True
                else:
                    return True
        return False

    def check(self, player_turn):
        for key1, val1 in board.items():
            if val1 == ('K' if player_turn % 2 == 0 else 'k'):
                for key2, val2 in board.items():
                    if val2 in ('rnbqk' if player_turn % 2 == 0 else 'RNBQK'):
                        if self.valid_move(val2 + 'x' + key1, 1 if val2 in 'rnbqk' else 0, 1):
                            return True
                        elif self.valid_move(key2[0] + 'x' + key1, 1 if val2 in 'rnbqk' else 0, 1):
                            return True
                        else:
                            continue

        return False

    def game(self, player_turn, changes_dict):
        turns = 2
        while True:
            move = (input('Ход первого игрока: ') if player_turn % 2 == 0 else input('Ход второго игрока: '))
            if 'danger for' in move:
                danger = []
                for key1, val1 in board.items():
                    if key1 == move[-2:]:
                        for key2, val2 in board.items():
                            if val2 in ('prnbqk' if player_turn % 2 == 0 else 'PRNBQK'):
                                if self.valid_move(val2 + 'x' + key1, 1 if val2 in 'prnbqk' else 0, 1):
                                    print(1, val2 + 'x' + key1, 1 if val2 in ('prnbqk' if player_turn % 2 == 0 else 'PRNBQK') else 0)
                                    danger.append(key2)
                                elif self.valid_move(key2[0] + 'x' + key1, 1 if val2 in 'prnbqk' else 0, 1):
                                    print(2, key2[0] + 'x' + key1, 1 if val2 in 'prnbqk' else 0, 1)
                                    danger.append(key2)
                                else:
                                    continue
                print('its -', *danger)
                print('__continue__')
                continue
            if len(move) == 0:
                print('game over')
                break
            if move == 'move':
                start = input('press "d" for move forward.\npress "a" for move back.\npress enter to start playing.\n')
                counter = len(moves_list)
                another_player_turn = counter % 2
                while True:
                    if start == 'd':
                        while start == 'd':
                            self.valid_move(moves_list[counter][0], another_player_turn)
                            board[moves_list[counter][1][0]] = moves_list[counter][1][1]
                            board[moves_list[counter][2][0]] = moves_list[counter][2][1]
                            counter += 1
                            another_player_turn += 1
                            print(self.print_board())
                            start = input()
                    if start == 'a':
                        counter -= 1
                        while start == 'a':
                            if 'x' in moves_list[counter][0]:
                                board[moves_list[counter][1][0]] = moves_list[counter][-1]
                                board[moves_list[counter][2][0]] = moves_list[counter][1][1]
                            else:
                                board[moves_list[counter][1][0]] = moves_list[counter][2][1]
                                board[moves_list[counter][2][0]] = moves_list[counter][1][1]
                            print(self.print_board())
                            start = input('press "d" for move forward.\npress "a" for move back.\npress enter to start playing.\n')
                            if start == 'a':
                                counter -= 1
                                player_turn -= 1
                    if start == '':
                        self.game(another_player_turn, changes_dict)
            if move == 'save game':
                file = input('file name - ')
                f = open(file, 'w')
                f.writelines("%s\n" % line for line in moves_list)
                f.close()
                print('game successfully saved')
                continue
            if move == 'play game':
                changes = []
                file = input('file name - ')
                f = open(file, 'r')
                print(self.print_board())
                lines = [line.rstrip() for line in f]
                another_player_turn = 0
                start = input('press "d" for move forward.\npress "a" for move back.\npress enter to start playing.\n')
                aq = []
                for move_el in lines:
                    changes.append([move_el])
                    self.valid_move(move_el, another_player_turn)
                    if move_el == '0-0' or move_el == '0-0-0':
                        board[list(changes_dict)[0]] = list(changes_dict.values())[0]
                        board[list(changes_dict)[1]] = list(changes_dict.values())[1]
                        board[list(changes_dict)[2]] = list(changes_dict.values())[2]
                        board[list(changes_dict)[3]] = list(changes_dict.values())[3]
                        aq.append({list(changes_dict)[0]: list(changes_dict.items())[2][1]})
                        aq.append({list(changes_dict)[1]: list(changes_dict.items())[3][1]})
                        aq.append({list(changes_dict)[2]: list(changes_dict.items())[1][1]})
                        aq.append({list(changes_dict)[3]: list(changes_dict.items())[0][1]})
                        changes[-1].append(list(changes_dict.items())[-1])
                        changes[-1].append(list(changes_dict.items())[-2])
                        changes[-1].append(list(changes_dict.items())[-3])
                        changes[-1].append(list(changes_dict.items())[-4])
                    else:
                        rem = board[move_el[-2:]]
                        board[list(changes_dict)[0]] = list(changes_dict.values())[0]
                        board[list(changes_dict)[1]] = list(changes_dict.values())[1]
                        aq.append({list(changes_dict)[0]: list(changes_dict.items())[1][1]})
                        aq.append({list(changes_dict)[1]: list(changes_dict.items())[0][1]})
                        changes[-1].append(list(changes_dict.items())[-1])
                        changes[-1].append(list(changes_dict.items())[-2])
                        if 'x' in move_el:
                            changes[-1].append(rem)
                    another_player_turn += 1
                for key in board.keys():
                    if key[1] in '3456':
                        board[key] = '.'
                    if key[1] == '7':
                        board[key] = 'p'
                    if key[1] == '2':
                        board[key] = 'P'
                    board['a1'] = 'R'
                    board['b1'] = 'N'
                    board['c1'] = 'B'
                    board['d1'] = 'Q'
                    board['e1'] = 'K'
                    board['f1'] = 'B'
                    board['g1'] = 'N'
                    board['h1'] = 'R'
                    board['a8'] = 'r'
                    board['b8'] = 'n'
                    board['c8'] = 'b'
                    board['d8'] = 'q'
                    board['e8'] = 'k'
                    board['f8'] = 'b'
                    board['g8'] = 'n'
                    board['h8'] = 'r'
                another_player_turn = 0
                counter = 0
                while True:
                    if start == 'd':
                        while start == 'd':
                            if changes[counter][0] == '0-0' or changes[counter][0] == '0-0-0':
                                board[changes[counter][1][0]] = '.'
                                board[changes[counter][2][0]] = '.'
                                board[changes[counter][3][0]] = changes[counter][3][1]
                                board[changes[counter][4][0]] = changes[counter][4][1]
                            else:
                                board[changes[counter][1][0]] = changes[counter][1][1]
                                board[changes[counter][2][0]] = changes[counter][2][1]
                            counter += 1
                            another_player_turn += 1
                            print(self.print_board())
                            start = input('press "d" for move forward.\npress "a" for move back.\npress enter to start playing.\n')
                    if start == 'a':
                        counter -= 1
                        while start == 'a':
                            if changes[counter][0] == '0-0' or changes[counter][0] == '0-0-0':
                                board[changes[counter][1][0]] = changes[counter][3][1]
                                board[changes[counter][2][0]] = changes[counter][4][1]
                                board[changes[counter][3][0]] = '.'
                                board[changes[counter][4][0]] = '.'
                            else:
                                if 'x' in changes[counter][0]:
                                    board[changes[counter][1][0]] = changes[counter][-1]
                                    board[changes[counter][2][0]] = changes[counter][1][1]
                                else:
                                    board[changes[counter][1][0]] = changes[counter][2][1]
                                    board[changes[counter][2][0]] = changes[counter][1][1]
                            counter -= 1
                            player_turn -= 1
                            print(self.print_board())
                            start = input()
                    if start == '':
                        self.game(another_player_turn, changes_dict)
            if self.valid_move(move, player_turn):
                rem = board[move[-2:]]
                if move == '0-0' or move == '0-0-0':
                    board[list(changes_dict.keys())[0]] = changes_dict[list(changes_dict.keys())[0]]
                    board[list(changes_dict.keys())[1]] = changes_dict[list(changes_dict.keys())[1]]
                    board[list(changes_dict.keys())[2]] = changes_dict[list(changes_dict.keys())[2]]
                    board[list(changes_dict.keys())[3]] = changes_dict[list(changes_dict.keys())[3]]
                else:
                    if self.check(player_turn):
                        while self.check(player_turn):
                            board[list(changes_dict.keys())[0]] = changes_dict[list(changes_dict.keys())[0]]
                            board[list(changes_dict.keys())[1]] = changes_dict[list(changes_dict.keys())[1]]
                            if self.check(player_turn):
                                board[list(changes_dict.keys())[0]] = changes_dict[list(changes_dict.keys())[1]]
                                board[list(changes_dict.keys())[1]] = changes_dict[list(changes_dict.keys())[0]]
                                print('Невозможно сделать ход, это шах и мат королеве!!')
                                print(self.print_board())
                                move = (input('Ход первого игрокa: ') if player_turn % 2 == 0 else input('Ход второго игрока: '))
                                changes_dict.clear()
                                self.valid_move(move, player_turn)
                            else:
                                break
                        board[list(changes_dict.keys())[0]] = changes_dict[list(changes_dict.keys())[0]]
                        board[list(changes_dict.keys())[1]] = changes_dict[list(changes_dict.keys())[1]]
                    else:
                        board[list(changes_dict)[0]] = changes_dict[list(changes_dict.keys())[0]]
                        board[list(changes_dict)[1]] = changes_dict[list(changes_dict)[1]]
                        if self.check(player_turn):
                            while self.check(player_turn):
                                board[list(changes_dict.keys())[0]] = changes_dict[list(changes_dict.keys())[0]]
                                board[list(changes_dict.keys())[1]] = changes_dict[list(changes_dict.keys())[1]]
                                if self.check(player_turn):
                                    board[list(changes_dict.keys())[0]] = changes_dict[list(changes_dict.keys())[1]]
                                    board[list(changes_dict.keys())[1]] = changes_dict[list(changes_dict.keys())[0]]
                                    print('Невозможно сделать ход, это шах и мат королеве!')
                                    print(self.print_board())
                                    move = (input('Ход первого игрока: ') if player_turn % 2 == 0 else input(
                                        'Ход второго игрока: '))
                                    changes_dict.clear()
                                    self.valid_move(move, player_turn)
                                else:
                                    break
                    moves_list.append([move])
                    qwe.append({list(changes_dict)[0]: list(changes_dict.items())[1][1]})
                    qwe.append({list(changes_dict)[1]: list(changes_dict.items())[0][1]})
                    moves_list[-1].append(list(changes_dict.items())[-1])
                    moves_list[-1].append(list(changes_dict.items())[-2])
                    if 'x' in move:
                        moves_list[-1].append(rem)
                        print(rem, moves_list)
            else:
                print('Невозможно сделать ход, попробуйте снова!')
                player_turn -= 1
            turns += 1
            player_turn += 1
            changes_dict.clear()
            print(self.print_board())
            print(f'Действие {turns // 2}')

Chess_game_01 = Chess(board)
print(Chess_game_01.print_board())
print(Chess_game_01.game(player_turn, changes_dict))
board = {'a8': 'r', 'b8': 'n', 'c8': 'b', 'd8': 'q', 'e8': 'k', 'f8': 'b', 'g8': 'n', 'h8': 'r',
                  'a7': 'p', 'b7': 'p', 'c7': 'p', 'd7': 'p', 'e7': 'p', 'f7': 'p', 'g7': 'p', 'h7': 'p',
                  'a6': '.', 'b6': '.', 'c6': '.', 'd6': '.', 'e6': '.', 'f6': '.', 'g6': '.', 'h6': '.',
                  'a5': '.', 'b5': '.', 'c5': '.', 'd5': '.', 'e5': '.', 'f5': '.', 'g5': '.', 'h5': '.',
                  'a4': '.', 'b4': '.', 'c4': '.', 'd4': '.', 'e4': '.', 'f4': '.', 'g4': '.', 'h4': '.',
                  'a3': 'K', 'b3': '.', 'c3': '.', 'd3': '.', 'e3': '.', 'f3': '.', 'g3': '.', 'h3': '.',
                  'a2': '.', 'b2': 'P', 'c2': 'P', 'd2': 'P', 'e2': 'P', 'f2': 'P', 'g2': 'P', 'h2': 'P',
                  'a1': 'R', 'b1': 'N', 'c1': 'B', 'd1': 'Q', 'e1': '.', 'f1': 'B', 'g1': 'N', 'h1': 'R'}


Chess_game_02 = Chess(board)
print(Chess_game_02.print_board())
print(Chess_game_02.game(player_turn, changes_dict))







