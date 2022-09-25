from game.card import card

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__ (self):
        self.first_card = card()
        self.first_card.draw_card()
        self.cards = [self.first_card.new_card]
        self.is_playing = True
        self.choice = ""
        self.score = 0
        self.total_score = 300

    def start_game (self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        while self.is_playing:
            self.show_last_card()
            self.get_input()
            self.next_card()
            self.get_score()
            self.game_state()
            print()

        self.game_over()


    def show_last_card(self):
        print(f"The card is: {self.cards[-1]}")

    def next_card(self):
        new_card = card()
        new_card.draw_card()
        new_card_value = new_card.new_card
        if len(self.cards) < 13:
            while new_card_value in self.cards:
                new_card.draw_card()
                new_card_value = new_card.new_card
        else:
            self.is_playing = False
        self.cards.append(new_card_value)
        print(f"Next card was: {new_card_value}")

    def get_input(self):
        if len(self.cards) == 13:
            return
        else:
            self.choice = input("Higher or lower? [h/l] ")

    def get_score(self):
        if self.choice == "h":
            if self.cards[-1] > self.cards[-2]:
                self.score = 100
            else:
                self.score = -75
        elif self.choice == "l":
            if self.cards[-1] > self.cards[-2]:
                self.score = -75
            else:
                self.score = 100

        self.total_score += self.score
        if self.total_score > 0:
            print(f"Your score is: {self.total_score}")
        else:
            print("Your score is: 0")
            self.is_playing = False

    def game_state(self):

        if len(self.cards) == 13:
            self.is_playing = False
        else:
            game_over = input("Play again? [y/n] ")

            if game_over == "y":
                return
            elif game_over == "n":
                self.is_playing = False

    def game_over(self):
        print("Game Over!")
        print(f"Your final score was: {self.total_score}")

