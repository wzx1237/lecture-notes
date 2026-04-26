# Done by WANG,Zhi Xin. student ID: 21150652
# COMP1021 Music System

import turtle # Import the turtle module for drawing
import music  # Import the music module for playing music
import time   # Import the time module for time.sleep()
import random # Import the random module for randomizing music

# Initialize the music data
music_data = []


# A dictionary containing the menu settings
main_menu = {
    # menu key: (caption, position and size, colour)
    "load": ("Load Music", (-240, 90, 200, 120), "cyan"),
    "play": ("Play Music", (0, 90, 200, 120), "yellow"),
    "clear": ("Clear Music", (240, 90, 200, 120), "pink"),
    "instrument": ("Change Instrument", (-240, -70, 200, 120), "magenta"),
    "transpose": ("Transpose Music", (0, -70, 200, 120), "orange"),
    "speed": ("Adjust Speed", (240, -70, 200, 120), "red"),
    "special1": ("Special 1", (-180, -230, 320, 120), "light green"),
    "special2": ("Special 2", (180, -230, 320, 120), "light blue")
}


# This function draws a coloured box at (x, y) with a size of (w, h)
def drawBox(color, x, y, w, h):
    turtle.fillcolor(color)
    turtle.goto(x - w / 2, y - h / 2)
    turtle.down()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.goto(x, y)

    
# This function creates the menu on the turtle window
def drawMenu():
    turtle.hideturtle()
    turtle.up()
    turtle.width(4)

    turtle.tracer(False)    # Disable any turtle animation
    
    turtle.clear()

    # Write the title
    turtle.goto(0, 250)
    turtle.write("Python Music System", align="center", \
                 font=("Arial", 30, "bold"))

    # Draw the menu boxes
    for menu_info in main_menu.values():
        caption = menu_info[0]
        x, y, w, h = menu_info[1]
        color = menu_info[2]

        drawBox(color, x, y, w, h)

        turtle.goto(x, y - 10)
        turtle.write(caption, align="center", \
                     font=("Arial", 14, "bold"))

    turtle.tracer(True)    # Refresh the turtle window


# This function shows the music summary
def updateMusicSummary():
    text_turtle.up()
    text_turtle.hideturtle()

    text_turtle.clear()
    text_turtle.goto(0, 200)

    if len(music_data) == 0:
        # Music is empty
        summary = "Click on the 'Load Music' area to load a music file"
    else:
        # Number of notes
        summary = "No. of notes = " + str(len(music_data)) + ", "

        # Duration
        duration = 0
        for note in music_data:
            if note[0] + note[2] > duration:
                duration = note[0] + note[2]
        mins = int(duration / 60)
        secs = round(duration % 60, 2)
        summary = summary + "song duration = " + str(mins) + "m " + str(secs) + "s, "

        # Instrument
        summary = summary + "instrument = " + music.instrument_list[music.current_instrument]
        
    text_turtle.write(summary, align="center", font=("Arial", 14, "normal"))
    turtle.listen()


# This function loads some music into the music data list
def loadMusic():
    global music_data

    # Get the song list from the song folder
    song_list = music.getsonglist()
    song_menu = ""
    for i in range(len(song_list)):
        song_menu = song_menu + str(i) + ": " + song_list[i][0] + "\n"
    if song_menu == "":
        song_menu = "No music files available"
    
    # Ask the user for the music file
    filename = turtle.textinput("Music File", song_menu + \
                   "\nPlease give me a music file number or a file name:")
    if filename == None:
        return      # If the user enters nothing then stop this function now

    # Get the song for numeric input
    if filename.isnumeric():
        filename = song_list[int(filename)][1]

    # Open the file for reading
    file = open(filename, "r")

    # Reset the music data
    music_data = []

    # Read the data into the music list
    for line in file:
        # Read each line as a music note
        note = line.rstrip().split("\t")

        # Convert the data to the right data type
        note[0] = float(note[0])  # Time
        note[1] = int(note[1])    # Pitch
        note[2] = float(note[2])  # Duration

        # Add the note at the end of the music
        music_data.append(note)

    # Close the file
    file.close()

    # Update the music summary
    updateMusicSummary()


# This function plays the music
def playMusic():
    global music_data

    # Clear the music data in the music module
    music.clear()

    # Add the music notes
    for i in range(len(music_data)):
        # Show progress every 10 notes
        if i % 10 == 0:
            turtle.tracer(False)
            text_turtle.clear()
            text_turtle.write("Adding note " + str(i) + \
                              " of " + str(len(music_data)), \
                              align="center", font=("Arial", 14, "normal"))
            turtle.tracer(True)

        # Add the note
        note = music_data[i]
        music.addnote(note[0], note[1], note[2])

    # Update the music summary
    updateMusicSummary()

    # Play the music
    music.play()


# This function clear the cureent load music
def clearMusic():
    global music_data
    
    # Clear the current music data
    music_data = []

    # Update the music summary
    updateMusicSummary()


