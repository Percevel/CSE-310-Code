from ast import Global
from asyncio.windows_events import NULL
from sys import maxsize
import arcade

SPRITE_SCALING = 1

SCREEN_WIDTH = 380
SCREEN_HEIGHT = 380
SCREEN_TITLE = "Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 20

global MOVED
global MAZE
global PLAYERX
global PLAYERZ
global KEY
global EMPTYVIS
global VIS
EMPTYVIS = [['0' for x in range(20)] for y in range(20)]
VIS = EMPTYVIS
KEY = False
MOVED = True


# A single node of a singly linked list
class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):  
    self.head = None
  
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

class Player(arcade.Sprite):

    def update(self):
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class Mapper():
    def __init__(self) -> None:
        lister = []
        file1 = open('mazeMaps/maze1.txt','r')
        Lines = file1.readlines()
        for line in Lines:
            lister.append(line.split(','))
        MAZE.insert(lister)
        file1.close()

        lister = []
        file1 = open('mazeMaps/maze2.txt','r')
        Lines = file1.readlines()
        for line in Lines:
            lister.append(line.split(','))
        MAZE.insert(lister)
        file1.close()

        lister =[]
        file1 = open('mazeMaps/maze3.txt','r')
        Lines = file1.readlines()
        for line in Lines:
            lister.append(line.split(','))
        MAZE.insert(lister)
        file1.close()

        global MAZEDATA 
        MAZEDATA = MAZE.head
    pass

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(width, height, title)

        # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None

        # Set the background color
        arcade.set_background_color(arcade.color.WHITE)

    def drawMaze(self):
            y = 0
            for line in MAZEDATA.data:
                x = 0
                for cell in line:
                    if cell.strip() == '1':
                        arcade.draw_rectangle_filled((x*20+10),380-(y*20+10),20, 20, arcade.color.GREEN)
                    elif cell.strip() == "3" and KEY == False:
                        arcade.draw_rectangle_filled((x*20+10),380-(y*20+10),20, 20, arcade.color.YELLOW)
                    elif cell.strip() == "4":
                        arcade.draw_rectangle_filled((x*20+10),380-(y*20+10),20, 20, arcade.color.RED)
                    x += 1
                y += 1

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player("Maze_explorer.png", SPRITE_SCALING)
        self.player_sprite.center_x = 10
        self.player_sprite.center_y = 350
        self.PLAYERX = 0
        self.PLAYERY = 1
        self.player_list.append(self.player_sprite)

        self.changevis()

        

    def changeLev(self):
        global MAZEDATA
        
        MAZEDATA = MAZEDATA.next
        y = 0
        for line in MAZEDATA.data:
            x = 0
            for cell in line:
                if cell.strip() == '2':
                    print("found!")
                    self.player_sprite.center_x = (x*20+10)
                    self.player_sprite.center_y = 380-(y*20+10)
                    self.PLAYERX = x
                    self.PLAYERY = y
                    print(f'{self.player_sprite.center_x},{self.player_sprite.center_y},{self.PLAYERX},{self.PLAYERY}')
                x += 1
            y += 1
        self.changevis()

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw all the sprites.
        self.player_list.draw()

        self.drawMaze()

        self.visibility()

    def on_update(self, delta_time):
        """ Movement and game logic """
        global MAZEDATA

        # Move the player
        self.player_list.update()
        self.player_sprite.change_y = 0
        self.player_sprite.change_x = 0

        if MAZEDATA.data[self.PLAYERY][self.PLAYERX].strip() == '3':
            self.KEY = True
        if MAZEDATA.data[self.PLAYERY][self.PLAYERX].strip() == '4' and self.KEY == True:
            self.changeLev()

    def changevis(self):
        global MAZEDATA
        global PLAYERY
        global PLAYERX
        global VIS
        global EMPTYVIS
        VIS = EMPTYVIS
        curry = self.PLAYERY
        currx = self.PLAYERX

        y = 0
        for line in MAZEDATA.data:
            x = 0
            for cell in line:
                if cell != '5':
                    VIS[y][x] = MAZEDATA.data[y][x]
                x += 1
            y += 1

        VIS[self.PLAYERY][self.PLAYERX] = '5'
        VIS[self.PLAYERY - 1][self.PLAYERX] = '5'
        VIS[self.PLAYERY + 1][self.PLAYERX] = '5'
        VIS[self.PLAYERY][self.PLAYERX - 1] = '5'
        VIS[self.PLAYERY][self.PLAYERX + 1] = '5'

        while MAZEDATA.data[curry - 1][currx].strip() == '0':
            VIS[curry - 2][currx] = '5'
            VIS[curry - 1][currx-1] = '5'
            VIS[curry - 1][currx+1] = '5'
            curry -= 1
        curry = self.PLAYERY
        currx = self.PLAYERX
        while MAZEDATA.data[curry + 1][currx].strip() == '0':
            VIS[curry + 2][currx] = '5'
            VIS[curry + 1][currx-1] = '5'
            VIS[curry + 1][currx+1] = '5'
            curry += 1
        curry = self.PLAYERY
        currx = self.PLAYERX
        while MAZEDATA.data[curry][currx - 1].strip() == '0':
            VIS[curry][currx - 2] = '5'
            VIS[curry + 1][currx-1] = '5'
            VIS[curry - 1][currx - 1] = '5'
            currx -= 1
        curry = self.PLAYERY
        currx = self.PLAYERX
        while MAZEDATA.data[curry][currx + 1].strip() == '0':
            VIS[curry][currx+ 2] = '5'
            VIS[curry + 1][currx+1] = '5'
            VIS[curry - 1][currx + 1] = '5'
            currx += 1

    def visibility(self):
        global VIS

        y = 0
        for line in VIS:
            x = 0
            for cell in line:
                if cell != '5':
                    arcade.draw_rectangle_filled((x*20+10),380-(y*20+10),20, 20, arcade.color.BLACK)
                x += 1
            y += 1

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """
        if MOVED:
            self.MOVED = False

            # If the player presses a key, update the speed
            if key == arcade.key.UP and MAZEDATA.data[self.PLAYERY - 1][self.PLAYERX].strip() != '1':
                self.player_sprite.change_y = MOVEMENT_SPEED
                self.PLAYERY -= 1
                self.changevis()
                return
            elif key == arcade.key.DOWN and MAZEDATA.data[self.PLAYERY + 1][self.PLAYERX].strip() != '1':
                self.player_sprite.change_y = -MOVEMENT_SPEED
                self.PLAYERY += 1
                self.changevis()
                return
            elif key == arcade.key.LEFT and MAZEDATA.data[self.PLAYERY][self.PLAYERX - 1].strip() != '1':
                self.player_sprite.change_x = -MOVEMENT_SPEED
                self.PLAYERX -= 1
                self.changevis()
                return
            elif key == arcade.key.RIGHT and MAZEDATA.data[self.PLAYERY][self.PLAYERX + 1].strip() != '1':
                self.player_sprite.change_x = MOVEMENT_SPEED
                self.PLAYERX += 1
                self.changevis()
                return

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        # If a player releases a key, zero out the speed.
        # This doesn't work well if multiple keys are pressed.
        # Use 'better move by keyboard' example if you need to
        # handle this.
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.MOVED = True
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.MOVED = True

def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    MAZE = LinkedList()
    Mapper()
    main()