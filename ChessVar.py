# author: Anthony Stark
# gitHub username: astark117
# date created: 2/25/2024
# description: Allows the user to play a variant of chess with fairy pieces (Falcon and Hunter). All pieces follow
#              classic chess rules, and the chess board is set up like a standard board. Fairy pieces can be entered
#              only after a player loses a piece other than a pawn, and playing one constitutes a turn. There is no
#              classic checkmate, the game ends when the user captures the opponents king piece.
#              White pieces are displayed in black font on a light grey background.
#              Black pieces are displayed in yellow font on a black background.

class Piece:
    """
    Base class for all chess pieces. Represents a chess piece with its color and symbol.
    """
    def __init__(self, color):
        self._color = color
        self._symbol = None

    def get_color(self):
        '''
        returns color of a piece
        '''
        return self._color

    def get_symbol(self):
        '''
        returns the symbol of a piece.
        If a piece is white the symbol is capitalized.
        If a piece is black the symbol is lowercase.
        '''
        if self._color == 'white':
            return self._symbol.upper()
        else:
            return self._symbol


class Pawn(Piece):
    """
    Represents a pawn chess piece and the allowed moves it can make.
    """
    def __init__(self, color):
        """
        initializes a pawn chess piece with symbol 'p'
        :param color:
        """
        super().__init__(color)
        self._symbol = 'p'

    def valid_move(self, from_square, to_square):
        '''
        Can move forward 1 space vertically. If it is in the starting position it can move forward 2 spaces vertically.
        It cannot capture by moving vertically, to capture a piece it must move forward diagonally. This is the
        only time it can move forward diagonally.
        :param from_square:
        :param to_square:
        :return: False if move is not valid
        :return: 'pawn_capture' if the move is a diagonal capture move
        :return: True if move is valid and not a capture
    '''
        from_row = from_square.get_row()
        from_col = from_square.get_col()
        to_row = to_square.get_row()
        to_col = to_square.get_col()

        if self.get_color() == 'black':
            direction = -1
            start_row = 6
        else:
            direction = 1
            start_row = 1

        if from_col == to_col:
            # regular pawn move, one row forward
            if to_row == from_row + direction:
                return True
            # starting pawn move, can move 2 rows forward
            elif from_row == start_row and to_row == from_row + 2 * direction:
                return True
            else:
                return False
        # capture move diagonal (left or right) and 1 row forward
        elif abs(to_col - from_col) == 1 and to_row == from_row + direction:
            if to_square.get_piece() == self.get_color():
                return False
            elif to_square.get_piece() is None:
                return False
            else:
                return 'pawn_capture'
        else:
            return False


class Rook(Piece):
    """
    Represents a rook chess piece and the allowed moves it can make.
    """
    def __init__(self, color):
        """
        initializes a rook chess piece with symbol 'r'
        :param color:
        """
        super().__init__(color)
        self._symbol = 'r'

    def valid_move(self, from_square, to_square):
        """
        Can move either horizontally or vertically, forwards or backwards, an unlimited number of spaces.
        :param from_square:
        :param to_square:
        :return: False if move is invalid
        :return: True if move is valid
        """
        from_row = from_square.get_row()
        from_col = from_square.get_col()
        to_row = to_square.get_row()
        to_col = to_square.get_col()

        # The rook can move vertically or horizontally as many spaces as it wants
        if from_row == to_row and from_col != to_col:
            return True
        elif from_row != to_row and from_col == to_col:
            return True
        else:
            return False


class Knight(Piece):
    """
    Represents a knight chess piece and valid moves it can make.
    """
    def __init__(self, color):
        """
        initializes a knight chess piece with symbol 'n'
        :param color:
        """
        super().__init__(color)
        self._symbol = 'n'

    def valid_move(self, from_square, to_square):
        """
        Can move 2 spaces vertically and 1 space horizontally or 2 spaces horizontally and 1 space vertically.
        Can move forwards and backwards and can also hop over other pieces.
        :param from_square:
        :param to_square:
        :return: False if move is invalid
        :return: True if move is valid
        """
        from_row = from_square.get_row()
        from_col = from_square.get_col()
        to_row = to_square.get_row()
        to_col = to_square.get_col()

        # Knight moves 2 columns over and 1 row over or 2 rows over and 1 column over in any direction
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            return True
        else:
            return False


