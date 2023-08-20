import text_adventure as adv_file
import game_py as game_file

player = adv_file.Player()
game = adv_file.Game()

def start():
    message = game.narrator1()
    game_file.display_message(message)
    adv_file.time.sleep(2)
    player.place_choice = 'Murder Mystery'
    game_file.screen.fill(game_file.black)

    game_file.display_message('What is your name, endorsed guest?')
    player.name = game_file.get_player_input().title()
    print(player.name)
    adv_file.time.sleep(1)
    game_file.screen.fill(game_file.black)

    game_file.display_message('And what room are you from?\n\n'
                                    '>Room 09\n'
                                    '>Room 13\n'
                                    '>Room 256\n>').lower()
    player.pclass = game_file.get_player_input().lower()
    player.creation(player.place_choice)
    game_file.screen.fill(game_file.black)

    game_file.display_message(player.intro)
    adv_file.time.sleep(1)


start()
game_file.screen.fill(game_file.black)
game_file.pygame.display.update()
game_file.clock.tick(60)