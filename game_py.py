import sys
import pygame
import time


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


def display_message(message):
    displayed_text = ''
    index = 0
    lines = []

    while index < len(message):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        displayed_text += message[index]
        index += 1

        # Update the lines based on displayed_text
        lines = split_text(displayed_text, font, 1000 - 2 * 50)

        # Display wrapped text
        y_position = 50
        for line in lines:
            text_surface = font.render(line, True, white)
            screen.blit(text_surface, (50, y_position))
            y_position += font.get_height()  # Move to the next line

        pygame.display.update()
        time.sleep(0.08)  # Adjust the delay time as needed
    return displayed_text


def get_player_input():
    player_input = '> '
    input_rect = pygame.Rect(50, 500, 140, 32)
    color = pygame.Color('lightskyblue3')
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
        input_surface = font.render(player_input, True, white)
        input_rect_new = pygame.Surface((input_rect.width, input_rect.height))
        input_rect_new.fill(color)
        input_rect_new.blit(input_surface, (5, 5))
        screen.blit(input_rect_new, (input_rect.left, input_rect.top))
        input_rect.w = input_surface.get_width() + 10
        pygame.display.update()

    return player_input


pygame.init()

screen = pygame.display.set_mode((1000, 667))
pygame.display.set_caption('Text Adventure with Python')
font = pygame.font.Font("freesansbold.ttf", 22)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)

'''user_text = '>'
input_rect = pygame.Rect(50, 500, 140, 32)
color = pygame.Color('lightskyblue3')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                user_text = '>'
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
    screen.fill(black)
    pygame.draw.rect(screen, color, input_rect, 2)
    
    text = "This is a long text that needs to be wrapped to the next line when it exceeds the window's boundaries."
    max_line_width = 1000 - 2 * 50
    lines = split_text(text, font, max_line_width)
    display_message(lines)
    
    text_surface = font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    input_rect.w = text_surface.get_width() + 10'''
if __name__ == '__main__':
    while True:
        text = 'Test message'
        position = (50, 50)
        #lines = split_text(text, font, 1000 - 2 * 50)
        message_displayed = display_message(text)
        user_answer = get_player_input()

        screen.fill(black)
        pygame.display.update()
        clock.tick(60)
