import numpy as np
from typing import List, Tuple

# ManhattanDistance Heuristics. Take the X and Y coordinates of every value in the GoalState and the CurrentState. Calculate the total ManhattenDistance and return it



def successor_state_generator(current_state):
    successors = []
    possible_moves = ["Up", "Down", "Left", "Right"]

    # first step is finding where the B is:
    x_position_blank = np.argwhere(current_state == 'B')[0][0]
    y_position_blank = np.argwhere(current_state == 'B')[0][1]

    
    pass


def DepthFirstSearch(istate, gstate):
    open_list = [istate]
    closed_list = []

    while open_list:
        current_state = open_list.pop()
        closed_list.append(current_state)

        if current_state == gstate:
            return closed_list

        for successor in successor_state_generator(istate):
            open_list.push(successor)


def BreathFirstSearch(istate, gstate):
    open_list = [istate]
    closed_list = []

    while open_list:
        current_state = open_list.pop()
        closed_list.append(current_state)

        if current_state == gstate:
            return closed_list

        for successor in successor_state_generator(istate):
            closed_list.append(successor)


def BestFirst(istate, gstate, heuristics):
    open_list = [istate]
    closed_list = []

    while open_list:
        current_state = open_list.pop()
        closed_list.append(current_state)

        if current_state == gstate:
            return closed_list

        open_list += sorted(successor_state_generator(istate),
                            lambda x: heuristics(x))


def Astar(istate, gstate, heuristics, ActualCost):
    pass


# General Search takes Initial State, GoalState,SearchStrategy,Heuristics
def general_search(istate, goal_state, search_strategy, heuristic=None):

    if heuristic:
        return search_strategy(istate, goal_state, heuristic)

    return search_strategy(istate, goal_state)


def main():

 # Transform the string inputs into a 2 day array that will be easier to keep track of x and Y positions.
    # GoalState = list("1238B4765")
    GoalState = list("12345678B")
    current_state = list("5B8421736")
    GoalStateArray = np.array(GoalState).reshape((-1, 3))
    current_state = np.array(current_state).reshape((-1, 3))

# The Use of the Numpy module allows this easy conversion. Then , we can run some heuristics
    print(
        f"The ManhattenDistance is : {manhatten_distance(current_state, GoalStateArray)}")
    print(
        f"The Hamming Distance is :  {hamming_distance(current_state,GoalStateArray)}")
    # print(GoalStateArray)

    general_search(current_state, GoalStateArray,
                   DepthFirstSearch, manhatten_distance)


def manhatten_distance(CurrentState: List[List[str]], FinalState: List[List[str]]) -> int:
    # Values that can be taken by the puzzle
    values = ['1', '2', '3', '4', '5', '6', '7', '8']
    xsum = 0
    ysum = 0
    for value in values:
        final_state_pos_x = np.argwhere(FinalState == value)[0][0]
        final_state_pos_y = np.argwhere(FinalState == value)[0][1]
        current_state_pos_x = np.argwhere(CurrentState == value)[0][0]
        current_state_pos_y = np.argwhere(CurrentState == value)[0][1]
        xsum += abs(final_state_pos_x-current_state_pos_x)
        # add the values in X and Y from the difference GoalState-CurrentState
        ysum += abs(final_state_pos_y-current_state_pos_y)

    return xsum + ysum  # Return the Total


def hamming_distance(CurrentState: List[List[str]], FinalState: List[List[str]]) -> int:
    # Values that can be taken by the puzzle
    values = ['1', '2', '3', '4', '5', '6', '7', '8']
    counter = 0
    for value in values:
        final_state_pos_x = np.argwhere(FinalState == value)[0][0]
        final_state_pos_y = np.argwhere(FinalState == value)[0][1]
        current_state_pos_x = np.argwhere(CurrentState == value)[0][0]
        current_state_pos_y = np.argwhere(CurrentState == value)[0][1]
        if (final_state_pos_x != current_state_pos_x or final_state_pos_y != current_state_pos_y):
            counter += 1

    return (counter)


if __name__ == '__main__':
    main()
