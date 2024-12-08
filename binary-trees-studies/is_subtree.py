# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
            Two trees s and t are said to be identical if their root values are same 
            and their left and right subtrees are identical. Can you write this in form of recursive formulae?
        '''
        
        if not root:
            return False

        if root.val == subRoot.val:
            res = self.isIdentical(root, subRoot)
            return res
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isIdentical(self, s, t):
        print(s.val if s else None, t.val if t else None)

        if not s and not t:
            print("1")
            return True
        
        if not s and t:
            print("2")
            return False

        if not t and s:
            print("3")
            return False

        if s.val != t.val:
            print("4")
            return False

        return self.isIdentical(s.left, t.left) and self.isIdentical(s.right, t.right)
    

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subroot = TreeNode(4)
subroot.left = TreeNode(1)
subroot.right = TreeNode(2)

sol = Solution()
print(sol.isSubtree(root, subroot))

# print(root.val, root.left.val, root.right.val, root.left.left.val, root.left.right.val)
# print(subroot.val, subroot.left.val, subroot.right.val)