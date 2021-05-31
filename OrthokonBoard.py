class OrthokonBoard:

    # initialize data members
    def __init__(self):

        # define initial board
        # list of rows in each column, column/row number corresponds to list number
        # R = red, E = empty, Y = yellow
        self._board = [["R", "E", "E", "Y"], #  column 0
                       ["R", "E", "E", "Y"], #  column 1
                       ["R", "E", "E", "Y"], #  column 2
                       ["R", "E", "E", "Y"]] #  column 3
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

        # loop for number of spaces moved
        for i in range(abs(from_row - to_row) - 1):

            # check if new space is empty
            if self._board[from_col][from_row - (i + 1)] == "E":
                # replace new space with piece from last space
                self._board[from_col][from_row - (i + 1)] = self._board[from_col][from_row - i]

                # mark last space as empty
                self._board[from_col][from_row - i] = "E"

    # method that moves a piece orthogonally downwards
    def __move_down(self, from_col, from_row, to_row):

        # first check if any pieces are in the way
        for i in range(abs(from_row - to_row) - 1):

            if self._board[from_col][from_row + (i + 1)] != "E":

                return False

        # loop for number of spaces moved
        for i in range(abs(from_row - to_row) - 1):

            # check if new space is empty
            if self._board[from_col][from_row + (i + 1)] == "E":

                # replace new space with piece from last space
                self._board[from_col][from_row + (i + 1)] = self._board[from_col][from_row + i]

                # mark last space as empty
                self._board[from_col][from_row + i] = "E"

        return True

    # method that moves a piece orthogonally rightwards
    def __move_right(self, from_col, to_col, from_row):

        # loop for number of spaces moved
        for i in range(abs(from_col - to_col) - 1):

            # check if new space is empty
            if self._board[from_col + (i + 1)][from_row] == "E":

                # replace new space with piece from last space
                self._board[from_col + (i + 1)][from_row] = self._board[from_col + i][from_row]

                # mark last space as empty
                self._board[from_col + i][from_row] = "E"

    # method that moves a piece orthogonally leftwards
    def __move_left(self, from_col, to_col, from_row):

        # loop for number of spaces moved
        for i in range(abs(from_col - to_col) - 1):

            # check if new space is empty
            if self._board[from_col - (i + 1)][from_row] == "E":
                # replace new space with piece from last space
                self._board[from_col - (i + 1)][from_row] = self._board[from_col - i][from_row]

                # mark last space as empty
                self._board[from_col - i][from_row] = "E"

    # method that flips pieces that are orthogonally adjacent after a move
    def _subvert_piece(self, col, row):




    def make_move(self, from_col, from_row, to_col, to_row):

        # check if piece was moved to same location as origin
        if from_col == to_col and from_row == to_row:

            return False # Failed to move!

        # check if the move is orthogonal
        if from_col == to_col or from_row == to_row:

            # check if move is vertical
            if from_col == to_col:

                # check if moving up
                if from_row > to_row:

                    # move piece up using _move_up method
                    self.__move_up(from_col, from_row, to_row)

                # check if moving down
                if from_row < to_row:

                    # move piece down using _move_down method
                    self.__move_down(from_col, from_row, to_row)

            # check if move is horizontal
            if from_row == to_row:

                # check if moving right
                if from_col > to_col:

                    # move piece right using __move_right method
                    self.__move_right(from_col, from_row, to_col)

            self._subvert_piece(to_col, to_row)
            return True

        # check if move is diagonal
        elif abs(from_col - to_col) // abs(from_row - to_row) == 1:

board = OrthokonBoard()
board.make_move(0, 3, 0, 0)  # The yellow player moves a piece diagonally, flipping one red piece to yellow
# board.make_move(0, 2, 2, 0)  # The red player moves a piece diagonally, flipping two yellow pieces to red

board.print_board()

print(board.get_current_state())