import os

class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
        
    def can_move_to(self, board, x, y):
        if not (0 <= x <= 7 and 0 <= y <= 7):
            return False
        if board[x][y] is None or board[x][y].color != self.color:
            return True
        return False
    #If a move is out of bounds or the destination square is occupied by a friendly piece, then the piece cannot move there.

    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')

    def add_move(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []


class Pawn(Piece):

    def __init__(self, color):
        self.dir = -1 if color == 'white' else 1
        self.en_passant = False
        super().__init__('pawn', color, 1.0)
    def can_move_to(self, board, x, y):
        if not super().can_move_to(board, x, y):
            return False
        #The delta_x and delta_y variables are used to calculate the difference between the current position and the destination position. Then, the code checks each square between the current position and the destination position (excluding the current position and the destination position) to see if there is a piece occupying that square. If there is, then the piece cannot move to the destination position because it would be jumping over another piece.


        # Check if there is a piece in the way of the move
        if self.color == 'white':
            if board.get_piece(x, y+1) is not None:
                return False
        else:
            if board.get_piece(x, y-1) is not None:
                return False

        return True


class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color, 3.0)

class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3.001)

class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color, 5.0)

class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color, 9.0)

class King(Piece):

    def __init__(self, color):
        self.left_rook = None
        self.right_rook = None
        super().__init__('king', color, 10000.0)