class Bishop(Piece):
    """
    Represents a bishop chess piece.
    """
    def __init__(self, color):
        """
        initializes a bishop chess piece with symbol 'b'
        :param color:
        """
        super().__init__(color)
        self._symbol = 'b'

    def valid_move(self, from_square, to_square):
        """
        Can move diagonally, both forwards and backwards, an unlimited number of spaces.
        :param from_square:
        :param to_square:
        :return: False if move is invalid
        :return: True if move is valid
        """
        from_row = from_square.get_row()
        from_col = from_square.get_col()
        to_row = to_square.get_row()
        to_col = to_square.get_col()

        # bishop can move any number of rows and columns over, as long as num of rows = num of columns
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)
        if row_diff == col_diff:
            return True
        else:
            return False


class Queen(Piece):
    """
    Represents a queen chess piece.
    """
    def __init__(self, color):
        """
        initializes a queen chess piece with symbol 'q'
        :param color:
        """
        super().__init__(color)
        self._symbol = 'q'

    def valid_move(self, from_square, to_square):
        """
        Can move in any direction an unlimited number of spaces.
        :param from_square:
        :param to_square:
        :return: False if invalid move
        :return: True if move is valid
        """
        from_row = from_square.get_row()
        from_col = from_square.get_col()
        to_row = to_square.get_row()
        to_col = to_square.get_col()

        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        # queen can move like a bishop and rook combined
        if row_diff == col_diff:
            return True
        elif from_row == to_row and from_col != to_col:
            return True
        elif from_row != to_row and from_col == to_col:
            return True
        else:
            return False


class King(Piece):
    """
    Represents a king chess piece.
    """
    def __init__(self, color):
        """
        initializes a king chess piece with symbol 'k'
        :param color:
        """
        super().__init__(color)
        self._symbol = 'k'

    def valid_move(self, from_square, to_square):
        """
        Can move in any direction but only by one space.
        :param from_square:
        :param to_square:
        :return: False if invalid move
        :return: True if move is valid
        """
        from_row = from_square.get_row()
        from_col = from_square.get_col()
        to_row = to_square.get_row()
        to_col = to_square.get_col()

        # king can move in any direction but only by one space
        row_diff = abs(to_row - from_row)
        col_diff = abs(to_col - from_col)

        if row_diff <= 1 and col_diff <= 1:
            return True
        else:
            return False


class Falcon(Piece):
    """
    Represents a Falcon fairy chess piece - special variant of chess
    """
    def __init__(self, color):
        """
        initializes a Falcon chess piece with symbol 'f'
        :param color:
        """
        super().__init__(color)
        self._symbol = 'f'

    def valid_move(self, from_square, to_square):
        """
        Moves forward like a bishop and backward like a rook
        :param from_square:
        :param to_square:
        :return: False if invalid move
        :return: True if move is valid
        """
        from_row = from_square.get_row()
        from_col = from_square.get_col()
        to_row = to_square.get_row()
        to_col = to_square.get_col()

        row_diff = to_row - from_row
        col_diff = to_col - from_col

        if self.get_color() == 'white':
            if row_diff >= 0:
                if abs(row_diff) == abs(col_diff):
                    return True
                else:
                    return False
            else:
                if from_row == to_row and from_col != to_col:
                    return True
                else:
                    return False
        else:
            if row_diff <= 0:
                if abs(row_diff) == abs(col_diff):
                    return True
                else:
                    return False
            else:
                if from_col == to_col and from_row != to_row:
                    return True
                else:
                    return False