# This function returns the available instrument list
def getInstrumentList():
    # Get the available instrument list
    instruments = music.getavailableinstruments()

    # Build the instrument list
    instrument_list = ""
    for index in range(len(instruments)):
        instrument_list = instrument_list + str(instruments[index]) + " : " + \
                          music.instrument_list[instruments[index]] + "\n"
        if index > 9:
            instrument_list = instrument_list + "\n" + \
                              "...only the first 10 are shown...\n"
            break

    return instrument_list


# This function changes the instrument
def changeInstrument():
    # Get the instrument list
    message = getInstrumentList() + "\n" + \
              "Please enter the instrument number (0-127):"

    # Ask the user for the instrument number
    instrument = turtle.numinput("Change Instrument", message)

    #####
    #
    # TODO:  
    # - Convert the variable to an appropiate type
    instrument = int(instrument)
    # - Change the instrument appropriately
    music.setinstrument(instrument)
    #
    #####

    # Update the music summary
    updateMusicSummary()


# This function transposes the music pitch
def transpose():
    global music_data

    # Ask the user for the transposition number
    change = turtle.numinput("Transpose", "Please enter the transposition:")

    #####
    #
    # TODO:
    # - Convert the variable to an appropiate type
    change = int(change)
    # - Adjust the pitch of all notes appropriately
    for note in music_data:
        note[1]=note[1]+change
        note[1]=max(min(note[1],108),21)
    #
    #####
    
    # Update the music summary
    updateMusicSummary()


# This function adjusts the speed of the music
def adjustSpeed():
    global music_data

    # Ask the user for the speed change
    speedchange = turtle.numinput("Adjust Speed", \
                  "Please enter the new speed, in percentage:")

    #####
    #
    # TODO:
    # - Convert the variable to an appropiate type
    speedchange = int(speedchange)
    # - Adjust the speed of all notes appropriately
    for note in music_data:
        note[2]=note[2]*(100/speedchange)
        note[0]=note[0]*(100/speedchange)
    #
    #####

    # Update the music summary
    updateMusicSummary()


# This function will repeat the music multiple times
def special1():
    global music_data

    # Ask the user for number of times to repeat
    repeat_count = turtle.numinput("Repeat Music", \
                   "Please enter the number of times to repeat:")

    #####
    #
    # TODO:
    # - Convert the variable to an appropiate type
    repeat_count = int(repeat_count)
    # - Repeat the music the given number of times
    mymusic=[]
    for music_index in range(repeat_count):
        for i in range(len(music_data)):
            note=music_data[i]
            mid=note[0]# in case we change the music_data
            note[0]=music_data[i][0]+music_index*(music_data[-1][0]+music_data[-1][2])
            new_note=[note[0],note[1],note[2]]
            mymusic.append(new_note)
            note[0]=mid# this line is very important!
    music_data=mymusic
    #
    #####

    # Update the music summary
    updateMusicSummary()


# This function makes some random music based on the existing music
def special2():
    global music_data

    #####
    #
    # TODO:
    # - Use either approach to randomize the pitch numbers of the music
    pitch=[]
    for i in range(len(music_data)):
        pitch.append(music_data[i][1])
    random.shuffle(pitch)
    for i in range(len(music_data)):
        music_data[i][1]=pitch[i]
    #
    #####

    # Update the music summary
    updateMusicSummary()


# This function handles the screen click and the menu selection
def handleMenu(x, y):
    # Get the menu item that the user has clicked on
    selected_key = None
    for key, menu_info in main_menu.items():
        menux, menuy, menuw, menuh = menu_info[1]
        if x > menux - menuw / 2 and x < menux + menuw / 2 and \
           y > menuy - menuh / 2 and y < menuy + menuh / 2:
            selected_key = key

    # Run the corresponding functions for each menu item
    if selected_key == "load":
        loadMusic()
    elif selected_key == "play":
        playMusic()
    elif selected_key == "clear":
        clearMusic()
    elif selected_key == "instrument":
        changeInstrument()
    elif selected_key == "transpose":
        transpose()
    elif selected_key == "speed":
        adjustSpeed()
    elif selected_key == "special1":
        special1()
    elif selected_key == "special2":
        special2()


# This function prints the current music data in the output
def printMusicData():
    global music_data

    print("Current music data:")
    for note in music_data:
        print(note[0], note[1], note[2], sep=", ")
    print("")


# Set up the turtle module
turtle.setup(800, 700)
turtle.speed(0)

# Show the menu
drawMenu()

# Create a new turtle to show music summary
text_turtle = turtle.Turtle()

# Update the music summary
updateMusicSummary()

# Set up the screen click event
turtle.onscreenclick(handleMenu)

# Set up the print key event
turtle.onkeypress(printMusicData, "p")
turtle.listen()
turtle.done()

# Kill any currently playing sounds and remove the sound
music.stop(True)
