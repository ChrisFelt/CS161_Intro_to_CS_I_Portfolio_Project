class OrthokonBoard:

    # initialize data members
    def __init__(self):

        # define initial board
        # list of rows in each column, column/row number corresponds to list number
        # R = red, E = empty, Y = yellow
        self._board = [["R", "E", "E", "Y"],  # column 0
                       ["R", "E", "E", "Y"],  # column 1
                       ["R", "E", "E", "Y"],  # column 2
                       ["R", "E", "E", "Y"]]  # column 3
        self._current_state = "UNFINISHED"

    # get method returning current game state
    def get_current_state(self):

        return self._current_state

    # print the board
    def print_board(self):

        for i in range(len(self._board)):

            print(self._board[i])

    # method that moves a piece orthogonally upwards
    def __move_up(self, from_col, from_row, to_row):

        # first check if any pieces are in the way
        for i in range(abs(from_row - to_row)):  # loop number of spaces moved

            if self._board[from_col][from_row - (i + 1)] != "E":

                return False

        # loop for number of spaces moved
        for i in range(abs(from_row - to_row)):

            # check if new space is empty
            if self._board[from_col][from_row - (i + 1)] == "E":

                # replace new space with piece from last space
                self._board[from_col][from_row - (i + 1)] = self._board[from_col][from_row - i]

                # mark last space as empty
                self._board[from_col][from_row - i] = "E"

        return True

    # method that moves a piece orthogonally downwards
    def __move_down(self, from_col, from_row, to_row):

        # first check if any pieces are in the way
        for i in range(abs(from_row - to_row)):  # loop number of spaces moved

            if self._board[from_col][from_row + (i + 1)] != "E":

                return False

        # loop for number of spaces moved
        for i in range(abs(from_row - to_row)):

            # check if new space is empty
            if self._board[from_col][from_row + (i + 1)] == "E":

                # replace new space with piece from last space
                self._board[from_col][from_row + (i + 1)] = self._board[from_col][from_row + i]

                # mark last space as empty
                self._board[from_col][from_row + i] = "E"

        return True

    # method that moves a piece orthogonally rightwards
    def __move_right(self, from_col, from_row, to_col):

        # first check if any pieces are in the way
        for i in range(abs(from_col - to_col)):  # loop number of spaces moved

            if self._board[from_col + (i + 1)][from_row] != "E":

                return False

        # loop for number of spaces moved
        for i in range(abs(from_col - to_col)):

            # check if new space is empty
            if self._board[from_col + (i + 1)][from_row] == "E":

                # replace new space with piece from last space
                self._board[from_col + (i + 1)][from_row] = self._board[from_col + i][from_row]

                # mark last space as empty
                self._board[from_col + i][from_row] = "E"

        return True

    # method that moves a piece orthogonally leftwards
    def __move_left(self, from_col, from_row, to_col):

        # first check if any pieces are in the way
        for i in range(abs(from_col - to_col)):  # loop number of spaces moved

            if self._board[from_col - (i + 1)][from_row] != "E":

                return False

        # loop for number of spaces moved
        for i in range(abs(from_col - to_col)):

            # check if new space is empty
            if self._board[from_col - (i + 1)][from_row] == "E":
                # replace new space with piece from last space
                self._board[from_col - (i + 1)][from_row] = self._board[from_col - i][from_row]

                # mark last space as empty
                self._board[from_col - i][from_row] = "E"

        return True

    # method for moving diagonally up and rightwards
    def __move_up_and_right(self, from_col, from_row, to_row):

        # first check if any pieces are in the way
        # assumes destination is exactly 45 degrees from origin
        for i in range(abs(from_row - to_row)):  # loop number of spaces moved

            if self._board[from_col + (i + 1)][from_row - (i + 1)] != "E":

                return False

        # loop for number of spaces moved
        for i in range(abs(from_row - to_row)):

            # check if new space is empty
            if self._board[from_col + (i + 1)][from_row - (i + 1)] == "E":

                # replace new space with piece from last space
                self._board[from_col + (i + 1)][from_row - (i + 1)] = self._board[from_col + i][from_row - i]

                # mark last space as empty
                self._board[from_col + i][from_row - i] = "E"

        return True

    # method for moving diagonally up and leftwards
    def __move_up_and_left(self, from_col, from_row, to_row):

        # first check if any pieces are in the way
        # assumes destination is exactly 45 degrees from origin
        for i in range(abs(from_row - to_row)):  # loop number of spaces moved

            if self._board[from_col - (i + 1)][from_row - (i + 1)] != "E":
                return False

        # loop for number of spaces moved
        for i in range(abs(from_row - to_row)):

            # check if new space is empty
            if self._board[from_col - (i + 1)][from_row - (i + 1)] == "E":

                # replace new space with piece from last space
                self._board[from_col - (i + 1)][from_row - (i + 1)] = self._board[from_col - i][from_row - i]

                # mark last space as empty
                self._board[from_col - i][from_row - i] = "E"

        return True

    # method for moving diagonally down and rightwards
    def __move_down_and_right(self, from_col, from_row, to_row):

        # first check if any pieces are in the way
        # assumes destination is exactly 45 degrees from origin
        for i in range(abs(from_row - to_row)):  # loop number of spaces moved

            if self._board[from_col + (i + 1)][from_row + (i + 1)] != "E":
                return False

        # loop for number of spaces moved
        for i in range(abs(from_row - to_row)):

            # check if new space is empty
            if self._board[from_col + (i + 1)][from_row + (i + 1)] == "E":

                # replace new space with piece from last space
                self._board[from_col + (i + 1)][from_row + (i + 1)] = self._board[from_col + i][from_row + i]

                # mark last space as empty
                self._board[from_col + i][from_row + i] = "E"

        return True

    # method for moving diagonally down and leftwards
    def __move_down_and_left(self, from_col, from_row, to_row):

        # first check if any pieces are in the way
        # assumes destination is exactly 45 degrees from origin
        for i in range(abs(from_row - to_row)):  # loop number of spaces moved

            if self._board[from_col - (i + 1)][from_row + (i + 1)] != "E":
                return False

        # loop for number of spaces moved
        for i in range(abs(from_row - to_row)):

            # check if new space is empty
            if self._board[from_col - (i + 1)][from_row + (i + 1)] == "E":
                # replace new space with piece from last space
                self._board[from_col - (i + 1)][from_row + (i + 1)] = self._board[from_col - i][from_row + i]

                # mark last space as empty
                self._board[from_col - i][from_row + i] = "E"

        return True

    # method that flips pieces that are orthogonally adjacent after a move
    def __subvert_piece(self, col, row):

        # check spaces in adjacent rows
        for i in range(-1, 2):

            # exclude positions outside the board
            if row + i in range(4):

                # check if opposing piece present
                if self._board[col][row + i] != "E" and self._board[col][row + i] != self._board[col][row]:

                    # flip the piece!
                    self._board[col][row + i] = self._board[col][row]

        # check spaces in adjacent columns
        for i in range(-1, 2):

            # exclude positions outside the board
            if col + i in range(4):

                # check if opposing piece present
                if self._board[col + i][row] != "E" and self._board[col + i][row] != self._board[col][row]:

                    # flip the piece!
                    self._board[col + i][row] = self._board[col][row]

    # method for checking the state of the board and declaring a winner
    def __check_win(self):

        # check if no red pieces remain
        if "R" not in self._board[0] and "R" not in self._board[1] and \
                "R" not in self._board[2] and "R" not in self._board[3]:

            # yellow wins
            self._current_state = "YELLOW WON"
            return True

        # check if no yellow pieces remain
        elif "Y" not in self._board[0] and "Y" not in self._board[1] and \
                "Y" not in self._board[2] and "Y" not in self._board[3]:

            # red wins
            self._current_state = "RED WON"
            return True

        else:  # not necessary?

            return False  # no winner yet

    # method for handling piece movement on the board
    def make_move(self, from_col, from_row, to_col, to_row):

        # check if piece was moved to same location as origin
        if from_col == to_col and from_row == to_row:

            return False  # Failed to move!

        # check if destination is within the board
        elif from_col > 3 or from_row > 3 or to_col > 3 or to_row > 3:

            return False  # Out of bounds!

        # check if space is empty
        elif self._board[from_col][from_row] == "E":

            return False  # nothing to move!

        # check if the move is orthogonal
        elif from_col == to_col or from_row == to_row:

            # check if move is vertical
            if from_col == to_col:

                # check if moving up
                if from_row > to_row:

                    # check if move is legal using __move_up method
                    # moves piece if True
                    if self.__move_up(from_col, from_row, to_row):

                        # flip opponent's adjacent pieces
                        self.__subvert_piece(to_col, to_row)

                        # check if this move resulted in a win condition
                        self.__check_win()
                        return True

                    else:

                        return False

                # check if moving down
                if from_row < to_row:

                    # check if move is legal using __move_down method
                    # moves piece if True
                    if self.__move_down(from_col, from_row, to_row):

                        # flip opponent's adjacent pieces
                        self.__subvert_piece(to_col, to_row)

                        # check if this move resulted in a win condition
                        self.__check_win()
                        return True

                    else:

                        return False

            # check if move is horizontal
            if from_row == to_row:

                # check if moving right
                if from_col < to_col:

                    # check if move is legal using __move_right method
                    # moves piece if True
                    if self.__move_right(from_col, from_row, to_col):

                        # flip opponent's adjacent pieces
                        self.__subvert_piece(to_col, to_row)

                        # check if this move resulted in a win condition
                        self.__check_win()
                        return True

                    else:

                        return False

                # check if moving left
                if from_col > to_col:

                    # check if move is legal using __move_left method
                    # moves piece if True
                    if self.__move_left(from_col, from_row, to_col):

                        # flip opponent's adjacent pieces
                        self.__subvert_piece(to_col, to_row)

                        # check if this move resulted in a win condition
                        self.__check_win()
                        return True

                    else:

                        return False

        # check if move is diagonal
        elif abs(from_col - to_col) // abs(from_row - to_row) == 1:

            # check if moving rightwards
            if from_col < to_col:

                # check if moving up
                if from_row > to_row:

                    # check if move is legal using __move_up_and_right method
                    # moves piece if True
                    if self.__move_up_and_right(from_col, from_row, to_row):

                        # flip opponent's adjacent pieces
                        self.__subvert_piece(to_col, to_row)

                        # check if this move resulted in a win condition
                        self.__check_win()
                        return True

                    else:

                        return False

                # check if moving down
                if from_row < to_row:

                    # check if move is legal using __move_up_and_right method
                    # moves piece if True
                    if self.__move_down_and_right(from_col, from_row, to_row):

                        # flip opponent's adjacent pieces
                        self.__subvert_piece(to_col, to_row)

                        # check if this move resulted in a win condition
                        self.__check_win()
                        return True

                    else:

                        return False

            # check if moving leftwards
            if from_col > to_col:

                # check if moving up
                if from_row > to_row:

                    # check if move is legal using __move_up_and_left method
                    # moves piece if True
                    if self.__move_up_and_left(from_col, from_row, to_row):

                        # flip opponent's adjacent pieces
                        self.__subvert_piece(to_col, to_row)

                        # check if this move resulted in a win condition
                        self.__check_win()
                        return True

                    else:

                        return False

                # check if moving down
                if from_row < to_row:

                    # check if move is legal using __move_down_and_left method
                    # moves piece if True
                    if self.__move_down_and_left(from_col, from_row, to_row):

                        # flip opponent's adjacent pieces
                        self.__subvert_piece(to_col, to_row)

                        # check if this move resulted in a win condition
                        self.__check_win()
                        return True

                    else:

                        return False




board = OrthokonBoard()

print(board.make_move(0, 3, 2, 1))
board.print_board()
print(board.get_current_state())

print(board.make_move(3, 3, 1, 1))
board.print_board()
print(board.get_current_state())

print(board.make_move(1, 3, 0, 3))
board.print_board()
print(board.get_current_state())

print(board.make_move(2, 3, 3, 3))
board.print_board()
print(board.get_current_state())

print(board.make_move(0, 3, 0, 1))
board.print_board()
print(board.get_current_state())

print(board.make_move(3, 3, 3, 1))
board.print_board()
print(board.get_current_state())


board2 = OrthokonBoard()
print(board2.make_move(0, 0, 2, 2))
board2.print_board()
print(board2.get_current_state())

print(board2.make_move(3, 0, 1, 2))
board2.print_board()
print(board2.get_current_state())

print(board2.make_move(1, 0, 0, 0))
board2.print_board()
print(board2.get_current_state())

print(board2.make_move(2, 0, 3, 0))
board2.print_board()
print(board2.get_current_state())

print(board2.make_move(0, 0, 0, 2))
board2.print_board()
print(board2.get_current_state())

print(board2.make_move(3, 0, 3, 2))
board2.print_board()
print(board2.get_current_state())