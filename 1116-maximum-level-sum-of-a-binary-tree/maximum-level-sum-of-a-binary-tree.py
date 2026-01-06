# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        # cool brute level order T - bfs
        if not root:
            return 0

        queue = deque([root])
        # print(queue)
        min_level = float('inf')
        prev_sum = -float('inf')

        currLevel = 1
        while queue:
            size = len(queue)
            level_Sum = 0
            

            for i in range(size):
                node = queue.popleft()
                # level.append(node.val)
                level_Sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # print(level_Sum, prev_sum, currLevel)
            if level_Sum > prev_sum:
                prev_sum = level_Sum
                min_level = currLevel
            
            currLevel += 1

        return min_level
        