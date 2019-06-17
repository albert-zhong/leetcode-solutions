# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if not nums:
            return None
        
        max_index, max_value = max(enumerate(nums), key = lambda x : x[1])
        
        root = TreeNode(max(nums))
        
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        
        return root
		