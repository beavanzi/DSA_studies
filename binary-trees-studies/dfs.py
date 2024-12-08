def DFS_iterative(root):
    stack = [root]
    
    while stack:
        node = stack.pop()
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)



def DFS_recursive(root):
    if not root:
        return

    print(root.val)
    
    DFS_recursive(root.left)
    DFS_recursive(root.right)
        

class TreeNode():
    def __init__(self, val) -> None:
        self.left = None
        self.right = None
        self.val = val

root = TreeNode(7)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.right = TreeNode(8)

DFS_recursive(root)

#print(root.val, root.left.val, root.left.left.val, root.right.val)