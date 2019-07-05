# 15-112, Summer 2, TP
######################################
# Full name: Jose Saravia
# Section: A
# Andrew ID: jsaravia
######################################

# ------ Code is still being tested ------
# File is used for testing obstacle deployment code
import copy
import random
import math

import GameObject
import GameUI



# global uiData = None

# Template for creating new boards
EMPTY_BOARD = [[0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0]]

# Contains canvas coordinate where obstacle spawns
# locations are labeled with chars for clarity

# normal
a = (-60, 200)
b = (-60, 320)
c = (-60, 440)
d = (60, 680)
e = (180, 680)
f = (300, 680)

# Diagonals

g = (-60, 80)
h = (420, 80)
i = (420, 560)
j = (-60, 560)

# center coordinate
z = (180, 320)

SPAWN_MAP = [[g, 0, 0, 0, 0, 0, h],
             [a, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [b, 0, 0, z, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [c, 0, 0, 0, 0, 0, 0],
             [j, d, 0, e, 0, f, i]]


# Any Class or function that wants to use a board,
# must create a board through this function
# Returns: A list of count boards with 1 or more player moves
def createBoards(count=1, level=1):

    print("Create Boards", level)

    boards = []

    for i in range(count):
        # creates playable board
        board = Board(level)
        while (board.isPlayable != True):
            board = Board(level)
        boards.append(board)

    if(len(boards) == 1):
        return boards[0]
    return boards


class Board(object):

    minObstacleCount = 1
    maxObstacleCount = 4
    # level = 1

    def __init__(self, level):

        self.level = level
        self.levelSetUp()
        self.obstacleCount = random.randint(Board.minObstacleCount,
                                            Board.maxObstacleCount)
        self.obstacleList = []
        self.obstacleBoard = self.createBoard()
        self.powerList = [PowerItems(self.obstacleBoard)] \
            if (random.randint(1, 10) == 5) else []
        self.obstacleBoardPaths = self.getPaths()
        self.totalPlayerMoves = Board.countMoves(EMPTY_BOARD,
                                                 self.obstacleBoardPaths,
                                                 (3, 3), 1, 3, 0)
        self.isPlayable = self.isPlayable()

    # Could be a source of lag: If so don't deepcopy EMPTY_BOARD
    # Creates board
    def createBoard(self):

        board = copy.deepcopy(EMPTY_BOARD)
        for count in range(self.obstacleCount):
            # obstacle = random.choice([obstacleNormal(), obstacleDiagonal()])
            obstacle = self.getObstacle()
            # add obstacle to board
            spawn = obstacle.getSpawnLocation()
            board[spawn[0]][spawn[1]] = obstacle.getId()
            self.obstacleList.append(obstacle)

        return board

    # Game level based logic - levels increase every 15 points
    def getObstacle(self):

        level = self.level
        if(level == 1):
            return obstacleNormal()
        elif(level == 2):
            return random.choice([obstacleNormal(), obstacleDiagonal()])
        elif(level >= 3):
            return random.choice([obstacleNormal(), obstacleDiagonal(),
                           obstacleOcillating()])


    def levelSetUp(self):

        level = self.level

        if (level == 1):
            Board.maxObstacleCount = 3
        elif (level == 2):
            Board.minObstacleCount = 2
            Board.maxObstacleCount = 3
        elif (level == 3):
            Board.minObstacleCount = 2
            Board.maxObstacleCount = 6
        else:
            Obstacle.increaseObstacleSpeed()

    # A board is playable if the player can move without dying
    def isPlayable(self):

        if(self.totalPlayerMoves >= 1):
            return True
        return False

    # Calculates the path of all spawned obstacles
    # This path board is used to calculate its playability
    def getPaths(self):
        board = copy.deepcopy(self.obstacleBoard)

        for obstacle in self.obstacleList:
            obstacle.getPath(board)

        return board

    # Long comment for when I revisit this project
    # Counts the number of possible moves the player can make in obsBoard
    # (the board with obstacle paths). This function is using backtracking to
    # count the number of moves the player can make.
    # In short it simulates an actual player playing on the obsBoard
    # Params: emptyBoard -> 2D list, obsBoard -> 2D list, center ->
    # center row and col of board, curNum -> int first obstacle ID (color 1)
    # maxNum -> Max obstacle ID (mix of all color obstacles),
    # count -> int of moves
    # Return: int Count of moves
    @staticmethod
    def countMoves(emptyBoard, obsBoard, center, curNum, maxNum, count):


        cC, cR = center

        if(curNum == maxNum):
            return 0

        # test moves with obstacles of id 2
        if(curNum % 2 == 0):
            for c in [cC - 2, cC + 2, cC]:

                Board.changeBoard(emptyBoard, cR, c, curNum)

                if(Board.isValid(emptyBoard, obsBoard, maxNum)):
                    count += 1
                    Board.countMoves(emptyBoard, obsBoard, center,
                                     curNum + 1, maxNum, count)
                emptyBoard[cR][c] = 0
        else:
            # test moves with obstacles of id 1
            for r in [cR - 2, cR + 2, cR]:

                Board.changeBoard(emptyBoard, r, cC, curNum)

                if (Board.isValid(emptyBoard, obsBoard, maxNum)):
                    count = Board.countMoves(emptyBoard, obsBoard, center,
                                             curNum + 1, maxNum, count)
                emptyBoard[r][cC] = 0

        return count

    # Used for counting moves
    @staticmethod
    def changeBoard(board, r, c, newNum):

        if (board[r][c] != 0):
            board[r][c] += newNum
        else:
            board[r][c] = newNum

    # checks if move is valid, used for counting moves
    @staticmethod
    def isValid(boardP, boardO, intersect):

        for loc in [(3, 3), (3, 1), (3, 5), (1, 3), (5, 3)]:

            r = loc[0]
            c = loc[1]

            if (boardP[r][c] == 0):
                continue

            if (boardP[r][c] == boardO[r][c] or  # If equal number
                boardO[r][c] == intersect or  # If spot has all players
                # players all in one spot, but an obstacle is in the spot
                    (boardP[r][c] == intersect and boardO[r][c] != 0)):
                return False

        return True

    def increaseMaxObstacleCount(self):
        Board.maxObstacleCount += 1

    def increaseMinObstacleCount(self):
        Board.minObstacleCount += 1


    # ONLY USED FOR TESTING
    def printBoardData(self):

        print("SpawnBoard")
        printBoard(self.obstacleBoard)
        print("Board with paths")
        printBoard(self.obstacleBoardPaths)
        print()
        print("Move Count", self.totalPlayerMoves)
        print("Is Playable", self.isPlayable)


class Obstacle(GameObject.GameObject):

    SPEED = 20
    def __init__(self, direction, spawnLoc, id):

        radius = GameUI.UIData.obstacleRadius
        self.id = id
        self.direction = direction
        self.spawnLoc = spawnLoc
        self.canvasStartLocation = SPAWN_MAP[self.spawnLoc[0]][self.spawnLoc[1]]
        x, y = self.canvasStartLocation[0], self.canvasStartLocation[1]
        speedX, speedY = (Obstacle.SPEED * self.direction[1],
                          Obstacle.SPEED  * self.direction[0])

        color = GameUI.UIData.colorB
        if(self.id % 2 == 0):
            color = GameUI.UIData.colorA

        super().__init__(x, y, radius, color, speedX, speedY)

    @staticmethod
    def increaseObstacleSpeed():

        if(Obstacle.SPEED != 30):
            Obstacle.SPEED += 1

    def move(self):
        self.x += self.speedX
        self.y -= self.speedY

    def draw(self, canvas):
        super().draw(canvas)

    @staticmethod
    def placePath(board, r, c, id):

        # check if in bound
        max = len(board)
        if(r < 0 or r > max or c < 0 or c > max): return

        if (board[r][c] >= 3):
            board[r][c] = 3
        elif (board[r][c] > 1 and id == 1):
            board[r][c] += id
        elif (board[r][c] == 1 and id == 2):
            board[r][c] += id
        else:
            board[r][c] = id

    def getId(self):
        return self.id

    def getDirection(self):
        return self.direction

    def getSpawnLocation(self):
        return self.spawnLoc

    def getSpawnCol(self):
        return self.spawnLoc[1]

    def getSpawnRow(self):
        return self.spawnLoc[0]


class obstacleNormal(Obstacle):

    def __init__(self):

        self.id = random.choice([1,2])
        self.setUpObstacle()
        super().__init__(self.direction, self.spawnLoc, self.id)

    def setUpObstacle(self):

        if(self.id == 1):
            self.direction = (0, 1)
            self.spawnLoc = random.choice([(1, 0), (3, 0), (5, 0)])
        else:
            self.direction = (1, 0)
            self.spawnLoc = random.choice([(6, 1), (6, 3), (6, 5)])

    def getPath(self, board):

        r, c = self.getSpawnRow(), self.getSpawnCol()
        id = self.getId()

        while(c < len(board) and id == 1):
            Obstacle.placePath(board, r, c, id)
            c += self.getDirection()[1]

        while (r >= 0 and id == 2):
            Obstacle.placePath(board, r, c, id)
            r -= self.getDirection()[0]


class obstacleDiagonal(Obstacle):

    def __init__(self):

        self.id = random.choice([1, 2, 3, 4])
        self.setUpObstacle()
        super().__init__(self.direction, self.spawnLoc, self.id)

    def setUpObstacle(self):

        data = {1: ((1, 1), (0, 0), 1),
                2: ((1, -1), (0, 6), 2),
                3: ((-1, -1), (6, 6), 1),
                4: ((-1, 1), (6, 0), 2)}

        idData = data.get(self.id)
        self.direction, self.spawnLoc = idData[0], idData[1]
        self.id = idData[2]

    def move(self):
        self.x += self.getSpeedX()
        self.y += self.getSpeedY()

    def getPath(self, board):

        r = self.spawnLoc[0]
        c = self.spawnLoc[1]
        dir = self.direction
        id = self.id

        def pathHelper():
            Obstacle.placePath(board, r - dir[0], c, id)
            Obstacle.placePath(board, r, c - dir[1], id)
            Obstacle.placePath(board, r, c, id)

        while(self.getSpawnCol() == 0 and c < len(board)-1):
            r += dir[0]
            c += dir[1]
            pathHelper()

        while (self.getSpawnCol() == 6 and c > 0):
            r += dir[0]
            c += dir[1]
            pathHelper()

class obstacleOcillating(Obstacle):

    def __init__(self):
        self.id = random.choice([1, 2])
        self.setUpObstacle()
        self.amplitude = random.choice([20, 30])
        self.period = 5
        super().__init__(self.direction, self.spawnLoc, self.id)

    def setUpObstacle(self):
        data = {1: ((0, 1), (3, 0), 1),
                2: ((-1, 0), (6, 3), 2)}

        idData = data.get(self.id)
        self.direction, self.spawnLoc = idData[0], idData[1]
        self.id = idData[2]

    def move(self):

        amplitude = self.getAmplitude()
        period = self.getPeriod()

        # Get coordinates of sin equation
        if (self.getId() == 1):

            self.setY(self.getY() + amplitude * math.sin(
                period * self.getX()))
            self.setX(self.getX() + self.getSpeedX())
        else:
            self.setX(self.getX() + amplitude * math.sin(
                period * self.getY()))
            self.setY(self.getY() + self.getSpeedY())

    def getPath(self, board):

        r, c = self.getSpawnLocation()
        id = self.getId()

        while (self.getId() == 1 and c <= len(board) - 1):
            board[r - 1][c] = id
            board[r][c] = id
            board[r + 1][c] = id
            c += self.getDirection()[1]

        while (self.getId() == 2 and r >= 0):

            board[r][c] = id
            board[r][c + 1] = id
            if (self.getAmplitude() == 30):
                board[r][c + 2] = id
            r += self.getDirection()[0]

    def getAmplitude(self):
        return self.amplitude

    def getPeriod(self):
        return self.period

    def setAmplitude(self, amplitude):
        self.amplitude = amplitude

    def setPeriod(self, period):
        self.period = period



# Method Prints 2D list in a readable format
# ONLY USED FOR DEBUGGING
def printBoard(board):

    for row in range(len(board)):
        for col in range(len(board[0])):
            print(" " + str(board[row][col]) + " ", end="")
        print()


# Class manages power-ups and power-downs
class PowerItems(Obstacle):

    def __init__(self, board):

        self.id = random.choice([1])
        self.setUpObstacle(board)
        super().__init__(self.direction, self.spawnLoc, self.id)
        self.setColor(None)

    def setUpObstacle(self, board):

        if(self.id == 1):
            self.direction = (0, 1)
            self.spawnLoc = random.choice([(1, 0), (3, 0), (5, 0)])
            # Makes sure power item is not above obstacle
            while( board[self.spawnLoc[0]][self.spawnLoc[1]] != 0):
                self.spawnLoc = random.choice([(1, 0), (3, 0), (5, 0)])
        else:
            self.direction = (1, 0)
            self.spawnLoc = random.choice([(6, 1), (6, 3), (6, 5)])

    def getImage(self):

        if(self.id == 1):
            return GameUI.UIData.powerItemImages[0]

    def move(self):
        self.x += self.speedX
        self.y -= self.speedY

    def draw(self, canvas):

        x, y = self.getX(), self.getY()
        r = 26
        canvas.create_oval(x - r, y - r, x +r, y +r, fill=GameUI.UIData.colorB, width = 0)
        canvas.create_image(x, y, image=self.getImage())

    def __str__(self):
        return "power"