class Hunter(Piece):
    """
    Represents a Hunter fairy chess piece - special variant of chess.
    """
    def __init__(self, color):
        """
        initializes a hunter chess piece with symbol 'h'
        :param color:
        """
        super().__init__(color)
        self._symbol = 'h'

    def valid_move(self, from_square, to_square):
        """
        Moves forward like a rook and backward like a bishop.
        :param from_square:
        :param to_square:
        :return False if invalid move:
        :return True if move is valid:
        """
        from_row = from_square.get_row()
        from_col = from_square.get_col()
        to_row = to_square.get_row()
        to_col = to_square.get_col()
        row_diff = to_row - from_row
        col_diff = to_col - from_col

        if self.get_color() == 'black':
            if row_diff >= 0:
                if abs(row_diff) == abs(col_diff):
                    return True
                else:
                    return False
            else:
                if from_row == to_row and from_col != to_col:
                    return True
                else:
                    return False
        else:
            if row_diff <= 0:
                if abs(row_diff) == abs(col_diff):
                    return True
                else:
                    return False
            else:
                if from_col == to_col and from_row != to_row:
                    return True
                else:
                    return False


class Player:
    """
    Represents a player of the chess game.
    """
    def __init__(self, color):
        '''
        initializes a player object with a color, list of pieces captured from their opponent, and fairy pieces
        in reserve.
        :param color:
        '''
        self._color = color
        self._captured = []
        self._fairy_pieces = ['h', 'f']
        self._fairy_played_count = 0

    def get_captured_pieces(self):
        '''
        returns the pieces a player has captured
        '''
        return self._captured

    def get_fairy_pieces(self):
        '''
        returns the fairy pieces a player has in reserve
        '''
        return self._fairy_pieces

    def get_color(self):
        '''
        returns the player color
        '''
        return self._color

    def add_captured(self, piece):
        '''
        adds an opponent's piece that the player captured to the captured list
        :param piece:
        '''
        self._captured.append(piece)

    def remove_fairy_piece(self, piece):
        '''
        removes a fairy piece from the fairy_piece list if it is brought into play.
        :param piece:
        '''
        self._fairy_pieces.remove(piece)

    def get_fairy_played_count(self):
        '''
        returns count of number of fairy pieces played
        '''
        return self._fairy_played_count

    def inc_fairy_played_count(self):
        '''
        increments fairy pieces played counter
        '''
        self._fairy_played_count += 1


class Square:
    """
    Represents a square on the chess board and any chess pieces on it as well as the row and column of its location.
    """
    def __init__(self, col, row):
        """
        initializes a square object with a column and row value indicating position on a grid.
        :param col:
        :param row:
        """
        self._piece = None
        self._row = row
        self._col = col

    def get_piece(self):
        '''
        returns piece on square
        '''
        return self._piece

    def get_row(self):
        '''
        returns the row of the square
        '''
        return self._row

    def get_col(self):
        '''
        returns the column of the square
        '''
        return self._col

    def add_piece(self, piece):
        '''
        adds a piece object onto a square
        :param piece:
        '''
        self._piece = piece

    def remove_piece(self):
        '''
        removes a piece from a square, replacing it with None
        '''
        self._piece = None


