# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

##################
## Comment/uncomment the relevant lines, depending on which version of Python you have
##################

# For Python 3.5:
#from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 

# For Python 3.6:
from ps2_verify_movement36 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.6


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = math.floor(width)
        self.height = math.floor(height)
        self.cleaned_tiles = []
        
        
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        cleaned_tile = (math.floor(pos.getX()),math.floor(pos.getY()))
        if cleaned_tile not in self.cleaned_tiles:
                self.cleaned_tiles.append(cleaned_tile)
        

    def isTileCleaned(self, m,n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        pos = (m,n)
        
        return pos in self.cleaned_tiles
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return len(self.cleaned_tiles)

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        pos = Position(random.randint(0,self.width), random.randint(0,self.height))
        while not(self.isPositionInRoom(pos)):
            pos = Position(random.randint(0,self.width), random.randint(0,self.height))
        return pos
            

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x = pos.getX()
        y = pos.getY()
        return (x < self.width and x >= 0 and y < self.height and y >= 0)




# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        angle = random.randint(0,359)
        self.direction = angle
        room.cleanTileAtPosition(self.position)
        
        

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
                 
        return self.direction
        

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position
        

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        raise NotImplementedError


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        d = self.getRobotDirection()
        p = self.getRobotPosition()
        s = self.speed
        r = self.room
        p1 = p.getNewPosition(d,s)
        while not(r.isPositionInRoom(p1)):
            d1 = random.randint(0,360)
            self.setRobotDirection(d1)
            p1 = p.getNewPosition(self.getRobotDirection(),s)
        self.setRobotPosition(p1)
        r.cleanTileAtPosition(self.getRobotPosition())
        

# Uncomment this line to see your implementation of StandardRobot in action!
##testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    tiles = width * height
    time_step_list = []
    while num_trials > 0:
        """time_steps is reset to 0 for each trial, trial starts with no clean tiles,
           ,no robots and no known number of time_steps"""
        time_steps = 0
        room = RectangularRoom(width,height)
        robots = {}
#        bots = []
        
#        anim = ps2_visualize.RobotVisualization(num_robots, width, height,1)
        robots = [robot_type(room, speed) for r in range(num_robots)]
#        for bot in robots:
#            bots.append(bot)
        while room.getNumCleanedTiles()/tiles < min_coverage:
            """continues code while percentage of cleaned tiles in terms of total tiles
                is less than min_coverage"""
#            anim.update(room, bots)
            for bot in robots:
                """for each robot, the robot moves to a new position and cleans it.
                Each robot's list of cleaned tiles is appended to the master list of
                cleaned tiles"""
#                pos = bot.getRobotPosition()
#                d = bot.getRobotDirection()
#                new = pos.getNewPosition(d,speed)
#                if not(room.isPositionInRoom(new)):
#                    time_steps += 1
                bot.updatePositionAndClean()
                
                
                
            """duplicate tiles from cleaned are removed"""    
            
            time_steps += 1
            """after all robots moved/cleaned a tile, time_step counter goes up by 1"""
            
           
        time_step_list.append(time_steps)
        """append num of time_steps for each trial to time_step_list"""
        
        num_trials -= 1
        
        
        """show that each trial is finished"""
#        anim.done()
    total = sum(time_step_list)
    
    """return average time_steps in time_step_list"""
        
       
    return total/len(time_step_list)   
# Uncomment this line to see how much your simulation takes on average
##print(runSimulation(1, 1.0, 10, 10, 0.75, 30, StandardRobot))


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        d = self.getRobotDirection()
        p = self.getRobotPosition()
        s = self.speed
        r = self.room
        d2 = random.randint(0,360)
        while d2 == d:
            d2 = random.randint(0,360)
        self.setRobotDirection(d2)
        p1 = p.getNewPosition(self.getRobotDirection(),s)
        while not(r.isPositionInRoom(p1)):
            d1 = random.randint(0,360)
            while d1 == d2:
                d1 = random.randint(0,360)
            self.setRobotDirection(d1)
            p1 = p.getNewPosition(self.getRobotDirection(),s)
        self.setRobotPosition(p1)
        r.cleanTileAtPosition(self.getRobotPosition())


num_robot_range = range(1, 11)
times1 = []
times2 = []
for num_robots in num_robot_range:
    print("Plotting", num_robots, "robots...")
    times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
    times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
pylab.plot(num_robot_range, times1)
pylab.plot(num_robot_range, times2)
pylab.title('Time It Takes Two Robots To Clean 80% Of Variously Shaped Rooms')
pylab.legend(('StandardRobot', 'RandomWalkRobot'))
pylab.xlabel('Number of Robots')
pylab.ylabel('Time steps')
pylab.show()

   

    
aspect_ratios = []
times1 = []
times2 = []
for width in [10, 20, 25, 50]:
    height = 300//width
    print("Plotting cleaning time for a room of width:", width, "by height:", height)
    aspect_ratios.append(float(width) / height)
    times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
    times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
pylab.plot(aspect_ratios, times1)
pylab.plot(aspect_ratios, times2)
pylab.title('Time It Takes Two Robots To Clean 80% Of Variously Shaped Rooms')
pylab.legend(('StandardRobot', 'RandomWalkRobot'))
pylab.xlabel('Aspect Ratio')
pylab.ylabel('Time steps')
pylab.show()




