# 15-112, Summer 2, TP
######################################
# Full name: Jose Saravia
# Section: A
# Andrew ID: jsaravia
######################################

from tkinter import *
from tkinter import ttk
import time
import math
import GameObject
import GameUI
import GameBoard
import PlusTests
# from threading import Timer
#
# import threading
# Base template for animations was retrieved from course website
# https://pd43.github.io/notes/code/events-example0.py
# photo = photo = PhotoImage(data=img)

# ----------- MODEL -----------


# Initialize the data which will be used to draw on the screen.

# Used for replaying the game
def replay(data, oldScore):

    init(data)
    data.oldScore = oldScore

def quit(data):

    replay(data, data.score)

def init(data):

    # Player Data
    initPlayer(data)

    # Board Data
    data.boardCount = 3
    ## TEST NOTE: Modify second field to change starting level ##
    data.boards = GameBoard.createBoards(data.boardCount, 1)

    # Game Data
    initGameData(data)

    # Initialize UI elements
    data.ui.initUiElements(data.root, data)
    data.ui.removePauseUi()
    data.ui.removeSplashUi()
    data.ui.removePauseButton()
    data.ui.removeHelpButton()

    # Print board for testing purposes
    # for b in data.boards:
    #     b.printBoardData()


def initGameData(data):

    # Game State
    data.isPlaying = False
    data.hasExitedPause = False
    data.isPaused = False
    data.levelHasChanged = False
    data.isInHelpMenu = False
    data.score = 0
    data.oldScore = None
    data.level = 1

    # Time Data
    data.startTime = 0
    data.timeOnPause = 0
    data.pauseTime = 0
    data.timeExitPause = 0

    # Powerup data
    data.hasReversePower = False
    data.hasColorSwitchPower = False
    data.hasSlowPower = False
    data.hasInvinPower = False


def initPlayer(data):

    w, h = data.width, data.height

    # 2 player controlled circles
    data.player1 = GameObject.Player(("Left", "Right"),
                                     data.ui.playerAMaxRadius,
                                     data.ui.ballAColor,
                                     1, w, h)
    data.player2 = GameObject.Player(("Up", "Down"),
                                     data.ui.playerBMaxRadius,
                                     data.ui.ballBColor,
                                     2, w, h)
    # Player background
    data.player1Pad = GameObject.DirectionPad(data.ui.ballBgColor,
                                              data.ui.ballBgRadius + 2,
                                              1, w, h)
    data.player2Pad = GameObject.DirectionPad(data.ui.ballBgColor,
                                              data.ui.ballBgRadius + 2,
                                              2, w, h)

    getPlayerControlDirections(data)


def getPlayerControlDirections(data):

    data.player1DirA = data.player1.getDirections()[0]
    data.player1DirB = data.player1.getDirections()[1]
    data.player2DirA = data.player2.getDirections()[0]
    data.player2DirB = data.player2.getDirections()[1]


# --------- CONTROLLER --------


def mousePressed(event, data):
    pass


def keyReleased(event, data):

    key = event.keysym
    data.keyPressed.discard(key)


def keyPressed(event, data):
    key = event.keysym

    # Initialize the game
    if (not data.isPlaying and
        not data.isPaused and
        key == "space"):
        data.player2.minimizeAnimation(data.ui.playerBMinRadius, .001)
        data.startTime = time.time()
        data.isPlaying = True
        data.score = 0

    # For pausing the game
    if (data.isPlaying and key == "p"):
        # Call pause button, its id is 5
        data.ui.onButton(data, 5)

    if(not data.isPlaying or data.isPaused): return

    # Only add arrow keys to keyPressed set if pressed
    if(key in {"Left", "Right", "Up", "Down"}):
        data.keyPressed.add(key)
        playerControls(data)

    if(key == "m" or data.hasReversePower):
        data.player1.invertDirection()
        data.player2.invertDirection()
        getPlayerControlDirections(data)
        data.hasReversePower = False

    if(key == "l"):
        data.level += 1

def reverseBack(data):
    data.hasReversePower = True


def timerFired(data):

    if(not data.isPlaying or data.isPaused): return

    movePlayersToCenter(data)
    removeUsedBoards(data)

    # If player has just exited the pause screen, wait
    if (not data.hasExitedPause):
        moveObstacles(data)
        checkForPlayerCollsion(data)
        increaseScore(data)

