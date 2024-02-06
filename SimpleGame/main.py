import numpy as np
import pickle
import argparse
import os

from state import State
from player import HumanPlayer

if __name__ == "__main__":
    p1 = HumanPlayer("human1")
    p2 = HumanPlayer("human2")
    st = State(p1, p2)
    st.playGame()