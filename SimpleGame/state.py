import numpy as np

from configs import Configs


class State():
    def __init__(self, p1, p2):
        self.configs = Configs()
        self.BOARD_COLS = self.configs.BOARD_COLS
        self.BOARD_ROWS = self.configs.BOARD_ROWS
        #        self.POLICIES_DIR = self.configs.POLICIES_DIR

        self.p1 = p1
        self.p2 = p2
        self.roundCount = 0

        self.board = np.zeros((self.BOARD_ROWS, self.BOARD_COLS))
#        print(self.board)
#        print(self.board.ndim)
        self.boardHash = None
        self.isEnd = False
        self.playerSymbol = 1

    #    def getHash(self):
    #        self.boardHash = str(self.board.reshape(self.BOARD_ROWS * self.BOARD_COLS))
    #        return self.boardHash

    def getAvailablePositions(self):
        positions = []
        for i in range(self.BOARD_ROWS):
            for j in range(self.BOARD_COLS):
                if self.board[i][j] == 0:
                    positions.append((i, j))
#        print(positions)
        return positions

    def winner(self):
        player1Score = 0
        player2Score = 0
        """
        Values on board: Player 1: 1 || Player 2: -1
        To check if there is a winner/draw
        """

        for i in range(self.BOARD_COLS):

            if self.board[0][i] == 1:
                player1Score += i

            elif self.board[0][i] == -1:
                player2Score += i

        if self.roundCount == 7 and int(player1Score) > int(player2Score):
            self.isEnd = True

            return 1
        elif self.roundCount == 7 and int(player1Score) < int(player2Score):
            self.isEnd = True
            return -1
        elif self.roundCount == 7 and int(player1Score) == int(player2Score):
            self.isEnd = True
            return 0


        #game continues
        self.isEnd = False
        return None

    def updateStates(self, position):
        self.board[position] = self.playerSymbol

        # Switch player
        self.playerSymbol = 1 if self.playerSymbol == -1 else -1

    def reset(self):
        self.board = np.zeros((self.BOARD_ROWS, self.BOARD_COLS))
        self.boardHash = None
        self.isEnd = False
        self.playerSymbol = 1

    #    def giveReward(self):
    #        """
    #        At game end only
    #        """
    #        result = self.winner()
    #
    #        if result == 1:
    #            self.p1.feedReward(1)
    #            self.p2.feedReward(0)
    #
    #        elif result == -1:
    #            self.p1.feedReward(0)
    #            self.p2.feedReward(1)
    #
    #        else:
    #            # if its a draw
    #            self.p1.feedReward(0.1) # less reward
    #            self.p2.feedReward(0.5) # to make p1 more aggressive

    # play 2 humans
    def playGame(self):

        while not self.isEnd:
            self.showBoard()
            # Player 1
            positions = self.getAvailablePositions()
            p1_action = self.p1.chooseAction(positions)
            # take action and upate board state
            self.updateStates(p1_action)
            self.showBoard()
            # check board status if it is end
            win = self.winner()

            self.roundCount += 1


            if win is not None:
                if win == 1:
                    print(self.p1.name, "wins!")
                elif win == 1:
                    print(self.p1.name, "wins!")
                else:
                    print("tie!")
                self.reset()
                break

            else:
                # Player 2
                positions = self.getAvailablePositions()
                p2_action = self.p2.chooseAction(positions)

                self.updateStates(p2_action)
                self.showBoard()
                win = self.winner()
                self.roundCount += 1

                if win is not None:
                    if win == -1:
                        print(self.p2.name, "wins!")
                    elif win == 1:
                        print(self.p1.name, "wins!")
                    else:
                        print("tie!")
                    self.reset()
                    break



    def showBoard(self):
        # p1: x  p2: o
        for i in range(0, self.BOARD_ROWS):
            print("  0   1   2   3   4   5   6   7")
            print('------------------------------------')
            out = '| '
            for j in range(0, self.BOARD_COLS):
                if self.board[i, j] == 1:
                    token = 'x'
                if self.board[i, j] == -1:
                    token = 'o'
                if self.board[i, j] == 0:
                    token = ' '
                out += token + ' | '
            print(out)
        print('------------------------------------')