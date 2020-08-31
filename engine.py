""" Chess Engine """
import chess
# Initial chess board
BOARD = chess.Board()

def generate_piece_count(board, colour):
    """ Calculates and returns a dictionary with piece counts """
    # Create a dictionary to store values
    pieces = {}
    # Split the FEN board to just the pieces
    fen = board.fen().split(" ")[0]
    # Counting pieces depeneding on colour
    king = fen.count('k') if colour == 'K' else fen.count('K')
    queen = fen.count('q') if colour == 'Q' else fen.count('Q')
    rook = fen.count('r') if colour == 'R' else fen.count('R')
    knight = fen.count('n') if colour == 'N' else fen.count('N')
    bishop = fen.count('b') if colour == 'B' else fen.count('B')
    pawn = fen.count('p') if colour == 'P' else fen.count('p')
    # Setting dictionary keys
    pieces['King'] = king
    pieces['Queen'] = queen
    pieces['Rook'] = rook
    pieces['Knight'] = knight
    pieces['Bishop'] = bishop
    pieces['Pawn'] = pawn
    return pieces


def evaluate_position(board, side):
    """ Evaluation function for chess game """
    pass
