# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        i = -1

        while q:
            
            size = len(q)

            i += 1
            level = []
            roots = []

            # print(i, level,roots)
            for _ in range(size):

                curr = q.popleft()
                

                if i % 2:
                    roots.append(curr)
                    level.append(curr.val)    
                # i += 1            

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if level and roots:

                level = level[::-1]
                # print(level, roots)
                j = 0
                for ind in level:
                    roots[j].val = ind
                    j += 1
        return root 

