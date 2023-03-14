import numpy as np
import time
from typing import List
from copy import deepcopy



# Function Tester is used to make sure that two states are equal. Might need it , might not.
def Tester(list_of_state, State_to_be_found) -> bool:
    for state in list_of_state:
        if np.array_equal(State_to_be_found, state):
            return True
    return False


# This generator will generate all the children of any given puzzle
def successor_state_generator(current_state, depth_counter=None, succ_dict=None) -> List[List]:
    successors = []
    #NOT COMPLETED < DOES NOT WORK YET 
    #Step 1 : find all values and pair
    my_dict = {1:0,2:0,3:0,4:0,5:0,6:0}
    for number,row in enumerate(current_state):
        for column,value in enumerate(row):
    #       print(f"the value {value} is at position {number},{column}")
            pass

    #find Pairs

    for number,row in enumerate(current_state):
        for column,value in enumerate(row):
            if value in my_dict:
                my_dict[value]+=1
    
    #print(my_dict)


    for values in my_dict:
        if my_dict[values]>1:
            x_position_1,y_position_1 = np.argwhere(current_state == values)[0]
            x_position_2,y_position_2 = np.argwhere(current_state == values)[1]        
            print(f"The x position and y position for the first instance of {values} is {x_position_1}, {y_position_1}")
            print(f"The x position and y position for the second instance of {values} is {x_position_2}, {y_position_2}")


            # while x_position_1!=x_position_2:
            #     delta_position =  x_position_2 - x_position_1
            #     to_move = x_po2sition_1 + delta_position
            #     current_state[]
    return successors, depth_counter

def BestFirst(istate, gstate, heuristics):

    print("BestFirst Search Started ")
    open_list = [istate]
    closed_list = []
    i = 0
    while open_list:
        current_state = open_list.pop(0)
        closed_list.append(current_state)
        if np.array_equal(current_state, gstate):
            print(
                f"Puzzle has been solved, this is the final closed list : ")
            for state in closed_list:
                print(state)
                print("\n \n")
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
            f"Puzzle has been solved, this is the final closed list : ")
            for state in closed_list:
                print(state)
                print("\n \n")
                print(f"Finished with itteration {i}")
            return closed_list

        list_of_successor, depth_counter = successor_state_generator(
            current_state, depth_counter, successor_dict)
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

        


# General Search takes Initial State, GoalState,SearchStrategy,Heuristics


def general_search(istate, goal_state, search_strategy, heuristic):
    print(f"General Search has been called with personal Heuristic")
    return search_strategy(istate, goal_state, heuristic)


def my_heuristic(CurrentState: List[List[str]], FinalState: List[List[str]]) -> int:
    counter = 0
    for i in range(len(CurrentState)):
       for j in range(len(CurrentState)):
           if CurrentState[i][j] == 0:
               counter += 1
    point_value = counter * 10
    print (point_value)



def main():

    # Transform the string inputs into a 2 day array that will be easier to keep track of x and Y positions.
    current_state = [[1,2,3,4],[2,0,0,0],[3,0,0,0],[4,0,0,0]]
    current_state = np.array(current_state).reshape(4,4)
    goal_state =[[3,-2,-2,-2],[-3,2,1,-1],[-3,-3,3,1],[4,-4,-4,4]]
    goal_state = np.array(goal_state).reshape(4,4)


    print("The Initial state :")
    for row in current_state:
        print (row)

    print ("\n") 
    # print("The Goal state :")
    # for row in goal_state:
    #     print(row)
    

    # The Use of the Numpy module allows this easy conversion. Then , we can run some heuristics

    #successor_state_generator(current_state)
    #general_search(current_state,goal_state,BestFirst)

    #my_heuristic(current_state,goal_state)

if __name__ == '__main__':
    main()
