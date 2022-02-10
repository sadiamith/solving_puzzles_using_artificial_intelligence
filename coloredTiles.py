import math as math
from copy import deepcopy

# taking in the problem array and describing it in my terms of my word


class State(object):
    """

       Assuming the the problem state is a 2d array which we represent by a list
       example: ['GGG', 'GGG, 'GGG']

       Note: Each state will need to store the action that created that state
       in a class variable called "action" to get full use out of scripts such
       as see_solutions.py
    """

    def __init__(self, puzzle):
        """
        Initialize a new State object.

        """
        self.action = 'Initial state'
        self.puzzle = puzzle
        self.nrows = len(self.puzzle)
        self.ncols = len(self.puzzle[0])
        # TODO: implement this function.  Add parameters as needed.

    def __str__(self):
        """ A string representation of the State """
        # TODO: implement this function.
        return '{}'.format(str(self.puzzle))

    def __eq__(self, other):
        """ Defining this function allows states to be compared
        using the == operator """
        # TODO: implement this function.
        return self.puzzle == other.puzzle

    def invert_state(self, row, col):
        # TODO
        self.puzzle[row][col] = not self.puzzle[row][col]
        if(row-1 >= 0):
            self.puzzle[row-1][col] = not self.puzzle[row-1][col]
        if(row+1 < self.nrows):
            self.puzzle[row+1][col] = not self.puzzle[row+1][col]
        if(col-1 >= 0):
            self.puzzle[row][col-1] = not self.puzzle[row][col-1]
        if(col+1 < self.ncols):
            self.puzzle[row][col+1] = not self.puzzle[row][col+1]


class Problem(object):
    """The Problem class defines aspects of the problem.
       One of the important definitions is the transition model for states.
       To interact with search classes, the transition model is defined by:
            is_goal(s): returns true if the state is the goal state.
            actions(s): returns a list of all legal actions in state s
            result(s,a): returns a new state, the result of doing action a in state s

    """

    def __init__(self, nrows, ncols, start=None):
        """ The problem is defined by an initial grid of tiles.

            :param nrows: number of rows in the tile puzzle
            :param ncols: number of columns in the tile puzzle
            :param start: a list of strings where each character is R or G.  Each string represents one row of the grid
            i.e: ['GGG', 'GRG', 'GGG']
        """
        # TODO: implement this function. You can change the parameters if you really want, but then you will have to change the calls in run_search.py
        self.nrows = nrows
        self.ncols = ncols
        if start is not None:
            self.init_state = State(self.__convert_to_boolean_list(start))
        # the possible actions would be a tuple of two ints
        # representing coordiante pair of (row, column) of n x n array
        self.actions_list = []
        for x in range(self.nrows):
            for y in range(self.ncols):
                self.actions_list.append((x, y))

        # the goal state would be the same puzzle with the same dimension
        # only the value would be all TRUE
        goal_puzzle = []
        for i in range(nrows):
            row = []
            for j in range(ncols):
                row.append(True)
            goal_puzzle.append(row)
        self.goal_state = State(goal_puzzle)

    def __convert_to_boolean_list(self, list):
        new_list = [[col for col in row] for row in list]
        for x in range(len(new_list)):
            for y in range(len(new_list[x])):
                if(new_list[x][y] == 'G'):
                    new_list[x][y] = True
                else:
                    new_list[x][y] = False

        return new_list

    def create_initial_state(self):
        """ returns the initial state of othe problem
        """
        # TODO: implement this function.
        return self.init_state

    def is_goal(self, a_state: State):
        """Returns True if the given state is a goal state"""
        """for me, goal state is arr = [
            [true, true, true],
            [true, true, true],
            [true, true, true]
        ]"""

        return a_state == self.goal_state

    def actions(self, a_state: State):
        """ Returns all the actions that are legal in the given state.

        """
        # TODO: implement this function.
        return self.actions_list

    def result(self, a_state: State, an_action):
        """Given a state and an action, return the resulting state.
        An action is a tuple of 2 ints representing coordinates (row, col)
        """
        # TODO: implement this function.
        copied_puzzle = deepcopy(a_state.puzzle)
        new_state = State(copied_puzzle)
        new_state.action = an_action
        new_state.invert_state(an_action[0], an_action[1])

        return new_state


# end of file
