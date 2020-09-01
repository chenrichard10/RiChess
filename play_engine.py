""" Module for playing the game """
import chess
import engine

def start_game(colour):
    """ Start a new game against the engine """
    turn = 1
    board = chess.Board()
    print('(っ◕‿◕)っ  Chess (っ◕‿◕)っ ')
    print("Good Luck!")
    print(board)
    print("\n")

    while not board.is_checkmate():
        if turn % 2 == colour:
            #top_moves = engine.generate_top_moves(board, colour)
            #print("Top moves:")
            #print(top_moves)
            try:
                move = input("Your move:")
                board.push_san(move)
                print(board)
                print("\n")
            except AttributeError:
                print("Illegal move!")
                continue
        else:
            """
            print("     Thonking.....\n \
                    ▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒▒▒\n \
                    ▒▒▒▒▒▄█▀▀░░░░░░▀▀█▄▒▒▒▒▒\n \
                    ▒▒▒▄█▀▄██▄░░░░░░░░▀█▄▒▒▒\n \
                    ▒▒█▀░▀░░▄▀░░░░▄▀▀▀▀░▀█▒▒\n \
                    ▒█▀░░░░███░░░░▄█▄░░░░▀█▒\n \
                    ▒█░░░░░░▀░░░░░▀█▀░░░░░█▒\n \
                    ▒█░░░░░░░░░░░░░░░░░░░░█▒\n \
                    ▒█░░██▄░░▀▀▀▀▄▄░░░░░░░█▒\n \
                    ▒▀█░█░█░░░▄▄▄▄▄░░░░░░█▀▒\n \
                    ▒▒▀█▀░▀▀▀▀░▄▄▄▀░░░░▄█▀▒▒\n \
                    ▒▒▒█░░░░░░▀█░░░░░▄█▀▒▒▒▒\n \
                    ▒▒▒█▄░░░░░▀█▄▄▄█▀▀▒▒▒▒▒▒\n \
                    ▒▒▒▒▀▀▀▀▀▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒")
            """
            top_moves = engine.generate_top_moves(board, -colour)
            print("Top moves:")
            print(top_moves)
            board.push(top_moves[0]['move'])
            print(board)
            print("\n")
            print("Engine's move:" + str(top_moves[0]['move']) + "\n")

        colour *= -1
        turn += 1

    if turn % 2 == colour:
        print("You lost!")
    else:
        print("You win!")

start_game(1)
