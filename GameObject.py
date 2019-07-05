# 15-112, Summer 2, TP
######################################
# Full name: Jose Saravia
# Section: A
# Andrew ID: jsaravia
######################################

from abc import ABC, abstractmethod
import time
import threading
# import GameBoard

# Abstract GameObject Class: CAN NEVER BE INSTANTIATED
class GameObject(ABC):

    # this variable is never modified
    DEFAULT_SPEED = 121

    def __init__(self, x, y, radius, color,
                 speedX = 0, speedY = 0, image = None):

        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speedX = speedX
        self.speedY = speedY
        self.image = image

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def draw(self, canvas):

        r = self.getRadius()
        (x , y) = self.getCenterCordinate()
        color = self.getColor()

        canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, width=0)

    # Used for obstacle collision
    @staticmethod
    def getDistance(x0, y0, x1, y1):
        return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

    # Getter Methods

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getCenterCordinate(self):
        return (self.getX(), self.getY())

    def getRadius(self):
        return self.radius

    def getColor(self):
        return self.color

    def getSpeedX(self):
        return self.speedX

    def getSpeedY(self):
        return self.speedY

    def getImage(self):
        return self.image

    # Setter Methods

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setRadius(self, radius):
        self.radius = radius

    def setColor(self, color):
        self.color = color

    def setSpeedX(self, speedX):
        self.speedX = speedX

    def setSpeedY(self, speedY):
        self.speedY = speedY

    def setImage(self, image):
        self.image = image


class Player(GameObject):

    def __init__(self, controlDirection, radius, color, id, screenW, screenH):

        x = screenW/2
        y = screenH/2
        radius = radius

        if(id == 1):
            speedX, speedY = GameObject.DEFAULT_SPEED, 0
        else:
            speedX, speedY = 0, GameObject.DEFAULT_SPEED

        self.id = id
        self.cX = x
        self.cY = y
        self.directions = controlDirection
        self.hasCollided = False
        self.isActive = False
        self.isInvincible = False
        super().__init__(x, y, radius, color, speedX, speedY)

    def moveToDirection(self, direction):

        xSpeed = self.getSpeedX()
        ySpeed = self.getSpeedY()

        if(self.getId() == 2):
            self.enlargAnimation(25, .01)

        # reverse speed if needed
        if (direction == "Left" or direction == "Up"):
            self.setSpeedX(-abs(xSpeed))
            self.setSpeedY(-abs(ySpeed))
        else:
            self.setSpeedX(abs(xSpeed))
            self.setSpeedY(abs(ySpeed))

        self.move()

    def move(self):

        x = self.getX()
        y = self.getY()

        if(60 <= x <= 300 and
           200 <= y <= 440):

            self.setX(x + self.getSpeedX())
            self.setY(y + self.getSpeedY())

    def moveToCenter(self):

        if(self.getId() == 2):
            self.minimizeAnimation(15, .01)

        # Only move to center if not in the center
        if(self.getX() == self.getCenterX() and
           self.getY() == self.getCenterY()): return

        cX = self.getCenterX()
        cY = self.getCenterY()
        x = self.getX()
        y = self.getY()

        self.movetToCenterHelper(cX, cY, x, y)

    def movetToCenterHelper(self, cX, cY, x, y):

        while (x != cX or y != cY ):

            if(self.getX() < self.getCenterX()):
                self.setSpeedX(abs(self.getSpeedX()))
                self.setX(self.getX() + self.getSpeedX())
            else:
                self.setSpeedX(-abs(self.getSpeedX()))
                self.setX(self.getX() + self.getSpeedX())

            if(self.getY() < self.getCenterY()):
                self.setSpeedY(abs(self.getSpeedY()))
                self.setY(self.getY() + self.getSpeedY())
            else:
                self.setSpeedY(-abs(self.getSpeedY()))
                self.setY(self.getY() + self.getSpeedY())

            x = self.getX()
            y = self.getY()

    def draw(self, canvas):
        super().draw(canvas)

    # Switch the game controls
    # Used for powerDown
    def invertDirection(self):

        d = self.getDirections()

        if (d == ("Left", "Right")):
            self.setDirections(("Up", "Down"))
        else:
            self.setDirections(("Left", "Right"))

    # Increase Player Radius
    def enlargAnimation(self, newRadius, duration=0.0):

        if(self.getRadius() == newRadius): return

        def enlarge():
            while(self.getRadius() < newRadius):
                self.setRadius(self.getRadius() + .5)
                time.sleep(duration)

        # Run animation on a different thread, allows the animation to be timed
        animationThread = threading.Thread(
            target=enlarge,
            args=[])
        animationThread.daemon = True  # Kills the thread when its done
        animationThread.start()

    # Decrease Player Radius
    def minimizeAnimation(self, newRadius, duration=0.0):

        if(self.getRadius() == newRadius): return

        def minimize():
            while (self.getRadius() > newRadius):
                self.setRadius(self.getRadius() - .5)
                time.sleep(duration)

        # Run animation on a different thread, allows the animation to be timed
        animationThread = threading.Thread(
            target=minimize,
            args=[])
        animationThread.daemon = True  # Kills the thread when its done
        animationThread.start()

    def checkCollision(self, other):

        if(isinstance(other, GameObject) is False): return False

        # get center cords of both objects and calculate the distance
        obstacleX, obstacleY = other.getCenterCordinate()
        playerX, playerY = self.getCenterCordinate()
        dis = GameObject.getDistance(playerX, playerY, obstacleX, obstacleY)

        # If both game objects have collided and are the same Color
        if(dis <= self.getRadius()*2 and
          (self.getColor() == other.getColor() or str(other) == "power")):
            return True
        # return False

    # Getters and Setters

    def getDirections(self):
        return self.directions

    def getId(self):
        return self.id

    def getCenterX(self):
        return self.cX

    def getCenterY(self):
        return self.cY

    def setDirections(self, directions):
        self.directions = directions

