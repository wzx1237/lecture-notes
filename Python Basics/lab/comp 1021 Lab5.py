# Done by WANG, Zhi Xin. Student ID: 21150652
"""

Lava Game

"""


import turtle
import time

# This is the map of the maze:
#   0 means nothing there
#   1 means wall 
#   2 means gold
#   3 means lava (there is no lava in the map at the start)

# Example map 1 

map = [
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 1, 1],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
total_rows = 9 # How many rows in the map 
total_cols = 9 # How many columns in the map 
player_row = 7 # This is the (start) row of the player, the index number
player_col = 6 # This is the (start) column of the player, the index number
target_gold_coins = 4 # How many gold coins the player needs to get
quantity_of_lava_cells_to_add_each_time = 4 # How many lava cells added each time


# Functions

def show_instructions():
    turtle.up()
    turtle.goto(total_cols/2, total_rows/2) # Go to the middle of the window
    turtle.down()
    turtle.color("blue")
    message = "Get the gold!\n\n"
    message = message + "You are a bird (blue square)\n"
    message = message + "You love shiny gold!\n"
    message = message + "Use the arrow keys to move around\n"
    message = message + "(up/ down/ left/ right)\n"
    message = message + "The room is flooding with lava (red squares)!\n"
    message = message + "Don't touch the lava!\n\n"
    message = message + str(quantity_of_lava_cells_to_add_each_time) 
    message = message + " cells of lava will be added\n"
    message = message + "each time you press a key\n\n"
    message = message + "You need to collect "
    message = message + str(target_gold_coins)
    message = message + " gold coins (yellow squares)\n"
    turtle.write(message, font=("Verdana", 20, "bold"), align="center")
    time.sleep(6) # Wait for a few seconds so the player can see the message
    turtle.clear() # Clear everything that the turtle has drawn so far
    
def show_success_message():   
    turtle.up()
    turtle.goto(total_cols/2, total_rows/2) # Go to the middle of the window
    turtle.down
    turtle.color("black")
    message = "You got the " + str(target_gold_coins) + " gold coins!"
    turtle.write(message, font=("Verdana", 40, "bold"), align="center")

def show_failure_message():   
    turtle.up()
    turtle.goto(total_cols/2, total_rows/2) # Go to the middle of the window
    turtle.down
    turtle.color("black")
    message = "You are dead!"
    turtle.write(message, font=("Verdana", 60, "bold"), align="center")

def draw_one_square(row, col, square_colour):
    # Temporarily stop updating the display
    turtle.tracer(False) 
    
    # Now draw a square
    for _ in range(4):
        turtle.forward(1)
        turtle.left(90)
    # (but it won't be visible until turtle.tracer(True) )
    turtle.up() # Take the pen off the page
    
    # Start at the bottom left corner of the square
    turtle.goto( col, row )
    turtle.down() # Put the pen down on the page
    # Set the fill colour and pen colour
    turtle.color(square_colour) 
    
    # Draw a filled square
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(1) # Use '1' because of the new coordinate ranges 
        turtle.left(90)
    turtle.end_fill()
    
    # Suddenly show everything drawn after turtle.tracer(False) 
    turtle.tracer(True) 

def add_lava():
    global map, game_being_played, lava_front_row, lava_front_col
    
    if game_being_played:
        for i in range(quantity_of_lava_cells_to_add_each_time):
            map[lava_front_row][lava_front_col] = 3 # Put lava in this cell
            
            # Check if the newly added lava has touched the player 
            if lava_front_row == player_row and lava_front_col == player_col: 
                game_being_played = False
                show_failure_message()
            else:
                draw_one_square(lava_front_row, lava_front_col, lava_colour) # Draw the lava cell

            lava_front_col = lava_front_col - 1 # Next lava will be the left square
            if lava_front_col < 0: # But maybe it's too far on the left (off the side)
               lava_front_row = lava_front_row - 1 # If so, move one row up
               lava_front_col = total_cols - 1 # And move to rightmost column
                   
def draw_map():
    for y in range(total_rows):
        for x in range(total_cols):
            if map[y][x] == 0:  # 0 = nothing is here
                draw_one_square(y, x, empty_space_colour)
            elif map[y][x] == 1:  # 1 = wall is here
                draw_one_square(y, x, wall_colour)
            elif map[y][x] == 2:  # 2 = gold is here
                draw_one_square(y, x, gold_colour)
            # No need to draw lava here
            # because there's no lava at the start of the game
    
    
