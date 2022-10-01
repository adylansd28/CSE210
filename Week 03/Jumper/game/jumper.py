import random

class Jumper:

    def __init__(self):

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

        self._lives -= 1

        if self._lives > 0:
            return True
        elif self._lives <= 0:
            return False