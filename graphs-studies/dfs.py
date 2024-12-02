def DFS_iterative(source, list_adj):
    stack = [source]
    visited = set()
    
    while stack:
        curr = stack.pop()
        visited.add(curr)
        
        for adj in list_adj[curr]:
            if adj not in visited:
                stack.append(adj)
                visited.add(adj)


def DFS_recursive(source, adj_list, visited):
   visited.add(source)
   print(source)
   
   # the base case here is to have an empty list as adjacent list
   # this way the loop will not do recursive calls
   # when we don't return anything explicit we do a implicity return None
   for adj in adj_list[source]:
       if adj not in visited:
           DFS_recursive(adj, adj_list, visited)


v = [0, 1, 2, 3]
adj_list = {i: [] for i in v}

adj_list[0].append(1)
adj_list[0].append(2)
#adj_list[1].append()
adj_list[2].append(3)
#adj_list[3].append()

# these ones won't be printed
adj_list[2].append(1)
adj_list[2].append(0)

visited = set()

DFS_recursive(0, adj_list, visited)
