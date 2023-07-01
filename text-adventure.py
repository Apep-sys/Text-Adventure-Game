class Player:
    def make_choice(self):
        self.choice = int(input("Make your choice (select 1, 2 or 3): "))
        return self.choice

    def creation(self, place_choice):
        fantasy_options = ['Knight', 'Mage', 'Druid']  # De facut clase pt fiecare optiune
        forest_options = ['Wawanakwa', 'Red Root', 'Blue Dawn']
        murder_mystery = ['09', '13', '256']
        if place_choice == 1:
            self.name = input("What is your name, scout?\n")
            self.pclass = int(input("And what camp do you come from?\n"
                                    "1. Camp Wawanakwa\n"
                                    "2. Camp Red Root\n"
                                    "3. Camp Blue Dawn\n"))
            self.place = 'Taibur Forest'
            self.detail1 = ['mapping', 'exploring', 'searching for tracks in the']
            self.intro = f"Welcome, {self.name}, to {self.place}. You were tasked by Camp {forest_options[self.pclass]}" \
                         f"with {self.detail1[self.pclass]} the Taibur Forest.\nCarefully weigh your choices, as your" \
                         f"survival depends on them. \nThe night sets in now...and you must survive it.  "

        if place_choice == 2:
            self.name = input("What is your name, adventurer?\n")
            self.pclass = int(input("And what order do you belong to?\n"
                                    "1. Knight\n"
                                    "2. Mage\n"
                                    "3. Druid\n"))
            self.place = 'Cave of Magtarr'
            self.detail1 = ['looking for the lost group', 'restoring the natural balance', 'defeating the creature']
            self.intro = f"I welcome thee, {fantasy_options[self.pclass]} {self.name} of the Great Country of Delirion.\n" \
                         f"Carefully listen, as you have been tasked with {self.detail1[self.pclass]} of the Cave of" \
                         f"Magtarr. \nNow, heed my call, as the challenges you will face must be met with proper thought" \
                         f"and strength of mind and body. \nMake it to the end of the cave and finish your task...but" \
                         f"beware the horrors in the dark."
        if place_choice == 3:
            self.name = input("What is your name, endorsed guest?\n")
            self.pclass = int(input("And what room are you from?\n"))
            self.place = 'Hotel Margot'
        self.state = 'alive'

    def change_state(self):
        self.state = 'dead'

class Game(Player):
    phases = 5
    places = [' forest trip', 'fantasy adventure', 'murder mystery']
    adventure_count = 0

    def narrator1(self):
        print("Tonight, we have a special guest.\nHe is here to begin a journey that will lead him...places."
              "\nIt is all up to him to make the right choices. Or the ones that seem right, anyway.\n")

    def narrator2(self):
        print("Tonight, we have a special guest.\nHe is here to begin a journey that will lead him...places."
              "\nHopefully, this time, he will be better. Better than those before him.\n Life is so short nowadays.\n")

    def narrator3(self):
        print("Tonight, we have a special guest.\nI think you all know him by now. Know what he is capable of.\n"
              "Or rather, what he's incapable of. Ha-ha-ha...-ha.\n")

    def narrator4(self):
        print("You are very close to the end of your adventure. Closer than you would like.\n")

    def narrator5(self):
        print("... ... ... ... YOU ARE SUCH A DISAPPOINTMENT. YOU. ARE. DEAD.\n")

    def game_start(self, player):
        # De adaugat anunt cu X din Y a venit etc.
        Game.adventure_count += 1
        Game.narrator1(self)
        print(f"Your choice for your setting is...: \n"
              f"1.{Game.places[0]}\n"
              f"2. {Game.places[1]}\n"
              f"3. {Game.places[2]}\n")
        player_choice = player.make_choice()
        player.creation(player_choice)
        print(player.intro)

player = Player()
game = Game()
game.game_start(player)
