import time


class Player:

    def __init__(self):
        self.name = None
        self.place = None
        self.detail1 = None
        self.level1 = None
        self.level2 = None
        self.pclass = None
        self.intro = None
        self.choice = None
        self.state = None # State of the player - Dead/Alive
        self.inventory = []
        self.items = None
        self.rooms1 = None
        self.rooms2 = None
        self.action = None
        self.check1 = False
        self.check2 = False
        self.temp_check = False
        self.place_choice = None
        self.game_end = False
    def make_choice(self):
        self.choice = input("\n>").lower()
        return self.choice

    def creation(self, place_choice):
        self.place_choice = place_choice
        fantasy_options = ['Knight', 'Mage', 'Druid']
        forest_options = ['Wawanakwa', 'Red Root', 'Blue Dawn']
        murder_options = ['room 09', 'room 13', 'room 256']
        '''if self.place_choice.title() == 'Forest Trip':
            self.name = input("What is your name, scout?\n>").title()
            self.pclass = int(input("And what camp do you come from?\n"
                                    "1. Camp Wawanakwa\n"
                                    "2. Camp Red Root\n"
                                    "3. Camp Blue Dawn\n>"))
            self.place = 'Taibur Forest'
            self.detail1 = ['mapping', 'exploring', 'searching for tracks in the']
            self.intro = f"Welcome, {self.name}, to {self.place}. You were tasked by Camp {forest_options[self.pclass - 1]}" \
                         f"with {self.detail1[self.pclass - 1]} the Taibur Forest.\nCarefully weigh your choices, as your" \
                         f"survival depends on them. \nThe night sets in now...and you must survive it. "
        if self.place_choice.title() == 'Fantasy Adventure':
            self.name = input("What is your name, adventurer?\n").title()
            self.pclass = int(input("And what order do you belong to?\n"
                                    "1. Knight\n"
                                    "2. Mage\n"
                                    "3. Druid\n>"))
            self.place = 'Cave of Magtarr'
            self.detail1 = ['looking for the lost group', 'restoring the natural balance', 'defeating the creature']
            self.intro = f"I welcome thee, {fantasy_options[self.pclass - 1]} {self.name} of the Great Country of Delirion.\n" \
                         f"Carefully listen, as you have been tasked with {self.detail1[self.pclass - 1]} of the {self.place}." \
                         f"\nNow, heed my call, as the challenges you will face must be met with proper thought" \
                         f"and strength of mind and body. \nMake it to the end of the cave and finish your task...but" \
                         f"beware the horrors in the dark."'''
        if self.place_choice.title() == 'Murder Mystery':
            self.name = "What is your name, endorsed guest?\n"
            self.place = 'Hotel Margot'
            self.detail1 = ['fashion gala', 'interview for your paper',
                            'guests\'s appetite']
            self.level1 = 'Hallway\n\n'
            self.rooms1 = ['Closet', 'Elevator', 'Balcony']
            self.items1 = ['Magnifying Glass', 'Fuse']
            self.intro = (f"Oh, dear! If it isn't {self.name}! We were expecting you, and we are pleased to have you.\n" 
                         f"Please, make yourself at home in our dear {self.place}. Your room is {self.pclass}.\n" 
                         f"For tonight, the {self.detail1[murder_options.index(self.pclass)]}, in the main hall, " 
                         f"awaits you. Do consider taking your time when " 
                         f"deciding how to best approach this event!\nIt won't be long until the MAIN event will begin...\n" 
                         f"Consider yourself lucky for the heads up. The other guests aren't so lucky. \nOne, in particular...\n" 
                         f"But enough talk! Go on! Have a wonderful evening!\nMaybe your last one.\n\n")
            if self.pclass == 'room 09':
                self.level2 = 'Basement\n'
            elif self.pclass == 'room 13' or self.pclass == 'room 256':
                self.level2 = 'The Lower Floor\n\n'
            self.rooms2 = ['The Green Door', 'The Black Door', 'The Red Door']
            self.items2 = ['Bloody Letter', 'VIP Ticket', 'Cursed Mark']

    def room_intro1(self):
        if self.place_choice.title() == 'Murder Mystery':
            message = ('You enter the dimly lit hallway, caught between the safety of your room and the mysteries ahead.\n' 
                'The air is still, carrying a hint of aged wood. The faded wallpaper peels, revealing the passage of time.\n' 
                'To your left, a closed door leads to a balcony, teasing glimpses of the outside world. \n' 
                'To your right, a slightly ajar door reveals a cramped closet, holding secrets within its limited space.\n' 
                'Straight ahead, a closed door guards the elevator, its faint hum echoing through the corridor.\n' 
                'You observe two items: a fuse, laying on a shelf, and a magnifying glass, somehow waiting for a firm hand to pick it up.\n' 
                'Anticipation settles upon you as you stand in this hallway, ready to unlock the stories within each room.\n'
                'The adventure awaits, just beyond the threshold.\n' )
            self.print_message(message)
            while self.check1 == False:
                if len(self.items1) > 0:
                    message = ('What is your next move?\n\n' 
                                   '>Go to Rooms\n' 
                                   '>Pick up Items\n')
                    self.print_message(message)

                    self.action = self.make_choice()
                else:
                    message = ('What is your next move?\n\n'
                          '>Go to Rooms\n')
                    self.print_message(message)
                    self.action = self.make_choice()
                if self.action.lower() == 'pick up items' and len(self.items1) > 0:
                    message = ('Which item do you pick up?\n\n')
                    self.print_message(message)
                    for i in self.items1:
                        message = (f'>{i}\n')
                        self.print_message(message)
                    self.action = self.make_choice()
                    if self.action.lower() == 'magnifying glass':
                        message = ('You pick up a magnifying glass. Hopefully, it will be useful in the way you think.\n')
                        self.print_message(message)
                        self.inventory.append('Magnifying Glass')
                        self.items1.remove('Magnifying Glass')
                        continue
                    elif self.action.lower() == 'fuse':
                        message = ('You picked up a fuse. Someone might miss it.\n')
                        self.print_message(message)
                        self.inventory.append('Fuse')
                        self.items1.remove('Fuse')
                        continue
                elif self.action.lower() == 'go to rooms':
                    message = ('Which room are you going to?\n\n'
                                     '>Closet\n'
                                     '>Elevator\n'
                                     '>Balcony\n')
                    self.print_message(message)
                    self.action = self.make_choice()
                    if self.action.lower() == 'closet' and 'Fuse' not in self.inventory:
                        message = ('You enter the cramped closet. The janitor\'s tools are lying about.\nThe stingy smell of cleaning '
                          'products bothers you, but due to the odor of the freshly washed sheets, it is a minor nuisance.\n'
                          'You think there is nothing interesting here to be seen, but then you spot a multitude of red spots, '
                          'splattered all over a sheet, in a tucked away basket.\nIt looks like...blood.\n'
                          'You take a mental note of this and return to the hallway.\n')
                        self.print_message(message)
                        continue
                    elif self.action.lower() == 'closet' and 'Fuse' in self.inventory:
                        message = ('As you enter the cramped closet, you hear an ominous buzz, followed by a cable having a sudden jolt of electricity.\n'
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
                        self.print_message(message)
                        self.change_state()
                        self.check1 = True
                    if self.action.lower() == 'balcony':
                        message = ('The wind lifts your hair...The fresh smell of the air makes you inhale with a sense of relief.\n'
                              'You are invigorated.\nOutside, you notice numerous black limousines are arriving.'
                              'The people coming out of them all wear red masks, along with black suits and dresses.\n'
                              'It looks like they were expected. A great portion of the hotel staff is waiting for them, '
                              'quickly rushing to escort them once they reach the hotel\'s steps.\n'
                              'An ominous aura surrounds these new guests...\n'
                              'You notice something peculiar about the limousines. They each seem to carry a certain symbol.\n'
                              'The symbols are beautifully blazoned on their hoods. A door, a candle and a circle.\n'
                              'You ponder this peculiarity for a second and then return to the hallway.\n')
                        self.print_message(message)
                        continue
                    if self.action.lower() == 'elevator':
                        self.check1 = True
    def room_intro2(self):
        if self.place_choice.title() == 'Murder Mystery':
            if self.pclass == 'room 09':
                pass # You arrive at the basement
            elif self.pclass == 'room 13' or self.pclass == 'room 256':
                message = ('The elevator descends smoothly, carrying you to the lower level. As the doors open, a cool atmosphere greets you.\n'
                      'Three distinct doors stand before you, each with its own allure.\n'
                      'To your left, a partially opened door with a tint of green reveals a glimpse of light streaming from within. The soft glow suggests the bathroom light may still be on, hinting at recent activity.\n'
                      'Straight ahead, a closed door painted in a bold shade of red captures your attention. Its vibrant color holds an air of intrigue, hiding the secrets that lie beyond its surface.\n'
                      'To your right, a sleek black door commands your curiosity. Its smooth exterior reflects the ambient light, promising a realm of mysteries waiting to be explored.\n'
                      'You stand at a pivotal moment, faced with choices that will shape your investigation.\n'
                      'The room with the green-tinged door may hold immediate interest, but the red and black doors hold their own enigmas.\n'
                      'It is time to make your move and uncover the truth that awaits behind one of these doors.\n\n')
                self.print_message(message)
                progression_check = -1
                first_door = None
                gunshot = False
                while self.check2 == False:
                    if progression_check == -1:
                        for i in self.rooms2:
                            message = (f'>Go to {i.lower()}\n')
                            self.print_message(message)
                    else:
                        self.rooms2.remove(progression_check)
                        self.rooms2.sort()
                        if len(self.rooms2) == 0:
                            break
                        for i in self.rooms2:
                            message = (f'>Go to {i.lower()}\n')
                            self.print_message(message)
                    self.action = self.make_choice()

                    if self.action.lower() == 'go to the green door':
                        if first_door == None:
                            first_door = 'Green'
                        message = ('You slowly open the dirty, stained green door and enter the room.\n'
                              'The first thing that draws your attention is the light in the bathroom.\n'
                              'Do you go to the bathroom?\n\n'
                              '>Yes\n'
                              '>No\n')
                        self.print_message(message)
                        progression_check = 'The Green Door'
                        self.action = self.make_choice()
                        if self.action.lower() == 'yes':
                            message = ('You enter the bathroom with careful steps. The door creaks as you open it.\n'
                            '...\n'
                            '...\n'
                            '...\n'
                            'You\'re shocked by the sight before you. A man has committed suicide in the bathtub.\n'
                            'The water has been running continuously and has overflowed, drenching your shoes.\n'
                            'As you try to quickly leave the room, in your panic, you slip on the wet floor, and hit your'
                            'head on the sink.\n'
                            'You are dead.\n')
                            self.print_message(message)
                            self.change_state()
                            self.check2 = True
                        elif self.action == 'no':
                            message = ('Deciding the bathroom is of no interest to you, you look around the room.\n'
                                  'Your gaze dances around, on the pictures on the walls, on the messy clothes thrown around,\n'
                                  'on the ugly furniture and wall paint. It is almost as someone intended this room to be '
                                  'the ugliest.\nLastly, your gaze settles upon a ticket on the bed.\nIt seems to be a VIP ticket.\n'
                                  'Do you take it?\n\n'
                                  '>Yes\n'
                                  '>No\n')
                            self.print_message(message)
                            self.action = self.make_choice()
                            if self.action == 'yes':
                                message = ('You carefully put the ticket in your jacket\'s inner pocket.\n')
                                self.print_message(message)
                                self.inventory.append('VIP Ticket')
                                self.items2.remove('VIP Ticket')
                            elif self.action == 'no':
                                message = ('You let the VIP ticket remain where it is. It is probably for the best, you think.\n')
                                self.print_message(message)
                            if first_door == 'Green':
                                message = ('Before leaving the room, a gunshot draws your attention. It seems like it came from the room '
                                      'with the black door.\nDo you pursue the gunshot?\n\n'
                                      '>Yes\n'
                                      '>No\n')
                                self.print_message(message)
                                self.action = self.make_choice()
                                if self.action == 'yes':
                                    gunshot = True
                                    message = ('You rush towards the black door, propelled by the piercing sound of the gunshot.\n'
                                          'As the door swings open, a surge of unease washes over you.\n'
                                          'The room is shrouded in an eerie atmosphere, adorned with sinister cult objects.\n'
                                          'Their unsettling presence creates a sense of foreboding, casting long, menacing shadows along the walls.\n'
                                          'The air is heavy with an otherworldly energy, as if the room itself holds a dark secret.\n'
                                          'Amidst this macabre scene, a chilling path of blood stains the floor, beckoning you deeper into the heart of the ominous mystery.\n'
                                          'Do you pursue further?\n\n'
                                          '>Yes\n'
                                          '>No\n')
                                    self.print_message(message)
                                    self.action = self.make_choice()
                                    if self.action == 'yes':
                                        message = ('The trail of blood leads you through the hidden door of a wardrobe.\n'
                                              'You enter something akin to a tunnel. The walls are carved and made of stone.\n'
                                              'The air becomes denser as you walk through the never-ending tunnel.\n'
                                              'You wonder how could such a structure exist in this place.\n'
                                              'The blood trail has somehow kept the same shape and consistence throughout the tunnel.\n'
                                              'You come to a dead end. A rock wall proudly defies you, by simply existing '
                                              'in your way.\nFive blocks of rock are protruding out of it, each with a different '
                                              'symbol carved on it.\nA door, a circle, a candle, a magnifying glass and a wand.\n'
                                              'How do you proceed?\n\n')
                                        self.print_message(message)
                                        step = 0  # Steps for completing the puzzle
                                        death_counter = 0  # Counter for the amount of times you can try pushing the blocks, 2 is max
                                        while self.temp_check == False:
                                            if 'Magnifying Glass' in self.inventory:
                                                message = ('>Introduce the magnifying glass in the carving representing it\n'
                                                      '>Push the blocks of rock\n')
                                                #TODO Bug where these options don't show up, but going to the black door does.
                                                # Order was Red Door and Green Door.
                                                self.print_message(message)
                                            else:
                                                message = ('>Push the blocks of rock\n')
                                                self.print_message(message)
                                            self.choice = self.make_choice()
                                            if self.choice == 'introduce the magnifying glass in the carving representing it':
                                                message = ('You take out your magnifying glass and fit it into the block\'s carving.\n'
                                                      'You are surprised it worked, as it seemed to be an odd choice.\n\n')
                                                self.inventory.remove('Magnifying Glass')
                                                step += 1
                                                self.print_message(message)
                                                continue
                                            elif self.choice == 'push the blocks of rock':
                                                message = ('As the blocks of rock are protruding, you decide they could also be made '
                                                      'to fit in.\nBut, there\'s a catch: in what order should you push them back in?\n\n'
                                                      '>Circle, door, wand, magnifying glass, candle\n'
                                                      '>Wand, door, candle, magnifying glass, triangle\n'
                                                      '>Door, candle, magnifying glass, circle, wand\n')
                                                self.print_message(message)
                                                self.choice = self.make_choice()
                                                if self.choice == 'door, candle, magnifying glass, circle, wand':
                                                    step += 1
                                                    death_counter += 1
                                                    if step < 2 and 'Magnifying Glass'  not in self.items1:
                                                        message = ('The decision you made seems to have been inspired.\n'
                                                                   'Something clicks inside the wall. The stone itself sends out a ripple throughout.\n'
                                                                   'The stone that seemed solid is now liquid in nature and you can see it pulsating in waves.\n'
                                                                   'Better than nothing, you think.\n')
                                                        self.print_message(message)
                                                        continue
                                                    elif step < 2 and 'Magnifying Glass' in self.items1:
                                                        message = (
                                                            'The decision you made seems to have been inspired.\n'
                                                            'Something clicks inside the wall. The stone itself sends out a ripple throughout.\n'
                                                            'But something is off. The solid stone now turns into a volatile, liquid substance.\n'
                                                            'Spikes of it are rising and sinking back everywhere. One reaches out so far that it grazes you.\n'
                                                            'The liquid substance reacts to your blood. Tne entire wall starts buzzing and turning waves of shades of crimson.\n\n')
                                                        self.print_message(message)
                                                        continue
                                                    else:
                                                        message = ('As you push the blocks back into place, stairs are starting to form below the rock wall.\n'
                                                            'They seem to be leading towards a bright, white light.\n'
                                                            'You descend the stairs. A gentle breeze can be felt, in a peculiar combination with feeling warm.\n'
                                                            'The emotions of hope and safety, that accompanied you during your descent, now evaporate.\n'
                                                            'A sentiment of dread like no other embraces you, holding you tightly, squeezing out your breath.\n'
                                                            'The hotel\'s walls emanate this feeling all around you. It must be something about the hotel, you think.\n'
                                                            'But you\'re gonna get through it. You have so little left to do. And so much, at the same time.\n\n')
                                                        self.temp_check = True
                                                        self.check2 = True
                                                        self.print_message(message)
                                                else:
                                                    if death_counter < 2:
                                                        message = ('You decide on a sequence and...nothing.\nA sinister hum is heard emanating'
                                                              ' from the wall.\n\n')
                                                        death_counter += 1
                                                        self.print_message(message)
                                                        continue
                                                    elif death_counter == 2:
                                                        message = ('The hum turns into a loud buzz that makes you cover up your ears...\n'
                                                              'And then, nothing. The wall then starts crumbling from the middle to the sides.\n'
                                                              'You see nothing but pitch black darkness before you. Then, you feel something on the back of your neck.\n'
                                                              'It\'s like a sting. It feels warm on your skin at first, but then its cold runs through your entire body.\n'
                                                              'You feel numb from the cold. Your head feels detached from your body, like it\'s floating...\n'
                                                              'The sequence of events that follows isn\'t very clear. You remember dropping on the ground.\n'
                                                              'A sensation that could be described as being engulfed, swallowed, by darkness that has teeth, is then felt.\n'
                                                              'In reality, your body is discovered in the room you heard the gunshot from.\n'
                                                              'It marks the beginning of the blood trail. You are found sitting on your knees, mouth wide open and eyes staring in awe at the ceiling.\n'
                                                              'Your pupils are fully dilated. Your bodily liquids have found their way out...\n'
                                                              'An unfortunate end.\n'
                                                              'You are dead.\n')
                                                        self.temp_check = True
                                                        self.check2 = True
                                                        self.change_state()
                                                        self.print_message(message)
                                    elif self.action == 'no':
                                        message = ('This hotel has definitely got something wrong going on, you think.\n'
                                              'You carefully walk around the room, analyzing everything and deciding if this would be the time\n'
                                              'to call the police. You notice a bloody letter on the desk facing the window.\n'
                                              'It seems to be the only item on that desk. It is sealed with a crimson seal, also reminiscent of blood.\n'
                                              'You step closer to it, curious of its contents. But first, you think, you should search the desk\'s drawers.\n'
                                              'Nothing comes out of your search, except for old, irrelevant papers, a broken cable and the hotel\'s assistance book.\n'
                                              'In this case, all that\'s left is taking the letter for yourself.\n'
                                              'Do you take it?\n\n'
                                              '>Yes\n'
                                              '>No\n')
                                        self.print_message(message)
                                        self.action = self.make_choice()
                                        if self.action == 'yes':
                                            message = ('Your curiosity got the better of you. You quickly take the letter and stuff it well.\n'
                                                  'Now, nobody will know what you\'ve been up to.')
                                            self.print_message(message)
                                        elif self.action == 'no':
                                            message = ('Perhaps it is wiser to let it where it is. Or so your confused senses tell you.\n')
                                            self.print_message(message)
                                        message = ('You can\'t help but wonder where the gunshot came from. It was clearly from this room.\n'
                                              'You could\'ve misheard. There is certainly no gun laying around.\n'
                                              'And there is certainly no way you will go after the blood trail. Perhaps in another life.\n\n')
                                        self.print_message(message)
                                elif self.action == 'no':
                                    message = ('Was that really a gunshot you just heard? You would rather not find out. Not the time, not the place to go investigating by yourself.\n'
                                               'You wonder if you should call the police, but decide not to. You hope this was not against your best interests.\n'
                                               'And so, after giving the room one last look, you ponder which door to explore next.\n')
                                    self.print_message(message)
                            else:
                                if len(self.rooms2) == 2:
                                    message = ('Now, time to see what is behind the final door.\n'
                                           'Nothing good, you think to yourself. Hopefully, that won\'t be the case. Just bad thoughts...\n')
                                    self.print_message(message)
                                else:
                                    message = ('Now, time to see what is behind the other doors.\n'
                                               'For a brief second, you feel a hand on your shoulder. Its grip is firm and violent.\n'
                                               'You turn around and survey the room. The shivers down your spine don\'t fail to appear.\n'
                                               'You feel light headed. Your steps are uncertain and heavy.\n'
                                               'You hold onto the wall on your way out and take a short break.\n'
                                               'This place is physically hurting you. You need to get to the end of it.\n'
                                               'As. Soon. As. Possible.\n')
                                    self.print_message(message)

                    elif self.action.lower() == 'go to the black door':
                        first_door = 'Black'
                        progression_check = 'The Black Door'

                        if gunshot == False:
                            message = ('You feel an irresistible urge to explore the black door, driven by an inexplicable force.\n'
                                  'As the door creaks open, a wave of cold dread washes over you.\n'
                                  'The room before you is a nightmarish tableau of eerie cult objects, their malevolent presence seeming to watch your every move.\n'
                                  'Sinister shadows writhe along the walls, as if alive and hungry for company.\n'
                                  'The air is thick with an oppressive sense of malevolence, sending shivers down your spine.\n'
                                  'Amidst this macabre display, a black, tall silhouette of a man can be seen standing in the middle of the room.\n'
                                  'It\'s smokey and fully physical, at the same time. An evil apparition.\n'
                                  'But it is not paying attention to you. To your right, another man can be seen. This one, flesh and bone.\n'
                                  'His clothes are torn and bloody, his face, a grin of exhaustion and desperation.\n'
                                  'A plethora of cult items can be seen around him, all broken and smashed.\n'
                                  'With desperation, he loads his gun and tries shooting the black figure. It does nothing.\n'
                                  'The figure dashes across the room, to the man, grabbing his head and quickly dragging it on the floor.\n'
                                  'The black figure seemingly disappears into a darkness in the back of the room, with the man\'s blood forming a trail to it.\n'
                                  'The trail seems to be leading deeper into the heart of the chilling mystery, filling you with a gnawing sense of impending doom.\n'
                                  'You are presented with a choice: follow the blood trail?\n\n'
                                  '>Yes\n'
                                  '>No\n')
                            self.print_message(message)
                            self.action = self.make_choice()
                            if self.action == 'yes':
                                message = ('You follow the blood trail through a secret door in the wardrobe.\n'
                                      'But, as soon as you step through, a darkness quickly engulfs you and throws you out of the room with force.\n'
                                      'The door immediately slams shut. You feel shivers everywhere in your body. You\'re too fearful to get off the ground and look around.\n'
                                      'A burning sensation can be felt on your arm. Gasping, you clutch your arm, and to your horror, you find a cursed mark etched upon your skin.\n'
                                      'The mark appears as a sinister, intricate glyph that seems to writhe with a life of its own.\n'
                                      'The dark ink spreads across your flesh like a malevolent stain, and you feel an unsettling, pulsating sensation emanating from the mark.\n'
                                      'The mark glows with an eerie, crimson light, casting an ominous shadow over your surroundings. It throbs with an unseen power, as if the malevolence from the black room has now bonded with your very being.\n'
                                      'Fear and confusion grip you as you realize you are now marked by an otherworldly force, and the sense of foreboding intensifies with each passing second.\n')
                                self.print_message(message)
                                self.inventory.append('Cursed Mark')
                            elif self.action =='no':
                                message = ('The chilling scene unfolds, overwhelming fear grips your heart. An eerie foreboding takes hold as you witness the nightmarish tableau.\n'
                                           'The wardrobe\'s door creaks open, cold dread washes over you, freezing you in place.\n'
                                           'Fear leaves you torn between curiosity and self-preservation. Maybe you should see where the trail is leading to, after all...\n'
                                           'Then, the image of the apparition comes back to you. The harrowing scene that unfolded before your eyes haunts you.\n'
                                           'You are unsure of where to find safe haven. It seems as it the malevolent entity is only toying with you, saving you for the last.\n'
                                           'You don\'t think it\'s really gone...The dread and evil are all around. You feel almost physically squeezed by it.\n'
                                           'You almost run out of breath a couple of times. You slowly get up, arms and legs trembling. No, you will not give in to the deadly curiosity.\n'
                                           'This is no place to die. You didn\'t come here for this.\n'
                                           'The ordeal leaves you scared and uncertain, unsure of the horrors that await and the choices you must make to survive.\n'
                                           'You carefully walk around the room, analyzing everything and deciding if this would be the time\n'
                                           'to call the police. You notice a bloody letter on the desk facing the window.\n'
                                           'It seems to be the only item on that desk. It is sealed with a crimson seal, also reminiscent of blood.\n'
                                           'You step closer to it, curious of its contents. But first, you think, you should search the desk\'s drawers.\n'
                                           'Nothing comes out of your search, except for old, irrelevant papers, a broken cable and the hotel\'s assistance book.\n'
                                           'In this case, all that\'s left is taking the letter for yourself.\n'
                                           'Do you take it?\n\n'
                                           '>Yes\n'
                                           '>No\n')
                                self.print_message(message)
                                self.action = self.make_choice()
                                if self.action == 'yes':
                                        message = ('If anything will serve you as proof of what happened here, it\'s this. You quickly took the letter and stuffed it well.\n'
                                                  'Now, maybe you will live to show the world what is truly happening here.\n\n')
                                        self.print_message(message)
                                elif self.action == 'no':
                                        message = ('Perhaps it is wiser to let it where it is. Or so your confused senses tell you.\n')
                                        self.print_message(message)
                        elif gunshot == True:
                            message = ('The door won\'t even budge. It now refuses to let you in.\n'
                                       'Should have been thorough with the room the first time.\n'
                                       'It is as if the door became a part of the wall itself. Curious indeed.\n\n')
                            self.print_message(message)

                    elif self.action.lower() == 'go to the red door':
                        progression_check = 'The Red Door'
                        message = ('As you step into the red room, a mysterious ambiance envelops you, carrying an aura of ancient secrets and mystical energies.\n'
                                   'The air is tinged with an intoxicating blend of incense and a faint scent of old parchment, with flickering candles cast dancing shadows upon the walls, creating an almost hypnotic effect.\n'
                                   'In the center of the room lies a crystal ball, perched atop an ornate stand, its surface glimmering with an otherworldly sheen.\n'
                                   'It beckons you to approach, offering cryptic insights into the future and a glimpse into the veiled realms of destiny.\n'
                                   'Tarot cards spread in a precise pattern whisper untold possibilities, while ancient tomes of arcane knowledge hold the wisdom of ages past.\n'
                                   'Five intriguing objects line a nearby table, each veiled in mystery, awaiting your firm hand.\n'
                                   'The air tingles with anticipation. What will it be first?\n\n')
                        self.print_message(message)
                        self.temp_check = False
                        choices = ['Crystal ball', 'Tarot cards', 'Table of objects', 'Go outside the room']
                        while self.temp_check == False:
                            for i in choices:
                                message = f'>{i}\n'
                                self.print_message(message)
                            self.action = self.make_choice()
                            if self.action == 'crystal ball':
                                if 'Cursed Mark' in self.inventory:
                                    message = ('Carefully walking closer to the ornate stand, you instinctively reach out to the crystal ball.\n'
                                            'As you do that, your mark burns. The crystal ball reacts to your mark and begins forming a swirling black smoke.\n'
                                            'From it, you can distinguish the same room you\'re in. You see yourself, and behind you...a dark face with sharp teeth, orange, mad eyes, sitting right on your shoulder.\n'
                                            'Then, the image shifts into a walk. It goes down some stairs, and ends up in the main area of the hotel. A large masked person towers over.\n'
                                            'It looks like he is guarding the entrance. The crystall ball goes blank again and cracks.\n\n')
                                    self.print_message(message)
                                    choices.remove('Crystal ball')
                                    choices.sort()
                                else:
                                    message = ('Carefully walking closer to the ornate stand, you instinctively reach out to the crystal ball.\n'
                                               'As you do that, the crystal ball begins forming a swirling white smoke.\n'
                                               'In it, you distinguish the room you\'re in. The image pans over to the table with the five objects.\n')
                                    self.print_message(message)
                                    if 'Bloody Letter' in self.inventory:
                                        message = ('A particular item seems to be glowing. It\'s the ancient tome.\n')
                                        self.print_message(message)
                                    elif 'Magnifying Glass' in self.inventory:
                                        message = ('A particular item seems to be glowing. It\'s the black mirror.\n')
                                        self.print_message(message)
                                    else:
                                        message = ('A particular item seems to be glowing. It\'s the silver ring.\n')
                                        self.print_message(message)
                                    message = ('Then, the image shifts into a walk. It goes down some stairs, and ends up in the main area of the hotel. A large masked person towers over.\n'
                                                'It looks like he is guarding the entrance. The crystall ball goes blank again and cracks.\n\n')
                                    self.print_message(message)
                                    choices.remove('Crystal ball')
                                    choices.sort()
                            elif self.action == 'tarot cards':
                                message = ('As you gingerly reach out to touch the deck, a sense of trepidation and excitement intertwines within you.\n'
                                           'The cards seem to respond to your presence, almost as if they were awaiting your arrival.\n'
                                           'As your fingers make contact with the smooth, worn edges, a surge of energy courses through your being.\n'
                                           'The deck feels warm, alive, and responsive in your hands. It is as though a subtle connection has been established between you and the ancient wisdom contained within.\n'
                                           'With every shuffle and cut, the cards seem to whisper secrets, each one a potential window into the vast tapestry of fate.\n'
                                           'You can\'t help but notice the way they shine in the light. Their golden tint gives a sense of comfort and safety.\n'
                                            'You instinctively draw and spread five cards out of the tarot deck on the table. Your hands move on their own.\n'
                                            'A light breeze flickers the candles, seemingly coming out of nowhere. The intensity of their flames now grows.\n'
                                            'After a brief pause, you turn one of the cards. Your hand trembles in doing so.\n')
                                self.print_message(message)
                                if 'Cursed Mark' in self.inventory and 'Bloody Letter' not in self.inventory:
                                    message = ('The first card is The Tower. It is followed by The Hanged Man, The Two of Swords, The Devil and The Wheel of Fortune.\n'
                                               'You do not know their meaning, but you don\'t need to. Your intuition and senses know what the sequence means.\n'
                                               'Your mark burns. You must get rid of it. You must be even more careful with your choices, as your life depends on them.\n'
                                               'And you must get rid of it as soon as possible. Maybe one of the items will help in that regard.\n\n')
                                    self.print_message(message)
                                    choices.remove('Tarot cards')
                                    choices.sort()
                                elif 'Bloody Letter' in self.inventory and 'Cursed Mark' not in self.inventory:
                                    message = ('The first card is The Hermit. It is followed by The High Priestess, The Page of Swords, The Justice and The Wheel of Fortune.\n'
                                               'Even though you never dealt with tarot cards before, you sense the meaning of the sequence. Their golden tint tells you all you need to know.\n'
                                               'The answers are right under your nose. You must look deeper, in what you know, in what you have. Your intuition is your salvation.\n\n')
                                    self.print_message(message)
                                    choices.remove('Tarot cards')
                                    choices.sort()
                                elif 'Bloody Letter' in self.inventory and 'Cursed Mark' in self.inventory:
                                    message = ('The first card is The Hermit. It is followed by The High Priestess, The Page of Swords, The Justice and The Wheel of Fortune.\n'
                                        'Even though you never dealt with tarot cards before, you sense the meaning of the sequence. Their golden tint tells you all you need to know.\n'
                                        'The answers are right under your nose. You must look deeper, in what you know, in what you have. Your intuition is your salvation.\n'
                                        'The key to removing your mark is hidden in the bloody letter and in this room. Perhaps in one of the objects, as well.\n\n')
                                    self.print_message(message)
                                    choices.remove('Tarot cards')
                                    choices.sort()
                                else:
                                    message = ('The first card is The World. It is followed by The Eight of Cups, The Three of Wands, The Ace of Pentacles and The Chariot.\n'
                                               'Despite never dealing with tarot cards before, you know what all of this means. You are close. It\'s almost over.\n'
                                               'Now, for the last part of this weird day, you must not let your guard down.\n\n')
                                    self.print_message(message)
                                    choices.remove('Tarot cards')
                                    choices.sort()
                            elif self.action == 'table of objects':
                                message = ('From the second you laid eyes on it, you knew it was there for you. All of this, was for you, somehow.\n'
                                           'You feel an unexplainable connection to everything that is happening. You must see this through.\n'
                                           'Five objects are carefully laid on the gold-edged cloth, made out of red silk, that covers the table.\n'
                                           'A ring, made out of silver.\n'
                                           'A black mirror, made out of obsidian.\n'
                                           'An ancient tome, made out of leather.\n'
                                           'A perfumed satchel, adorned with beautiful symbols.\n'
                                           'A rosary, of the simplest design.\n'
                                           'Something tells you you can only pick one. And that it is somewhat...relevant. Vital, rather.\n'
                                           'Which one will it be?\n\n'
                                           '>Silver ring\n'
                                           '>Black mirror\n'
                                           '>Ancient tome\n'
                                           '>Perfumed satchel\n'
                                           '>Rosary\n')
                                self.print_message(message)
                                self.action = self.make_choice()
                                choices.remove('Table of objects')
                                choices.sort()
                                if self.action == 'silver ring':
                                    message = ('You believe the ring will prove useful. How could it, though? It\'s just a ring.\n'
                                              'But, if it\'s one thing you learnt in this hotel, is that nothing is random.\n\n')
                                    self.print_message(message)
                                    self.inventory.append('Silver ring')
                                elif self.action == 'black mirror':
                                    message = ('The obsidian, heavy, black mirror seems the obvious choice for you.\n' 
                                              'Perhaps there is something to its blackness that will reveal a secret.\n\n')
                                    self.print_message(message)
                                    self.inventory.append('Black mirror')
                                elif self.action == 'ancient tome':
                                    message = ('The ancient tome definitely holds the information and secrets that will get you out of this place.\n'
                                              'Safely.\n\n')
                                    self.print_message(message)
                                    self.inventory.append('Ancient tome')
                                elif self.action == 'perfumed satchel':
                                    message = ('The perfumed satchel has a certain charm to it. Perhaps it is the perfume itself...\n'
                                               'And maybe that\'s a good thing. Could be exactly what you needed.\n'
                                               'Nevertheless, such a beautiful and charming object is better suited to your pocket, than this table.\n\n')
                                    self.print_message(message)
                                    self.inventory.append('Perfumed satchel')
                                elif self.action == 'rosary':
                                    message = ('Simplicity seems to be the best answer here. And besides, you need God.\n'
                                               'Faith will get you through this. You can feel it. Divinity is your salvation.\n\n')
                                    self.print_message(message)
                                    self.inventory.append('Rosary')
                            elif self.action == 'go outside the room':
                                message = ('Now, having seen enough of the room, you better leave it for now.\n'
                                           'Hopefully for you, you explored it thoroughly. You have a feeling it was crucial.\n\n')
                                self.print_message(message)
                                choices.remove('Go outside the room')
                                choices.sort()
                                self.temp_check = True

        self.state = 'alive'

    def print_message(self, message, delay = 0.01):
        for i in range(0, len(message), 2):
            print(message[i:i + 2], end='', flush=True)
            time.sleep(delay)

    def change_state(self):
        self.state = 'dead'


class Game(Player):
    phases = 1
    places = [' Forest Trip', 'Fantasy Adventure', 'Murder Mystery']
    adventure_count = 0

    def narrator1(self):
        message = ("Tonight, we have a special guest. He is here to begin a journey that will lead him...places."
              " It is all up to him to make the right choices. Or the ones that seem right, anyway.\n")
        #self.print_message(message)
        return message

    def narrator2(self):
        print("Tonight, we have a special guest.\nHe is here to begin a journey that will lead him...places."
              "\nHopefully, this time, he will be better. Better than those before him.\n Life is so short nowadays.\n")

    def narrator3(self):
        print("Tonight, we have a special guest.\nI think you all know him by now. Know what he is capable of.\n"
              "Or rather, what he's incapable of. Ha-ha-ha...-ha.\n")

    def narrator4(self):
        print("You are very close to the end of your adventure. Closer than you would like.\n")

    def narrator5(self):
        print("...\n...\n...\n...\nYOU ARE SUCH A DISAPPOINTMENT.\nYOU. ARE. DEAD.\n")

    def game_start(self, player):
        Game.adventure_count += 1
        if Game.phases == 1:
            self.narrator1()
        elif Game.phases == 2:
            self.narrator2()
        elif Game.phases == 3:
            self.narrator3()
        elif Game.phases == 4:
            self.narrator4()
        elif Game.phases == 5:
            self.narrator5()

        message = (f"Your choice for your setting is...: \n"
              f">{Game.places[0]}\n"
              f">{Game.places[1]}\n"
              f">{Game.places[2]}\n")
        self.print_message(message)
        player_choice = player.make_choice()
        player.creation(player_choice)
        self.print_message(player.intro)

    def first_room(self, player):
        message = (player.level1)
        self.print_message(message)
        player.room_intro1()

    def second_room(self, player):
        message = (player.level2)
        self.print_message(message)
        player.room_intro2()


def main():
    player = Player()
    game = Game()
    game.game_start(player)
    game.first_room(player)
    game.second_room(player)


if __name__ == '__main__':
    main()
