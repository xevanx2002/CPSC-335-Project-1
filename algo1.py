# Ekaterina Miakotina and Evan Wenzel

def new_graph(edges):
    graph = {} # created a new dictionary called graph tha will be represented as an adjacency list
    # use for-loop to iterate through all edges in edges
    for x, y in edges:
        # if x, the beginning of an edge, is not a key in a graph
        if x not in graph:
            graph[x] = [] # initialize it to an empty list
            graph[x].append(y) # append y to x as an adjacency list bc edge is x->y

        # checking if y exists
        if y not in graph:
            graph[y] = []

    # returning a dictionary called graph
    return graph

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
    
