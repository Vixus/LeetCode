"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""
from typing import List
from Tools.TreeFunctions import arrToTree

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def dfs(root, fromLeft):
            if root == None:
                return 0

            if fromLeft:
                if not root.left and not root.right:
                    return root.val

            return dfs(root.left, True) + dfs(root.right, False)

        return dfs(root, False)


def main():
    s = Solution()
    treeArr = [3, 9, 20, None, None, 15, 7]
    tree = arrToTree(treeArr)
    ans = s.sumOfLeftLeaves(tree)
    print(ans)


if __name__ == '__main__':
    main()