class DirectionPad(GameObject):

    def __init__(self, color, radius, id, screenW, screenH):

        self.x0= screenW//2 - radius/2
        self.y0= screenH//2 - radius/2
        self.x1= screenW//2 + radius/2
        self.y1= screenH//2 + radius/2
        self.cordCopy = [self.x0, self.y0, self.x1, self.y1]
        self.id = id


        if (id == 1):
            speedX, speedY = GameObject.DEFAULT_SPEED, 0
        else:
            speedX, speedY = 0, GameObject.DEFAULT_SPEED

        super().__init__(self.x0,self.y0,radius,color, speedX, speedY)
        self.points = self.getPoints()

    # Return a list of points needed to create a rounded corner rectangle
    def getPoints(self):

        r = self.getRadius()
        x0, y0 = self.getTopLeftCord()
        x1, y1 = self.getBottomRigthCord()

        # Coordinate math retrieved from https://stackoverflow.com/questions
        # /44099594/how-to-make-a-tkinter-canvas-rectangle-with-rounded-corners
        points = [x0 + r, y0, x0 + r, y0, x1 - r, y0, x1 - r, y0, x1, y0,
                  x1, y0 + r, x1, y0 + r, x1, y1 - r, x1, y1 - r, x1, y1,
                  x1 - r, y1, x1 - r, y1, x0 + r, y1, x0 + r, y1, x0, y1,
                  x0, y1 - r, x0, y1 - r, x0, y0 + r, x0, y0 + r, x0, y0]

        return points

    def moveToDirection(self, direction):

        xSpeed = self.getSpeedX()
        ySpeed = self.getSpeedY()

        if (direction == "Left" or direction == "Up"):
            self.setSpeedX(-abs(xSpeed))
            self.setSpeedY(-abs(ySpeed))
        else:
            self.setSpeedX(abs(xSpeed))
            self.setSpeedY(abs(ySpeed))

        self.move()

    def move(self):

        def moveHelper(speed):

            if (speed < 0):
                x0, y0 = self.getTopLeftCord()
                x0 += self.getSpeedX()
                y0 += self.getSpeedY()
                self.setTopLeftCord(x0, y0)
            else:
                x1, y1 = self.getBottomRigthCord()
                x1 += self.getSpeedX()
                y1 += self.getSpeedY()
                self.setBottomRigthCord(x1, y1)

        if(self.id == 1):

            if (60.0 - self.getRadius()/2 <= self.x0 and
                    self.x1 <= 300.0 + self.getRadius()/2):

                moveHelper(self.speedX)
        else:

            if(200.0 - self.getRadius()/2 <= self.y0 and
                    self.y1 <= 440.0 + self.getRadius()/2):

                moveHelper(self.speedY)

    def moveToCenter(self):

        self.setSpeedX(abs(self.getSpeedX()))
        self.setSpeedY(abs(self.getSpeedY()))

        # moves both cords to the center
        while (self.x0 < self.cordCopy[0]):
            self.x0 += self.getSpeedX()

        while(self.x0 > self.cordCopy[0]):
            self.x0 -= self.getSpeedX()

        while (self.x1 < self.cordCopy[2]):
            self.x1 += self.getSpeedX()

        while(self.x1 > self.cordCopy[2]):
            self.x1 -= self.getSpeedX()

        # y
        while (self.y0 < self.cordCopy[1]):
            self.y0 += self.getSpeedY()

        while(self.y0 > self.cordCopy[1]):
            self.y0 -= self.getSpeedY()

        while (self.y1 < self.cordCopy[3]):
            self.y1 += self.getSpeedY()

        while(self.y1 > self.cordCopy[3]):
            self.y1 -= self.getSpeedY()


    def getTopLeftCord(self):
        return (self.x0, self.y0)

    def setTopLeftCord(self, x0, y0):
        self.x0 = x0
        self.y0 = y0

    def getBottomRigthCord(self):
        return (self.x1, self.y1)

    def setBottomRigthCord(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    # Draws a rounded corner rectangle
    def draw(self, canvas):

        points = self.getPoints()
        color = self.getColor()
        canvas.create_polygon(points, fill=color, smooth=True, width=0)