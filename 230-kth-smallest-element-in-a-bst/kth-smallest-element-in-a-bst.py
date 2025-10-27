# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        maxHeap=[]
        q=deque([root])
        while q:
            for _ in range(len(q)):
                node=q.popleft()
                heapq.heappush(maxHeap,-node.val)
                if len(maxHeap)>k:
                    heapq.heappop(maxHeap)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return -maxHeap[0]
        