def check_possible_movement(row, col):


    # if col is too far to the left, return False         
    if col<0:
        return False
    # if col is too far to the right, return False        
    elif col>total_cols-1:
        return False
    # if row is too far up, return False
    elif row<0:
        return False
    # if row is too far down, return False
    elif row>total_rows-1:
        return False
    # if the position (row, col) is a wall, return False         
    elif map[row][col]==1:
        return False
    # if all the above checks pass, return True
    else:
        return True
    
def handle_if_lava(row, col):
    global game_being_played
    
    if game_being_played:
        
        if map[row][col] == 3: # 3 is lava
            game_being_played = False
            show_failure_message()


def handle_if_gold(row, col):
    global map, player_gold_coins, game_being_played
    
    if game_being_played:

        print("About to check for and handle gold")

        # if (row, col) contains gold (the value 2)
        if  map[row][col]==2:
        #    put a zero in that cell, because that gold is now taken by the player
            map[row][col]==0
        #    increase the number stored in player_gold_coins by 1
            player_gold_coins=player_gold_coins+1
        #    print how many target_gold_coins gold coins the player now has
            print(player_gold_coins)
        #    if the player now has target_gold_coins gold coins:
            if player_gold_coins==target_gold_coins:
        #        set game_being_played to False
                game_being_played=False
        #        show_success_message()
                show_success_message()

        
def do_primary_game_logic_with_movement(row_offset, col_offset):
    global player_row, player_col
        
    # Remember current player position before possibly changing it
    player_row_before_possible_change=player_row
    player_col_before_possible_change=player_col
    
    if check_possible_movement(player_row + row_offset, player_col + col_offset): # If can move
        player_row = player_row + row_offset
        player_col = player_col + col_offset

    if player_row != player_row_before_possible_change or \
       player_col != player_col_before_possible_change: # If player row or column (or both) has moved
        draw_one_square(player_row_before_possible_change, player_col_before_possible_change, empty_space_colour) # Old position
        draw_one_square(player_row, player_col, player_colour) # New position
        handle_if_gold(player_row, player_col) 
        handle_if_lava(player_row, player_col)

    add_lava() # Add lava (add lava even if the player doesn't actually move) 

def start_handling_key_presses():
    # After executing this function, it means that
    # from now onwards pressing the keys will work
    turtle.onkeypress(go_left, "Left") # Handle left arrow key
    turtle.onkeypress(go_right, "Right") # Handle right arrow key
    turtle.onkeypress(go_up, "Up") # Handle up arrow key
    turtle.onkeypress(go_down, "Down") # Handle down arrow key

def stop_handling_key_presses():
    # After executing this function, it means that
    # from now onwards pressing the keys will do nothing
    turtle.onkeypress(None, "Left") # Disable left arrow key action
    turtle.onkeypress(None, "Right") # Disable right arrow key action
    turtle.onkeypress(None, "Up") # Disable up arrow key action
    turtle.onkeypress(None, "Down") # Disable down arrow key action

def go_left():
    print("go_left() is being executed") # Useful message
    if game_being_played:
        stop_handling_key_presses()
        do_primary_game_logic_with_movement(0, -1)
        start_handling_key_presses()

def go_right():
    print("go_right() is being executed") # Useful message
    if game_being_played:
        stop_handling_key_presses()
        do_primary_game_logic_with_movement(0, 1)
        start_handling_key_presses()

def go_up():
    print("go_up() is being executed") # Useful message
    if game_being_played:
        stop_handling_key_presses()
        do_primary_game_logic_with_movement(-1, 0)
        start_handling_key_presses()
    
def go_down():
    print("go_down() is being executed") # Useful message
    if game_being_played:
        stop_handling_key_presses()
        do_primary_game_logic_with_movement(1, 0)
        start_handling_key_presses()
        
######################################
# This is the main part of the program.
# You don't need to change it.

# Colours used in the game
empty_space_colour="white"
player_colour="blue"
wall_colour="darkgrey"
gold_colour="gold"
lava_colour="firebrick1"

# Number of gold coins that the player currently has
player_gold_coins = 0

# The lava will start in the bottom right corner
lava_front_row=total_rows-1 
lava_front_col=total_cols-1 

# Make the x axis and y axis column ranges easy to use
turtle.setworldcoordinates(0, total_rows, total_cols, 0)

turtle.listen() # Make sure key presses go to the turtle window

turtle.hideturtle() # No need to see the turtle 
turtle.speed(0) # Make the turtle fast, for quick drawing

show_instructions() # Show text instructions

draw_map() # Show the whole map
draw_one_square(player_row, player_col, player_colour) # Draw the player

start_handling_key_presses() # Now the player can press the arrow keys



# Everything is ready, now the game begins
# This variable says whether the game is currently being played
# When the game is being played, it is True
# When the game has finished, it is False
game_being_played=True 

turtle.done() # This should be the last line of the program

