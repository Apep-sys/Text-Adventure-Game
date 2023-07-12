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
        self.state = None
        self.inventory = []
        self.items = None
        self.rooms1 = None
        self.rooms2 = None
        self.action = None
        self.check1 = False
        self.check2 = False
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
        if self.place_choice.title() == 'Forest Trip':
            self.name = input("What is your name, scout?\n>").title()
            self.pclass = int(input("And what camp do you come from?\n"
                                    "1. Camp Wawanakwa\n"
                                    "2. Camp Red Root\n"
                                    "3. Camp Blue Dawn\n>"))
            self.place = 'Taibur Forest'
            self.detail1 = ['mapping', 'exploring', 'searching for tracks in the']
            self.intro = f"Welcome, {self.name}, to {self.place}. You were tasked by Camp {forest_options[self.pclass - 1]}" \
                         f"with {self.detail1[self.pclass - 1]} the Taibur Forest.\nCarefully weigh your choices, as your" \
                         f"survival depends on them. \nThe night sets in now...and you must survive it.  "

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
                         f"beware the horrors in the dark."
        if self.place_choice.title() == 'Murder Mystery':
            self.name = input("What is your name, endorsed guest?\n").title()
            self.pclass = input("And what room are you from?\n"
                                    "1. Room 09\n"
                                    "2. Room 13\n"
                                    "3. Room 256\n>").lower()
            self.place = 'Hotel Margot'
            self.detail1 = ['fashion gala', 'interview for your paper',
                            'guests\'s appetite']
            self.level1 = 'Hallway\n'
            self.rooms1  = ['Closet', 'Elevator', 'Balcony']
            self.items = ['Magnifying Glass', 'Fuse']
            self.intro = f"Oh, dear! If it isn't {self.name}! We were expecting you, and we are pleased to have you.\n" \
                         f"Please, make yourself at home in our dear {self.place}. Your room is {self.pclass}.\n" \
                         f"For tonight, the {self.detail1[murder_options.index(self.pclass)]}, in the main hall, " \
                         f"awaits you. Do consider taking your time when " \
                         f"deciding how to best approach this event!\nIt won't be long until the MAIN event will begin...\n" \
                         f"Consider yourself lucky for the heads up. The other guests aren't so lucky. \nOne, in particular...\n" \
                         f"But enough talk! Go on! Have a wonderful evening!\nMaybe your last one.\n "
            if self.pclass == 'room 09':
                self.level2 = 'Basement'
            elif self.pclass == 'room 13' or self.pclass == 'room 256':
                self.level2 = 'The Lower Floor'
            self.rooms2 = ['The Green Door', 'The Red Door', 'The Black Door']
            self.items = ['Bloody Letter', 'VIP Ticket']

    def room_intro1(self):
        if self.place_choice.title() == 'Murder Mystery':
            print('You enter the dimly lit hallway, caught between the safety of your room and the mysteries ahead.\n' 
                'The air is still, carrying a hint of aged wood. The faded wallpaper peels, revealing the passage of time.\n' 
                'To your left, a closed door leads to a balcony, teasing glimpses of the outside world. \n' 
                'To your right, a slightly ajar door reveals a cramped closet, holding secrets within its limited space.\n' 
                'Straight ahead, a closed door guards the elevator, its faint hum echoing through the corridor.\n' 
                'You observe two items: a fuse, laying on a shelf, and a magnifying glass, somehow waiting for a firm hand to pick it up.\n' 
                'Anticipation settles upon you as you stand in this hallway, ready to unlock the stories within each room.\n'
                'The adventure awaits, just beyond the threshold.\n' )
            while self.check1 == False:
                print('What is your next move?\n' 
                               'Go to Rooms\n' 
                               'Pick up Items\n')
                self.action = self.make_choice()
                if self.action.lower() == 'pick up items':
                    print('Which item do you pick up?\n'
                          'Fuse\n'
                          'Magnifying Glass\n')
                    self.action = self.make_choice()
                    if self.action.lower() == 'magnifying glass':
                        print('You pick up a magnifying glass. Hopefully, it will be useful in the way you think.\n')
                        self.inventory.append('Magnifying Glass')
                        continue
                    elif self.action.lower() == 'fuse':
                        print('You picked up a fuse. Someone might miss it.\n')
                        self.inventory.append('Fuse')
                        continue
                elif self.action.lower() == 'go to rooms':
                    print('Which room are you going to?\n'
                                     'Closet\n'
                                     'Elevator\n'
                                     'Balcony\n')
                    self.action = self.make_choice()
                    if self.action.lower() == 'closet' and 'Fuse' not in self.inventory:
                        print('You enter the cramped closet. The janitor\'s tools are lying about.\nThe stingy smell of cleaning '
                          'products bothers you, but due to the odor of the freshly washed sheets, it is a minor nuisance.\n'
                          'You think there is nothing interesting here to be seen, but then you spot a multitude of red spots, '
                          'splattered all over a sheet, in a tucked away basket.\nIt looks like...blood.\n'
                          'You take a mental note of this and return to the hallway.\n')
                        continue
                    elif self.action.lower() == 'closet' and 'Fuse' in self.inventory:
                        print('As you enter the cramped closet, you hear an ominous buzz, followed by a cable having a sudden jolt of electricity.\n'
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
                        self.change_state()
                        self.check1 = True
                    if self.action.lower() == 'balcony':
                        print('The wind lifts your hair...The fresh smell of the air makes you inhale with a sense of relief.\n'
                              'You are invigorated.\nOutside, you notice numerous black limousines are arriving.'
                              'The people coming out of them all wear red masks, along with black suits and dresses.\n'
                              'It looks like they were expected. A great portion of the hotel staff is waiting for them, '
                              'quickly rushing to escort them once they reach the hotel\'s steps.\n'
                              'An ominous aura surrounds these new guests...\n'
                              'You return to the hallway.\n')
                        continue
                    if self.action.lower() == 'elevator':
                        self.check1 = True
    def room_intro2(self):
        if self.place_choice.title() == 'Murder Mystery':
            if self.pclass == 'room 09':
                pass # You arrive at the basement
            elif self.pclass == 'room 13' or self.pclass == 'room 256':
                print('The elevator descends smoothly, carrying you to the lower level. As the doors open, a cool atmosphere greets you.\n'
                      'Three distinct doors stand before you, each holding its own allure.\n'
                      'To your left, a partially opened door with a tint of green reveals a glimpse of light streaming from within. The soft glow suggests the bathroom light may still be on, hinting at recent activity.\n'
                      'Straight ahead, a closed door painted in a bold shade of red captures your attention. Its vibrant color holds an air of intrigue, hiding the secrets that lie beyond its surface.\n'
                      'To your right, a sleek black door commands your curiosity. Its smooth exterior reflects the ambient light, promising a realm of mysteries waiting to be explored.\n'
                      'You stand at a pivotal moment, faced with choices that will shape your investigation.\n'
                      'The room with the green-tinged door may hold immediate interest, but the red and black doors hold their own enigmas.\n'
                      'It is time to make your move and uncover the truth that awaits behind one of these doors.\n')
            while self.check2 == False:
                print('What is your next move?\n'
                      'Go to green bedroom\n'
                      'Go to black bedroom\n'
                      'Go to red bedroom\n')
                self.action = self.make_choice()
                if self.action.lower() == 'go to green bedroom':
                    print('You slowly open the dirty, stained green door and enter the room.\n'
                          'The first thing that draws your attention is the light in the bathroom.\n'
                          'Do you go to the bathroom?\n')
                    self.action = self.make_choice()
                    if self.action.lower() == 'yes':
                        print('You enter the bathroom with careful steps. The door creaks as you open it.\n'
                        '...\n'
                        '...\n'
                        '...\n'
                        'You\'re shocked by the sight before you. A man has committed suicide in the bathtub.\n'
                        'The water has been running continuously and has overflowed, drenching your shoes.\n'
                        'As you try to quickly leave the room, in your panic, you slip on the wet floor, and hit your'
                        'head on the sink.\n'
                        'You are dead.\n')
                        self.change_state()
                        self.check2 = True
                    elif self.action == 'no':
                        print('Deciding the bathroom is of no interest to you, you look around the room.\n'
                              'Your gaze dances around, on the pictures on the walls, on the messy clothes thrown around,\n'
                              'on the ugly furniture and wall paint. It is almost as someone intended this room to be '
                              'the ugliest.\nLastly, your gaze settles upon a ticket on the bed.\nIt seems to be a VIP ticket.\n'
                              'Do you take it?')
                        self.action = self.make_choice()
                        if self.action == 'yes':
                            print('You carefully put the ticket in your jacket\'s inner pocket.\n')
                            self.inventory.append('VIP Ticket')
                        elif self.action == 'no':
                            pass
                        print('Before leaving the room, a gunshot draws your attention. It seems like it came from the room '
                              'with the black door.\nDo you pursue the gunshot?\n')
                        self.action = self.make_choice()
                        if self.action == 'yes':
                            print('You rush towards the black door, propelled by the piercing sound of the gunshot.\n'
                                  'As the door swings open, a surge of unease washes over you.\n'
                                  'The room is shrouded in an eerie atmosphere, adorned with sinister cult objects.\n'
                                  'Their unsettling presence creates a sense of foreboding, casting long, menacing shadows along the walls.\n'
                                  'The air is heavy with an otherworldly energy, as if the room itself holds a dark secret.\n'
                                  'Amidst this macabre scene, a chilling path of blood stains the floor, beckoning you deeper into the heart of the ominous mystery.\n'
                                  'Do you pursue further?\n')
                            if self.action == 'yes':
                                print('The trail of blood leads you through the hidden door of a wardrobe.\n'
                                      'You enter something akin to a tunnel. The walls are carved and made of stone.\n'
                                      'A wooden door... ') # To be finished


                if self.action.lower() == 'go to red bedroom':
                    pass







        self.state = 'alive'

    def change_state(self):
        self.state = 'dead'


class Game(Player):
    phases = 1
    places = [' Forest Trip', 'Fantasy Adventure', 'Murder Mystery']
    adventure_count = 0

    @staticmethod
    def narrator1():
        print("Tonight, we have a special guest.\nHe is here to begin a journey that will lead him...places."
              "\nIt is all up to him to make the right choices. Or the ones that seem right, anyway.\n")

    @staticmethod
    def narrator2():
        print("Tonight, we have a special guest.\nHe is here to begin a journey that will lead him...places."
              "\nHopefully, this time, he will be better. Better than those before him.\n Life is so short nowadays.\n")

    @staticmethod
    def narrator3():
        print("Tonight, we have a special guest.\nI think you all know him by now. Know what he is capable of.\n"
              "Or rather, what he's incapable of. Ha-ha-ha...-ha.\n")

    @staticmethod
    def narrator4():
        print("You are very close to the end of your adventure. Closer than you would like.\n")

    @staticmethod
    def narrator5():
        print("... ... ... ... YOU ARE SUCH A DISAPPOINTMENT. YOU. ARE. DEAD.\n")

    @staticmethod
    def game_start(player):
        Game.adventure_count += 1
        if Game.phases == 1:
            Game.narrator1()
        elif Game.phases == 2:
            Game.narrator2()
        elif Game.phases == 3:
            Game.narrator3()
        elif Game.phases == 4:
            Game.narrator4()
        elif Game.phases == 5:
            Game.narrator5()

        print(f"Your choice for your setting is...: \n"
              f"1.{Game.places[0]}\n"
              f"2. {Game.places[1]}\n"
              f"3. {Game.places[2]}\n")
        player_choice = player.make_choice()
        player.creation(player_choice)
        print(player.intro)

    def first_room(self, player):
        print(player.level1)
        player.room_intro1()

    def second_room(self, player):
        print(player.level2)
        player.room_intro2()




player = Player()
game = Game()
game.game_start(player)
game.first_room(player)
game.second_room(player)