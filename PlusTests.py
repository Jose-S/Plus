import GameBoard

EMPTY_BOARD = GameBoard.EMPTY_BOARD

# ------- BOARDS WITH OBSTACLES -------
# Always True - 9 moves
boardOb0 = [[0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

# 1 straight - 6 moves
boardOb1 = [[0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]

# 3 straight - 2 moves
boardOb2 = [[0, 0, 0, 2, 0, 2, 0],
            [0, 0, 0, 2, 0, 2, 0],
            [0, 0, 0, 2, 0, 2, 0],
            [0, 0, 0, 2, 0, 2, 0],
            [0, 0, 0, 2, 0, 2, 0],
            [1, 1, 1, 3, 1, 3, 1],
            [0, 0, 0, 2, 0, 2, 0]]


# 1 diagonal - 6 moves
boardOb3 = [[1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 1]]

# 1 diagonal and 2 straight - 2 moves
boardOb4 = [[1, 1, 0, 0, 0, 2, 0],
            [1, 1, 1, 0, 0, 2, 0],
            [0, 1, 1, 1, 0, 2, 0],
            [0, 0, 1, 1, 1, 2, 0],
            [0, 0, 0, 1, 1, 3, 0],
            [1, 1, 1, 1, 1, 3, 1],
            [0, 0, 0, 0, 0, 3, 1]]

# Two diagonals and 2 straight - 1 move
boardOb5 = [[1, 1, 0, 0, 0, 2, 2],
            [1, 1, 1, 0, 2, 2, 2],
            [0, 1, 1, 3, 2, 2, 0],
            [0, 0, 3, 3, 3, 2, 0],
            [0, 2, 2, 3, 1, 3, 0],
            [3, 3, 3, 1, 1, 3, 1],
            [2, 2, 0, 0, 0, 3, 1]]

# 1 multi-color diagonal - 4 moves
boardOb6 = [[3, 3, 0, 0, 0, 0, 0],
            [3, 3, 3, 0, 0, 0, 0],
            [0, 3, 3, 3, 0, 0, 0],
            [0, 0, 3, 3, 3, 0, 0],
            [0, 0, 0, 3, 3, 3, 0],
            [0, 0, 0, 0, 3, 3, 3],
            [0, 0, 0, 0, 0, 3, 3]]

# 6 straight,  always False - 0 moves
boardOb7 = [[0, 2, 0, 2, 0, 2, 0],
            [1, 3, 1, 3, 1, 3, 1],
            [0, 2, 0, 2, 0, 2, 0],
            [1, 3, 1, 3, 1, 3, 1],
            [0, 2, 0, 2, 0, 2, 0],
            [1, 3, 1, 3, 1, 3, 1],
            [0, 2, 0, 2, 0, 2, 0]]

# ------- BOARDS WITH ALL POSSIBLE PLAYER MOVES-------

boardP0 = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 3, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]

boardP1 = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 2, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]

boardP2 = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 2, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]

boardP3 = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 2, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]

boardP4 = [[0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]

boardP5 = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 2, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]

boardP6 = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 2, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]

boardP7 = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 2, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]

boardP8 = [[0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 2, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0]]

def testIsValidBoard():

    print("Testing isValidBoard...", end="")
    assert(GameBoard.Board.isValid(boardP0, boardOb3, 3) == False)
    assert(GameBoard.Board.isValid(boardP1, boardOb3, 3) == False)
    assert(GameBoard.Board.isValid(boardP8, boardOb7, 3) == False)
    assert(GameBoard.Board.isValid(boardP8, boardOb0, 3) == True)
    assert(GameBoard.Board.isValid(boardP7, boardOb5, 3) == True)
    # assert(isValid(boardP1,boardOb3,3) == False)
    # assert(isValid(boardP1,boardOb3,3) == False)
    print("Passed!")


def testCountMoves():

    print("Testing countMoves...", end="")
    assert(GameBoard.Board.countMoves(EMPTY_BOARD, boardOb0, (3, 3), 1, 3, 0) == 9)
    assert(GameBoard.Board.countMoves(EMPTY_BOARD, boardOb1, (3, 3), 1, 3, 0) == 6)
    assert(GameBoard.Board.countMoves(EMPTY_BOARD, boardOb2, (3, 3), 1, 3, 0) == 2)
    assert(GameBoard.Board.countMoves(EMPTY_BOARD, boardOb3, (3, 3), 1, 3, 0) == 6)
    assert(GameBoard.Board.countMoves(EMPTY_BOARD, boardOb4, (3, 3), 1, 3, 0) == 2)
    assert(GameBoard.Board.countMoves(EMPTY_BOARD, boardOb5, (3, 3), 1, 3, 0) == 1)
    assert(GameBoard.Board.countMoves(EMPTY_BOARD, boardOb6, (3, 3), 1, 3, 0) == 4)
    assert(GameBoard.Board.countMoves(EMPTY_BOARD, boardOb7, (3, 3), 1, 3, 0) == 0)
    print("Passed!")


def runTests():

    testIsValidBoard()
    testCountMoves()