# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root : return []
        res, queue = [],collections.deque()
        queue.append(root)
        while queue:
            temp = collections.deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(res)%2 : temp.appendleft(node.val)
                else: temp.append(node.val)
                
                if node.left : queue.append(node.left)
                if node.right: queue.append(node.right) 
            res.append(list(temp))
        return res    
