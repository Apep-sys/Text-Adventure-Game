""" Module for storing the functions for handling music, message displays, image displays, player input,
    controlled execution of the individual level functions and initialization of the game

Functions:
    split_text(text, font, max_width): Function for splitting text, to make it able to fit in the game window
    display_message(value, message, coordinates=(50, 70)): Function for displaying messages, at given coordinates
    get_player_input(): Function for taking the player's input
    play_music(music_file, loops=0, fade=0, queue='', start=0): Function for playing music and customizing the songs
    check_state(player, function_list, param=None): Function for controlled execution of game level functions
"""

import sys
import pygame
import time
import random
from pygame import mixer

mixer.init()

# Loading the images for the levels
level1_img = pygame.image.load('Images\Level1_new.jpg')
level2_img_red = pygame.image.load('Images\Level2_Red.jpg')
level2_img_black = pygame.image.load('Images\Level2_Black.jpg')
level2_img_green = pygame.image.load('Images\Level2_Green.jpg')
level2_img_wardrobe = pygame.image.load('Images\Level2_Wardrobe.jpg')
level2_img_crystal = pygame.image.load('Images\Level2_Crystal.jpg')
level2_img_table = pygame.image.load('Images\Level2_Table.jpg')
level2_img_b_room = pygame.image.load('Images\Level2_B_room.jpg')
level2_img_tarot = pygame.image.load('Images\Level2_Tarot.jpg')
level2_img_mark = pygame.image.load('Images\Level2_Mark.jpg')
level3_img_lounge = pygame.image.load('Images\Level3_Lounge.jpg')
level3_img_letter = pygame.image.load('Images\Level3_Letter.jpg')
level4_img_guard = pygame.image.load('Images\Level4_Guard.jpg')
level4_img_party1 = pygame.image.load('Images\Level4_Party1.jpg')
level4_img_party2 = pygame.image.load('Images\Level4_Party2.jpg')
level4_img_shadow = pygame.image.load('Images\Level4_Shadow.jpg')
level4_img_evil = pygame.image.load('Images\Level4_Evil.jpg')
level4_img_good = pygame.image.load('Images\Level4_Good.jpg')
level4_img_true = pygame.image.load('Images\Level4_True.jpg')
level4_img_dead = pygame.image.load('Images\Level4_Dead.jpg')

# Function for splitting the text, to make it fit within the window size and have the letters go to the next line
# Upon reaching the window's boundaries
def split_text(text, font, max_width):
    """ Function for splitting the text, to make it fit within the window size and have the letters go to the next line
         Upon reaching the window's boundaries

    Args:
        text (str): Takes the text to be split
        font (str): Takes the used font for the text to be split
        max_width (int): Takes the amount of width accepted for text

    Returns:
        lines: A list of lines separated by space
    """

    words = text.split()
    lines = []
    current_line = ''

    for word in words:
        test_line = current_line + word + ' '
        test_width, _ = font.size(test_line)

        if test_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word + ' '

    lines.append(current_line)
    return lines


# Function for displaying the message given letter-by-letter, with the respective colours, and for temporarily increasing
# scrolling speed
def display_message(value, message, coordinates=(50, 70)):
    """ Function for displaying the message to the screen, letter by letter

        Args:
            value (int): Takes either 1 or 2, displaying a message as a paragraph for 2 and as new lines for 1
            message (str): Takes the message that is to be displayed
            coordinates (int, optional): Takes the coordinates of where to display the message
                        (default is (50, 70))

        Returns:
            displayed_text (str): The text to be displayed, formed letter by letter every 0.08 seconds
        """
    displayed_text = ''
    index = 0
    lines = []
    time_delayed = 0.08

    if value == 1:
        x_position, y_position = coordinates

        while index < len(message):
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        time_delayed = 0.01

                elif event.type == pygame.KEYUP:
                    time_delayed = 0.08

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            displayed_text += message[index]
            index += 1

            # Update the lines based on displayed_text
            lines = split_text(displayed_text, font, 1000 - 2 * 50)

            if y_position != 50:
                y_position = coordinates[1]
            else:
                y_position = 50
            for line in lines:
                text_surface = font.render(line, True, color_text)
                screen.blit(text_surface, (x_position, y_position))
                y_position += font.get_height() # Move to the next line

            pygame.display.update()
            time.sleep(time_delayed)  # Adjust the delay time as needed

    elif value == 2:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    time_delayed = 0.2

            elif event.type == pygame.KEYUP:
                time_delayed = 0.08

            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        x_position, y_position = coordinates
        for word in "".join(message):
            for letter in word:
                if letter == ">":       # If the letter is >, then the y position is increased and the word goes on the next line.
                    y_position += font.get_height() + 10
                    x_position = 50
                text_surface = font.render(letter, True, color_choices)
                screen.blit(text_surface, (x_position, y_position))
                size = pygame.font.Font.size(font, "".join(message))
                x_position += text_surface.get_width()   # To avoid adding the letters on the same coordinate of x, we increase it.

                pygame.display.update()
                time.sleep(time_delayed)

    return displayed_text


