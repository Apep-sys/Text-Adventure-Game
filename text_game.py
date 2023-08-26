import text_adventure as adv_file
import game_py as game_file

player = adv_file.Player()
game = adv_file.Game()

def start():
    #message = game.narrator1()
    message = 'uwu'
    game_file.display_message(1, message)
    adv_file.time.sleep(2)
    player.place_choice = 'Murder Mystery'
    game_file.screen.fill(game_file.black)

    game_file.display_message(1, 'What is your name, endorsed guest?\n')
    player.name = game_file.get_player_input().title()
    game_file.screen.fill(game_file.black)

    game_file.display_message(1, 'And what room are you from?\n\n')
    choices = ['>Room 09', '>ayaya', '>kkk']
    game_file.display_message(2, choices)

    player.pclass = game_file.get_player_input().lower()
    game_file.screen.fill(game_file.black)
    player.creation(player.place_choice)
    game_file.display_message(1, player.intro)
    adv_file.time.sleep(1)

def room1():
    message = ('You enter the dimly lit hallway, caught between the safety of your room and the mysteries ahead.\n'
                'The air is still, carrying a hint of aged wood. The faded wallpaper peels, revealing the passage of time.\n'
                'To your left, a closed door leads to a balcony, teasing glimpses of the outside world. \n'
                'To your right, a slightly ajar door reveals a cramped closet, holding secrets within its limited space.\n'
                'Straight ahead, a closed door guards the elevator, its faint hum echoing through the corridor.\n'
                'You observe two items: a fuse, laying on a shelf, and a magnifying glass, somehow waiting for a firm hand to pick it up.\n'
                'Anticipation settles upon you as you stand in this hallway, ready to unlock the stories within each room.\n'
                'The adventure awaits, just beyond the threshold.\n')
    game_file.display_message(1, message)
    game_file.screen.fill(game_file.black)
    while player.check1 == False:
        if len(player.items1) > 0:
            message = ('What is your next move?\n\n'
                       '>Go to Rooms\n'
                       '>Pick up Items\n')
            game_file.display_message(1, message)
            player.action = game_file.get_player_input()
        else:
            message = ('What is your next move?\n\n'
                       '>Go to Rooms\n')
            game_file.display_message(1, message)
            player.action = game_file.get_player_input()



start()
game_file.screen.fill(game_file.black)
room1()
game_file.screen.fill(game_file.black)

game_file.pygame.display.update()
game_file.clock.tick(60)