from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:

    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        puzzle (Puzzle): The game's secret word.
        jumper (Jumper): The game's jumper.
        terminal_service (TerminalService): For getting and displaying information on the terminal.
        game_on (boolean): Whether or not to keep playing.
        game_over_type(boolean): Determines the type of message that will be displayed when the game is over
    """

    def __init__(self):
        
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self._terminal_service = TerminalService()
        self._puzzle = Puzzle()
        self._jumper = Jumper()
        self._game_on = True
        self._game_over_type = False
        
    def start_game(self):
        
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """

        self._puzzle._get_new_played_word()
        self._terminal_service.write_text(self._puzzle._give_hint())
        self._terminal_service.write_text(self._jumper.get_jumper())

        while self._game_on:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

        self._game_over()

            
    def _get_inputs(self):
        """Moves the seeker to a new location.

        Args:
            self (Director): An instance of Director.
        """
        guessed_letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._puzzle._get_guessed_letter(guessed_letter)
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """

        verifier = self._puzzle._compare_play_guess()

        if verifier:
            second_verifier = self._jumper.strike()
            self._game_over_type = second_verifier
            self._game_on = second_verifier
        else:
            if self._puzzle._find_match():
                self._game_over_type = True
                self._game_on = False
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text(self._puzzle._give_hint())
        self._terminal_service.write_text(self._jumper.get_jumper())

    def _game_over(self):
        """shows a farewell message at the end of the program execution
        depending on whether it was a user victory or defeat

        Args:
            self (Director): An instance of Director.
        """
        if self._game_over_type == True:
            print("\nYou Won!")
        elif self._game_over_type == False:
            print("\nYou Loose!")