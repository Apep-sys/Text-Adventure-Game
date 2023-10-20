import time
import game_py as game_file


class Player:

    def __init__(self):
        self.name = None
        self.place = None
        self.intro = None
        self.pclass = None
        
        self.temp_check = False
        self.place_choice = None
        self.game_end = False
        
        self.choice = None
        self.action = None
        self.state = 'alive'  # State of the player - Dead/Alive
        
        self.inventory = []
        
        self.detail1 = None
        self.level1 = None
        self.rooms1 = None
        self.items1 = None
        self.check1 = False

        self.level2 = None
        self.rooms2 = None
        self.check2 = False
        self.items2 = None
        self.passing = False
        
        self.level3 = None
        self.items3 = None
        self.check3 = False

        self.level4 = None
        self.items4 = None
        self.check4 = False

        
        
    def make_choice(self):
        self.choice = input("\n>").lower()
        return self.choice

    def creation(self, place_choice):
        self.place_choice = place_choice
        murder_options = ['room 09', 'room 13', 'room 256']
        if self.place_choice.title() == 'Murder Mystery':
            self.place = 'Hotel Margot'
            self.detail1 = ['fashion gala', 'interview for your paper',
                            'business meeting']
            self.level1 = 'Hallway'
            self.rooms1 = ['Closet', 'Elevator', 'Balcony']
            self.items1 = ['Magnifying Glass', 'Fuse']
            while True:
                try:

                    self.intro = (f"Oh, dear! If it isn't {self.name}! We were expecting you, and we are pleased to have you.\n" 
                             f"Please, make yourself at home in our dear {self.place}. Your room is {self.pclass.title()}.\n" 
                             f"For tonight, the {self.detail1[murder_options.index(self.pclass)]}, in the main lobby, " 
                             f"awaits you. Do consider taking your time when " 
                             f"deciding how to best approach this event!\nIt won't be long until the MAIN event will begin...\n" 
                             f"Consider yourself lucky for the heads up. The other guests aren't so lucky. \nOne, in particular...\n" 
                             f"But enough talk! Go on! Have a wonderful evening!\nMaybe your last one.\n\n")

                except:
                    message = 'I did not understand that. Please repeat.'
                    game_file.display_message(1, message)
                    time.sleep(2)
                    game_file.screen.fill(game_file.black)

                    game_file.display_message(1, 'And what room will it be?')
                    choices = ['>Room 09', '>Room 13', '>Room 256']
                    game_file.display_message(2, choices, (50, 80))
                    self.pclass = game_file.get_player_input().lower()
                    game_file.screen.fill(game_file.black)

                    continue

                break
            
            if self.pclass == 'room 09':
                self.level2 = 'The Upper Floor'
            elif self.pclass == 'room 13' or self.pclass == 'room 256':
                self.level2 = 'The Lower Floor'
                
            self.rooms2 = ['The Green Door', 'The Black Door', 'The Red Door']
            self.items2 = ['Bloody Letter', 'VIP Ticket', 'Cursed Mark']

            self.level3 = 'Lounge'
            self.items3 = ['Opened Letter', 'Unopened Letter']
            self.level4 = 'Main Lobby'
            self.items4 = []

    def change_state(self):
        self.state = 'dead'


class Game(Player):
    phases = 1
    def narrator1(self):
        message = ("Tonight, we have a special guest. He is here to begin a journey that will lead him...places."
              " It is all up to him to make the right choices. Or the ones that seem right, anyway. ")
        return message

    def narrator2(self):
        message = ("Tonight, we have a special guest. I think you all know him by now. Know what he is capable of. "
              "Or rather, what he's incapable of. Ha-ha-ha...-ha. ")
        return message

    def narrator3(self):
        message = ("You are very close to the end of your adventure. Closer than you would like. ")
        return message

    def narrator4(self):
        message = ("... ... ... ... YOU ARE SUCH A DISAPPOINTMENT. YOU. ARE. DEAD. ")
        return message

    def game_start(self, game):
        if game.phases == 1:
            return self.narrator1()
        elif game.phases == 2:
            return self.narrator2()
        elif game.phases == 3:
            return self.narrator3()
        elif game.phases == 4:
            return self.narrator4()
