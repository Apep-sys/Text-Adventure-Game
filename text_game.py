import time

import text_adventure as adv_file
import game_py as game_file

player = adv_file.Player()
game = adv_file.Game()

def start():
    message = game.narrator1()
    #message = 'uwu'
    game_file.display_message(1, message)
    adv_file.time.sleep(2)
    player.place_choice = 'Murder Mystery'
    game_file.screen.fill(game_file.black)

    game_file.display_message(1, 'What is your name, endorsed guest?\n')
    player.name = game_file.get_player_input().title()
    game_file.screen.fill(game_file.black)

    game_file.display_message(1, 'And what room are you from?\n\n')
    choices = ['>Room 09', '>Room 13', '>Room 256']
    game_file.display_message(2, choices)

    player.pclass = game_file.get_player_input().lower()
    game_file.screen.fill(game_file.black)

    player.creation(player.place_choice)
    game_file.display_message(1, player.intro)


def room1():
    #message = 'uwu'
    message = ('You enter the dimly lit hallway, caught between the safety of your room and the mysteries ahead.\n'
                'The air is still, carrying a hint of aged wood. The faded wallpaper peels, revealing the passage of time.\n'
                'To your left, a closed door leads to a balcony, teasing glimpses of the outside world. \n'
                'To your right, a slightly ajar door reveals a cramped closet, holding secrets within its limited space.\n'
                'Straight ahead, a closed door guards the elevator, its faint hum echoing through the corridor.\n'
                'You observe two items: a fuse, laying on a shelf, and a magnifying glass, somehow waiting for a firm hand to pick it up.\n'
                'Anticipation settles upon you as you stand in this hallway, ready to unlock the stories within each room.\n'
                'The adventure awaits, just beyond the threshold.\n')
    game_file.display_message(1, message)
    time.sleep(2)
    game_file.screen.fill(game_file.black)

    while player.check1 == False:
        if len(player.items1) > 0:
            game_file.display_message(1, 'What is your next move?')
            choices = ['>Go to rooms', '>Pick up items']
            game_file.display_message(2, choices)
            player.action = game_file.get_player_input()
            game_file.screen.fill(game_file.black)

        else:
            game_file.display_message(1, 'What is your next move?')
            choices = ['>Go to rooms']
            game_file.display_message(2, choices)
            player.action = game_file.get_player_input()
            game_file.screen.fill(game_file.black)

        if player.action.lower() == 'pick up items' and len(player.items1) > 0:
            message = ('Which item do you pick up?')
            game_file.display_message(1, message)
            choices = []
            for i in player.items1:
                choices.append('>' + i)
            game_file.display_message(2, choices)
            player.action = game_file.get_player_input()
            game_file.screen.fill(game_file.black)

            if player.action.lower() == 'magnifying glass':
                message = ('You pick up a magnifying glass. Hopefully, it will be useful in the way that you think.\n')
                game_file.display_message(1, message)
                player.inventory.append('Magnifying Glass')
                player.items1.remove('Magnifying Glass')
                game_file.screen.fill(game_file.black)
                continue

            elif player.action.lower() == 'fuse':
                message = ('You picked up a fuse. Someone might miss it.\n')
                game_file.display_message(1, message)
                player.inventory.append('Fuse')
                player.items1.remove('Fuse')
                game_file.screen.fill(game_file.black)
                continue

        elif player.action.lower() == 'go to rooms':
            message = ('Which room are you going to?')
            choices = ['>Closet', '>Elevator', '>Balcony']
            game_file.display_message(1, message)
            game_file.display_message(2, choices)
            player.action = game_file.get_player_input()
            game_file.screen.fill(game_file.black)

            if player.action.lower() == 'closet' and 'Fuse' not in player.inventory:
                message = (
                    'You enter the cramped closet. The janitor\'s tools are lying about.\nThe stingy smell of cleaning '
                    'products bothers you, but due to the odor of the freshly washed sheets, it is a minor nuisance.\n'
                    'You think there is nothing interesting here to be seen, but then you spot a multitude of red spots, '
                    'splattered all over a sheet, in a tucked away basket.\nIt looks like...blood.\n'
                    'You take a mental note of this and return to the hallway.\n')
                game_file.display_message(1, message)
                time.sleep(1)
                game_file.screen.fill(game_file.black)

                continue

            elif player.action.lower() == 'closet' and 'Fuse' in player.inventory:
                message = (
                    'As you enter the cramped closet, you hear an ominous buzz, followed by a cable having a sudden jolt of electricity.\n'
                    'The entire hallway goes into lockdown and a red light turns on. The door slams shut behind you and it locks in place.\n'
                    'Hours pass in the confined space, and the stingy smell of cleaning products is omnipresent.\n'
                    'The chlorine starts taking its toll on your lungs. You do not feel like you can resist in there much longer.\n'
                    '...\n'
                    '...\n'
                    '...\n'
                    'Finally, footsteps can be heard. It\'s the janitor. You can make out a muffled voice...\n'
                    'It sounds like...like...they\'re looking for a fuse. And then it strikes you.\n'
                    'The fuse they\'re looking for is in your pocket. Tucked away, safely, behind the locked door.\n'
                    'With you.\n'
                    '...\n'
                    '...\n'
                    '...\n'
                    'Hours later, they come back with a fuse. Upon opening the closet door, they find you.\n'
                    'No, no. They find your body. \n'
                    'Cause of death: Asphyxiation.\n')
                game_file.display_message(1, message)
                time.sleep(2)
                player.change_state()
                player.check1 = True

            if player.action.lower() == 'balcony':
                message = (
                    'The wind lifts your hair...The fresh smell of the air makes you inhale with a sense of relief.\n'
                    'You are invigorated.\nOutside, you notice numerous black limousines are arriving. '
                    'The people coming out of them all wear red masks, along with black suits and dresses.\n'
                    'It looks like they were expected. A great portion of the hotel staff is waiting for them, '
                    'quickly rushing to escort them once they reach the hotel\'s steps.\n'
                    'An ominous aura surrounds these new guests...\n'
                    'You notice something peculiar about the limousines. They each seem to carry a certain symbol.\n'
                    'The symbols are beautifully blazoned on their hoods. A door, a candle and a circle.\n'
                    'You ponder this peculiarity for a second and then return to the hallway.\n')
                game_file.display_message(1, message)
                time.sleep(2)
                game_file.screen.fill(game_file.black)
                continue

            if player.action.lower() == 'elevator':
                player.check1 = True



start()
game_file.screen.fill(game_file.black)
room1()
game_file.screen.fill(game_file.black)

game_file.pygame.display.update()
game_file.clock.tick(60)