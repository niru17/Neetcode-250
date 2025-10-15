# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        pq=deque([p])
        qq=deque([q])
        while pq and qq:
            if len(pq)!=len(qq):
                return False
            for _ in range(len(pq)):
                nodep=pq.popleft()
                nodeq=qq.popleft()

                if not nodep and not nodeq:
                    continue
                if not nodep or not nodeq or nodep.val!=nodeq.val:
                    return False

                pq.append(nodep.left)
                pq.append(nodep.right)
                qq.append(nodeq.left)
                qq.append(nodeq.right)
        return not pq and not qq
        