class Board:
    """
    Represents the chess board with squares and pieces on it.
    """
    def __init__(self):
        '''
        Generates a grid representing the chess board and populates it with square objects that have a row and column
        coordinate as well as the chess pieces in their initial positions.
        '''
        self._board = []
        for column in range(8):
            row = []
            for grid in range(8):
                row.append(Square(grid, column))
            self._board.append(row)

        # Place pieces in initial position on the board
        self.place_piece(Rook('white'), 0, 0)  # Rook
        self.place_piece(Knight('white'), 0, 1)  # Knight
        self.place_piece(Bishop('white'), 0, 2)  # Bishop
        self.place_piece(Queen('white'), 0, 3)  # Queen
        self.place_piece(King('white'), 0, 4)  # King
        self.place_piece(Bishop('white'), 0, 5)  # Bishop
        self.place_piece(Knight('white'), 0, 6)  # Knight
        self.place_piece(Rook('white'), 0, 7)  # Rook
        self.place_piece(Pawn('white'), 1, 0)  # Pawn
        self.place_piece(Pawn('white'), 1, 1)  # Pawn
        self.place_piece(Pawn('white'), 1, 2)  # Pawn
        self.place_piece(Pawn('white'), 1, 3)  # Pawn
        self.place_piece(Pawn('white'), 1, 4)  # Pawn
        self.place_piece(Pawn('white'), 1, 5)  # Pawn
        self.place_piece(Pawn('white'), 1, 6)  # Pawn
        self.place_piece(Pawn('white'), 1, 7)  # Pawn

        self.place_piece(Rook('black'), 7, 0)  # Rook
        self.place_piece(Knight('black'), 7, 1)  # Knight
        self.place_piece(Bishop('black'), 7, 2)  # Bishop
        self.place_piece(Queen('black'), 7, 3)  # Queen
        self.place_piece(King('black'), 7, 4)  # King
        self.place_piece(Bishop('black'), 7, 5)  # Bishop
        self.place_piece(Knight('black'), 7, 6)  # Knight
        self.place_piece(Rook('black'), 7, 7)  # Rook
        self.place_piece(Pawn('black'), 6, 0)  # Pawn
        self.place_piece(Pawn('black'), 6, 1)  # Pawn
        self.place_piece(Pawn('black'), 6, 2)  # Pawn
        self.place_piece(Pawn('black'), 6, 3)  # Pawn
        self.place_piece(Pawn('black'), 6, 4)  # Pawn
        self.place_piece(Pawn('black'), 6, 5)  # Pawn
        self.place_piece(Pawn('black'), 6, 6)  # Pawn
        self.place_piece(Pawn('black'), 6, 7)  # Pawn

    def get_square(self, row, col):
        """
        returns square object at location given by row and column
        :param row:
        :param col:
        :return square:
        """
        return self._board[row][col]

    def place_piece(self, piece, row, col):
        """
        places a piece object onto a square object on the board
        :param piece:
        :param row:
        :param col:
        :return:
        """
        square = self._board[row][col]
        square.add_piece(piece)

    def print_board(self):
        '''
        prints the board for visualizing chess moves and error checking.
        White pieces are in black font on a light grey background
        Black pieces are in yellow font on a black background
        '''
        label_col = "   a b c d e f g h"
        header = "  |----------------|"
        print(label_col)
        print(header)
        for row in range(0, 8):
            print(str(row+1) + ' |', end="")
            for col in range(8):
                piece = self._board[row][col].get_piece()
                if piece is not None:
                    if piece.get_color() == 'black':
                        print("\033[1;33;40m" + piece.get_symbol() + "\033[0m", end=" ")
                    else:
                        print("\033[0;30;47m" + piece.get_symbol() + "\033[0m", end=" ")
                else:
                    print(".", end=" ")
            print('| ' + str(row+1))
        print(header)
        print(label_col)


