import numpy as np
import pickle
import os

from configs import Configs


class HumanPlayer:
    def __init__(self, name):
        self.name = name

    def chooseAction(self, positions):
        while True:
            input_1 = input("Input your action col:")
            if input_1:
                col = input_1
                action = (0, int(col))
            else:
                row = 0
                col = int(input("Input your action col:"))
                action = (row, col)
            if action in positions:
#will return only if chosen location is empty.
                return action

    # append a hash state
    def addState(self, state):
        pass

    # at the end of game, backpropagate and update states value
    def feedReward(self, reward):
        pass

    def reset(self):
        pass