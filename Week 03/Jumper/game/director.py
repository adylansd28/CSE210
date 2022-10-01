from game.terminal_service import TerminalService
from game.jumper import Jumper
from game.puzzle import Puzzle


class Director:

    def __init__(self):
        self._terminal_service = TerminalService()
        self._puzzle = Puzzle()
        self._jumper = Jumper()
        self._game_on = True
        self._game_over_type = False
        
    def start_game(self):

        self._puzzle._get_new_played_word()
        self._terminal_service.write_text(self._puzzle._give_hint())
        self._terminal_service.write_text(self._jumper.get_jumper())

        while self._game_on:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

        self._game_over()

            
    def _get_inputs(self):
        guessed_letter = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._puzzle._get_guessed_letter(guessed_letter)
        
    def _do_updates(self):

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
        self._terminal_service.write_text(self._puzzle._give_hint())
        self._terminal_service.write_text(self._jumper.get_jumper())

    def _game_over(self):
        if self._game_over_type == True:
            print("\nYou Won!")
        elif self._game_over_type == False:
            print("\nYou Loose!")