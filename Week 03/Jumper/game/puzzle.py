import random

class Puzzle:
    
    """The secret word that the user is trying to find. 
    
    The responsibility of Puzzle is to keep track of the leeter that is guessing the user,
    compare with the secret word and give a hint as a result. 
    
    Attributes:
        word_list (list[string]): list of words from which Puzzle will choose one at random
        word_playing (string): secret word that is randomly chosed to play with the user
        guessed_letter (string): letter that the user chooses to find out if it matches or not the letters of word_playing
        comparison_result (list[string]):list that saves the result of the comparison between the secret word and the letter chosen by the user
        self._loop_counter(int): variable to count the number of iterations a loop has performed
        self._true_counter (int):variable to count the number of iterations that another loop has performed
        self._verify_change (list[string]): save list allows to check if the "comparison_result" list has had changes during the game
    """
    
       
    def __init__(self):
        
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """

        self._word_list = [
            'abruptly', 
            'absurd', 
            'abyss', 
            'affix', 
            'askew', 
            'avenue', 
            'awkward', 
            'axiom', 
            'azure', 
            'bagpipes', 
            'bandwagon', 
            'banjo', 
            'bayou', 
            'beekeeper', 
            'bikini', 
            'blitz', 
            'blizzard', 
            'boggle', 
            'bookworm', 
            'boxcar', 
            'boxful', 
            'buckaroo', 
            'buffalo', 
            'buffoon', 
            'buxom', 
            'buzzard', 
            'buzzing', 
            'buzzwords', 
            'caliph', 
            'cobweb', 
            'cockiness', 
            'croquet', 
            'crypt', 
            'curacao', 
            'cycle', 
            'daiquiri', 
            'dirndl', 
            'disavow', 
            'dizzying', 
            'duplex', 
            'dwarves', 
            'embezzle', 
            'equip', 
            'espionage', 
            'euouae', 
            'exodus', 
            'faking', 
            'fishhook', 
            'fixable', 
            'fjord', 
            'flapjack', 
            'flopping', 
            'fluffiness', 
            'flyby', 
            'foxglove', 
            'frazzled', 
            'frizzled', 
            'fuchsia', 
            'funny', 
            'gabby', 
            'galaxy', 
            'galvanize', 
            'gazebo', 
            'giaour', 
            'gizmo', 
            'glowworm', 
            'glyph', 
            'gnarly', 
            'gnostic', 
            'gossip', 
            'grogginess', 
            'haiku', 
            'haphazard', 
            'hyphen', 
            'iatrogenic', 
            'icebox', 
            'injury', 
            'ivory', 
            'ivy', 
            'jackpot', 
            'jaundice', 
            'jawbreaker', 
            'jaywalk', 
            'jazziest', 
            'jazzy', 
            'jelly', 
            'jigsaw', 
            'jinx', 
            'jiujitsu', 
            'jockey', 
            'jogging', 
            'joking', 
            'jovial', 
            'joyful', 
            'juicy', 
            'jukebox', 
            'jumbo', 
            'kayak', 
            'kazoo', 
            'keyhole', 
            'khaki', 
            'kilobyte', 
            'kiosk', 
            'kitsch', 
            'kiwifruit', 
            'klutz', 
            'knapsack', 
            'larynx', 
            'lengths', 
            'lucky', 
            'luxury', 
            'lymph', 
            'marquis', 
            'matrix', 
            'megahertz', 
            'microwave', 
            'mnemonic', 
            'mystify', 
            'naphtha', 
            'nightclub', 
            'nowadays', 
            'numbskull', 
            'nymph', 
            'onyx', 
            'ovary', 
            'oxidize', 
            'oxygen', 
            'pajama', 
            'peekaboo', 
            'phlegm', 
            'pixel', 
            'pizazz', 
            'pneumonia', 
            'polka', 
            'pshaw', 
            'psyche', 
            'puppy', 
            'puzzling', 
            'quartz', 
            'queue', 
            'quips', 
            'quixotic', 
            'quiz', 
            'quizzes', 
            'quorum', 
            'razzmatazz', 
            'rhubarb', 
            'rhythm', 
            'rickshaw', 
            'schnapps', 
            'scratch', 
            'shiv', 
            'snazzy', 
            'sphinx', 
            'spritz', 
            'squawk', 
            'staff', 
            'strength', 
            'strengths', 
            'stretch', 
            'stronghold', 
            'stymied', 
            'subway', 
            'swivel', 
            'syndrome', 
            'thriftless', 
            'thumbscrew', 
            'topaz', 
            'transcript', 
            'transgress', 
            'transplant', 
            'triphthong', 
            'twelfth', 
            'twelfths', 
            'unknown', 
            'unworthy', 
            'unzip', 
            'uptown', 
            'vaporize', 
            'vixen', 
            'vodka', 
            'voodoo', 
            'vortex', 
            'voyeurism', 
            'walkway', 
            'waltz', 
            'wave', 
            'wavy', 
            'waxy', 
            'wellspring', 
            'wheezy', 
            'whiskey', 
            'whizzing', 
            'whomever', 
            'wimpy', 
            'witchcraft', 
            'wizard', 
            'woozy', 
            'wristwatch', 
            'wyvern', 
            'xylophone', 
            'yachtsman', 
            'yippee', 
            'yoked', 
            'youthful', 
            'yummy', 
            'zephyr', 
            'zigzag', 
            'zigzagging', 
            'zilch', 
            'zipper', 
            'zodiac', 
            'zombie', 
            ]

        self._word_playing = ""
        self._guessed_letter = ""
        self._comparison_result = []
        self._loop_counter = 0
        self._true_counter = 0
        self._verify_change = []

    def _get_new_played_word(self):
        
        """Choose randomly a new word to play for the user.

        Args:
            self (Puzzle): An instance of Puzzle.
        """

        self._word_playing = self._word_list[random.randint(0, len(self._word_list))]

        self._comparison_result = []
        for _ in self._word_playing:
            self._comparison_result.append("_")


    def _give_hint(self):
        
        """Gives a hint to the user

        Args:
            self (Puzzle): An instance of Puzzle.
            
        Returns:
            hint: String, the hint the user will get
        """

        hint = ""

        for _x in self._comparison_result:
            hint = hint + " " + _x

        return hint

    def _get_guessed_letter(self, guessed_letter):
        
        """Gets the letter that the user chooses

        Args:
            self (Puzzle): An instance of Puzzle.
            guessed_letter (string): letter that the user has choosed.
        """

        self._guessed_letter = guessed_letter

    def _compare_play_guess(self):
        
        """Compares the letter choose by the user and the secret word that is currently playing

        Args:
            self (Puzzle): An instance of Puzzle.
        
        Returns:
            boolean: True if user guessed a letter correctly, False if wrong
        """

        self._loop_counter = 0

        self._verify_change =[]


        for _b in self._comparison_result:
            self._verify_change.append(_b)

        for letter_compared in self._word_playing:
            if self._guessed_letter == letter_compared:
                self._comparison_result[self._loop_counter] = self._guessed_letter

            self._loop_counter += 1

        self._loop_counter = 0
        self._true_counter = 0

        for _a in self._comparison_result:
            if _a == self._verify_change[self._loop_counter]:
                self._true_counter +=1
            self._loop_counter += 1

        if self._true_counter == self._loop_counter:
            return True
        elif self._true_counter != self._loop_counter:
            return False


    def _find_match(self):
        
        """Determines whether the user has discovered the entire secret word or not yet

        Args:
            self (Puzzle): An instance of Puzzle.

        Returns:
            boolean: True if user guessed a the secret word, False if not yet
        """

        self._loop_counter = 0
        self._true_counter = 0

        for _z in self._word_playing:

            if _z == self._comparison_result[self._loop_counter]:
                self._true_counter += 1

            self._loop_counter += 1

        if self._true_counter != self._loop_counter:
            return False
        else:
            return True