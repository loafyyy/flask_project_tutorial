import random

class Exponentiator(object):
    def __init__(self, power=2):
        self.power = power

    def exponentiate(self, x):
        return x ** self.power + 1

def generate_random_number():
    return random.randint(-100, 100)