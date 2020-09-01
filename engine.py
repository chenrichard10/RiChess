""" Chess Engine """
import math
import chess

# Initial chess board
BOARD = chess.Board()
# Use legal moves to count mobility

def generate_piece_count(board, colour):
    """ Calculates and returns a dictionary with piece counts """
    # Create a dictionary to store values
    pieces = {}
    # Split the FEN board to just the pieces
    fen = board.fen().split(" ")[0]
    # Counting pieces depeneding on colour
    king = fen.count('k') if colour == 0 else fen.count('K')
    queen = fen.count('q') if colour == 0 else fen.count('Q')
    rook = fen.count('r') if colour == 0 else fen.count('R')
    knight = fen.count('n') if colour == 0 else fen.count('N')
    bishop = fen.count('b') if colour == 0 else fen.count('B')
    pawn = fen.count('p') if colour == 0 else fen.count('P')
    # Setting dictionary keys
    pieces['King'] = king
    pieces['Queen'] = queen
    pieces['Rook'] = rook
    pieces['Knight'] = knight
    pieces['Bishop'] = bishop
    pieces['Pawn'] = pawn
    return pieces


def count_doubled(board, colour):
    """ Function counts doubled pawns """
    pass


def evaluate_position(board, colour, legal_moves):
    """ Evaluation function for chess game """
    white_pieces = generate_piece_count(board, 1)
    #print("White Pieces:")
    #print(white_pieces)
    black_pieces = generate_piece_count(board, 0)
    #print("Black Pieces:")
    #print(black_pieces)
    material_score = 200  * (white_pieces['King'] - black_pieces['King']) \
                  + 9 * (white_pieces['Queen'] - black_pieces['Queen']) \
                  + 5 * (white_pieces['Rook'] - black_pieces['Rook']) \
                  + 3 * (white_pieces['Knight'] - black_pieces['Knight']) \
                  + 3 * (white_pieces['Bishop'] - black_pieces['Bishop']) \
                  + 1 * (white_pieces['Pawn'] - black_pieces['Pawn'])
    mobility_score = 0.01 * legal_moves
    #print("Score")
    #print(material_score)
    evaluation = mobility_score + material_score * colour
    return evaluation

def negamax(depth, board, alpha, beta, colour):
    """ Negamax decision tree """
    if depth == 0:
        return evaluate_position(board, colour, board.legal_moves.count()) * colour
    value = -1e9
    temp = board
    #print(board)
    for move in board.legal_moves:
        temp.push(move)
        value = -negamax(depth - 1, temp, -beta, -alpha, -colour)
        alpha = max(alpha, value)
        temp.pop()
        if alpha >= beta:
            break

    return value

def generate_top_moves(board, colour):
    """ Generates a list of top moves """
    scores = []
    for move in board.legal_moves:
        board.push(move)
        #print(board)
        scores.append({'move': move, 'score': negamax(4, board, -math.inf, math.inf, -colour)})
        board.pop()

    newlist = sorted(scores, key=lambda k: k['score'], reverse=True)
    return newlist[:3]

# Testing Function
def test(user_move):
    """ function used for testing game board and evaluation """
    colour = 1
    user_move = "temp"
    while user_move != "quit":
        print("Enter your move:")
        user_move = input()

        if user_move == 'eval':
            print(generate_top_moves(BOARD, -colour))
            continue

        if user_move == 'legal':
            for move in BOARD.legal_moves:
                print(move)
                continue
        try:
            BOARD.push_san(user_move)
        except AttributeError:
            print("Invalid move!")
        print(BOARD)

if __name__ == "__main__":
    test("move")
