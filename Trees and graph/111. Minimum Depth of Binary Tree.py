# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # Trường hợp cây rỗng
        if not root:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)

        # Xử lý các trường hợp nhánh rỗng∏
        if left_depth == 0 or right_depth == 0:
            # Nếu một trong hai nhánh rỗng, chọn độ sâu của nhánh kia
            return max(left_depth, right_depth) + 1
        else:
            # Nếu cả hai nhánh đều không rỗng, chọn độ sâu nhỏ nhất
            return min(left_depth, right_depth) + 1