# Removes boards that are not displaying obstacles and adds a new board
def removeUsedBoards(data):

    removeOutOfBoundObstacles(data)
    if(len(data.boards[0].obstacleList) == 0):
        data.boards.pop(0)
        data.boards.append(GameBoard.createBoards(1, data.level))


def checkForPlayerCollsion(data):

    obstacles = data.boards[0].obstacleList

    for obstacle in obstacles:
        if(data.player1.checkCollision(obstacle) or
           data.player2.checkCollision(obstacle)):
            replay(data, data.score)

    # if (len(data.boards[0].powerList) != 0):
    #     item = data.boards[0].powerList[0]
    #     if (data.player1.checkCollision(item)):
    #         data.hasReversePower = True
    #         data.boards[0].powerList = []
    #         # t = Timer(3.0, reverseBack, args=[data])
    #         # t.start()


def playerControls(data):

    # Player 1 Controls
    if (data.player1DirA in data.keyPressed):

        data.player1.moveToDirection(data.player1DirA)
        data.player1Pad.moveToDirection(data.player1DirA)

    elif (data.player1DirB in data.keyPressed):

        data.player1.moveToDirection(data.player1DirB)
        data.player1Pad.moveToDirection(data.player1DirB)

    # Player 2 Controls

    if (data.player2DirA in data.keyPressed):

        data.player2.moveToDirection(data.player2DirA)
        data.player2Pad.moveToDirection(data.player2DirA)

    elif (data.player2DirB in data.keyPressed):

        data.player2.moveToDirection(data.player2DirB)
        data.player2Pad.moveToDirection(data.player2DirB)


def movePlayersToCenter(data):

    if (data.player1DirA not in data.keyPressed and
                data.player1DirB not in data.keyPressed):

        data.player1.moveToCenter()
        data.player1Pad.moveToCenter()

    if (data.player2DirA not in data.keyPressed and
                data.player2DirB not in data.keyPressed):

        data.player2.moveToCenter()
        data.player2Pad.moveToCenter()


def moveObstacles(data):
    obstacles = data.boards[0].obstacleList

    for obstacle in obstacles:
        obstacle.move()

    if(len(data.boards[0].powerList) != 0):
        data.boards[0].powerList[0].move()

def removeOutOfBoundObstacles(data):

    l = data.boards[0].obstacleList

    for obstacle in l:
        if(obstacle.x < -60 or obstacle.x > 420 or
           obstacle.y < -40 or obstacle.y > 680):
            l.remove(obstacle)


def increaseScore(data):

    if(not data.isPlaying): return
    curTime = time.time()
    # Keep track of time spent on pause menu
    if (curTime - data.timeOnPause != curTime):
        data.pauseTime += curTime - data.timeOnPause
        data.timeOnPause = 0

    oldScore = data.score
    data.score = math.floor(curTime - data.startTime - data.pauseTime)

    # Level up when score changes
    if(data.score != oldScore):
        levelUp(data)

def levelUp(data):

    if(data.score % 15 == 0):
        data.level += 1
        data.levelHasChanged = True

# ----------- VIEW -----------


# It only draws on the canvas.
def redrawAll(canvas, data):

    # Draw player
    data.player1Pad.draw(canvas)
    data.player2Pad.draw(canvas)
    data.player1.draw(canvas)
    data.player2.draw(canvas)

    if(data.isPlaying and not data.isInHelpMenu):
        drawPlayingScreen(data, canvas)
    elif(not data.isInHelpMenu):
        drawSplashScreen(data, canvas)

    if(data.isPaused and not data.isInHelpMenu):
        drawPauseScreen(data, canvas)
    else:
        data.ui.removePauseUi()

    # Draw Counter when game is unpaused
    if(data.hasExitedPause):
        drawUnPausedCounter(data, canvas)

    if(data.isInHelpMenu):
        # data.player2.enlargAnimation(data.ui.playerBMaxRadius*5, .002)
        # data.ui.removeSplashUi()
        #
        # if(data.player2.getRadius() == data.ui.playerBMaxRadius*5):
        drawHelpMenu(data, canvas)

