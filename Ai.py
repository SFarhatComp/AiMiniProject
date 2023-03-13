import numpy as np
import time
from typing import List, Tuple
from copy import deepcopy
# ManhattanDistance Heuristics. Take the X and Y coordinates of every value in the GoalState and the CurrentState. Calculate the total ManhattenDistance and return it

def successor_state_generator(current_state):
    successors = []
    possible_moves = ["Up", "Down", "Left", "Right"]
    # first step is finding where the B is:
    x_position_blank = np.argwhere(current_state == 'B')[0][0]
    y_position_blank = np.argwhere(current_state == 'B')[0][1]

    print("THIS IS THE CURRENT STATE THAT IS BEING MODIFIED BY THE MOVES ")
    print(current_state)
    print("----------------------")
    #moving right
    if y_position_blank < 2 :
        #new_stateRight = current_state[:]
        new_stateRight = deepcopy(current_state)
        temporary_ = current_state[x_position_blank][y_position_blank+1]
        new_stateRight[x_position_blank][y_position_blank+1] = 'B'
        new_stateRight[x_position_blank][y_position_blank] = temporary_
        successors.append(new_stateRight)
        print("This is the new Successor State with value Right")
        print (new_stateRight.tolist())
        print ("-------------------")

    #moving Left
    if y_position_blank > 0 :
        new_stateLeft = current_state[:][:]
        new_stateLeft = deepcopy(current_state)
        temporary_ = current_state[x_position_blank][y_position_blank-1]
        new_stateLeft[x_position_blank][y_position_blank-1] = 'B'
        new_stateLeft[x_position_blank][y_position_blank] = temporary_
        successors.append(new_stateLeft)
        print("This is the new Successor State with value Left")
        print (new_stateLeft.tolist())
        print ("-------------------")


    #MovingUP

    if x_position_blank > 0 :
    
        new_stateUp = deepcopy(current_state)
        temporary_ = current_state[x_position_blank-1][y_position_blank]
        new_stateUp[x_position_blank-1][y_position_blank] = 'B'
        new_stateUp[x_position_blank][y_position_blank] = temporary_
        successors.append(new_stateUp)
        print("This is the new Successor State with value Up")
        print (new_stateUp.tolist())
        print ("-------------------")

    #movingDown

    if x_position_blank < 2 :
        new_stateDown = deepcopy(current_state)
        temporary_ = current_state[x_position_blank+1][y_position_blank]
        new_stateDown[x_position_blank+1][y_position_blank] = 'B'
        new_stateDown[x_position_blank][y_position_blank] = temporary_
        successors.append(new_stateDown)
        print("This is the new Successor State with value Down")
        print (new_stateDown.tolist())
        print ("-------------------")

   

    return successors




def DepthFirstSearch(istate, gstate):
    print("DepthFirstSearch has been called")
    open_list = [istate]
    closed_list = []

    print("THIS IS THE OPEN LIST BEFORE DOING ANYTHING")
    print(open_list)
    while open_list:
        current_state = open_list.pop()
        closed_list.append(current_state)
        print("This is the state that is passed to the successor ")
        print(current_state)
        if np.array_equal(current_state,gstate):
            print("The final value has been found")
            print(f"This is the closed list {closed_list}")
            return closed_list
        for successor in successor_state_generator(current_state):
            if successor not in open_list or successor not in closed_list:
                open_list.append(successor)
            
    

def BreathFirstSearch(istate, gstate):
    open_list = [istate]
    closed_list = []

    print(f"Inital Open list: {open_list}")
    print(f"Inital Closed list: {closed_list}")
    while open_list:
        current_state = open_list.pop(0)
        closed_list.append(current_state)
     

        if np.array_equal(current_state,gstate):
            print("Value was found")
            print(f"This is the closed list : {closed_list}")
            return closed_list

        for successor in successor_state_generator(current_state):
            # if successor not in open_list or successor not in closed_list:
            open_list.append(successor)
    
    
    

def BestFirst(istate, gstate, heuristics):
    
    print("BestFirst Search ")
    open_list = [istate]
    closed_list = []

    while open_list:
        current_state = open_list.pop()
        closed_list.append(current_state)

        if np.array_equal(current_state,gstate):
            return closed_list

        print(f"This is sorted : {sorted(successor_state_generator(current_state),key = lambda x : heuristics(current_state,gstate))}")
        open_list
        

        ## I AM THEERE I HAVE TO FIND A WAY TO APPEND THIS LIST TO THE OPEN LIST 
        print(f"This is the open list : {open_list}")
        time.sleep(3)
        
        


def Astar(istate, gstate, heuristics, ActualCost):
    pass

# General Search takes Initial State, GoalState,SearchStrategy,Heuristics


def general_search(istate, goal_state, search_strategy, heuristic=None):
    print(f"General Search has been called with Heursitic = {heuristic}")
    #time.sleep(3)
    if heuristic:
        return search_strategy(istate, goal_state, heuristic)

    return search_strategy(istate, goal_state)





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

def main():

 # Transform the string inputs into a 2 day array that will be easier to keep track of x and Y positions.
    # GoalState = list("1238B4765")
    GoalState = list("12345678B")
    current_state = list("1234567B8")
    GoalStateArray = np.array(GoalState).reshape((-1, 3))
    current_state = np.array(current_state).reshape((-1, 3))

# The Use of the Numpy module allows this easy conversion. Then , we can run some heuristics
    print(
        f"The ManhattenDistance is : {manhatten_distance(current_state, GoalStateArray)}")
    print(
        f"The Hamming Distance is :  {hamming_distance(current_state,GoalStateArray)}")
    print("This is the Initial State")
    print(current_state)
    #time.sleep(3)
    general_search(current_state, GoalStateArray,
                   BestFirst,manhatten_distance)

if __name__ == '__main__':
    main()
