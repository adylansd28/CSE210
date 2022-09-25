import random

class card:

    def __init__(self):
        self.new_card = 0

    def draw_card(self):
        self.new_card = random.randint(1,13)
