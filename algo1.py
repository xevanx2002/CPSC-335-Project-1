# Ekaterina Miakotina and Evan Wenzel

def create_adj_list(all_nodes, edges):
    """This function creates an adjacency list from edges"""
    # create a dictionary called adj_list that contains empty list as a value
    adj_list = {i: [] for i in range(all_nodes)}
    # loop over each directed edge
    for x, y in edges:
        adj_list[x].append(y) # append y to x in adjacency list
    return adj_list # return completed adjacency list

def cycle_detection(graph, vertex, visited, dfs_stack):
    """This function uses DFS to detect if a cycle exists in a directed graph"""
    # since we use sets here, we use add() method instead of append() to add a node
    visited.add(vertex)
    dfs_stack.add(vertex)

    # loop through all other vertecies in a graph to detect if cycle exists or no
    for other_vertex in graph[vertex]:
        # if other vertex was not visited, we use recursion
        if other_vertex not in visited:
            if cycle_detection(graph, other_vertex, visited, dfs_stack):
                return True
        # if other vertex is already in the stack - we found a cycle 
        elif other_vertex in dfs_stack:
            return True
        
        # after checking all vertecies, we have to remove from the stack
        dfs_stack.remove(vertex)

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

def main():
    all_nodes_input = int(input("Input: "))
    coordinates = input().strip()

    result = is_cycle(all_nodes_input, coordinates)

    print ("Output: ", result)

