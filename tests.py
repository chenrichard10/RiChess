import time 
import chess
import engine

board = chess.Board()
start = time.process_time()
#for i in range(0, 1000):
    #engine.evaluate_position(board, 1, board.legal_moves.count())
engine.generate_top_moves(board, 1)
#print(time.process_time() - start)

scholar_board = chess.Board()
# Test1 
