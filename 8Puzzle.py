import numpy as np
import time
from typing import List, Tuple
from copy import deepcopy

# ManhattanDistance Heuristics. Take the X and Y coordinates of every value in the GoalState and the CurrentState. Calculate the total ManhattenDistance and return it


def Tester(list_of_state, State_to_be_found) -> bool:

    for state in list_of_state:
        if np.array_equal(State_to_be_found, state):
            return True

    return False


def successor_state_generator(current_state, depth_counter = None, succ_dict =None):

    successors = []

    if depth_counter != None and succ_dict != None:
        depth_counter+=1
        string_current_state = "".join(
                map(str, [column for row in current_state for column in row]))
        if string_current_state not in succ_dict:
            succ_dict[string_current_state]=0   
    

    # Everytime a set of new child is generated, add +1 to a counter. That specific child is at that step
    possible_moves = ["Up", "Down", "Left", "Right"]
    # first step is finding where the B is:
    x_position_blank = np.argwhere(current_state == 'B')[0][0]
    y_position_blank = np.argwhere(current_state == 'B')[0][1]

    print("THIS IS THE CURRENT STATE THAT IS BEING MODIFIED BY THE MOVES ")
    print(current_state)
    print("----------------------")
    # moving right
    if y_position_blank < 2:
        # new_stateRight = current_state[:]
        new_stateRight = deepcopy(current_state)
        temporary_ = current_state[x_position_blank][y_position_blank+1]
        new_stateRight[x_position_blank][y_position_blank+1] = 'B'
        new_stateRight[x_position_blank][y_position_blank] = temporary_
        successors.append(new_stateRight)

        if depth_counter != None and succ_dict != None:
         
            string_new_stateRight = "".join(
                map(str, [column for row in new_stateRight for column in row]))
            if string_new_stateRight not in succ_dict:
                succ_dict[string_new_stateRight] = depth_counter

        # print("This is the new Successor State with value Right")
        # print(new_stateRight.tolist())
        # print("-------------------")

    # moving Left
    if y_position_blank > 0:
        new_stateLeft = current_state[:][:]
        new_stateLeft = deepcopy(current_state)
        temporary_ = current_state[x_position_blank][y_position_blank-1]
        new_stateLeft[x_position_blank][y_position_blank-1] = 'B'
        new_stateLeft[x_position_blank][y_position_blank] = temporary_
        successors.append(new_stateLeft)

        # print("This is the new Successor State with value Left")
        # print(new_stateLeft.tolist())
        # print("-------------------")
        if depth_counter != None and succ_dict != None:
            
            string_new_stateLeft = "".join(
                map(str, [column for row in new_stateLeft for column in row]))
            if string_new_stateLeft not in succ_dict:
                succ_dict[string_new_stateLeft] = depth_counter

    # MovingUP

    if x_position_blank > 0:

        new_stateUp = deepcopy(current_state)
        temporary_ = current_state[x_position_blank-1][y_position_blank]
        new_stateUp[x_position_blank-1][y_position_blank] = 'B'
        new_stateUp[x_position_blank][y_position_blank] = temporary_
        successors.append(new_stateUp)

        if depth_counter != None and succ_dict != None:
            
            string_new_stateUp = "".join(
                map(str, [column for row in new_stateUp for column in row]))
            if string_new_stateUp not in succ_dict:
                succ_dict[string_new_stateUp] = depth_counter

        # print("This is the new Successor State with value Up")
        # print(new_stateUp.tolist())
        # print("-------------------")

    # movingDown

    if x_position_blank < 2:
        new_stateDown = deepcopy(current_state)
        temporary_ = current_state[x_position_blank+1][y_position_blank]
        new_stateDown[x_position_blank+1][y_position_blank] = 'B'
        new_stateDown[x_position_blank][y_position_blank] = temporary_
        successors.append(new_stateDown)

        # print("This is the new Successor State with value Down")
        # print(new_stateDown.tolist())
        # print("-------------------")
        if depth_counter != None and succ_dict != None:
            
            string_new_stateDown = "".join(
                map(str, [column for row in new_stateDown for column in row]))
            if string_new_stateDown not in succ_dict:
                succ_dict[string_new_stateDown] = depth_counter

    
    return successors, depth_counter


def DepthFirstSearch(istate, gstate):

    print("DepthFirstSearch has been called")
    open_list = [istate]
    closed_list = []

    print(Tester(open_list, istate))
    # print("THIS IS THE OPEN LIST BEFORE DOING ANYTHING")
    # print(open_list)
    while open_list:
        current_state = open_list.pop()
        closed_list.append(current_state)
        print("This is the state that is passed to the successor generator\n")
        print(current_state)
        if np.array_equal(current_state, gstate):
            print("The Puzzle has been found")
            print(f"This is the final closed list {closed_list}")
            return closed_list

        for successor in successor_state_generator(current_state)[0]:
            if not Tester(open_list, successor) and not Tester(closed_list, successor):
                open_list.append(successor)


def BreathFirstSearch(istate, gstate):
    open_list = [istate]
    closed_list = []
    # print(f"Inital Open list: {open_list}")
    # print(f"Inital Closed list: {closed_list}")
    while open_list:
        current_state = open_list.pop(0)  # Here we pop 0 since it is a queue
        closed_list.append(current_state)

        if np.array_equal(current_state, gstate):
            print("Value was found")
            print(f"This is the closed list : {closed_list}")
            return closed_list

        for successor in successor_state_generator(current_state)[0]:
            if not Tester(open_list, successor) and not Tester(closed_list, successor):
                open_list.append(successor)


