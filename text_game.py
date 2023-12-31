import time
from pygame import mixer

import text_adventure as adv_file
import game_py as game_file

mixer.init()
mixer.music.set_volume(0.2)

player = adv_file.Player()
game = adv_file.Game()


# Function for starting the game - choosing a name, room and the intro.
def start():

    # The game will select an intro depending on the phase/playthrough the game is currently on.
    # Useful for replayability and detecting if the player has died beforehand.
    message = game.game_start(game)

    game_file.play_music('Music\intro.mp3', -1, 5000)

    game_file.display_message(1, message)
    adv_file.time.sleep(5)
    player.place_choice = 'Murder Mystery'
    game_file.screen.fill(game_file.black)

    game_file.display_message(1, 'What is your name, endorsed guest? ')
    player.name = game_file.get_player_input().title()
    game_file.screen.fill(game_file.black)

    game_file.display_message(1, 'And what room will it be?')
    choices = ['>Room 09', '>Room 13', '>Room 256']
    game_file.display_message(2, choices, (50, 80))
    player.pclass = game_file.get_player_input().lower()
    game_file.screen.fill(game_file.black)

    player.creation(player.place_choice)
    game_file.display_message(1, player.intro)

    mixer.music.fadeout(2000)


def room1():
    message = 'Level 1: Hallway'
    game_file.display_message(1, message, (395, 70))
    time.sleep(2)
    game_file.screen.fill(game_file.black)

    game_file.screen.blit(game_file.level1_img, (0, 0))

    game_file.play_music('Music\level1.mp3', -1, 5000)

    message = ('You enter the dimly lit hallway, caught between the safety of your room and the mysteries ahead. '
               'The air is still, carrying a hint of aged wood. The faded wallpaper peels, revealing the passage of time. '
               'To your left, a closed door leads to a balcony, teasing glimpses of the outside world.  '
               'To your right, a slightly ajar door reveals a cramped closet, holding secrets within its limited space. '
               'Straight ahead, a closed door guards the elevator, its faint hum echoing through the corridor. '
               'You observe two items: a fuse, laying on a shelf, and a magnifying glass, somehow waiting for a firm hand to pick it up. '
               'Anticipation settles upon you as you stand in this hallway, ready to unlock the stories within each room. '
               'The adventure awaits, just beyond the threshold. ')
    game_file.display_message(1, message)
    time.sleep(5)
    game_file.screen.fill(game_file.black)

    while player.check1 is False:

        game_file.screen.blit(game_file.level1_img, (0, 0))

        game_file.play_music('Music\level1.mp3', -1, 5000)

        if len(player.items1) > 0:
            game_file.display_message(1, 'What is your next move?')
            choices = ['>Go to rooms', '>Pick up items']
            game_file.display_message(2, choices)
            player.action = game_file.get_player_input()
            game_file.screen.fill(game_file.black)

        elif len(player.items1) == 0:
            game_file.display_message(1, 'What is your next move?')
            choices = ['>Go to rooms']
            game_file.display_message(2, choices)
            player.action = game_file.get_player_input()
            game_file.screen.fill(game_file.black)

        if player.action.lower() == 'pick up items' and len(player.items1) > 0:
            message = 'Which item do you pick up?'
            game_file.display_message(1, message)
            choices = []
            for i in player.items1:
                choices.append('>' + i)
            game_file.display_message(2, choices)
            player.action = game_file.get_player_input()
            game_file.screen.fill(game_file.black)

            if player.action.lower() == 'magnifying glass':

                game_file.play_music('Music\pickup.mp3')

                message = 'You pick up a magnifying glass. Hopefully, it will be useful in the way that you think. '
                game_file.display_message(1, message)
                player.inventory.append('Magnifying Glass')
                player.items1.remove('Magnifying Glass')
                game_file.screen.fill(game_file.black)
                continue

            elif player.action.lower() == 'fuse':

                game_file.play_music('Music\pickup.mp3')

                message = 'You picked up a fuse. Someone might miss it. '
                game_file.display_message(1, message)
                player.inventory.append('Fuse')
                player.items1.remove('Fuse')
                game_file.screen.fill(game_file.black)
                continue

        elif player.action.lower() == 'go to rooms':
            message = 'Which room are you going to? '
            choices = ['>Closet', '>Elevator', '>Balcony']
            game_file.display_message(1, message)
            game_file.display_message(2, choices)
            player.action = game_file.get_player_input()
            game_file.screen.fill(game_file.black)

            if player.action.lower() == 'closet' and 'Fuse' not in player.inventory:

                game_file.play_music('Music\slide_door.mp3')

                message = (
                    'You enter the cramped closet. The janitor\'s tools are lying about. The stingy smell of cleaning '
                    'products bothers you, but due to the odor of the freshly washed sheets, it is a minor nuisance. '
                    'You think there is nothing interesting here to be seen, but then you spot a multitude of red spots, '
                    'splattered all over a sheet, in a tucked away basket. It looks like...blood. '
                    'You take a mental note of this and return to the hallway. ')
                game_file.display_message(1, message)
                time.sleep(5)
                game_file.screen.fill(game_file.black)

                continue

            elif player.action.lower() == 'closet' and 'Fuse' in player.inventory:

                game_file.play_music('Music\slide_door.mp3', queue='Music\electricity.mp3')
                # Death ending nr. 1
                message = (
                    'As you enter the cramped closet, you hear an ominous buzz, followed by a cable having a sudden jolt of electricity. '
                    'The entire hallway goes into lockdown and a red light turns on. The door slams shut behind you and it locks in place. '
                    'Hours pass in the confined space, and the stingy smell of cleaning products is omnipresent. '
                    'The chlorine starts taking its toll on your lungs. You do not feel like you can resist in there much longer. '
                    'Finally, footsteps can be heard. It\'s the janitor. You can make out a muffled voice... '
                    'It sounds like...like...they\'re looking for a fuse. And then it strikes you. '
                    'The fuse they\'re looking for is in your pocket. Tucked away, safely, behind the locked door. '
                    'With you. '
                    'Hours later, they come back with a fuse. Upon opening the closet door, they find you. '
                    'No, no. They find your body.  '
                    'Cause of death: Asphyxiation. ')
                game_file.display_message(1, message)
                time.sleep(5)
                player.change_state()
                player.check1 = True

            if player.action.lower() == 'balcony':
                game_file.play_music('Music\slide_door.mp3', fade=3000, queue='Music\\balcony.mp3')

                message = (
                    'The wind lifts your hair...The fresh smell of the air makes you inhale with a sense of relief. '
                    'You are invigorated.\nOutside, you notice numerous black limousines are arriving. '
                    'The people coming out of them all wear red masks, along with black suits and dresses. '
                    'It looks like they were expected. A great portion of the hotel staff is waiting for them, '
                    'quickly rushing to escort them once they reach the hotel\'s steps. '
                    'An ominous aura surrounds these new guests... '
                    'You notice something peculiar about the limousines. They each seem to carry a certain symbol. '
                    'The symbols are beautifully blazoned on their hoods. A door, a candle and a circle. '
                    'You ponder this peculiarity for a second and then return to the hallway.  ')
                game_file.display_message(1, message)
                time.sleep(5)
                game_file.screen.fill(game_file.black)
                continue

            if player.action.lower() == 'elevator':
                game_file.play_music('Music\elevator.mp3', start=19)
                player.check1 = True

        else:
            message = 'I did not understand that. Please repeat. '
            game_file.display_message(1, message)
            time.sleep(2)
            game_file.screen.fill(game_file.black)
            continue


