# Ekaterina Miakotina and Evan Wenzel

import ast # we use import ast as it is the easiest way to convert input which is string in a python list of tuples

"""*** Algorithm logic begins here ***"""
def create_adj_list(all_nodes, edges):
    """This function creates an adjacency list from edges"""
    
    # create a dictionary called adj_list that contains empty list as a value
    adj_list = {i: [] for i in range(all_nodes)}
    
    # loop over each directed edge
    for x, y in edges:
        
        adj_list[x].append(y) # append y to x in adjacency list
        
    return adj_list # return completed adjacency list

def cycle_detection(adj_list, vertex, visited, curr_dfs_stack):
    """This function uses DFS to detect if a cycle exists in a directed graph"""
    
    # since we use sets here, we use add() method instead of append() to add a node
    visited.add(vertex)
    curr_dfs_stack.add(vertex)

    # loop through all other vertecies in a graph to detect if cycle exists or no
    for other_vertex in adj_list[vertex]:
    
        # if other vertex was not visited, we use recursion
        if other_vertex not in visited:
            
            if cycle_detection(adj_list, other_vertex, visited, curr_dfs_stack):
                
                return True
            
        # if other vertex is already in the stack - we found a cycle 
        elif other_vertex in curr_dfs_stack:
            
            return True
        
    # after checking all vertecies, we have to remove from the stack
    curr_dfs_stack.remove(vertex)

    # in case the cycle was not found - we return false
    return False

def is_cycle (all_nodes, edges):
    """This function checks if the cycle exists"""

    adjacency_list = create_adj_list(all_nodes, edges) #calling a helper function to create an adjacency list

    curr_stack = set() # empty set that will track current nodes
    
    visited = set() # empty set to check visited nodes

    # loop over every single vertex
    for vertex in range(all_nodes):
        
        # check if we visited a vertex or no
        if vertex not in visited:
            
            # if no - call for a helper function to see if the cycle exists
            if cycle_detection(adjacency_list, vertex, visited, curr_stack):
                
                return "Loop detected"
            
    return "No loop detected" # if the cycle was not detected - print no loop detecteds

"""*** Algorithm logic ends here ***"""

"""*** Global namespace zone - accept input and provides output ***"""

all_nodes_input = int(input("Input: "))# accepts nodes from the input that user provided

coordinates = input().strip() # string for coordinates input, strip used for spaces

# we are checikng if the input is valid and provide an output
try:
    
    all_coordinates = ast.literal_eval(coordinates)# coneverting string to the list

    # protection logic if coordinates are list
    if not isinstance(all_coordinates, list):
        
        print("error")
     
    else:

        # declare to variales to check if inputs are valid and total number of nodes
        is_v = True
        total_n = -1
        
        i = 0
        my_length = len(all_coordinates) # total length of all coordinates
        
        while i < my_length:

            # we are getting an object from coordinates at index i
            obj = all_coordinates[i]

            instance_check = isinstance(obj, tuple)

            # if check to see if tuple has a valid length of two objects
            if not (len(obj) == 2 and instance_check):

                # if something goes wrong - is valid false
                is_v = False
                # stop checking further immidiately
                break
            
            # here we look at each object closer as x and y
            x, y = obj

            # these if checks exists in order to update the total nodes that we look at
            # did this check for sample 2
            if x > total_n:
                total_n = x # if x coordinate greater than total nodes number - we assign x to total nodes number
                
            if y > total_n: # if y coordinate greater than total nodes number - we assign y to total nodes number
                total_n = y

            i += 1 # we are moving forward

        # after checking all objects and if they are all valid - we print output 
        if is_v:

            # if one of the nodes is greater than input , we adjust that
            if total_n >= all_nodes_input:
                
                all_nodes_input = total_n + 1

            # calling a function to pass the results and check if there is a cycle exists or no
            final_output = is_cycle(all_nodes_input, all_coordinates)

            # final output for the user
            print ("Output: ", final_output)
            
# exception check for us in case something goes wrong and we can now what the issue is
except Exception as meow_error:
    
    print("Invalid format for the input", meow_error) # helped a lot to debug


