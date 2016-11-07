from collections import namedtuple
from games import (Game)

class GameState:
    # def __init__(self, to_move, board, start_player,
    #              label=None,):
    #     self.to_move = to_move
    #     self.board = board
    #     self.label = label
    #     self.start_player = start_player
    def __init__(self, to_move, board, label=None,):
        self.to_move = to_move
        self.board = board
        self.label = label
        #self.start_player = start_player

    def __str__(self):
        if self.label == None:
            return super(GameState, self).__str__()
        return self.label

class FlagrantCopy(Game):
    """A flagrant copy of TicTacToe, from game.py
    It's simplified, so that moves and utility are calculated as needed
    Play TicTacToe on an h x v board, with Max (first player) playing 'X'.
    A state has the player to move and a board, in the form of
    a dict of {(x, y): Player} entries, where Player is 'X' or 'O'."""

    def __init__(self, h=3, v=3, k=3):
        self.h = h
        self.v = v
        self.k = k
        self.initial = GameState(to_move='X', board={})

    def actions(self, state):
        try:
            return state.moves
        except:
            pass
        "Legal moves are any square not yet taken."
        moves = []
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                if (x,y) not in state.board.keys():
                    moves.append((x,y))
        state.moves = moves
        return moves

    # defines the order of play
    def opponent(self, player):
        if player == 'X':
            return 'O'
        if player == 'O':
            return 'X'
        return None

    def result(self, state, move):
        if move not in self.actions(state):
            return state  # Illegal move has no effect
        board = state.board.copy()
        player = state.to_move
        board[move] = player
        next_mover = self.opponent(player)
        return GameState(to_move=next_mover, board=board)

    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        try:
            return state.utility if player == 'X' else -state.utility
        except:
            pass
        board = state.board
        util = self.check_win(board, 'X')
        if util == 0:
            util = -self.check_win(board, 'O')
        state.utility = util
        return util if player == 'X' else -util

    # Did I win?
    def check_win(self, board, player):
        # check rows
        for y in range(1, self.v + 1):
            if self.k_in_row(board, (1,y), player, (1,0)):
                return 1
        # check columns
        for x in range(1, self.h + 1):
            if self.k_in_row(board, (x,1), player, (0,1)):
                return 1
        # check \ diagonal
        if self.k_in_row(board, (1,1), player, (1,1)):
            return 1
        # check / diagonal
        if self.k_in_row(board, (3,1), player, (-1,1)):
            return 1
        return 0

    # does player have K in a row? return 1 if so, 0 if not
    def k_in_row(self, board, start, player, direction):
        "Return true if there is a line through start on board for player."
        (delta_x, delta_y) = direction
        x, y = start
        n = 0  # n is number of moves in row
        while board.get((x, y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = start
        while board.get((x, y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1  # Because we counted start itself twice
        return n >= self.k

    def terminal_test(self, state):
        "A state is terminal if it is won or there are no empty squares."
        return self.utility(state, 'X') != 0 or len(self.actions(state)) == 0

    def display(self, state):
        board = state.board
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
            print()

class Swag(Game):
    """A electronic version of the game Swag, described on thinkfun.com."""
    def __init__(self,#start_player
                 ):
        "Initializes a swag game with 3 bags"
        self.bag1 = Bag(
            bagNumber = 1,
            tokens = 3
        )
        self.bag2 = Bag(2,4)
        self.bag3 = Bag(3,5)
        #self.bag1tokens = 3
        #self.bag2tokens = 4
        #self.bag3tokens = 5
        board = {self.bag1.bagNumber:self.bag1.tokens,
                      self.bag2.bagNumber:self.bag2.tokens,self.bag3.bagNumber:self.bag3.tokens,4:6,5:7}
        self.initial = GameState(to_move = '1', board = board,#start_player=start_player
                                 )
       # self.bagNumber = 3
       # self.board = bags(self.bagNumber)
    #def __init__(self,bagNumber):
        #"Initializes a swag game with the given number of bags"
        #self.bagNumber = bagNumber
    #def bags(self, bagNumber):
    #"Creates a board for a given number of bags"
    def actions(self,state):
        "Determine the set of available actions"
        # try:
        #     return state.moves
        # except:
        #     pass
        # "You may take any number of tokens from only one bag."
        moves = []
        # bag1tokens = self.bag1.tokens
        # bag2tokens = self.bag2.tokens
        # bag3tokens = self.bag3.tokens
        bag1tokens = state.board[1]
        bag2tokens = state.board[2]
        bag3tokens = state.board[3]
        bag4tokens = state.board[4]
        bag5tokens = state.board[5]
        for x in range(1,bag1tokens + 1):
            moves.append((1,x))
        for y in range(1,bag2tokens + 1):
            moves.append((2,y))
        for z in range(1,bag3tokens + 1):
            moves.append((3,z))
        for r in range(1,bag4tokens+1):
            moves.append((4,r))
        for t in range(1,bag5tokens+1):
            moves.append((5,t))
        state.moves = moves
        return moves

    def opponent(self, player):
        "Returns who has the next turn"
        if player == '1':
            return '2'
        if player == '2':
            return '1'

    def utility(self, state, player):
        "Determines the utility of the player choosing a particular move"
        # try:
        #     return state.utility
        # except:
        #     pass
        board = state.board
        util = self.check_win(board,player) #'1')
        # if util == 0:
        #     if (board[1] == 0 and board[2] == 0) or (board[1] == 0 and board[3] ==0) or (board[2] == 0 and board[3] == 0):
        #         util = -1
        # if util == 0:
        #     util = -self.check_win(board,'2')
        state.utility = util
        lastPlayer = state.to_move
        to_return = util if lastPlayer == '1' else -util
        return to_return

    def check_win(self,board,player): #player):
        "Checks to see if the player has won"
        #if self.bag1.isEmpty() and self.bag2.isEmpty() and self.bag3.isEmpty():
        if board[1] == 0 and board[2] == 0 and board[3] == 0 and board[4] == 0 and board[5] == 0:
            #if player == self.initial.start_player:
                #return 1

            #return -1
            return 1
        return 0

    def terminal_test(self, state):
        "A terminal state means a player has one or no moves are left"
        value = self.utility(state, '1') != 0 or len(self.actions(state)) == 0
        #value = len(self.actions(state)) == 0
        return value

    def result(self,state,move):
        if move not in self.actions(state):
            return state  # Illegal move has no effect
        board = state.board.copy()
        player = state.to_move
        bag, tokens_taken = move
        board[bag] += -tokens_taken
        next_mover = self.opponent(player)
        return GameState(to_move=next_mover, board=board)


    def display(self, state):
        board = state.board
        print('1)',end='')
        for x in range(1, board[1] + 1):
            print('.', end= '')
            #print()
        #print(' ',end='')
        print()
        print('2)',end='')
        for y in range(1,board[2] + 1):
            print('.', end = '')
            #print()
        print()
        #print(' ', end='')
        print('3)',end='')
        for z in range(1,board[3]+1):
            print('.', end = '')
            # for y in range(1, self.v + 1):
            #     print(board.get((x, y), '.'), end=' ')
            #print()
        print()
        print('4)', end='')
        for y in range(1, board[4] + 1):
            print('.', end='')
            # print()
        print()
        print('5)', end='')
        for y in range(1, board[5] + 1):
            print('.', end='')
            # print()
        print()
class Bag():
    "Creates a bag with a number and a certain number of tokens"
    def __init__(self,bagNumber,tokens):
        self.bagNumber = bagNumber
        self.tokens = tokens
    def isEmpty(self):
        if self.bagNumber == 0:
            return True
        return False

myGame = FlagrantCopy()

# won = GameState(
#     to_move = 'O',
#     board = {(1,1): 'X', (1,2): 'X', (1,3): 'X',
#              (2,1): 'O', (2,2): 'O',
#             },
#     label = 'won'
# )
#
# winin1 = GameState(
#     to_move = 'X',
#     board = {(1,1): 'X', (1,2): 'X',
#              (2,1): 'O', (2,2): 'O',
#             },
#     label = 'winin1'
# )
#
# losein1 = GameState(
#     to_move = 'O',
#     board = {(1,1): 'X', (1,2): 'X',
#              (2,1): 'O', (2,2): 'O',
#              (3,1): 'X',
#             },
#     label = 'losein1'
# )
#
# winin3 = GameState(
#     to_move = 'X',
#     board = {(1,1): 'X', (1,2): 'O',
#              (2,1): 'X',
#              (3,1): 'O',
#             },
#     label = 'winin3'
# )
#
# losein3 = GameState(
#     to_move = 'O',
#     board = {(1,1): 'X',
#              (2,1): 'X',
#              (3,1): 'O', (1,2): 'X', (1,2): 'O',
#             },
#     label = 'losein3'
# )
#
# winin5 = GameState(
#     to_move = 'X',
#     board = {(1,1): 'X', (1,2): 'O',
#              (2,1): 'X',
#             },
#     label = 'winin5'
# )
#
# lost = GameState(
#     to_move = 'X',
#     board = {(1,1): 'X', (1,2): 'X',
#              (2,1): 'O', (2,2): 'O', (2,3): 'O',
#              (3,1): 'X'
#             },
#     label = 'lost'
# )


myGame2 = Swag(#'1'
               )

won = GameState(
    to_move = '1',
    board = {1:0,2:0,3:0,4:0,5:0},
    label = 'win'
)
#The Gamestates below are formatted as winxyz where x is the number of moves to win, y is the bag to win from, and z is the number
#of tokens
win111 = GameState(
    to_move = '2',
    board = {1:1,2:0,3:0,4:0,5:0},
    label = 'win1 taking one from bag 1'
)
win112 = GameState(
    to_move = '2',
    board = {1:2,2:0,3:0,4:0,5:0},
    label = 'win2 taking two from 1',
    #start_player = '1'
)
win113 = GameState(
    to_move = '2',
    board = {1:3,2:0,3:0,4:0,5:0},
    label = 'win3 taking 3 from 1'
)
win121 = GameState(
    to_move = '2',
    board = {1:0,2:1,3:0,4:0,5:0},
    label = 'win4 taking 1 from 2'
)
win122 = GameState(
    to_move = '2',
    board = {1:0,2:2,3:0,4:0,5:0},
    label = 'winin1 taking 2 from 2'
)
win123 = GameState(
    to_move = '2',
    board = {1:0,2:3,3:0,4:0,5:0},
    label = 'win5 taking 3 from 2'
)
win124 = GameState(
    to_move = '2',
    board = {1:0,2:4,3:0,4:0,5:0},
    label = 'win6 taking 4 from 2'
)
win131 = GameState(
    to_move = '2',
    board = {1:0,2:0,3:1,4:0,5:0},
    label = 'win7 taking 1 from 3'
)
win135 = GameState(
    to_move = '2',
    board = {1:0,2:0,3:5,4:0,5:0},
    label = 'win8 taking 5 from 3'
)
start = GameState(
    to_move = '1',
    board = {1:3,2:4,3:5,4:6,5:7},
    label = 'start'
)
test = GameState(
    to_move = '1',
    board = {1:2,2:3,3:2,4:4,5:2},
    label = 'test'
)


myGames = {
    # myGame: [
    #     won,
    #     winin1, losein1, winin3, losein3, winin5,
    #     lost,
    # ]
    myGame2: [
        won,
        win111,
        win112, win113,win121,win122,win123,win124,win131,win135,start,test
    ]
}