def room2():
    game_file.play_music('Music\level2.mp3', loops=-1, fade=5000)

    if player.pclass == 'room 09':
        message = 'Level 2: The Upper Level'
        level = 'the upper level'
        game_file.display_message(1, message, (365, 70))
        time.sleep(2)
        game_file.screen.fill(game_file.black)

    elif player.pclass == 'room 13' or player.pclass == 'room 256':
        message = 'Level 2: The Lower Level'
        level = 'the lower level'
        game_file.display_message(1, message, (365, 70))
        time.sleep(2)
        game_file.screen.fill(game_file.black)



    message = (
        f'The elevator descends smoothly, carrying you to {level}. As the doors open, a cool atmosphere greets you. '
        'Three distinct doors stand before you, each with its own allure. '
        'To your left, a partially opened door with a tint of green reveals a glimpse of light streaming from within. The soft glow suggests the bathroom light may still be on, hinting at recent activity. '
        'Straight ahead, a closed door painted in a bold shade of red captures your attention. Its vibrant color holds an air of intrigue, hiding the secrets that lie beyond its surface. '
        'To your right, a sleek black door commands your curiosity. Its smooth exterior reflects the ambient light, promising a realm of mysteries waiting to be explored. '
        'You stand at a pivotal moment, faced with choices that will shape your investigation. '
        'The room with the green-tinged door may hold immediate interest, but the red and black doors hold their own enigmas. '
        'It is time to make your move and uncover the truth that awaits behind one of these doors.')
    game_file.display_message(1, message)
    time.sleep(5)
    game_file.screen.fill(game_file.black)
    progression_check = -1
    first_door = None
    gunshot = False

    while player.check2 == False:

        game_file.play_music('Music\level2.mp3', loops=-1, fade=5000)

        if progression_check == -1:
            message = 'Where do you choose to go?'
            game_file.display_message(1, message)
            choices = []
            for i in player.rooms2:
                choices.append('>Go to ' + i.lower())
            game_file.display_message(2, choices)
        else:
            player.rooms2.remove(progression_check)
            player.rooms2.sort()
            if len(player.rooms2) == 0:
                break
            choices = []
            for i in player.rooms2:
                choices.append('>Go to ' + i.lower())
            game_file.display_message(2, choices)
        player.action = game_file.get_player_input()
        game_file.screen.fill(game_file.black)

        if player.action.lower() == 'go to the green door':

            game_file.screen.blit(game_file.level2_img_green, (0, 0))

            game_file.play_music('Music\slide_door.mp3')

            if first_door is None:

                while True:
                    first_door = 'Green'
                    message = ('You slowly open the dirty, stained green door and enter the room. '
                               'The first thing that draws your attention is the light in the bathroom. '
                               'Do you go to the bathroom?')
                    game_file.display_message(1, message)
                    choices = ['>Yes', '>No']
                    game_file.display_message(2, choices, (50, 100))
                    progression_check = 'The Green Door'
                    player.action = game_file.get_player_input()
                    game_file.screen.fill(game_file.black)

                    if player.action.lower() == 'yes':

                        game_file.play_music('Music\door_creak.mp3')

                        # Death ending nr. 2
                        message = ('You enter the bathroom with careful steps. The door creaks as you open it. '
                                   'You\'re shocked by the sight before you. A man has committed suicide in the bathtub. '
                                   'The water has been running continuously and has overflowed, drenching your shoes. '
                                   'As you try to quickly leave the room, in your panic, you slip on the wet floor, and hit your '
                                   'head on the sink. '
                                   'You are dead. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        player.change_state()
                        player.check2 = True

                    elif player.action.lower() == 'no':
                        message = ('Deciding the bathroom is of no interest to you, you look around the room. '
                                   'Your gaze dances around, on the pictures on the walls, on the messy clothes thrown around, '
                                   'on the ugly furniture and wall paint. It is almost as someone intended this room to be '
                                   'the ugliest. Lastly, your gaze settles upon a ticket on the bed. It seems to be a VIP ticket. '
                                   'Do you take it?')
                        game_file.display_message(1, message)
                        choices = ['>Yes', '>No']
                        game_file.display_message(2, choices, (50, 150))
                        player.action = game_file.get_player_input()
                        game_file.screen.fill(game_file.black)

                        if player.action.lower() == 'yes':

                            game_file.play_music('Music\pickup.mp3')

                            message = 'You carefully put the ticket in your jacket\'s inner pocket. '
                            game_file.display_message(1, message)
                            player.inventory.append('VIP Ticket')
                            player.items2.remove('VIP Ticket')
                            game_file.screen.fill(game_file.black)

                        elif player.action.lower() == 'no':
                            message = (
                                'You let the VIP ticket remain where it is. It is probably for the best, you think. ')
                            game_file.display_message(1, message)
                            game_file.screen.fill(game_file.black)

                        if first_door == 'Green':

                            game_file.play_music('Music\gunshot.mp3')

                            message = (
                                'Before leaving the room, a gunshot draws your attention. It seems like it came from the room '
                                'with the black door.\nDo you pursue the gunshot?')
                            choices = ['>Yes', '>No']
                            game_file.display_message(1, message)
                            game_file.display_message(2, choices, (50, 95))
                            player.action = game_file.get_player_input()
                            game_file.screen.fill(game_file.black)

                            if player.action.lower() == 'yes':

                                game_file.play_music('Music\slide_door.mp3', queue='Music\drama.mp3')

                                gunshot = True
                                message = (
                                    'You rush towards the black door, propelled by the piercing sound of the gunshot. '
                                    'As the door swings open, a surge of unease washes over you. '
                                    'The room is shrouded in an eerie atmosphere, adorned with sinister cult objects. '
                                    'Their unsettling presence creates a sense of foreboding, casting long, menacing shadows along the walls. '
                                    'The air is heavy with an otherworldly energy, as if the room itself holds a dark secret. '
                                    'Amidst this macabre scene, a chilling path of blood stains the floor, beckoning you deeper into the heart of the ominous mystery. '
                                    'Do you pursue further?')
                                choices = ['>Yes', '>No']
                                game_file.display_message(1, message)
                                game_file.display_message(2, choices, (50, 215))
                                time.sleep(1)
                                player.action = game_file.get_player_input()
                                game_file.screen.fill(game_file.black)

                                if player.action.lower() == 'yes':

                                    game_file.play_music('Music\dread.mp3', loops=-1)

                                    game_file.screen.blit(game_file.level2_img_wardrobe, (0, 0))

                                    message = ('The trail of blood leads you through the hidden door of a wardrobe. '
                                               'You enter something akin to a tunnel. The walls are carved and made of stone. '
                                               'The air becomes denser as you walk through the never-ending tunnel. '
                                               'You wonder how could such a structure exist in this place. '
                                               'The blood trail has somehow kept the same shape and consistence throughout the tunnel. '
                                               'You come to a dead end. A rock wall proudly defies you, by simply existing '
                                               'in your way. Five blocks of rock are protruding out of it, each with a different '
                                               'symbol carved on it. A door, a circle, a candle, a magnifying glass and a wand. '
                                               'How do you proceed?')
                                    game_file.display_message(1, message)
                                    step = 0  # Steps for completing the puzzle
                                    death_counter = 0  # Counter for the amount of times you can try pushing the blocks, 2 is max
                                    while player.temp_check is False:

                                        if 'Magnifying Glass' in player.inventory:
                                            choices = ['>Introduce the magnifying glass in the carving representing it',
                                                       '>Push the blocks of rock']
                                            game_file.display_message(2, choices, (50, 260))

                                        else:
                                            choices = ['>Push the blocks of rock']
                                            game_file.display_message(2, choices, (50, 260))
                                        player.action = game_file.get_player_input()
                                        game_file.screen.fill(game_file.black)

                                        if player.action.lower() == 'introduce the magnifying glass in the carving representing it':

                                            game_file.play_music('Music\pickup.mp3')

                                            message = (
                                                'You take out your magnifying glass and fit it into the block\'s carving. '
                                                'You are surprised it worked, as it seemed to be an odd choice.  ')
                                            player.inventory.remove('Magnifying Glass')
                                            step += 1
                                            game_file.display_message(1, message)
                                            game_file.screen.fill(game_file.black)
                                            time.sleep(5)
                                            continue

                                        elif player.action.lower() == 'push the blocks of rock':

                                            game_file.play_music('Music\stone.mp3')

                                            message = (
                                                'As the blocks of rock are protruding, you decide they could also be made '
                                                'to fit in.\nBut, there\'s a catch: in what order should you push them back in?')
                                            choices = ['>Circle, door, wand, magnifying glass, candle',
                                                       '>Wand, door, candle, magnifying glass, triangle',
                                                       '>Door, candle, magnifying glass, circle, wand']
                                            game_file.display_message(1, message)
                                            game_file.display_message(2, choices, (50, 80))
                                            player.action = game_file.get_player_input()
                                            time.sleep(5)
                                            game_file.screen.fill(game_file.black)

                                            if player.action.lower() == 'door, candle, magnifying glass, circle, wand':
                                                step += 1
                                                death_counter += 1
                                                if step < 2 and 'Magnifying Glass' not in player.items1:
                                                    message = ('The decision you made seems to have been inspired. '
                                                               'Something clicks inside the wall. The stone itself sends out a ripple throughout. '
                                                               'The stone that seemed solid is now liquid in nature and you can see it pulsating in waves. '
                                                               'Better than nothing, you think. ')
                                                    game_file.display_message(1, message)
                                                    time.sleep(5)
                                                    game_file.screen.fill(game_file.black)
                                                    continue

                                                elif step < 2 and 'Magnifying Glass' in player.items1:
                                                    message = (
                                                        'The decision you made seems to have been inspired. '
                                                        'Something clicks inside the wall. The stone itself sends out a ripple throughout. '
                                                        'But something is off. The solid stone now turns into a volatile, liquid substance. '
                                                        'Spikes of it are rising and sinking back everywhere. One reaches out so far that it grazes you. '
                                                        'The liquid substance reacts to your blood. Tne entire wall starts buzzing and turning waves of shades of crimson.  ')
                                                    game_file.display_message(1, message)
                                                    time.sleep(5)
                                                    game_file.screen.fill(game_file.black)
                                                    continue

                                                else:

                                                    game_file.play_music('Music\epic.mp3')

                                                    message = (
                                                        'As you push the blocks back into place, stairs are starting to form below the rock wall. '
                                                        'They seem to be leading towards a bright, white light. '
                                                        'You descend the stairs. A gentle breeze can be felt, in a peculiar combination with feeling warm. '
                                                        'The emotions of hope and safety, that accompanied you during your descent, now evaporate. '
                                                        'A sentiment of dread like no other embraces you, holding you tightly, squeezing out your breath. '
                                                        'The hotel\'s walls emanate this feeling all around you. It must be something about the hotel, you think. '
                                                        'But you\'re gonna get through it. You have so little left to do. And so much, at the same time. ')
                                                    player.temp_check = True
                                                    player.check2 = True
                                                    player.passing = True
                                                    game_file.display_message(1, message)
                                                    time.sleep(5)
                                                    game_file.screen.fill(game_file.black)

                                            else:
                                                if death_counter < 2:
                                                    message = (
                                                        'You decide on a sequence and...nothing. A sinister hum is heard emanating '
                                                        'from the wall.')
                                                    death_counter += 1
                                                    game_file.display_message(1, message)
                                                    time.sleep(2)
                                                    game_file.screen.fill(game_file.black)
                                                    continue

                                                # Death ending nr. 3
                                                elif death_counter == 2:
                                                    message = (
                                                        'The hum turns into a loud buzz that makes you cover up your ears... '
                                                        'And then, nothing. The wall then starts crumbling from the middle to the sides. '
                                                        'You see nothing but pitch black darkness before you. Then, you feel something on the back of your neck. '
                                                        'It\'s like a sting. It feels warm on your skin at first, but then its cold runs through your entire body. '
                                                        'You feel numb from the cold. Your head feels detached from your body, like it\'s floating... '
                                                        'The sequence of events that follows isn\'t very clear. You remember dropping on the ground. '
                                                        'A sensation that could be described as being engulfed, swallowed, by darkness that has teeth, is then felt. '
                                                        'In reality, your body is discovered in the room you heard the gunshot from. '
                                                        'It marks the beginning of the blood trail. You are found sitting on your knees, mouth wide open and eyes staring in awe at the ceiling. '
                                                        'Your pupils are fully dilated. Your bodily liquids have found their way out... '
                                                        'An unfortunate end. '
                                                        'You are dead. ')
                                                    player.temp_check = True
                                                    player.check2 = True
                                                    player.change_state()
                                                    game_file.display_message(1, message)
                                                    time.sleep(5)

                                elif player.action.lower() == 'no':
                                    message = ('This hotel has definitely got something wrong going on, you think.\n'
                                               'You carefully walk around the room, analyzing everything and deciding if this would be the time\n'
                                               'to call the police. You notice a bloody letter on the desk facing the window.\n'
                                               'It seems to be the only item on that desk. It is sealed with a crimson seal, also reminiscent of blood.\n'
                                               'You step closer to it, curious of its contents. But first, you think, you should search the desk\'s drawers.\n'
                                               'Nothing comes out of your search, except for old, irrelevant papers, a broken cable and the hotel\'s assistance book.\n'
                                               'In this case, all that\'s left is taking the letter for yourself.\n'
                                               'Do you take it?')
                                    choices = ['>Yes',
                                               '>No']
                                    game_file.display_message(1, message)
                                    game_file.display_message(2, choices, (50, 250))
                                    player.action = game_file.get_player_input()
                                    game_file.screen.fill(game_file.black)

                                    if player.action.lower() == 'yes':

                                        game_file.play_music('Music\pickup.mp3')

                                        message = (
                                            'Your curiosity got the better of you. You quickly take the letter and stuff it well. '
                                            'Now, nobody will know what you\'ve been up to.')
                                        player.inventory.append('Bloody Letter')
                                        game_file.display_message(1, message)
                                        time.sleep(2)
                                        game_file.screen.fill(game_file.black)

                                    elif player.action.lower() == 'no':
                                        message = (
                                            'Perhaps it is wiser to let it where it is. Or so your confused senses tell you. ')
                                        game_file.display_message(1, message)
                                        time.sleep(2)
                                        game_file.screen.fill(game_file.black)

                                    message = (
                                        'You can\'t help but wonder where the gunshot came from. It was clearly from this room. '
                                        'You could\'ve misheard. There is certainly no gun laying around. '
                                        'And there is certainly no way you will go after the blood trail. Perhaps in another life. ')
                                    game_file.display_message(1, message)
                                    time.sleep(5)
                                    game_file.screen.fill(game_file.black)

                            elif player.action.lower() == 'no':
                                message = (
                                    'Was that really a gunshot you just heard? You would rather not find out. Not the time, not the place to go investigating by yourself. '
                                    'You wonder if you should call the police, but decide not to. You hope this was not against your best interests. '
                                    'For a brief second, you feel a hand on your shoulder. Its grip is firm and violent. '
                                    'You turn around and survey the room. The shivers down your spine don\'t fail to appear. '
                                    'You feel light headed. Your steps are uncertain and heavy. '
                                    'You hold onto the wall on your way out and take a short break. '
                                    'This place is physically hurting you. You need to get to the end of it. '
                                    'As. Soon. As. Possible.'
                                    'And so, after giving the room one last look, you ponder which door to explore next.')

                                game_file.play_music('Music\slide_door.mp3')

                                game_file.display_message(1, message)
                                time.sleep(5)
                                game_file.screen.fill(game_file.black)
                        else:
                            if len(player.rooms2) == 2:
                                message = ('Now, time to see what is behind the final door. '
                                           'Nothing good, you think to yourself. Hopefully, that won\'t be the case. Just bad thoughts... ')
                                game_file.display_message(1, message)
                                time.sleep(2)
                                game_file.screen.fill(game_file.black)

                    else:
                        message = 'I did not understand that. Please repeat. '
                        game_file.display_message(1, message)
                        time.sleep(2)
                        game_file.screen.fill(game_file.black)
                        continue

                    break

        elif player.action.lower() == 'go to the black door':

            game_file.screen.blit(game_file.level2_img_black, (0, 0))

            game_file.play_music('Music\slide_door.mp3')

            first_door = 'Black'
            progression_check = 'The Black Door'

            if gunshot is False:
                while True:

                    game_file.play_music('Music\drama.mp3', loops=-1)

                    message = (
                        'You feel an irresistible urge to explore the black door, driven by an inexplicable force. '
                        'As the door creaks open, a wave of cold dread washes over you. '
                        'The room before you is a nightmarish tableau of eerie cult objects, their malevolent presence seeming to watch your every move. '
                        'Sinister shadows writhe along the walls, as if alive and hungry for company. '
                        'The air is thick with an oppressive sense of malevolence, sending shivers down your spine. '
                        'Amidst this macabre display, a black, tall silhouette of a man can be seen standing in the middle of the room. '
                        'It\'s smokey and fully physical, at the same time. An evil apparition. '
                        'But it is not paying attention to you. To your right, another man can be seen. This one, flesh and bone. '
                        'His clothes are torn and bloody, his face, a grin of exhaustion and desperation. '
                        'A plethora of cult items can be seen around him, all broken and smashed. '
                        'With desperation, he loads his gun and tries shooting the black figure. It does nothing. '
                        'The figure dashes across the room, to the man, grabbing his head and quickly dragging it on the floor. '
                        'The black figure seemingly disappears into a darkness in the back of the room, with the man\'s blood forming a trail to it. '
                        'The trail seems to be leading deeper into the heart of the chilling mystery, filling you with a gnawing sense of impending doom. '
                        'You are presented with a choice: follow the blood trail? ')
                    choices = ['>Yes',
                               '>No']
                    game_file.display_message(1, message)
                    game_file.display_message(2, choices, (50, 405))
                    player.action = game_file.get_player_input()
                    time.sleep(1)
                    game_file.screen.fill(game_file.black)

                    if player.action.lower() == 'yes':

                        game_file.play_music('Music\dread.mp3', loops=-1)

                        message = ('You follow the blood trail through a secret door in the wardrobe. '
                                   'But, as soon as you step through, a darkness quickly engulfs you and throws you out of the room with force. '
                                   'The door immediately slams shut. You feel shivers everywhere in your body. You\'re too fearful to get off the ground and look around. '
                                   'A burning sensation can be felt on your arm. Gasping, you clutch your arm, and to your horror, you find a cursed mark etched upon your skin. '
                                   'The mark appears as a sinister, intricate glyph that seems to writhe with a life of its own. '
                                   'The dark ink spreads across your flesh like a malevolent stain, and you feel an unsettling, pulsating sensation emanating from the mark. '
                                   'The mark glows with an eerie, crimson light, casting an ominous shadow over your surroundings. It throbs with an unseen power, as if the malevolence from the black room has now bonded with your very being.\n'
                                   'Fear and confusion grip you as you realize you are now marked by an otherworldly force, and the sense of foreboding intensifies with each passing second. ')
                        game_file.display_message(1, message)

                        game_file.screen.blit(game_file.level2_img_mark, (0, 0))

                        time.sleep(5)
                        player.inventory.append('Cursed Mark')
                        game_file.screen.fill(game_file.black)

                    elif player.action.lower() == 'no':
                        while True:

                            game_file.screen.blit(game_file.level2_img_b_room, (0, 0))

                            game_file.play_music('Music\drama.mp3')

                            message = (
                                'The chilling scene unfolds, overwhelming fear grips your heart. An eerie foreboding takes hold as you witness the nightmarish tableau. '
                                'The wardrobe\'s door creaks open, cold dread washes over you, freezing you in place. '
                                'Fear leaves you torn between curiosity and self-preservation. Maybe you should see where the trail is leading to, after all... '
                                'Then, the image of the apparition comes back to you. The harrowing scene that unfolded before your eyes haunts you. '
                                'You are unsure of where to find safe haven. It seems as it the malevolent entity is only toying with you, saving you for the last. '
                                'You don\'t think it\'s really gone...The dread and evil are all around. You feel almost physically squeezed by it. '
                                'You almost run out of breath a couple of times. You slowly get up, arms and legs trembling. No, you will not give in to the deadly curiosity. '
                                'This is no place to die. You didn\'t come here for this. '
                                'The ordeal leaves you scared and uncertain, unsure of the horrors that await and the choices you must make to survive. '
                                'You carefully walk around the room, analyzing everything and deciding if this would be the time '
                                'to call the police. You notice a bloody letter on the desk facing the window. '
                                'It seems to be the only item on that desk. It is sealed with a crimson seal, also reminiscent of blood. '
                                'You step closer to it, curious of its contents. But first, you think, you should search the desk\'s drawers. '
                                'Nothing comes out of your search, except for old, irrelevant papers, a broken cable and the hotel\'s assistance book. '
                                'In this case, all that\'s left is taking the letter for yourself. '
                                'Do you take it?')
                            choices = ['>Yes',
                                       '>No']
                            game_file.display_message(1, message)
                            game_file.display_message(2, choices, (110, 460))
                            game_file.get_player_input()
                            time.sleep(1)
                            game_file.screen.fill(game_file.black)

                            if player.action.lower() == 'yes':

                                game_file.play_music('Music\pickup.mp3')

                                message = (
                                    'If anything will serve you as proof of what happened here, it\'s this. You quickly took the letter and stuffed it well. '
                                    'Now, maybe you will live to show the world what is truly happening here. ')
                                game_file.display_message(1, message)
                                time.sleep(5)
                                game_file.screen.fill(game_file.black)

                            elif player.action.lower() == 'no':
                                message = (
                                    'Perhaps it is wiser to let it where it is. Or so your confused senses tell you. ')
                                game_file.display_message(1, message)
                                time.sleep(2)
                                game_file.screen.fill(game_file.black)

                            else:
                                message = 'I did not understand that. Please repeat. '
                                game_file.display_message(1, message)
                                time.sleep(2)
                                game_file.screen.fill(game_file.black)
                                continue

                            break

                    else:
                        message = 'I did not understand that. Please repeat. '
                        game_file.display_message(1, message)
                        time.sleep(2)
                        game_file.screen.fill(game_file.black)
                        continue

                    break


            elif gunshot is True:

                game_file.play_music('Music\locked_door.mp3')

                message = ('The door won\'t even budge. It now refuses to let you in. '
                           'Should have been thorough with the room the first time. '
                           'It is as if the door became a part of the wall itself. Curious indeed.  ')
                game_file.display_message(1, message)
                time.sleep(5)
                game_file.screen.fill(game_file.black)

        elif player.action.lower() == 'go to the red door':

            game_file.screen.blit(game_file.level2_img_red, (0, 0))

            game_file.play_music('Music\slide_door.mp3')
            game_file.play_music('Music\letter_read.mp3', loops=-1)

            progression_check = 'The Red Door'
            message = (
                'As you step into the red room, a mysterious ambiance envelops you, carrying an aura of ancient secrets and mystical energies. '
                'The air is tinged with an intoxicating blend of incense and a faint scent of old parchment, with flickering candles cast dancing shadows upon the walls, creating an almost hypnotic effect. '
                'In the center of the room lies a crystal ball, perched atop an ornate stand, its surface glimmering with an otherworldly sheen. '
                'It beckons you to approach, offering cryptic insights into the future and a glimpse into the veiled realms of destiny. '
                'Tarot cards spread in a precise pattern whisper untold possibilities, while ancient tomes of arcane knowledge hold the wisdom of ages past. '
                'Five intriguing objects line a nearby table, each veiled in mystery, awaiting your firm hand. '
                'The air tingles with anticipation.')
            player.temp_check = False
            choices = ['Crystal ball', 'Tarot cards', 'Table of objects', 'Go outside of the room']
            game_file.display_message(1, message)
            display_check = False

            while player.temp_check is False:

                game_file.play_music('Music\letter_read.mp3', loops=-1)

                if display_check is False:
                    game_file.display_message(2, 'So then, what path do you choose?', (50, 290))
                    display_check = True
                else:
                    game_file.display_message(2, 'So then, what path do you choose?', (50, 50))

                if len(choices) == 4:
                    y_position = 300
                    for i in choices:
                        game_file.display_message(2, '> ' + i, (50, y_position))
                        y_position += 20
                    player.action = game_file.get_player_input()
                    game_file.screen.fill(game_file.black)

                else:
                    y_position = 70
                    for i in choices:
                        game_file.display_message(2, '> ' + i, (50, y_position))
                        y_position += 20
                    player.action = game_file.get_player_input()
                    game_file.screen.fill(game_file.black)

                if player.action.lower() == 'crystal ball':

                    game_file.screen.blit(game_file.level2_img_crystal, (0, 0))

                    if 'Cursed Mark' in player.inventory:
                        message = (
                            'Carefully walking closer to the ornate stand, you instinctively reach out to the crystal ball. '
                            'As you do that, your mark burns. The crystal ball reacts to your mark and begins forming a swirling black smoke. '
                            'From it, you can distinguish the same room you\'re in. You see yourself, and behind you...a dark face with sharp teeth, orange, mad eyes, sitting right on your shoulder. '
                            'Then, the image shifts into a walk. It goes down some stairs, and ends up in the main area of the hotel. A large masked person towers over. '
                            'It looks like he is guarding the entrance. A fiery image of a large book snaps before your eyes. The crystall ball goes blank again and cracks. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)
                        choices.remove('Crystal ball')
                        choices.sort()

                    else:
                        message = (
                            'Carefully walking closer to the ornate stand, you instinctively reach out to the crystal ball. '
                            'As you do that, the crystal ball begins forming a swirling white smoke. '
                            'In it, you distinguish the room you\'re in. The image pans over to the table with the five objects. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)

                        if 'Bloody Letter' in player.inventory:
                            message = 'A particular item seems to be glowing. It\'s the silver ring. '
                            game_file.display_message(1, message)
                            time.sleep(2)
                            game_file.screen.fill(game_file.black)

                        elif 'Magnifying Glass' in player.inventory:
                            message = 'A particular item seems to be glowing. It\'s the black mirror. '
                            game_file.display_message(1, message)
                            time.sleep(2)
                            game_file.screen.fill(game_file.black)

                        else:
                            message = 'A particular item seems to be glowing. It\'s the ancient tome. '
                            game_file.display_message(1, message)
                            time.sleep(2)
                            game_file.screen.fill(game_file.black)

                        message = (
                            'Then, the image shifts into a walk. It goes down some stairs, and ends up in the main area of the hotel. A large masked person towers over. '
                            'It looks like he is guarding the entrance. The crystall ball goes blank again and cracks. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)
                        choices.remove('Crystal ball')
                        choices.sort()

                elif player.action.lower() == 'tarot cards':

                    game_file.screen.blit(game_file.level2_img_tarot, (0, 0))

                    game_file.play_music('Music\epic.mp3', loops=-1)

                    message = (
                        'As you gingerly reach out to touch the deck, a sense of trepidation and excitement intertwines within you. '
                        'The cards seem to respond to your presence, almost as if they were awaiting your arrival. '
                        'As your fingers make contact with the smooth, worn edges, a surge of energy courses through your being. '
                        'The deck feels warm, alive, and responsive in your hands. It is as though a subtle connection has been established between you and the ancient wisdom contained within. '
                        'With every shuffle and cut, the cards seem to whisper secrets, each one a potential window into the vast tapestry of fate. '
                        'You can\'t help but notice the way they shine in the light. Their golden tint gives a sense of comfort and safety. '
                        'You instinctively draw and spread five cards out of the tarot deck on the table. Your hands move on their own. '
                        'A light breeze flickers the candles, seemingly coming out of nowhere. The intensity of their flames now grows. '
                        'After a brief pause, you turn one of the cards. Your hand trembles in doing so. ')
                    game_file.display_message(1, message)
                    time.sleep(5)
                    game_file.screen.fill(game_file.black)

                    if 'Cursed Mark' in player.inventory and 'Bloody Letter' not in player.inventory:
                        message = (
                            'The first card is The Tower. It is followed by The Hanged Man, The Two of Swords, The Devil and The Wheel of Fortune. '
                            'You do not know their meaning, but you don\'t need to. Your intuition and senses know what the sequence means. '
                            'Your mark burns. You must get rid of it. You must be even more careful with your choices, as your life depends on them. '
                            'And you must get rid of it as soon as possible. Maybe one of the items will help in that regard. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)
                        choices.remove('Tarot cards')
                        choices.sort()

                    elif 'Bloody Letter' in player.inventory and 'Cursed Mark' not in player.inventory:
                        message = (
                            'The first card is The Hermit. It is followed by The High Priestess, The Page of Swords, The Justice and The Wheel of Fortune. '
                            'Even though you never dealt with tarot cards before, you sense the meaning of the sequence. Their golden tint tells you all you need to know. '
                            'The answers are right under your nose. You must look deeper, in what you know, in what you have. Your intuition is your salvation. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)
                        choices.remove('Tarot cards')
                        choices.sort()

                    elif 'Bloody Letter' in player.inventory and 'Cursed Mark' in player.inventory:
                        message = (
                            'The first card is The Hermit. It is followed by The High Priestess, The Page of Swords, The Justice and The Wheel of Fortune. '
                            'Even though you never dealt with tarot cards before, you sense the meaning of the sequence. Their golden tint tells you all you need to know. '
                            'The answers are right under your nose. You must look deeper, in what you know, in what you have. Your intuition is your salvation. '
                            'The key to removing your mark is hidden in the bloody letter and in this room. Perhaps in one of the objects, as well. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)
                        choices.remove('Tarot cards')
                        choices.sort()

                    else:
                        message = (
                            'The first card is The World. It is followed by The Eight of Cups, The Three of Wands, The Ace of Pentacles and The Chariot. '
                            'Despite never dealing with tarot cards before, you know what all of this means. You are close. It\'s almost over. '
                            'Now, for the last part of this weird day, you must not let your guard down. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)
                        choices.remove('Tarot cards')
                        choices.sort()

                elif player.action.lower() == 'table of objects':

                    game_file.screen.blit(game_file.level2_img_table, (0, 0))

                    game_file.play_music('Music\epic.mp3', loops=-1)

                    message = (
                        'From the second you laid eyes on it, you knew it was there for you. All of this, was for you, somehow. '
                        'You feel an unexplainable connection to everything that is happening. You must see this through. '
                        'Five objects are carefully laid on the gold-edged cloth, made out of red silk, that covers the table. '
                        'A ring, made out of silver. '
                        'A black mirror, made out of obsidian. '
                        'An ancient tome, made out of leather. '
                        'A perfumed satchel, adorned with beautiful symbols. '
                        'A rosary, of the simplest design. '
                        'Something tells you you can only pick one. And that it is somewhat...relevant. Vital, rather. '
                        'Which one will it be?')
                    temp_choices = ['>Silver ring',
                                    '>Black mirror',
                                    '>Ancient tome',
                                    '>Perfumed satchel',
                                    '>Rosary']
                    game_file.display_message(1, message)
                    game_file.display_message(2, temp_choices, (50, 230))
                    player.action = game_file.get_player_input()
                    game_file.screen.fill(game_file.black)
                    choices.remove('Table of objects')
                    choices.sort()

                    if player.action.lower() == 'silver ring':
                        message = (
                            'You believe the ring will prove useful. How could it, though? It\'s just a ring. '
                            'But, if it\'s one thing you learnt in this hotel, is that nothing is random. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)
                        player.inventory.append('Silver Ring')

                    elif player.action.lower() == 'black mirror':
                        message = ('The obsidian, heavy, black mirror seems the obvious choice for you. '
                                   'Perhaps there is something to its blackness that will reveal a secret. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)
                        player.inventory.append('Black Mirror')

                    elif player.action.lower() == 'ancient tome':
                        message = (
                            'The ancient tome definitely holds the information and secrets that will get you out of this place. '
                            'Safely. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)
                        player.inventory.append('Ancient Tome')

                    elif player.action.lower() == 'perfumed satchel':
                        message = (
                            'The perfumed satchel has a certain charm to it. Perhaps it is the perfume itself... '
                            'And maybe that\'s a good thing. Could be exactly what you needed. '
                            'Nevertheless, such a beautiful and charming object is better suited to your pocket, than this table. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)
                        player.inventory.append('Perfumed Satchel')

                    elif player.action.lower() == 'rosary':
                        message = ('Simplicity seems to be the best answer here. And besides, you need God. '
                                   'Faith will get you through this. You can feel it. Divinity is your salvation. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)
                        player.inventory.append('Rosary')

                elif player.action.lower() == 'go outside of the room':

                    game_file.play_music('Music\slide_door.mp3')

                    message = ('Now, having seen enough of the room, you better leave it for now. '
                               'Hopefully for you, you explored it thoroughly. You have a feeling it was crucial. ')
                    game_file.display_message(1, message)
                    time.sleep(5)
                    game_file.screen.fill(game_file.black)
                    choices.remove('Go outside of the room')
                    choices.sort()
                    player.temp_check = True

                else:
                    message = 'I did not understand that. Please repeat. '
                    game_file.display_message(1, message)
                    time.sleep(2)
                    game_file.screen.fill(game_file.black)
                    continue

        else:
            message = 'I did not understand that. Please repeat. '
            game_file.display_message(1, message)
            progression_check = -1
            time.sleep(2)
            game_file.screen.fill(game_file.black)
            continue


def room3():
    message = ('The three doors opened up ways to different worlds, that\'s for sure, you think... '
               'And those worlds left a mark on you. You are now convinced this hotel is by no means a regular hotel. '
               'It\'s a place of evil and ill intent. Besides, you can\'t shake the feeling that this is about you. '
               'Somehow, it\'s connected to you. But despite everything going on, you\'re not sure that\'s a bad thing. '
               'There is a slight simmer of hope in this whole situation. And it\'s waiting somewhere close. Closer than you might think.')
    game_file.display_message(1, message)
    time.sleep(5)
    game_file.screen.fill(game_file.black)

    message = 'Level 3: Lounge'
    game_file.display_message(1, message, (395, 70))
    time.sleep(2)
    game_file.screen.fill(game_file.black)

    while player.check3 is False:

        game_file.screen.blit(game_file.level3_img_lounge, (0, 0))

        game_file.play_music('Music\level3.mp3', loops=-1)

        message = ('Having arrived to Hotel Margot\'s Lounge area, you decide it would be best for you to rest some. '
                   'Continuing in your current state would not be smart. Besides, you need to understand what is going on. '
                   'And to do that, you must think through the events and try to find a logic, a pattern, a connection. '
                   'You spot a large fireplace in the middle of the lounge. With unsure steps, you approach it. '
                   'A red couch is there, to support the heavy thoughts that will go through your mind. It matches the flames of the fireplace. '
                   'You sit down on it. The red couch is made of leather, that squeaks when you sit on it. The sound is unpleasant. '
                   'Yet another thing in this hotel that manages to break your mood and spirit. Just great. '
                   'You need to pull yourself together and get to the bottom of everything that is going on. Now. ')
        game_file.display_message(1, message)
        time.sleep(5)
        game_file.screen.fill(game_file.black)

        while True:
            if 'Bloody Letter' in player.inventory:

                game_file.screen.blit(game_file.level3_img_letter, (0, 0))

                message = (
                    'You notice a red spot on your jacket. Blood, definitely. At this point, it\'s something rather regular. '
                    'And then you remember where it came from. '
                    'You took the bloody letter that was on the desk and stuffed it into the inner pocket. Perhaps this '
                    'letter will offer some context to the rooms that you went through. Or the hotel itself. '
                    'So then, will you open it? Or will you let the information fly away?')
                choices = ['>Open the letter', '>Don\'t open the letter']
                game_file.display_message(1, message)
                game_file.display_message(2, choices, (50, 180))
                player.action = game_file.get_player_input()
                game_file.screen.fill(game_file.black)

                if player.action.lower() == 'open the letter':
                    message = (
                        'No, you won\'t let it fly away. Taking this decision makes you feel empowered. As if you\'re finally starting to fight back. '
                        'You will get out of this hotel, alive. You are hellbent on it. Now, for the letter. ')
                    game_file.display_message(1, message)
                    player.inventory.append('Opened Letter')
                    time.sleep(5)
                    game_file.screen.fill(game_file.black)

                    message = (
                        'The crimson seal of the letter is the only thing between you and its contents. You could rip it off. '
                        'Perhaps it\'s better to carefully slice it open, though. ')
                    choices = ['>Rip it off', '>Slice it open']
                    game_file.display_message(1, message)
                    game_file.display_message(2, choices, (50, 100))
                    player.action = game_file.get_player_input()
                    game_file.screen.fill(game_file.black)

                    if player.action.lower() == 'rip it off':
                        message = (
                            'You choose to brute force your way through a delicate letter. Your choice, not mine... '
                            'The crimson seal is strong enough to oppose your first attempt at ripping it off. '
                            'But, since you are very stubborn, you try again, and you rip half of the letter along with the seal. '
                            'Succces.')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)

                        message = ('However, the damage done to the letter isn\'t too bad, and you can still read it. '
                                   'The two halves can be put together. The paper is stained with a dried black sludge. The handwriting is frantic, as if penned by a soul trapped in eternal torment. '
                                   'It unveils the grim history of this place, a sanctuary turned into a house of horrors. You read the following...')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)

                    elif player.action.lower() == 'slice it open':

                        game_file.play_music('Music\open_letter.mp3')

                        message = 'Gentle does it. Be the scalpel, not the hammer.'
                        game_file.display_message(1, message)
                        time.sleep(2)
                        game_file.screen.fill(game_file.black)

                        if player.pclass == 'room 09':
                            message = (
                                'You reach for one of your hairpins and try to use its sharp point to open the letter.'
                                'The seal is tougher than you expected. After a bit of struggle, you succeed. ')
                            game_file.display_message(1, message)
                            time.sleep(5)
                            game_file.screen.fill(game_file.black)

                        elif player.pclass == 'room 13':
                            message = (
                                'There was not a time when your pen didn\'t come in handy. It always serves you right, no matter the job. '
                                'You take out your pen with the grace of a swordsman and carefully remove the crimson seal from the letter '
                                'Another success. ')
                            game_file.display_message(1, message)
                            time.sleep(5)
                            game_file.screen.fill(game_file.black)

                        elif player.pclass == 'room 256':
                            message = (
                                'It looks likey were right to gift you a pocket knife. A businessman\'s surprise tool, they said. '
                                'So then, time to put it to work. A smooth quick slash later, the letter stands opened before you. '
                                'Good job, knife. And good job, you.')
                            game_file.display_message(1, message)
                            time.sleep(5)
                            game_file.screen.fill(game_file.black)

                    game_file.play_music('Music\letter_read.mp3', loops=-1)

                    message = f'Dear {player.name}, '
                    game_file.display_message(1, message)
                    message = (
                        'Be not surprised, as these events were bound to happen. All of us knew. Except for, well, you. ')
                    game_file.display_message(1, message, (50, 110))
                    message = (
                        'The reason you are reading this is because I wanted you to. That is correct. Me. And my choice. ')
                    game_file.display_message(1, message, (50, 160))
                    message = (
                        'The choice to break free of the Great Plan. Of...him. The shadow. The pursuer. The reason for my torment. ')
                    game_file.display_message(1, message, (50, 210))
                    message = (
                        'My punishment is eternal, now I know this. But I will try to ensure the salvation of my hotel. To rid it of its curse. ')
                    game_file.display_message(1, message, (50, 260))
                    message = (
                        'This, that you hold in your hands, is a chronicle of unspeakable events that have happened between these very walls. ')
                    game_file.display_message(1, message, (50, 310))
                    message = (
                        'The hotel is as old as 300 years old. It was supposed to be a beacon in the night for weary travelers. ')
                    game_file.display_message(1, message, (50, 360))
                    message = (
                        'A refuge for those in need. A place where people could be safe in the night. Somewhere where there would be no harm. ')
                    game_file.display_message(1, message, (50, 410))
                    message = (
                        'And it was, for quite some time. In those old days, Hotel Margot was one of a kind. A sanctuary through and through. ')
                    game_file.display_message(1, message, (50, 460))
                    message = (
                        'There was not a soul that had anything ill to say about my hotel. These grounds were marked by kindness and safety. ')
                    game_file.display_message(1, message, (50, 510))
                    message = (
                        'That was all changed in a dreadful night, marked by a red moon and a cold, freezing wind, when they arrived.')
                    game_file.display_message(1, message, (50, 560))
                    time.sleep(5)
                    game_file.screen.fill(game_file.black)

                    message = (
                        'A group of people dressed in red gowns, like the moon itself. A single black, vertical stripe marked each of their foreheads.')
                    game_file.display_message(1, message)
                    message = (
                        'They came and promised things we could only dream of. A life that would never end, devoid of any kind of pain. Youth, eternal. ')
                    game_file.display_message(1, message, (50, 110))
                    message = (
                        'All in exchange for our loyalty. Loyalty signed in blood. And, the Hotel Margot. Relinquish the claim over its grounds, for it to be forever cursed. ')
                    game_file.display_message(1, message, (50, 160))
                    message = (
                        'We did just that. Unknowingly selling our souls and lives to darkness and evil. The Hotel Margot became a place tainted by blood and death. ')
                    game_file.display_message(1, message, (50, 210))
                    message = (
                        'Many of us died. And many more, that came to seek shelter between its walls. Sacrifices to a god beyond our time and existence. ')
                    game_file.display_message(1, message, (50, 260))
                    message = (
                        'A god that would require endless rivers of blood and pain. A god of death. Or rather, of undeath. ')
                    game_file.display_message(1, message, (50, 310))
                    message = (
                        'And so, the rest of us that remained, for partaking in these blasphemies and perversions of life, were given what we bargained for. ')
                    game_file.display_message(1, message, (50, 360))
                    message = (
                        'A curse. Along with an eternal guest of the Hotel. Forever bound in servitude to him. That was, until I broke free. ')
                    game_file.display_message(1, message, (50, 410))
                    message = (
                        'The Great Plan had been laid out to us from the very beginning. You were prophesied to arrive to Hotel Margot, along with your blood. ')
                    game_file.display_message(1, message, (50, 460))
                    message = (
                        'Your blood is that of an ancient family, known for being close to the Saints. A blood so pure and innocent, evil shakes at the thought of it.')
                    game_file.display_message(1, message, (50, 510))
                    message = (
                        'And so, your sacrifice would ensure darkness would hold the grasp in this world for a very long time. Hence, I thwarted as much as I could of the Plan.')
                    game_file.display_message(1, message, (50, 560))
                    time.sleep(5)
                    game_file.screen.fill(game_file.black)

                    message = (
                        'The five objects of the red room are all mine. Blood of mine spilled on each of them, and they were sanctified by God. ')
                    game_file.display_message(1, message)
                    message = (
                        'The act of allying with God has given me the power to overcome the shadow\'s will. But even so, I could not escape him. ')
                    game_file.display_message(1, message, (50, 120))
                    message = (
                        'It was enough to give you the help and information that you needed. I hope you chose the right object, for only with it can you hope to destroy the shadow. ')
                    game_file.display_message(1, message, (50, 180))
                    message = (
                        'As for the Hotel Margot, your blood will cleanse it and bring peace to it. And all the restless souls within it. Me included. ')
                    game_file.display_message(1, message, (50, 230))
                    message = (
                        'Destroy the shadow, and the cult will fall with it. Trust your gut. At some point, your blood will have to meet my object. I put my last ounce of faith into you.')
                    game_file.display_message(1, message, (50, 280))
                    message = 'May faith be your guide. '
                    game_file.display_message(1, message, (50, 330))
                    message = 'Yours in dread, '
                    game_file.display_message(1, message, (50, 400))
                    message = 'Count Elrah'
                    game_file.display_message(1, message, (50, 420))
                    time.sleep(5)
                    game_file.screen.fill(game_file.black)

                    message = (
                        'Having read these words, you take a second to ponder everything. It almost all makes sense. '
                        'How you felt that everything is tied to you... Made, and placed for you. It isn\'t some egotistical thought. '
                        'It is a reality. And this reality is very scary. You don\'t feel like you are up to the task Count Elrah has given you. '
                        'Your head starts hurting, and it feels like it will only get worse. You do not understand how exactly to destroy the shadow. '
                        'Or where. You remember what the reception told you. The main lobby is the end point for all of it. It\'s where you need to be. '
                        'A few hours ago, you wouldn\'t have thought any of this would be possible. That it\'s pure fantasy to think of these things. '
                        'That\'s changed. You\'re changed. You take a few more minutes to rest before standing up. Scared, for sure, but also faithful, and, '
                        'with a bit of luck, confident. This letter has given you the direction that you needed. It brought to you a larger perspective. '
                        'And a purpose. You feel like you owe Count Elrah your life. He sacrificed himself for this knowledge to get to you. '
                        'If it weren\'t for him, you would have been clueless, and you would have fallen right into the cult\'s death trap. '
                        'You will destroy them before any of that happens. ')
                    game_file.display_message(1, message)
                    time.sleep(5)
                    game_file.screen.fill(game_file.black)

                elif player.action.lower() == 'don\'t open the letter':
                    player.inventory.append('Unopened Letter')

                    if 'Cursed Mark' in player.inventory:
                        message = (
                            'Perhaps whatever is written on this letter is not meant for prying eyes. You think this while clutching your mark on the arm. '
                            'Even though, it might have helped getting rid of...your affliction. Or perhaps, it could have made it worse. '
                            'Anyway, you need to continue searching for the slightest clue as to what\'s going on. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)

                    else:
                        message = (
                            'Perhaps whatever is written on this letter is not meant for prying eyes. There is a slim chance it could hide a clue... '
                            'But it is a chance nonetheless. Anyway, best to search other things for it. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)

                else:
                    message = ('I did not understand that. Please repeat. ')
                    game_file.display_message(1, message)
                    time.sleep(2)
                    game_file.screen.fill(game_file.black)
                    continue
            break

        game_file.screen.blit(game_file.level2_img_red, (0, 0))

        message = (
            'You stand up shortly after your internal monologue and take a look around. The Lounge is a room with turquoise, dirty walls, supported by '
            'gold tinted-columns. A grand chandelier hangs from the middle of its ceiling. The chandelier seems to have been unused for a long time. '
            'The red candles have melted away and covered the chandelier in a web of wax. A parfumed scent can be still felt from it. '
            'The room itself is decorated by paintings on the walls. Large and small paintings, with frames of golden or brown colour, are spread all over. '
            'Almost as if they didn\'t know what to fill the space with. As you step closer to one of them, you spot a reddish, nearly washed away, stain, '
            'behind one of the paintings. Then you see another, at the next painting. This one is larger and less washed away. The sudden realization hits you: '
            'These paintings are all hiding these stains, which, with no doubt now, are blood. How could this hotel still have actual clients book rooms with the state that it is in? '
            'A bar is present in the middle of the lounge. The bartender seems absent, cleaning away at a glass. '
            'The chair and couches laying around are empty. The entire Lounge is devoid of any life and movement, except you and the bartender. '
            'Given how there is no visible clue at hand, you decide to ask him a few things. '
            'While walking towards the bar, you pass a painting of a man dressed in a black, purple-striped vest, with a ruffled shirt underneath. '
            'Blood red buttons are adorning the vest. A single golden button holds the sleeve tight. His shirt\'s collar is also red, with golden edges. '
            'The painting surprised him in a nonchalant posture, mischievously, but elegantly, watching you. A faint smile can be traced on his young face. '
            'The man seems in his early 30\'s. His black eyes let off such a feeling of sadness, that it forces you to obediently look downwards, as to avoid it. '
            'Brown-tinted letters read, in the left corner: Count Elrah Margot, 1773.')
        game_file.display_message(1, message)
        time.sleep(5)
        game_file.screen.fill(game_file.black)

        game_file.play_music('Music\drama.mp3', loops=-1)

        if 'Opened Letter' in player.inventory:
            message = (
                'So this is him. The one that wrote and left you the letter. The man that, in a strange way, tried saving your life. '
                'And gave his in doing so. You notice a detail that eluded your sight before: a silver, shining ring, on his ring finger. '
                'In fact, that\'s what he is actually holding. A silver...bullet? Why would anyone be immortalized while holding something as peculiar as a silver bullet?')
            game_file.display_message(1, message)
            time.sleep(5)
            game_file.screen.fill(game_file.black)

        if 'Cursed Mark' in player.inventory:
            message = (
                'This is the same man from the black room. How do you just now think of it? He was there. You saw him get dragged away into the closet. '
                'But he didn\'t even look at you when you entered. It was as if you weren\'t really there. So then, was he? '
                'It must be real. The gunshot was, for sure. If he is holding a bullet in this painting, and he shot the gun, then he must be a gun '
                'enthusiast. Could there be a connection? Did he shoot a silver bullet? Was it supposed to hurt the shadow? '
                'Now this, just gave you more questions than answers. Or maybe... ')
            game_file.display_message(1, message)
            time.sleep(5)
            game_file.screen.fill(game_file.black)

        message = (
            'As you pass the eerie painting and approach the bar, you feel an inexplicable chill run down your spine. Ignoring the unsettling atmosphere, you pull a stool closer and take a seat. '
            'The bartender, a gaunt figure with sunken eyes, continues methodically cleaning a glass with an almost robotic precision. '
            'His pallid complexion is striking, as if drained of life itself, and his gaze never seems to meet yours. '
            'It\'s as if he exists in a world of his own, detached from the dimly lit surroundings. '
            'As you open your mouth to ask your question, he drops the towel and the glass, and, with the same expression, turns aside and points with his arm and hand '
            'toward the hall leading out of the lounge. It is the hall that leads to the Main Lobby. You stand up and set on towards it. ')
        game_file.display_message(1, message)
        time.sleep(5)
        game_file.screen.fill(game_file.black)

        player.check3 = True


def room4():
    message = 'Level 4: Main Lobby'
    game_file.display_message(1, message, (385, 70))
    time.sleep(2)
    game_file.screen.fill(game_file.black)

    while player.check4 is False:

        game_file.screen.blit(game_file.level4_img_guard, (0, 0))

        game_file.play_music('Music\dread.mp3', loops=-1)

        message = (
            'Walking down the hall towards the Main Lobby, you arrive at its entrance. A large, tall man is standing there. '
            'His mask is made of bone, with ornate symbols etched into it. As you get closer, you realize he is towering over you. '
            'He says not a word. He is wearing a black and red elegant costume, made out of pants and a vest. '
            'His hand reaches forward, expecting to be given something. His black eyes can be seen through the mask. '
            'He is not patient. You must give him what he needs. But what is it?')
        game_file.display_message(1, message)
        time.sleep(5)
        game_file.screen.fill(game_file.black)

        while True:
            if len(player.inventory) > 0:
                message = 'He requires an item, you think. Must be something that will grant you access.'
                choices = []

                for i in player.inventory:
                    choices.append('>Hand over the ' + i)

                game_file.display_message(1, message)
                game_file.display_message(2, choices, (50, 90))
                player.action = game_file.get_player_input()
                game_file.screen.fill(game_file.black)

                message = 'Are you sure this is the right item?'
                choices = ['>Yes', '>No']
                game_file.display_message(1, message)
                game_file.display_message(2, choices, (50, 90))
                player.temp_check = game_file.get_player_input()
                game_file.screen.fill(game_file.black)

                if player.temp_check.lower() == 'yes':

                    if player.action.lower() == 'hand over the vip ticket':
                        message = (
                            'You slowly remove your VIP ticket out of your pocket and hand it over. For a second, you believe '
                            'this was the wrong choice. The large man holds the ticket in the air, as if it was an offering. The ticket is simply '
                            'set ablaze at once and it visibly turns to dust. The man repeats the same movement like the bartender: '
                            'he moves to the side and extends his arm towards the entrance. \'You\'re expected\', he says with a deep voice. ')
                        game_file.display_message(1, message)
                        player.inventory.remove('VIP Ticket')
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)
                        break

                    # Death ending nr. 4
                    elif 'hand over the' in player.action.lower():
                        message = (
                            f'You hand him the {player.action.lower()[13:]}. He holds it in his hand for a second, then proceeds to crush it. '
                            f'His black eyes settle upon you. A piercing gaze, quite literally. You feel your heart being strangled. '
                            f'As if an unseen force has grasped it and is now squeezing it, almost ripping out of you. He walks slowly towards you. '
                            f'By the time he reaches you, you are on the floor, frantically gasping for air. His hand reaching for you is the last thing you see, '
                            f'as you pass out. This is the end.')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)

                        player.change_state()
                        player.check4 = True
                        break

                    else:
                        message = 'I did not understand that. Please repeat. '
                        game_file.display_message(1, message)
                        time.sleep(2)
                        game_file.screen.fill(game_file.black)
                        continue


                elif player.temp_check.lower() == 'no':
                    continue

                else:
                    message = 'I did not understand that. Please repeat. '
                    game_file.display_message(1, message)
                    time.sleep(2)
                    game_file.screen.fill(game_file.black)
                    continue

            else:

                # Death Ending nr. 5
                message = (
                    'After giving you a short look, he lowers his hand and stays still for a good minute. His gaze is fixed upon you all this time. '
                    'Shivers running down your spine tell you this is not the optimal scenario. You try turning away, but as soon as your body moves, '
                    'his is before you. He grabs you by your chest. You feel your heart being strangled. '
                    'As if an unseen force has grasped it and is now squeezing it, almost ripping out of you. The last thing you see is his bone mask, '
                    'and his void black eyes. You pass out. This is the end. ')
                game_file.display_message(1, message)
                time.sleep(5)
                game_file.screen.fill(game_file.black)

                player.change_state()
                player.check4 = True
                break

        game_file.screen.blit(game_file.level4_img_party1, (0, 0))

        game_file.play_music('Music\level4.mp3', loops=-1)

        message = (
            'You walk carefully, but hastily, to the entrance. You are careful not to touch or interact with the man in any way. '
            'Upon entering the Main Lobby, you set your sight on the people before you. Their red masks shine in the eerie, dim, orange light of the Lobby. '
            'They all wear black suits and different red masks. There are multiple groups of them. Some wear masks depicting animals, some wear masks '
            'depicting human faces surprised in various emotions, while a few, wear masks of otherwordly, monstrous creatures. '
            'None of them seems to have noticed your presence. They carry along with their weird masked ball. They chat among themselves and drink cocktails. '
            'Not a great variety in cocktails, you think, as most of them match the colour of the masks. What a themed party. '
            'They are sitting around on couches, chairs, forming small groups around the place. One thing that seems out of place is the lack of music. '
            'What kind of ball has no music? Only their incessant discussions in the form of whispers can be heard. Hisses, almost. '
            'The bartender here seems just as lively as the other one. He doesn\'t even mix the drink, just pours it from the tap. '
            'Isn\'t the tap meant for beer, though? Must be a strong punch. The guard said they were expecting me. They don\'t seem very fond of my presence, so far. ')
        game_file.display_message(1, message)
        time.sleep(5)
        game_file.screen.fill(game_file.black)

        if 'Cursed Mark' in player.inventory:
            message = (
                'You grasp the mark on your arm. It is unbelievably hot, and it is pulsing, as if it\'s alive. You must snuff out this semblance of life. '
                'As you do this, a few of the people before you slowly turn their heads towards you. It is a behavior that is picked up by more and more of them. '
                'You realize the whispers and hissing is mostly gone now. You have their attention. A light akin to a twilight with purple undertones is now basking everyone in the lobby. '
                'The atmosphere has got much heavier. You get the feeling they are eagerly waiting for every breath you draw. It anticipates the moment of the last. ')
            game_file.display_message(1, message)
            time.sleep(5)
            game_file.screen.fill(game_file.black)

        elif 'Opened Letter' in player.inventory:
            message = (
                'The dim light is one thing you have had enough of in this hotel. Makes everything feel so uncomfortable and...agitated. '
                'As soon as you think that, the light dims even more. The whole lobby is now basked in a twilight with purple undertones. '
                'Party is getting weirder. Too bad you are here to break it. This must be the cult the Count has spoken of. You don\'t wait for shivers to run down your spine, this time. '
                'You know what you have to do. Question is...how? How does one go about facing a shadow and an entire cult? The objects in the red room should lend you a metaphorical hand here. ')
            game_file.display_message(1, message)
            time.sleep(5)
            game_file.screen.fill(game_file.black)

        elif 'Unopened Letter' in player.inventory:
            message = (
                'So then, whatever is going down will go down nevertheless here. With these people. Or whatever they are. If anything I have will come in handy, now is the time '
                'to look for it.')
            game_file.display_message(1, message)
            time.sleep(5)
            game_file.screen.fill(game_file.black)

        game_file.screen.blit(game_file.level4_img_party2, (0, 0))

        message = (
            'As these thoughts go through your mind, the air quickly becomes denser. It gets hard to breathe. The people in the lobby stop any form of activity and stand up to watch you dead in the eye. '
            'A few groups start surrounding you. They are all coordinated, as if controlled by a hive mind. They close in on you, forcing you to advance towards the others. '
            'The monstrous masks seem to be the bosses, as they simply wait the prey to be delivered to them. The human masks start chanting in a foreign language. '
            'The animal masks are their grunts. As the human masks chant, the air loses density, but you can now see this density gain a shape: a corporeal shadow, towering over everyone in the lobby. '
            'It reaches as high as the ceiling. The monstrous masks take their masks off and reveal the palid faces beneath. Their facial features are sharp and bone-like, reminiscent of the tall man with the '
            'bone mask. They have an almost skeletal appearance, even vampiric. Their eyes are of a deep red, small and fixated on you. With the same coordination, each of them takes a dagger and stabs themselves in the gut. '
            'They drop to their knees and accompany the chanting with their screams. These continous screams are a reverence to the shadow. ')
        game_file.display_message(1, message)
        time.sleep(5)
        game_file.screen.fill(game_file.black)

        while player.check4 is False:

            game_file.screen.blit(game_file.level4_img_evil, (0, 0))

            game_file.play_music('Music\level4.mp3', loops=-1)

            message = (
                'You must reach deep into yourself and bring out your innermost trait. The information you have received and collected so far will make the difference. What will you do now? ')
            choices = ['>Stand and fight', '>Run towards the second exit', '>Offer yourself to the shadow']
            game_file.display_message(1, message)
            game_file.display_message(2, choices, (50, 130))
            player.action = game_file.get_player_input()
            game_file.screen.fill(game_file.black)

            # Good Endings - 3 endings + 1 extras
            if player.action.lower() == 'stand and fight':

                while True:
                    if len(player.inventory) > 0:
                        message = (
                            'You need to check your pockets. Whatever you have, you must use it. It\'s now or never. ')
                        choices = []
                        for i in player.inventory:
                            choices.append('>' + i)
                        game_file.display_message(1, message)
                        game_file.display_message(2, choices, (50, 110))
                        message = 'What will you do with these items?'
                        choices = ['>Combine the items', '>Renounce the items']
                        game_file.display_message(1, message, (50, 320))
                        game_file.display_message(2, choices, (50, 330))
                        player.action = game_file.get_player_input()
                        game_file.screen.fill(game_file.black)

                        if player.action.lower() == 'combine the items':
                            message = 'Which items will you combine?'
                            choices = []

                            if 'Magnifying Glass' in player.inventory and 'Black Mirror' in player.inventory:
                                choices.append('>Combine the magnifying glass and the black mirror')

                            if 'Fuse' in player.inventory and 'Silver Ring' in player.inventory:
                                choices.append('>Combine the fuse and the silver ring')

                            if 'Magnifying Glass' in player.inventory and 'Ancient Tome' in player.inventory:
                                choices.append('>Combine the magnifying glass and the ancient tome')

                            game_file.display_message(1, message)
                            game_file.display_message(2, choices, (50, 90))
                            player.action = game_file.get_player_input()
                            game_file.screen.fill(game_file.black)

                            # Loop for Stand And Fight endings
                            while True:

                                game_file.play_music('Music\epic.mp3', loops=-1)

                                # Ending 1 - Darkness Pierced Variation
                                if player.action.lower() == 'combine the magnifying glass and the black mirror':
                                    message = (
                                        'The gloomy light coming through the magnifying glass seems to clear itself and come out pure. '
                                        'By taking the magnifying glass to the black mirror, the purity of the light starts dispelling the blackness of the mirror. '
                                        'As you hold them aloft, their energies resonate and intertwine, creating a blinding vortex of light and shadow. '
                                        'The people of the lobby now rather resemble gaunt-faced creatures, with vampiric features. '
                                        'They wail as the light and shadow dance around you, seemingly forced to go after you. They vaporize at the touch of the vortex. '
                                        'The shadow grows larger, but it is now erratic, chaotic, spreading everywhere and trying to push as many creatures towards you. '
                                        'It is scared. The vortex becomes faster and faster, creating a sound akin to hearing a tornado through the creaks of a window. '
                                        'The vampiric creatures ignore the shadow and are now trying to escape the vortex. The entire Lobby is affected by it, as the '
                                        'walls are shaking and cracking, and the chandelier is swinging wildly. '
                                        'With a mighty burst of energy, a colossal portal emerges, bridging the gap between worlds. '
                                        'It draws the shadow into its depths, along with several vampiric creatures. The shadow is fighting, trying to escape, but the light binds it '
                                        'and the darkness pulls on it. The shadow is visibly being ripped apart. It screams in agony.')
                                    game_file.display_message(1, message)
                                    time.sleep(5)
                                    game_file.screen.fill(game_file.black)

                                # Ending 2 - Shine of Tomorrow Variation
                                elif player.action.lower() == 'combine the fuse and the silver ring':
                                    message = (
                                        'Equipped with the Silver Ring, Count Elrah\'s symbol against evil, and the Magnifying Glass, you confront the shadow that engulfs the Main Lobby. '
                                        'The shadow grows more menacing as you approach, and the people, now emerging with vampiric features from under their masks, hiss and growl, eager to draw your blood. '
                                        'You activate the Fuse, creating a blinding explosion of light. The Silver Ring catches the light onto itself and purifies it, enhancing it tenfold. '
                                        'You are now holding a shining halo in your hand, blinding everyone in the lobby. The shadow\'s power is visibly being diminished by the light. '
                                        'The vampiric creatures flee to hide from the light or get burnt from being too close. With a grave sound, the shadow rushes towards you. '
                                        'It is its last attempt at defeating you. A long, black arm extends towards you, as coming from an abyss, its claws almost reaching you. '
                                        'The light denies it from hurting you in any way. The shadow is being ripped apart by the light. It screams and wails with otherwordly sounds. '
                                        'Its orange, mad eyes are fixating you. You are looking true evil in the face. With mercy in your heart, you extend your arm to the shadow\'s. '
                                        'And grab it. As you grab it, the shadow is consumed by the light, filling all its evil with purity. It explodes and dissipates into thin air with a last scream. '
                                        'The remaining vampire creatures fall to the ground. The entire lobby goes dark for a few seconds, only to make place to the warm, inviting light, falling through its ceiling. '
                                        'The chandelier ignites gently, its flames now reminding of a peaceful hearth. ')
                                    game_file.display_message(1, message)
                                    time.sleep(5)
                                    game_file.screen.fill(game_file.black)

                                # Ending 3 - Flames of Salvation Variation
                                elif player.action.lower() == 'combine the magnifying glass and the ancient tome':
                                    message = (
                                        'The gloomy light coming through the magnifying glass seems to clear itself and come out pure. '
                                        'With this in mind, you open the Ancient Tome that was in the Red Room. '
                                        'You see bloody drawings and symbols, markings, belonging to the occult. '
                                        'You take a wild guess and believe what you have in your hands now is a tome containing witchcraft, rituatls and the like. '
                                        'And perhaps, it is not even a random tome. It might hold special importance. Count Elrah has given it for a reason. '
                                        'What you thought were people now turn out to be something akin to vampires, with very gaunt and sharp features. They hiss and growl, ready to pounce on you. '
                                        'The shadow enlarges itself and seems to be covering the entire Main Lobby in a dome of darkness. The only logical move here is obvious. '
                                        'With no other source of heat in your vicinity, you reflect the chandelier\'s light towards the tome. The purified light acts instantly. '
                                        'The tome catches on fire, with the blood and black ink on it gaining...life? They shrivel and writhe, but to no avail. '
                                        'The fire consumes them and pages of the book. The shadow is visibly hurt by this, as its shreaks hurt your ears. The vampiric creatures follow its example. '
                                        'You seem to have hurt the hivemind. The tome might be the same tome used to have summoned this creature of darkness. It binds it here. '
                                        'The entire tome is engulfed by the fire, radiating a heat that expunges your enemies. The shadow catches on fire too, burning in agony. '
                                        'In a matter of minutes, nothing is left of the shadow, nor of its evil and heavy presence. The air is no longer hard to breathe. '
                                        'A feeling of serenity fills you. Calmness.')
                                    game_file.display_message(1, message)
                                    time.sleep(5)
                                    game_file.screen.fill(game_file.black)

                                else:
                                    message = 'I did not understand that. Please repeat. '
                                    game_file.display_message(1, message)
                                    time.sleep(2)
                                    game_file.screen.fill(game_file.black)
                                    continue

                                break

                            # Good Ending - As The Dust Settles

                            game_file.screen.blit(game_file.level4_img_good, (0, 0))

                            game_file.play_music('Music\good_ending.mp3', loops=-1)

                            message = (
                                'As the dust settles, you find yourself standing in a transformed Main Lobby. '
                                'The curse is lifted, and the once malevolent shadows have given way to warm, inviting light. '
                                'The hotel is free from the darkness that plagued it for centuries. '
                                'Several of the creatures are laying around, their masks shattered and their humanity returned to them. '
                                'They are weak and frail, and will need help to fully restore. The calmness of the Main Lobby brings '
                                'tranquility to your heart. Your journey comes to an end, leaving you with a sense of fulfillment and accomplishment. ')
                            game_file.display_message(1, message)
                            time.sleep(5)
                            game_file.screen.fill(game_file.black)
                            player.check4 = True

                            # Good Ending - Extra Scene
                            if 'Cursed Mark' in player.inventory:
                                message = (
                                    'As you walk out of the hotel, your Cursed Mark, no longer glowing, remains etched onto your skin. An evil chill is felt as you lay eyes on it. '
                                    'No longer scared, you valiantly brush it off and have faith in what is to come. ')
                            game_file.display_message(1, message)
                            time.sleep(5)
                            game_file.screen.fill(game_file.black)

                            break

                        elif player.action.lower() == 'renounce the items':
                            message = (
                                'None of these items have any real value. They are all just...random objects. You do not see how any of them could stop an entire army of people. '
                                'And the shadow. Best to let them be and see if there is anything else in the Main Lobby that could help you. ')
                            game_file.display_message(1, message)
                            time.sleep(5)
                            game_file.screen.fill(game_file.black)
                            player.inventory = []
                            player.action = 'run towards the second exit'

                        else:
                            message = 'I did not understand that. Please repeat. '
                            game_file.display_message(1, message)
                            time.sleep(2)
                            game_file.screen.fill(game_file.black)
                            continue

                    else:
                        message = ('Sadly, your pockets are empty. You do not own any items to defend yourself with... '
                                   'This only leaves two choices...')
                        choices = ['>Run towards the second exit', '>Offer yourself to the shadow']
                        game_file.display_message(1, message)
                        game_file.display_message(2, choices, (50, 120))
                        player.action = game_file.get_player_input()
                        game_file.screen.fill(game_file.black)
                        break

            # True Endings - 5 endings + 2 extras
            elif player.action.lower() == 'run towards the second exit':
                message = (
                    'You are surrounded here. You must gain better ground. Or, be somewhere close to the exit, in case things go awry. '
                    'The main exit seems to be the answer here. ')
                game_file.display_message(1, message)
                time.sleep(5)
                game_file.screen.fill(game_file.black)

                message = (
                    'You dart to the exit and find yourself on an elevated scene of sorts. You see all of them coming towards you. Their vampiric features have now '
                    'surfaced. The shadow is behind them, controlling and pushing them forward. ')
                game_file.display_message(1, message)
                game_file.screen.fill(game_file.black)

                if 'Ancient Tome' not in player.inventory:
                    message = (
                        'You spot a large book sitting on your right, on a white, circular chair. It looks just like the one from the Red Room. '
                        'This could be your second chance to pick the right option. ')
                    game_file.display_message(1, message)
                    game_file.screen.fill(game_file.black)

                elif 'Ancient Tome' in player.inventory:
                    message = (
                        'Before your eyes flashes a short vision: the Ancient Tome, sitting wide opened on the table from the Red Room. '
                        'The image moves closer, towards revealing its pages. A fast flurry of pages go by, until it reaches the page depicting the shadow. '
                        'The shadow\'s eyes can be seen glowing, and as you get closer, it tries dragging you in. '
                        'The Ancient Tome is the one containing the Shadow, then. It must be destroyed.')
                    game_file.display_message(1, message)
                    time.sleep(5)
                    game_file.screen.fill(game_file.black)

                # True Ending section for having the Mark

                game_file.play_music('Music\epic.mp3', loops=-1)

                if 'Cursed Mark' in player.inventory:
                    message = (
                        'You pick up the Ancient Tome and hold it tightly. As you open it, your entire body freezes. The mark on your arm responds to it. '
                        'You feel the connection between the two. The tome\'s pages are covered in various symbols and markings, all done in an ink that resembles your mark. '
                        'It writhes and moves, almost as if it\'s alive. Some of the pages are stained by blood. Rituals, must be. '
                        'You can almost hear the shadow whispering. You feel its voice inside your head. You want it to get out. It won\'t stop. '
                        'It is fearful. Scared of what you might do with the ancient tome. This is its weakness. ')
                    game_file.display_message(1, message)
                    time.sleep(5)
                    game_file.screen.fill(game_file.black)

                    # Loop for True Ending
                    while True:
                        message = (
                            'Will you use the Ancient Tome by itself? Or perhaps, you will combine it with another item from the Red Room?')
                        choices = ['>Use the Ancient Tome by itself', '>Combine the Ancient Tome']
                        game_file.display_message(1, message)
                        game_file.display_message(2, choices, (50, 100))
                        player.action = game_file.get_player_input()
                        game_file.screen.fill(game_file.black)

                        # Ending 4 - Tears of Silver

                        game_file.play_music('Music\letter_read.mp3', loops=-1)

                        if player.action.lower() == 'use the ancient tome by itself':
                            message = (
                                'The tome alone will do. So you hope. The connection between you, or rather, the shadow, and the book is undeniable. '
                                'The whispering is louder and louder, and it even suppresses your own thoughts. You can not begin to process or think about how to handle this. '
                                'The vampiric creatures are getting closer to you. One comes from the side and reaches your arm, trying to throw you to the ground. '
                                'In a panic, you do the only thing anyone would do in your situation: you use the ancient tome to bash its head. A hit is enough. '
                                'The creature is taken down. The blood that was splattered from the hit landed on the pages. The symbols glow crimson and spread all over the page. '
                                'Your arm is shaking uncontrollably, now taken by the Cursed Mark\'s power. The tome is activated by blood, of course. This is what strengthens the shadow. '
                                'So then, the opposite of blood must stop everything. But what is it the opposite of blood? As you try to get a grasp of yourself, all seems lost. '
                                'The whispers are now loud voices that suppress your own thoughts, your own body is being slowly taken by the shadow and the creatures are reaching their hands '
                                'to grab you. Yet again, you do the only thing anyone would do in your situation: you weep. You cry, as everything is taken out from under you. '
                                'The shadow swallows the last dim light. ')
                            game_file.display_message(1, message)
                            time.sleep(5)
                            game_file.screen.fill(game_file.black)

                            message = (
                                'As your tears roll down your cheeks, they catch a glitter of hope. Quite literally. Your tears are the only source of light in that dark place. '
                                'A rain of tears tears through the ancient tome, as if they were acid. The tome starts disintegrating into thin air, your tears undoing its corruption and '
                                'rituals. The symbols and markings on it disappear, writhing away to their deaths. The vampiric creatures all scream in unison, in agony, falling to the ground. '
                                'Some who touched you also disintegrate. The shadow\'s darkness is filled with holes of light, akin to the ancient tome. The tome kept it binded to this world. '
                                'Its screams of agony vibrate through your head and make you pass out...')
                            game_file.display_message(1, message)
                            time.sleep(2)
                            game_file.screen.fill(game_file.black)

                        elif player.action.lower() == 'combine the ancient tome':
                            message = 'What will you combine it with?'
                            choices = []
                            temp_choices_0 = ['Silver Ring', 'Magnifying Glass', 'Rosary',
                                              'Perfumed Satchel',
                                              'Black Mirror']
                            temp_choices_1 = ['combine the ancient tome with the magnifying glass',
                                              'combine the ancient tome with the silver ring',
                                              'combine the ancient tome with the black mirror']
                            temp_choices_2 = ['combine the ancient tome with the perfumed satchel',
                                              'combine the ancient tome with the rosary']

                            if 'Magnifying Glass' in player.inventory:
                                choices.append('>Combine the ancient tome with the magnifying glass')
                            if 'Silver Ring' in player.inventory:
                                choices.append('>Combine the ancient tome with the silver ring')
                            if 'Black Mirror' in player.inventory:
                                choices.append('>Combine the ancient tome with the black mirror')
                            if 'Perfumed Satchel' in player.inventory:
                                choices.append('>Combine the ancient tome with the perfumed satchel')
                            if 'Rosary' in player.inventory:
                                choices.append('>Combine the ancient tome with the rosary')
                            else:
                                pass

                            if choices:
                                game_file.display_message(1, message)
                                game_file.display_message(2, choices, (50, 90))
                                player.action = game_file.get_player_input()
                                game_file.screen.fill(game_file.black)

                            while True:
                                item_check = 0
                                for i in temp_choices_0:
                                    if i not in player.inventory:
                                        item_check += 1
                                if item_check == 6:
                                    message = (
                                        'You have nothing on you that could be combined with it. Your only option is to use it as it is. ')
                                    game_file.display_message(1, message)
                                    game_file.screen.fill(game_file.black)
                                    break

                                # Ending 5 - Mouth of Darkness
                                if player.action.lower() in temp_choices_1:

                                    game_file.screen.blit(game_file.level4_img_shadow, (0, 0))

                                    message = (
                                        'No matter what you\'re trying to do with your items, it just won\'t work. '
                                        'The vampiric creatures are being pushed towards you by the shadow. It stays behind them, controlling each and every one. '
                                        'The light of the room is slowly filled by the darkness of the shadow. Your cursed mark is the only one glowing with a crimson glow. '
                                        'Your arm starts twitching uncontrollably, dragging you towards the mass of creatures. You try to fight it, but it easily overpowers you. '
                                        'The arm is no longer listening to you. Slowly, but surely, it\'s spreading to the rest of your body. Your limbs and senses betray you in the most critical moment. '
                                        'You drop to your knees, beaten. Hope is lost now. The shadow towers over you, with its orange mad eyes smiling. '
                                        'A gaping mouth forms out of its darkness. And so ends your...journey. You died.')
                                    game_file.display_message(1, message)
                                    game_file.screen.fill(game_file.black)
                                    time.sleep(5)
                                    player.change_state()
                                    player.check4 = True
                                    break

                                elif player.action.lower() in temp_choices_2:

                                    # Ending 6 - Faith and Despair

                                    game_file.play_music('Music\epic.mp3', loops=-1)

                                    if player.action.lower() == 'combine the ancient tome with the rosary':
                                        message = (
                                            'The vampiric creatures are being pushed towards you by the shadow. It stays behind them, controlling each and every one. '
                                            'The light of the room is slowly filled by the darkness of the shadow. '
                                            'In a daring act of bravery, you hold the Rosary, its beads glowing with a divine light, and the Ancient Tome, a sinister relic pulsating with dark power. '
                                            'As you put the Rosary on the wide opened Ancient Tome, the symbols on the tome writhe and squirm, as if resisting the impending ritual. '
                                            'The shadow seems to be directly tied to the tome, as you can hear its panicked whispers inside your head. '
                                            'Drops of blood-stained history drip from its pages, forming a pool of crimson beneath you. '
                                            'A blinding surge of energy envelops the Main Lobby. The Rosary\'s light clashes with the tome\'s darkness, creating a dazzling spectacle. '
                                            'The very air crackles with intensity as the ritual unfolds, challenging the very fabric of the hotel\'s existence. '
                                            'With a final push of faith, the bindings of the Shadow are shattered. The Ancient Tome, once a source of the hotel\'s curse, disintegrates into ash. '
                                            'The Rosary\'s glow intensifies, banishing the last vestiges of darkness. '
                                            'The Main Lobby transforms, its atmosphere cleansing into an aura of tranquility and hope. '
                                            'You feel lightheaded, as if your energy was just drawn out. You pass out, soundly. ')
                                        game_file.display_message(1, message)
                                        time.sleep(5)
                                        game_file.screen.fill(game_file.black)

                                    # Ending 7 - Fragrance of Purity

                                    game_file.play_music('Music\epic.mp3', loops=-1)

                                    if player.action.lower() == 'combine the ancient tome with the perfumed satchel':
                                        message = (
                                            'Gripping the Perfumed Satchel and the Ancient Tome tightly, you embark on the ritual. '
                                            'The Ancient Tome, its pages stained with drops of blood, resists your touch, but you persist, guided by determination. '
                                            'The shadow seems to be directly tied to the tome, as you can hear its panicked whispers inside your head. '
                                            'A powerful surge of energy envelops the Main Lobby. '
                                            'The Perfumed Satchel releases a soothing aroma, intertwining with the darkness emanating from the tome. '
                                            'The air crackles with a blend of fragrant sweetness and ancient power. '
                                            'In a decisive moment, the bindings of the Shadow snap. The Ancient Tome crumbles into ash, its malevolent essence neutralized. '
                                            'The Main Lobby undergoes a profound transformation, its atmosphere cleansing into an aura of tranquility and hope. '
                                            'You\'ve severed the sinister connection between the cult\'s rituals and the Shadow, saving not only the hotel but also countless souls trapped within. '
                                            'The Perfumed Satchel, now infused with the essence of liberation, remains in your hands. '
                                            'Your journey concludes with the hotel bathed in newfound light, a sanctuary of peace rising from the remnants of an ancient malevolence. '
                                            'However, the battle was not without consequence, as you now feel tired and exhausted. As if your energy was just drawn out. '
                                            'You try to stand, but you end up passing out. ')
                                        game_file.display_message(1, message)
                                        time.sleep(5)
                                        game_file.screen.fill(game_file.black)

                            break

                        else:
                            message = 'I did not understand that. Please repeat.'
                            game_file.display_message(1, message)
                            time.sleep(2)
                            game_file.screen.fill(game_file.black)
                            continue

                        # True Ending - Purification

                        game_file.screen.blit(game_file.level4_img_true, (0, 0))

                        game_file.play_music('Music\good_ending.mp3', loops=-1)

                        message = (
                            'A multitude of faint voices wake you up. Your eyes are greeted by the light that now fills the Main Lobby, and the Hotel Margot itself. A team of medics '
                            'arrived to take care of everyone. You are being carried on a stretcher towards the ambulance. As you turn your head from left to right, you see that the vampiric '
                            'creatures have had their humanity returned to them. They are all passed out, in a circle, around the spot you were taken from. The light flooding the lobby puts a smile on your face, '
                            'as you now know the curse has been lifted. You defeated the shadow. You touch your arm, trying to find the Cursed Mark. All you find is a faint scar, that looks as if it\'s almost healed. '
                            'You\'ve won. You survived. ')
                        game_file.display_message(1, message)
                        time.sleep(5)
                        game_file.screen.fill(game_file.black)
                        player.check4 = True

                        # True Ending - Extra Scene
                        if 'Opened Letter' in player.inventory:
                            message = (
                                'As you are taken outside the hotel, the painting of Count Elrah slowly starts fading away. In its stead, a beautiful scenery of a green meadow, covered in coloured flowers, '
                                'under a golden, warm sun, remains. '
                                'The patches of dried blood around it turn into beautiful floral patterns. The grime and dirt is slowly replaced by patches of green grass. '
                                'A silver ring is picked up by one of the medics. Its shine is beautiful and hence, appraised. The medic leaves it where it was found, to find its way to its owner. ')
                            game_file.display_message(1, message)
                            time.sleep(5)
                            game_file.screen.fill(game_file.black)

                        break

                    break

                # True Ending for not having the mark - Intrusion of Evil
                elif 'Cursed Mark' not in player.inventory:

                    game_file.screen.blit(game_file.level4_img_shadow, (0, 0))

                    message = (
                        'As you put your hand on it, your body freezes. You are unable to move any muscle. You can only move your eyes around. '
                        'The vampiric creatures are creepily making their way towards you. The shadow is slowly pushing them from behind. '
                        'Your entire arm begins to be covered in ritualistic symbols and marking. It spreads all over your body. '
                        'Your eyes are no exception. You see the symbols floating around you, everywhere. They glow and pulse crimson. '
                        'An evil laugh can be heard throughout the Main Lobby. You feel as if your energy, your life force, is being drained away. '
                        'You drop on the floor. The last thing you see is the shadow standing above you, with those glowing, orange eyes. '
                        'An intense cold is spread across your body, as the shadow starts engulfing you. Your journey is over. You died. ')
                    game_file.display_message(1, message)
                    time.sleep(5)
                    game_file.screen.fill(game_file.black)
                    player.check4 = True
                    player.change_state()

                    break

            # Bad Endings - 1 ending + 2 extras
            elif player.action.lower() == 'offer yourself to the shadow':

                game_file.screen.blit(game_file.level4_img_shadow, (0, 0))

                game_file.play_music('Music\\bad_ending.mp3', loops=-1)

                message = (
                    'In a moment of despair, you choose to surrender yourself to the encroaching shadow. '
                    'The Main Lobby grows darker as the malevolent presence envelops you entirely. '
                    'The room seems to sigh in relief as your essence merges with the darkness. ')
                game_file.display_message(1, message)
                time.sleep(5)
                game_file.screen.fill(game_file.black)

                if 'Cursed Mark' in player.inventory:
                    message = (
                        'The cursed mark on your arm pulses once, then fades, as if acknowledging the inevitable. '
                        'The ancient evil claims you, and your existence becomes one with the shadow that has haunted the hotel for centuries. ')
                    game_file.display_message(1, message)
                    time.sleep(5)
                    game_file.screen.fill(game_file.black)

                message = (
                    'Your sacrifice, though heartbreaking, serves a purpose. The hotel\'s curse deepens, but the shadow\'s hunger is momentarily sated.'
                    'The Main Lobby, once a battleground, falls into an eerie stillness. The Cult of the Shadow, sensing victory, withdraws, leaving the hotel in a state of eerie tranquility.'
                    'The world outside continues, unaware of the sacrifice made within the hotel\'s walls. A choice that will affect the world, even if the world knows it not. ')
                game_file.display_message(1, message)
                time.sleep(5)
                game_file.screen.fill(game_file.black)
                player.change_state()
                player.check4 = True

            else:
                message = 'I did not understand that. Please repeat. '
                game_file.display_message(1, message)
                time.sleep(2)
                game_file.screen.fill(game_file.black)
                continue


# Function for the case where a second game is began in the same playthrough and the player stumbles upon their old body
# The room can be stumbled upon OR NOT after the second level/room
def dead_room(temp_inventory):

    game_file.screen.blit(game_file.level4_img_dead, (0, 0))

    game_file.play_music('Music\drama.mp3')

    message = ('Suddenly, the ceiling opens wide open right in front of you. From the gaping darkness comes falling a...'
               'body. It nonchalantly lands on the floor, as if that\'s where it was supposed to be, in the first place. '
               'Upon closer inspection, you notice a crucial detail: the body is faceless. It somehow sports similar clothes to yours...'
               'Quite peculiar, even for this hotel. ')
    game_file.display_message(1, message)
    time.sleep(5)
    game_file.screen.fill(game_file.black)

    while True:
        message = 'So then, will  you rummage through the...thing\'s pockets, or let it rest peacefully? '
        choices = ['>Rummage through pockets', '>Let it rest']
        game_file.display_message(1, message)
        game_file.display_message(2, choices, (50, 90))
        player.action = game_file.get_player_input()
        game_file.screen.fill(game_file.black)

        if player.action.lower() == 'rummage through pockets':
            inventory = []
            message = 'You find and take the following: '
            game_file.display_message(1, message)

            if temp_inventory:
                if 'Cursed Mark' in temp_inventory:
                    message = ('Sadly, the end. The glowing mark on its arm catches life and jumps onto you, as you reach out '
                               'your hand. You can feel it crawling on your skin. It quickly reaches your throat and...'
                               'Snuffs out your life. A tragic end. ')
                    game_file.display_message(1, message, (50, 90))
                    time.sleep(5)
                    game_file.screen.fill(game_file.black)
                    player.change_state()

                elif 'Black Mirror' in temp_inventory:
                    message = ('Sadly, the end. As you draw out what seems to be a black mirror, your eyes meet its glass. '
                               'But the reflection is all wrong. You do not see yourself, but a pair of orange, mad eyes, '
                               'looking back at you. And that grin...The grin is all you remember as you slowly fade out... '
                               'A hand reaches towards you, from the black mirror, and drags you in. A tragic end. ')
                    game_file.display_message(1, message, (50, 90))
                    time.sleep(5)
                    game_file.screen.fill(game_file.black)
                    player.change_state()

                else:
                    for x in temp_inventory:
                        if x not in player.inventory:
                            inventory.append(x)
                            player.inventory.append(x)
                            game_file.display_message(2, inventory, (50, 90))

                    if not inventory:
                        message = 'You didn\'t find anything which you didn\'t already own. Good try, nevertheless. '
                        game_file.display_message(1, message, (50, 90))
                        game_file.screen.fill(game_file.black)

            else:
                message = ('There is nothing to be found on the body. Couldn\'t hurt to try. Actually, it could. Maybe this '
                           'is for the better. ')
                game_file.display_message(1, message, (50, 90))
                time.sleep(5)
                game_file.screen.fill(game_file.black)

        elif player.action.lower() == 'let it rest':
            message = ('You decided it is best not to disturb the dead...especially when they are faceless and make an '
                       'appearance like that.')
            game_file.display_message(1, message)
            time.sleep(5)
            game_file.screen.fill(game_file.black)

        else:
            message = 'I did not understand that. Please repeat. '
            game_file.display_message(1, message)
            time.sleep(2)
            game_file.screen.fill(game_file.black)
            continue

        break


function_list = [room1, room2, dead_room, room3, room4]

while player.state == 'alive':

    start()
    game_file.screen.fill(game_file.black)


    # Checking the game object's phases attribute.
    # phase = 1 -> first playthrough, no temp_inventory needed
    # phase = 2+ -> second or more playthrough, temp_inventory needed for dead_room function
    # check_state executes the room functions and checks the player state for dead OR alive
    if game.phases == 1:
        check = game_file.check_state(player, function_list)
    else:
        check = game_file.check_state(player, function_list, temp_inventory)


    # If the player state is dead -> it will give the player the option to replay or end the game session there
    if check is False:
        message = ('It seems you have perished. How unfortunate. Would you like to try your luck again? ')
        choices = ['>Yes', '>No']
        game_file.display_message(1, message)
        game_file.display_message(2, choices, (50, 90))
        player.action = game_file.get_player_input()
        game_file.screen.fill(game_file.black)

        # Upon agreeing to play again, the phases attribute of the game object is increased to 2, now moving into
        # dead_room function
        if player.action.lower() == 'yes':
            player.state = 'alive'
            game.phases += 1

            # Upon reaching the fourth phase/playthrough, the game is officially over.
            if game.phases == 4:
                message = ('What a disappointment you are. This is the end. You are dead. ')
                game_file.display_message(1, message)
                game_file.screen.fill(game_file.black)
                game_file.play_music('Music\\bad_ending.mp3')
                time.sleep(5)
                break

            # In case the player does another playthrough, their inventory will be saved in temp_inventory
            # The current player object will be deleted, with a new one taking its place in the NEW PLAYTHROUGH
            temp_inventory = player.inventory
            del player
            player = adv_file.Player()
            continue

        else:

            # In case the player chooses not to play again, it will be game over.
            game_file.play_music('Music\\bad_ending.mp3')
            message = ('What a disappointment you are. So be it. Let the end be the end and nothing else. ')
            game_file.display_message(1, message)
            game_file.screen.fill(game_file.black)
            break


game_file.pygame.display.update()
game_file.clock.tick(60)