# Function for taking the input of the player in its given rectangle and returning said input
def get_player_input():
    """ Function for taking the input of the player in its given rectangle and returning said input

        Args:
            No arguments

        Returns:
            player_input: Returns the text of the player's input
        """
    player_input = '> '
    input_rect = pygame.Rect(50, 500, 140, 32)
    color = color_danger
    waiting = True

    while waiting:

        # General event check for quitting the game and typing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                # If the Enter key is pressed, the 'waiting' value is made False so the next iteration is cancelled
                # And the arrow symbol '>' that is shown when giving input with the get_player_input function
                # gets replaced with an empty string, for ease of usage and manipulation of the player's input
                if event.key == pygame.K_RETURN:
                    waiting = False
                    player_input = player_input.replace('> ', '')

                # Pressing backspace for deleting a letter
                elif event.key == pygame.K_BACKSPACE:
                    player_input = player_input[:-1]

                # The letters are added to the input and final message as they are typed
                else:
                    player_input += event.unicode

        pygame.draw.rect(screen, color, input_rect)
        input_surface = font.render(player_input, True, black)
        input_rect_new = pygame.Surface((input_rect.width, input_rect.height))
        input_rect_new.fill(color)
        input_rect_new.blit(input_surface, (5, 5))
        screen.blit(input_rect_new, (input_rect.left, input_rect.top))
        input_rect.w = input_surface.get_width() + 10
        pygame.display.update()

    return player_input


# Function for playing music, allowing music queueing and usage of parameters such as loops and fade
def play_music(music_file, loops=0, fade=0, queue='', start=0):
    """ Function for playing music, allowing music queueing and usage of parameters such as loops and fade
        Works best with mp3 files, because of the usage of the keyword arguments

            Args:
                music_file (str): The sound/music file to be played
                loops (int, optional): How many times to loop a sound/music file
                    (default is 0)
                fade (int, optional): After how many seconds the sound file will start fading out
                    (default is 0)
                queue (str, optional): The next sound/music file to be played after the music_file arg
                    (default is '', no file)
                start (int, optional): The position in seconds from where the sound file should begin playing
                    (default is 0)

            Returns:
                Nothing
    """
    mixer.music.load(music_file)

    # It will only queue music in the case the queue parameter is given at the function's call
    if queue:
        mixer.music.queue(queue)

    mixer.music.play(loops, fade, start)


# Function for calling the room function and checking the player state for dead or alive
def check_state(player, function_list, param=None):
    """ Function for executing the room function and checking the player state for dead or alive

                Args:
                    player (object): The object whose attributes we're checking
                    function_list (list): The list of functions which we will consecutively call
                    param (optional): Parameter for bypassing the third room function call
                        (default is None)

                Returns:
                    False, in case the state attribute of the player object is 'dead'
        """

    for room in function_list:

        if player.state == 'alive' and room == function_list[3]:

            # If the passing variable of the player object is true, it passes the execution of the third room
            if player.passing is True:
                screen.fill(black)
                pass

            else:

                # If the check_state function is given the temp_inventory argument, it will enter this case:
                # Case if the player has died and stumbled upon their body
                # This case will only play when the function_list reaches the dead_room while iterating
                if param and room == function_list[2]:

                    # Chance of the dead room appearing
                    dead_room_chance = random.randint(0, 1)
                    if dead_room_chance:

                        # If the result is 1, it will play the dead_room function
                        room(param)

                    else:
                        # If the result is 0, it will just pass and go to the next room in line
                        pass

                    # To prevent the room always executing, we give back to param the value None
                    param = None

                # Generally, this function just executes the room/level functions
                room()
                screen.fill(black)

        else:
            return False


# Initialization of the game, game title, window size, fonts, and colours
pygame.init()

screen = pygame.display.set_mode((1000, 667))
pygame.display.set_caption('Text Adventure with Python')
font = pygame.font.Font("freesansbold.ttf", 22)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
color_text = (204, 119, 34)
color_choices = (255, 191, 0)
color_danger = (255, 87, 51)