class ChessVar:
    """
    Represents the ChessVar game. Manages the game including turn order, moves, captures and game state.
    White player starts with the first move.
    """
    def __init__(self):
        '''
        initializes a new game with the board, game state, and both players.
        Starts the game off with the white player going first.
        '''
        self._board = Board()
        self._game_state = 'UNFINISHED'
        self._players = {'white': Player('white'), 'black': Player('black')}
        self._curr_player = self._players['white']

    def get_board(self):
        '''
        returns the game board
        '''
        return self._board

    def get_game_state(self):
        """
        Returns the current state of the game.
        Returns:
            - 'UNFINISHED', 'WHITE_WON', 'BLACK_WON'
        """
        return self._game_state

    def change_game_state(self):
        '''
        Changes game state from 'UNFINISHED' to "BLACK_WON" or "WHITE_WON when called"
        '''
        if self._curr_player.get_color() == 'white':
            self._game_state = 'WHITE_WON'
        else:
            self._game_state = 'BLACK_WON'
        return self.get_game_state()

    def change_turn(self):
        '''
        Called after a valid move has been made. Switches turn to next player.
        '''
        if self._curr_player.get_color() == 'white':
            self._curr_player = self._players['black']
        else:
            self._curr_player = self._players['white']

    def get_current_player(self):
        '''
        Returns the current player (white or black)
        '''
        return self._curr_player

    def get_player(self, color):
        """
        Returns the player object of the color specified.
        :param color:
        :return player:
        """
        return self._players[color]

    def make_move(self, from_square_str, to_square_str):
        """
        Determines if a move on the board is valid, if it is the move is made and opponent pieces are captured if
        applicable.
        :param from_square_str: string representing the square object the object is moving from
        :param to_square_str: string representing the square object the object is moving to
        :return True if the move is made successfully:
        :return False if move violates rules:
        """
        # converts string representation and adjusts for zero-based indexing to convert to square objects
        col_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        from_row = int(from_square_str[1]) - 1
        from_col = col_dict[from_square_str[0]]
        to_row = int(to_square_str[1]) - 1
        to_col = col_dict[to_square_str[0]]

        # checks if piece moved off board
        if to_row > 7 or to_col > 7 or to_row < 0 or to_col < 0:
            return False

        to_square = self._board.get_square(to_row, to_col)
        from_square = self._board.get_square(from_row, from_col)
        moving_piece = from_square.get_piece()

        # checks to see if player is moving their own piece
        if moving_piece is None:
            return False
        if moving_piece.get_color() != self._curr_player.get_color():
            return False

        # checks to see if game has ended
        if self.get_game_state() != "UNFINISHED":
            return False

        # checks if move violates rules of piece
        if moving_piece.valid_move(from_square, to_square) is False:
            return False

        # skips collision checking for knights since they can hop other pieces
        if isinstance(moving_piece, Knight):
            # moves to an empty square if passes all tests
            if to_square.get_piece() is None:
                self.move_process(moving_piece, from_square, to_square)
                return True
            # captures piece and moves to that square if it lands on an opponent's piece
            elif to_square.get_piece().get_color != from_square.get_piece().get_color():
                self.capture_piece(to_square)
                self.move_process(moving_piece, from_square, to_square)
                return True
            else:
                return False

        # adjusts captures for pawns so only diagonal moves can capture opponent's pieces
        # and initial 2 square move can hop other pieces
        elif isinstance(moving_piece, Pawn):
            if self.collision_check(to_row, to_col, from_row, from_col) is False:
                return False
            # moves piece to an empty square if it passes all tests
            if to_square.get_piece() is None:
                self.move_process(moving_piece, from_square, to_square)
                return True
            # captures opponent piece and moves to that square only if it is a diagonal move
            elif moving_piece.get_color() != to_square.get_piece().get_color() \
                    and moving_piece.valid_move(from_square, to_square) == 'pawn_capture':
                self.capture_piece(to_square)
                self.move_process(moving_piece, from_square, to_square)
                return True
            else:
                return False

        # checks for collisions with pieces in path of moving piece for all pieces except knights and pawns
        else:
            if self.collision_check(to_row, to_col, from_row, from_col) is False:
                return False
            # moves piece to an empty square if it passes all tests
            if to_square.get_piece() is None:
                self.move_process(moving_piece, from_square, to_square)
                return True
            # captures piece if it passes tests and lands on an opponent's piece
            elif moving_piece.get_color() != to_square.get_piece().get_color():
                self.capture_piece(to_square)
                self.move_process(moving_piece, from_square, to_square)
                return True
            else:
                return False

    def collision_check(self, to_row, to_col, from_row, from_col):
        """
        Returns false if a collision with another piece occurs, violating game rules.
        :param to_row: row value of square piece is moving to
        :param to_col: column value of square piece is moving to
        :param from_row: row value of square piece is moving from
        :param from_col: column value of square piece is moving from
        :return false if a collision with another piece occurs:
        """
        if to_row == from_row:
            row_direction = 0
        elif to_row > from_row:
            row_direction = 1
        else:
            row_direction = -1

        if to_col == from_col:
            col_direction = 0
        elif to_col > from_col:
            col_direction = 1
        else:
            col_direction = -1

        curr_row = from_row + row_direction
        curr_col = from_col + col_direction
        while curr_row != to_row or curr_col != to_col:
            curr_square = self._board.get_square(curr_row, curr_col)
            if curr_square.get_piece() is not None:
                return False
            curr_row += row_direction
            curr_col += col_direction

    def move_process(self, moving_piece, from_square, to_square):
        """
        Moves a piece from one square to another and removes it from the starting square.
        :param moving_piece: piece object being moved
        :param from_square: square object piece is moving from
        :param to_square: square object piece is moving to
        :return:
        """
        to_row = to_square.get_row()
        to_col = to_square.get_col()

        self._board.place_piece(moving_piece, to_row, to_col)
        from_square.remove_piece()
        self.get_game_state()
        self.change_turn()

    def capture_piece(self, square):
        """
        Captures an opponents piece and moves it into the player's captured pieces list
        :param square:
        :return:
        """
        cap_piece = square.get_piece()
        if isinstance(cap_piece, King):         # changes game state if a king is captured
            self.change_game_state()
        curr_player = self.get_current_player()
        curr_player.add_captured(cap_piece)
        square.remove_piece()

    def enter_fairy_piece(self, piece_symbol, square_str):
        """
        Enters a fairy piece onto the board.
        :param piece_symbol: Type of the fairy piece ('F', 'H', 'f', 'h')
        :param square_str: The square on which the fairy piece is entering.
        :return False if entering violates rules:
        :return True if the fairy piece is entered successfully:
        """
        # need to check to see if a rook, knight, queen, bishop was captured in the square during
        # last turn.
        col_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        sq_row = int(square_str[1]) - 1
        sq_col = col_dict[square_str[0]]
        square = self._board.get_square(sq_row, sq_col)
        curr_player = self.get_current_player()
        replace_piece = ['n', 'r', 'b', 'q']
        major_pieces_cap_count = 0

        if piece_symbol.lower() not in curr_player.get_fairy_pieces():
            return False

        # for white fairy piece entering play
        if curr_player.get_color() == 'white':
            if piece_symbol == 'H':
                piece_type = Hunter
            elif piece_symbol == 'F':
                piece_type = Falcon
            else:
                return False

            curr_captured = self.get_player('black').get_captured_pieces()

            # checks if major pieces captured > fairy pieces played, invalid if not
            for piece in curr_captured:
                if piece.get_symbol().lower() in replace_piece:
                    major_pieces_cap_count += 1

            if major_pieces_cap_count > curr_player.get_fairy_played_count():
                if (square.get_row() == 0 or square.get_row() == 1) and square.get_piece() is None:
                    square.add_piece(piece_type('white'))
                    curr_player.remove_fairy_piece(piece_symbol.lower())
                    curr_player.inc_fairy_played_count()
                    self.get_game_state()
                    self.change_turn()
                    return True
                else:
                    return False
            else:
                return False
        # for black fairy piece entering play
        else:
            if piece_symbol == 'h':
                piece_type = Hunter
            elif piece_symbol == 'f':
                piece_type = Falcon
            else:
                return False
            curr_captured = self.get_player('white').get_captured_pieces()

            # checks if major pieces captured > fairy pieces played, invalid if not
            for piece in curr_captured:
                if piece.get_symbol() in replace_piece:
                    major_pieces_cap_count += 1

            if major_pieces_cap_count > curr_player.get_fairy_played_count():
                if (square.get_row() == 7 or square.get_row() == 6) and square.get_piece() is None:
                    square.add_piece(piece_type('black'))
                    curr_player.remove_fairy_piece(piece_symbol)
                    curr_player.inc_fairy_played_count()
                    self.get_game_state()
                    self.change_turn()
                    return True
                else:
                    return False
            else:
                return False

