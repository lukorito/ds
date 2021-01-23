# Find an unknown integer 1 ≤ x ≤ N by asking k questions “Is x = y?” (for any 1 ≤ y ≤ N ). When you ask such a question, simply enter "y" instead of "Is x=y?" Your opponent will reply either “Yes”, or “x < y”, or “x > y.
# Recursion

import random

class Questions:
    def __init__(self, k):
        self.k = k
        self.N = pow(2, k) - 1
        self.count = k
        self.x = random.randint(1, k)

    def check_value(self, value):
        self.count = self.count - 1
        print(f"You have {self.count} chances remaining")
        if value == self.x:
            print(f"Value found: {self.x}")
            return True
        elif value > self.x:
            print(f"X is smaller than: {value}")
            return False
        elif value < self.x:
            print(f"X is larger than: {value}")
            return False
k_values = [2,4,7,21]


def question_script():
    question = Questions(4)
    while question.count > 0:
        value = input(f"Choose a number between 1 and {question.N}: ")
        if question.check_value(int(value)):
            break;

question_script()
