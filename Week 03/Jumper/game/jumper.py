import random

class Jumper:

    """
        The person that is trying to find the secret word of Puzzle 

        Jumper responsability of the attempts that the user has left and shows a graphic signal accordingly

        Attributes:
            lives (int): Lives that the jumper has (1-4).
            current_jumper (string): The current graph signal from the jumper.
            jumpers (list[string]): List of graphic signals that jumper can display.
    """

    def __init__(self):

        """
        Constructs a new Jumper.

        Args:
            self (Jumper): An instance of Jumper.
        """

        self._lives = 4
        self._current_jumper =""
        self._jumpers =[
            "  /‾‾\ \n  \‾‾/ \n   \/  \n    0  \n   /|\ \n   / \ ",
            "  /  \ \n  \‾‾/ \n   \/  \n    0  \n   /|\ \n   / \ ",
            "  \  / \n   \/  \n    0  \n   /|\ \n   / \ ",
            "   \/  \n    0  \n   /|\ \n   / \ ",
            "    x  \n   /|\ \n   / \ "
        ]
    
    def get_jumper(self):

        """Gets the current grapich signal jumper needs to show.
            Args:
                self (Jumper): An instance of Jumper.

            Returns:
                string: The current graphic signal of jumper
        """

        self._current_jumper = self._jumpers[0]

        if self._lives == 0:
            self._current_jumper = self._jumpers[4]
        elif self._lives == 1:
            self._current_jumper = self._jumpers[3]
        elif self._lives == 2:
            self._current_jumper = self._jumpers[2]
        elif self._lives == 3:
            self._current_jumper = self._jumpers[1]
        elif self._lives == 4:
            self._current_jumper = self._jumpers[0]

        return "\n" + self._current_jumper + "\n\n^^^^^^^"
        
    def strike(self):
        """removes a parachute line from the jumper for a failed attempt.

            Args:
                self (Jumper): An instance of Jumper.
            Returns:
                boolean: True if jumper still has lives left, false if the last line of the parachute has already been deleted
        """

        self._lives -= 1

        if self._lives > 0:
            return True
        elif self._lives <= 0:
            return False