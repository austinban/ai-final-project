from collections import namedtuple
from games import (Game)
from copy import deepcopy


class GameState:
    def __init__(self, to_move, board, label=None, depth=8):
        self.to_move = to_move
        self.board = board
        self.label = label
        self.MaxDepth = depth

    def __str__(self):
        if self.label == None:
            return super(GameState, self).__str__()
        return self.label


class DotsandBoxes(Game):

    """A copy of the game dots and boxes. This game is played on a board that is 3 by 3 square
    the goal is to create a completed square first."""


    def __init__(self, h=3, v=3):
        self.h = h
        self.v = v
        self.initial = GameState(to_move='---', board={})


    def actions(self, state):

        try:
            return state.moves
        except:
            pass
        "Legal moves are any square not yet taken."
        moves = []
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                if (x, y) not in state.board:
                    moves.append((x, y))
        state.moves = moves
        return moves

    def _makeMove(self, line1, line2):
        """return a new move and makes sure it's legal"""
        x, y = line2[0] - line1[0], line2[1] - line1[1]
        assert ((abs(x) == 1 and abs(y) == 0) or
                 (abs(x) == 0 and abs(y) == 1))
        if line1 < line2:
            return (line1, line2)
        else:
            return (tuple(line2), tuple(line1))


# defines the order of play
    def opponent(self, player):
        if player == 'Player 1':
            return 'Player 2'
        if player == 'Player 2':
            return 'Player 1'
        return None


    def result(self, state, move):
        if move not in self.actions(state):
            return state  # Illegal move has no effect
        board = deepcopy(state.board)
        player = state.to_move
        assert isinstance(board, object)
        # board[move] = player
        next_mover = self.opponent(player)
        return GameState(to_move=next_mover, board=board)


    def utility(self, state, player):
        "Return the value to player; 1 for win, -1 for loss, 0 otherwise."
        try:
            return state.utility if player == '---' else -state.utility
        except:
            pass
        board = state.board
        util = self.check_win(board, '---')
        if util == 0:
            util = -self.check_win(board, '---')
        state.utility = util
        return util if player == '---' else -util

    # Did I win?


    def check_win(self, board, player):
        # check rows
        for y in range(1, self.v + 1):
            if self.k_in_row(board, (1, y), player, (1, 0)):
                return 1
        # check columns
        for x in range(1, self.h + 1):
            if self.k_in_row(board, (x, 1), player, (0, 1)):
                return 1
        # check \ diagonal
        if self.k_in_row(board, (1, 1), player, (1, 1)):
            return 1
        # check / diagonal
        if self.k_in_row(board, (3, 1), player, (-1, 1)):
            return 1
        return 0

    # does player have K in a row? return 1 if so, 0 if not


    def k_in_row(self, board, start, player, direction):
        # "Return true if there is a line through start on board for player."
        # (delta_x, delta_y) = direction
        # x, y = start
        # n = 0  # n is number of moves in row
        # while board.get((x, y)) == player:
        #     n += 1
        #     x, y = x + delta_x, y + delta_y
        # x, y = start
        # while board.get((x, y)) == player:
        #     n += 1
        #     x, y = x - delta_x, y - delta_y
        # n -= 1  # Because we counted start itself twice

        # n >=
        return self.v

    def _isSquareMove(self, move):
        b = self.board
        mmove = self._makemove
        move = ((x1, y1), (x2, y2))
        captured_squares = []
        if self._isHorizontal(move):
            for j in [-1, 1]:
                if (b.has_key(mmove((x1, y1), (x1, y1 - j)))
                    and b.has_key(mmove((x1, y1 - j), (x1 + 1, y1 - j)))
                    and b.has_key(mmove((x1 + 1, y1 - j), (x2, y2)))):
                    captured_squares.append(min([(x1, y1), (x1, y1 - j),
                                                 (x1 + 1, y1 - j), (x2, y2)]))
        else:
            for j in [-1, 1]:
                if (b.has_key(mmove((x1, y1), (x1 - j, y1)))
                    and b.has_key(mmove((x1 - j, y1), (x1 - j, y1 + 1)))
                    and b.has_key(mmove((x1 - j, y1 + 1), (x2, y2)))):
                    captured_squares.append(min([(x1, y1), (x1 - j, y1),
                                                 (x1 - j, y1 + 1), (x2, y2)]))
        return captured_squares

    def Horizontal(self, move):
        # return true is the move is horizontal
        return abs(move[0][0] - move[1][0]) == 1

    def Vertical(self, move):
        # return true if the move is vertical
        return not self.Horizontal(self, move)

    def getBoxes(self):
        # returns a dictionary of boxes
        # not needed
        return self.squares

    def terminal_test(self, state):
        "A state is terminal if it is won or there are no empty squares."
        return self.utility(state, 'X') != 0 or len(self.actions(state)) == 0


    def display(self, state):
        board = state.board
        for x in range(1, self.h + 1):
            for y in range(1, self.v + 1):
                print(board.get((x, y), '.'), end=' ')
            print()



myGame = DotsandBoxes()

Box1 = [[(0, 0), (1, 0)], [(1, 0), (1, 1)], [(1, 1), (0, 1)],
        [(0, 1), (0, 0)],
        ]

Box2 = [[(1, 1), (1, 0)], [(2, 1), (1, 1)], [(2, 0), (2, 1)],
        [(1, 0), (2, 0)],
        ]

Box3 = [[(0, 1), (1, 1)], [(1, 1), (1, 2)], [(1, 2), (0, 2)],
        [(0, 2), (0, 1)],
        ]

Box4 = [[(1, 1), (2, 1)], [(2, 1), (2, 2)], [(2, 2), (1, 2)],
        [(1, 2), (1, 1)],
        ]

# Box6 = [[(2, 1), (3, 1)], [(3, 1), (3, 2)], [(3, 2), (2, 2)],
#         [(2, 2), (2, 1)],
#         ]
#
# Box7 = [[(0, 2), (1, 2)], [(1, 2), (1, 3)], [(1, 3), (0, 3)],
#         [(0, 3), (0, 2)],
#         ]
#
# Box8 = [[(1, 2), (2, 2)], [(2, 2), (2, 3)], [(2, 3), (1, 3)],
#         [(1, 3), (1, 2)],
#         ]
# Box9 = [[(2, 2), (3, 2)], [(3, 2), (3, 3)], [(3, 3), (2, 3)],
#         [(2, 3), (2, 2)],
#         ]

won = GameState(
    to_move='+--',
    # width=4,
    # height=4,
    board=(Box1, Box2, Box3, Box4,
           ),
    label='won'
)

winin1 = GameState(
    to_move='+--',
    # width=4,
    # height=4,
    board=[Box1, Box2, Box3, Box4,
           ],
    label='won'
)
losein1 = GameState(
    to_move='+--',
    # width=4,
    # height=4,
    board=[Box1, Box2,
           ],
    label='won'
)
winin3 = GameState(
    to_move='+--',
    #  width=4,
    # height=4,
    board=[Box1, Box2,
           ],
    label='won'
)
losein3 = GameState(
    to_move='+--',
    # width=4,
    # height=4,
    board=[Box1,
           ],
    label='won'
)
winin5 = GameState(
    to_move='+--',
    # width=4,
    # height=4,
    board=[Box1,
           ],
    label='won'
)
lost = GameState(
    to_move='---',
    # width=4,
    # height=4,
    board=[
    ],
    label='lost'
)

myGames = {
    myGame: [
        won,
        winin1, losein1, winin3, losein3, winin5,
        lost,
    ]
}