def BestFirst(istate, gstate, heuristics):

    print("BestFirst Search Started ")
    open_list = [istate]
    closed_list = []
    i = 0
    while open_list:
        current_state = open_list.pop(0)
        closed_list.append(current_state)
        print(f"this is iteration number : {i}")
        i += 1
        if np.array_equal(current_state, gstate):
            print(
                f"Puzzle has been solved, this is the final closed list {closed_list} ")

            print(f"Finished with itteration {i}")
            return closed_list

        for successor in successor_state_generator(current_state)[0]:
            if not Tester(open_list, successor) and not Tester(closed_list, successor):
                open_list.append(successor)
        # Sorted function will call my heuristic directly on each item in my open list which will sort them given my heuristic
        open_list = sorted(open_list, key=lambda x: heuristics(x, gstate))


def Astar(istate, gstate, heuristics):
    print("A* Search Started ")
    # Start it at -1 because we increment it at each time a current state is poped. However if current state = goal state from first tri then G(n) should be 0
    depth_counter = 0
    successor_dict = {}
    open_list = [istate]
    closed_list = []
    i = 0
    while open_list:
        current_state = open_list.pop(0)
        closed_list.append(current_state)

        if np.array_equal(current_state, gstate):
            print(
                f"Puzzle has been solved, this is the final closed list {closed_list} ")
            return closed_list

        list_of_successor,depth_counter = successor_state_generator(current_state, depth_counter, successor_dict) 
        for successor in list_of_successor:
            if not Tester(open_list, successor) and not Tester(closed_list, successor):
                open_list.append(successor)

        # Sorted function will call my heuristic directly on each item in my open list which will sort them given my heuristic
        open_list = sorted(
            open_list, key=lambda x: heuristics(x, gstate) + successor_dict["".join(
                map(str, [column for row in x for column in row]))])



        for x in open_list:
            print(f"The current value of each state is {x} : ")
            
            print(successor_dict["".join(
                map(str, [column for row in x for column in row]))])
    
    
        print(f"ITTERATION {i}")
        i += 1


# General Search takes Initial State, GoalState,SearchStrategy,Heuristics


def general_search(istate, goal_state, search_strategy, heuristic=None):
    print(f"General Search has been called with Heursitic = {heuristic}")
    # time.sleep(3)
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

    return counter


def permutation_inversion(CurrentState: List[List[str]], FinalState: List[List[str]]) -> int:
    string_current_state = "".join(
        map(str, [column for row in CurrentState for column in row]))
    print(string_current_state)
    inversion_count = 0
    string_current_state = string_current_state.replace("B", "0")

    print(string_current_state)
    for i in range(0, len(string_current_state)-1):
        for j in range(i+1, len(string_current_state)):
            if (string_current_state[i] == "0" or string_current_state[j] == "0"):
                pass
            elif int(string_current_state[i]) > int(string_current_state[j]):
                print("-------------COMPARAISON")
                print(string_current_state[i])
                print(string_current_state[j])
                inversion_count += 1
                print(f"This is the inversion count {inversion_count}")
                # time.sleep(3)

    return inversion_count




def my_heuristic(CurrentState: List[List[str]], FinalState: List[List[str]]) -> int:
    # Values that can be taken by the puzzle
    values = ['1', '2', '3', '4', '5', '6', '7', '8']
    my_dict = {}
    xsum = 0
    ysum = 0
    for value in values:
        final_state_pos_x = np.argwhere(FinalState == value)[0][0]
        final_state_pos_y = np.argwhere(FinalState == value)[0][1]
        current_state_pos_x = np.argwhere(CurrentState == value)[0][0]
        current_state_pos_y = np.argwhere(CurrentState == value)[0][1]
        xsum += abs(final_state_pos_x-current_state_pos_x)
        
        if (current_state_pos_x == final_state_pos_x and current_state_pos_y != final_state_pos_y) or (current_state_pos_y == final_state_pos_y and current_state_pos_x != final_state_pos_x) :
            my_dict[value] = (current_state_pos_x,current_state_pos_y)

        #this if statement find every one taht is already on the correct line or column,If they are already in the right column buut at the wrond place, it means they will have to moove in order to allow one to go in. So +1 extra step
    
        #if they are on the same x or y axis , it means that they will have to overlapp at some point unless they are already at the correct positomn


        # add the values in X and Y from the difference GoalState-CurrentState
        ysum += abs(final_state_pos_y-current_state_pos_y)

    return xsum + ysum + len(my_dict)  # Return the Total

def main():

    # Transform the string inputs into a 2 day array that will be easier to keep track of x and Y positions.

    # Test Cases for DFS
    #current_state =  list("12B453786")
    #GoalState = list("12345678B")

    # Test Cases for BFS
    #GoalState = list("12345678B")
    #current_state = list("123456B78")

    # Test Case for BEST FIRST SEARCH
    GoalState = list("12345678B")
    #current_state = list("25B461783")
    current_state = list("7421B5863")
    GoalStateArray = np.array(GoalState).reshape((-1, 3))
    current_state = np.array(current_state).reshape((-1, 3))


    print(manhatten_distance(current_state,GoalStateArray))
    print(my_heuristic(current_state,GoalStateArray))

#The Use of the Numpy module allows this easy conversion. Then , we can run some heuristics

    print(f"The Hamming Distance is :  {hamming_distance(current_state,GoalStateArray)}")

    # print("This is the Initial State")
    # print(current_state)
    # # time.sleep(3)

    #general_search(current_state,GoalStateArray,BreathFirstSearch)

    general_search(current_state, GoalStateArray,
                    Astar, manhatten_distance)


if __name__ == '__main__':
    main()
