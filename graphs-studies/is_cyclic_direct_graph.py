# 0, 1, 2, 3
def is_any_cycle(adj, u, visited, rec_stack):
                
                # 0 1 2 3
    if not visited[u]:
      
        # Mark the current node as visited
        # and part of recursion stack
        
        # [True, False, False, False], [True, True, False, False], [True, True, True, False], [True, True, True, True
        visited[u] = True
        
       # [True, False, False, False], [True, True, False, False], [True, True, True, False], [True, True, True, True
        rec_stack[u] = True

        # Recur for all the vertices 
        # adjacent to this vertex

                # 0, #1, #2, #3
                # 3 doesnt have any adjacent vertex
        for x in adj[u]:
                    # 1, 2, 3               # stopped 0, # stopped 1, # stopped 2
                                            # stopped 0, # stopped 1, False
                                            # stopped 0, False
                                            # False
            if not visited[x] and is_any_cycle(adj, x, visited, rec_stack):
                return True
            elif rec_stack[x]:
                return True 
            
    # Remove the vertex from recursion stack
    # 3, 2
    rec_stack[u] = False
    return False # stopped 2 return here as False, stopped 1 return here as False, stopped 0 return here as False, active 0 return here as False



def is_cyclic(adj, V):
    visited = [False] * V
    rec_stack = [False] * V

    # Call the recursive helper function to
    # detect cycle in different DFS trees
    for i in range(V):
        if not visited[i] and is_any_cycle(adj, i, visited, rec_stack):
            return True

    return False

# Driver function
if __name__ == "__main__":
    V = 4
    adj = [[] for _ in range(V)]

    # Adding edges to the graph
    # adj[0].append(1)
    # adj[0].append(2)
    # adj[1].append(2)
    # adj[2].append(0)
    # adj[2].append(3)
    # adj[3].append(3)
    
    adj[0].append(1)
    adj[1].append(2)
    adj[2].append(3)
    
    # Function call
    if is_cyclic(adj, V):
        print("Contains Cycle")
    else:
        print("No Cycle")