class Player:

    def __init__(self):
        self.name = None
        self.place = None
        self.detail1 = None
        self.level1 = None
        self.pclass = None
        self.intro = None
        self.room_intro2 = None
        self.choice = None
        self.state = None
        self.inventory = []
        self.items = None
        self.rooms1 = None
        self.action1 = None
        self.check1 = False
    def make_choice(self):
        self.choice = input("\n>").lower()
        return self.choice

    def creation(self, place_choice):
        self.place_choice = place_choice
        fantasy_options = ['Knight', 'Mage', 'Druid']  # De facut clase pt fiecare optiune
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
            self.detail1 = ['fashion gala, in the main hall,', 'interview for your paper, in the main hall,',
                            'guests\'s appetite, in the main hall,']
            self.level1 = 'Hallway\n'
            self.rooms1  = ['Closet', 'Elevator', 'Balcony']
            self.items = ['Magnifying Glass', 'Fuse']
            self.intro = f"Oh, dear! If it isn't {self.name}! We were expecting you, and we are pleased to have you.\n" \
                         f"Please, make yourself at home in our dear {self.place}. Your room is {self.pclass}.\n" \
                         f"For tonight, the {self.detail1[murder_options.index(self.pclass)]} " \
                         f"awaits you. Do consider taking your time when " \
                         f"deciding how to best approach this event!\nIt won't be long until the MAIN event will begin...\n" \
                         f"Consider yourself lucky for the heads up. The other guests aren't so lucky. \nOne, in particular...\n" \
                         f"But enough talk! Go on! Have a wonderful evening!\nMaybe your last one.\n "

    def room_intro1(self):
        if self.place_choice.title() == 'Murder Mystery':
            print('You enter the dimly lit hallway, caught between the safety of your room and the mysteries ahead.\n ' 
                'The air is still, carrying a hint of aged wood. The faded wallpaper peels, revealing the passage of time.\n ' 
                'To your left, a closed door leads to a balcony, teasing glimpses of the outside world. \n' 
                'To your right, a slightly ajar door reveals a cramped closet, holding secrets within its limited space.\n ' 
                'Straight ahead, a closed door guards the elevator, its faint hum echoing through the corridor.\n ' 
                'You observe two items: a fuse, laying on a shelf, and a magnifying glass, somehow waiting for a firm hand to pick it up.' 
                'Anticipation settles upon you as you stand in this hallway, ready to unlock the stories within each room. The adventure awaits, just beyond the threshold.\n' 
                'What is your next move?\n' 
                'Go to Rooms\n' 
                'Pick up Items\n')
            while self.check1 == False:
                print('What is your next move?\n' 
                               'Go to Rooms\n' 
                               'Pick up Items\n')
                self.action1 = self.make_choice()
                if self.action1.lower() == 'pick up items':
                    print('Which item do you pick up?\n'
                          'Fuse\n'
                          'Magnifying Glass\n')
                    self.action1 = self.make_choice()
                    if self.action1.lower() == 'magnifying glass':
                        print('You pick up a magnifying glass. Hopefully, it will be useful in the way you think.\n')
                        self.inventory.append('Magnifying Glass')
                        continue
                    elif self.action1.lower() == 'fuse':
                        print('You picked up a fuse. Someone might miss it.\n')
                        self.inventory.append('Fuse')
                        continue
                elif self.action1.lower() == 'go to rooms':
                    print('Which room are you going to?\n'
                                     'Closet\n'
                                     'Elevator\n'
                                     'Balcony\n')
                    self.action1 = self.make_choice()
                    if self.action1.lower() == 'closet' and 'Fuse' not in self.inventory:
                        print('You enter the cramped closet. The janitor\'s tools are lying about.\nThe stingy smell of cleaning '
                          'products bothers you, but due to the odor of the freshly washed sheets, it is a minor nuisance.\n'
                          'You think there is nothing interesting here to be seen, but then you spot a multitude of red spots, '
                          'splattered all over a sheet, in a tucked away basket.\nIt looks like...blood.\n'
                          'You take a mental note of this and return to the hallway.\n')
                        continue
                    elif self.action1.lower() == 'closet' and 'Fuse' in self.inventory:
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
                    if self.action1.lower() == 'balcony':
                        print('The wind lifts your hair...')
                    # Need to finish the rest of the rooms.





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




player = Player()
game = Game()
game.game_start(player)
game.first_room(player)