def drawHelpMenu(data, canvas):

    data.player2.enlargAnimation(data.ui.playerBMaxRadius * 5, .002)
    data.ui.removeSplashUi()
    data.ui.removePauseButton()

    if (data.player2.getRadius() == data.ui.playerBMaxRadius * 5):

        cX, cY = (data.width//2, data.height//2)
        canvas.create_image(cX, cY, image=data.ui.helpImage)
        data.ui.showHelpButton()


def drawPlayingScreen(data, canvas):

    data.ui.removeSplashUi()
    data.ui.showPauseButton()
    if (not data.isPaused):
        data.player1.minimizeAnimation(data.ui.playerRadius, .0001)
    drawObstacles(data, canvas)
    drawScore(data, canvas)
    drawLevel(data, canvas)



def drawSplashScreen(data, canvas):

    cX, cY = (data.width//2, data.height//2)
    y = (cY - data.ui.playerAMaxRadius) // 2
    canvas.create_image(cX, y, image=data.ui.halfTitleImage)
    data.ui.showSplashUi()
    data.ui.removePauseButton()
    canvas.create_text(cX, cY, text="SPACE", font="futura 30 bold",
                       fill=data.ui.bgColor)

    # Used for displaying the core of the player
    if(data.oldScore is not None):
        cx, cy = data.width // 2, data.height // 2
        canvas.create_text(cx, cy + 175, text=str(data.oldScore), font="futura 50",
                           fill="white")

def drawPauseScreen(data, canvas):

    if (data.player1.getRadius() != data.ui.playerAMaxRadius):
        # data.timeOnPause = time.time()
        data.player2.enlargAnimation(data.ui.playerBMaxRadius, .002)
        data.player1.enlargAnimation(data.ui.playerAMaxRadius, .001)
    data.ui.showPauseUi()


def drawUnPausedCounter(data, canvas):

    cX, cY = (data.width//2, data.height//2)
    totalSec = 3
    seconds = (math.floor(time.time() - data.timeExit))

    if (seconds == totalSec):
        # Modified for algorithm readability
        data.hasExitedPause = False
    else:
        canvas.create_text(cX, cY, text=str(totalSec - seconds),
                           font="futura 150 bold",
                           fill=data.ui.ballBColor)


def drawScore(data, canvas):

    cx, y = data.width//2, data.height - 75
    canvas.create_text(cx, y, text=str(data.score), font="futura 50",
                       fill="white")

def drawLevel(data, canvas):

    cx, y = data.width // 2, data.height - 25
    if(data.levelHasChanged):
        canvas.create_text(cx, y, text=str(data.level), font="futura 16",
                           fill="white")

    data.levelHasChanged = True


def drawObstacles(data, canvas):

    l = data.boards[0].obstacleList
    for o in l:
        o.draw(canvas)

    if (len(data.boards[0].powerList) != 0):
        data.boards[0].powerList[0].draw(canvas)



####################################
####################################
# use the run function as-is
####################################
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyReleaseWrapper(event, canvas, data):
        keyReleased(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    # Set up data and call init
    class Struct(object): pass

    data = Struct()
    data.width = width
    data.height = height
    data.ui = GameUI.UIData(width, height)
    data.keyPressed = set()
    data.timerDelay = 100  # milliseconds
    # create the root and the canvas
    root = Tk()
    root.resizable(width=FALSE, height=FALSE)

    # Chanage theme from aqua(Default) to clam
    # This allows the button background to be changed in mac
    rootThemes = ttk.Style()
    rootThemes.theme_use("clam")

    # Store Root for Button
    data.root = root

    canvas = Canvas(root, width=data.width,
                    height=data.height, bg=data.ui.bgColor)
    canvas.pack()

    init(data)

    root.bind("<Button-1>", lambda event:
        mousePressedWrapper(event, canvas, data))
    # root.bind("<Key>", lambda event:
    #     keyPressedWrapper(event, canvas, data))
    root.bind("<KeyPress>", lambda event:
        keyPressedWrapper(event, canvas, data), add='+')
    root.bind("<KeyRelease>", lambda event:
        keyReleaseWrapper(event, canvas, data), add='+')
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


PlusTests.runTests()
run(360, 640)