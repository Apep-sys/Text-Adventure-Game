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

def split_text(text, font, max_width):
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


def display_message(value, message, coordinates=(50, 70)):
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
                time.sleep(time_delayed)    #pygame.wait

    return displayed_text

def get_player_input():
    player_input = '> '
    input_rect = pygame.Rect(50, 500, 140, 32)
    color = color_danger#pygame.Color('lightskyblue3')
    waiting = True

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                    player_input = player_input.replace('> ', '')
                elif event.key == pygame.K_BACKSPACE:
                    player_input = player_input[:-1]
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

def play_music(music_file, loops=0, fade=0, queue='', start=0):
    mixer.music.load(music_file)
    if queue:
        mixer.music.queue(queue)
    mixer.music.play(loops, fade, start)


# Function for executing the room function and checking the player state for dead or alive
def check_state(player, function_list, param=None):
    for room in function_list:

        if player.state == 'alive':

            if player.passing is True:
                screen.fill(black)
                pass

            else:

                # If the check_state function is given the temp_inventory argument, it will enter this case:
                # Case if the player has died and stumbled upon their body
                if param:

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

                room()
                screen.fill(black)

        else:
            return False



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

