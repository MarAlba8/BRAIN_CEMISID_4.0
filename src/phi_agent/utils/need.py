import random
import numpy as np


# random.seed(2)
class Need:
    def __init__(self, sign=0, degree=0, len_degree=4):

        self.len_sign = 2
        self.len_degree = len_degree

        if sign == None and degree == None:
            self.state = np.array([sign, degree])
        else:
            self.state = np.array([sign, degree], dtype=np.int8)

        self.sign_str = {0: "+", 1: "-"}

    def __str__(self):
        if self.state[0] != None and self.state[1] != None:
            return f"{self.sign_str[self.state[0]]}{self.state[1] / self.len_degree}"
        else:
            return "None"

    def __repr__(self):
        if self.state[0] != None and self.state[1] != None:
            return f"{self.sign_str[self.state[0]]}{self.state[1] / self.len_degree}"
        else:
            return "None"

    def __add__(self, other):
        if other.state[0] == None or other.state[1] == None:
            return Need(self.state[0], self.state[1])
        elif self.state[0] == None or self.state[1] == None:
            return Need(other.state[0], other.state[1])

        if self.state[1] == 0 and other.state[1] == 0:
            return Need(self.state[0], self.state[1])

        elif self.state[0] == 0:
            if other.state[0] == 0:
                sign = 0
                degree = min(self.state[1] + other.state[1], self.len_degree)
            else:
                if self.state[1] >= other.state[1]:
                    sign = 0
                    degree = self.state[1] - other.state[1]
                else:
                    sign = 1
                    degree = abs(self.state[1] - other.state[1])
        else:
            if other.state[0] == 1:
                sign = 1
                degree = min(self.state[1] + other.state[1], self.len_degree)
            else:
                if self.state[1] >= other.state[1]:
                    sign = 1
                    degree = self.state[1] - other.state[1]
                else:
                    sign = 0
                    degree = abs(self.state[1] - other.state[1])

        return Need(sign, degree)

    def __lt__(self, other):  # To get called on comparison using < operator.
        if self.state[0] == None and self.state[1] == None and other.state[0] != None and other.state[1] != None:
            return True
        elif other.state[0] == None and other.state[1] == None and self.state[0] != None and self.state[1] != None:
            return False
        elif self.state[0] == 0 and other.state[0] == 0:
            return self.state[1] < other.state[1]
        elif self.state[0] == 1 and other.state[0] == 1:
            return self.state[1] > other.state[1]
        elif self.state[0] == 0 and other.state[0] == 1:
            return False
        elif self.state[0] == 1 and other.state[0] == 0:
            return True

    def __eq__(self, other):  # To get called on comparison using == operator.
        if self.state[0] == other.state[0] and self.state[1] == other.state[1]:
            return True
        else:
            return False

    def __ne__(self, other):  # To get called on comparison using != operator.
        if self == other:
            return False

    def __le__(self, other):  # To get called on comparison using <= operator.
        if self == other:
            return True
        elif self < other:
            return True
        else:
            return False

    def __gt__(self, other):  # To get called on comparison using > operator.
        if self < other:
            return False
        else:
            return True

    def __ge__(self, other):  # To get called on comparison using >= operator.
        if self == other:
            return True
        elif self > other:
            return True
        else:
            return False

    def reset(self):
        sign = random.randint(0, 1)
        degree = random.randint(0, 2)
        self.state = np.array([sign, degree], dtype=np.int8)

    def sample(self):
        sign = random.randint(0, 1)
        degree = random.randint(0, 3)
        return Need(sign, degree)

    def none(self):
        return Need(None, None)

    def zero(self):
        return Need(0, 0)
