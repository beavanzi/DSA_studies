def DFS(root, list_adj):
    stack = [root]
    visited = set()
    
    while stack:
        curr = stack.pop()
        
        for adj in list_adj[curr]:
            if adj not in visited:
                stack.append(adj)
                visited.add(adj)
                