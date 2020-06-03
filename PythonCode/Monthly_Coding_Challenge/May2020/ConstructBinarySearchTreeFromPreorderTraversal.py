import numpy as np
from typing import List
from collections import Counter
from Tools.TreeFunctions import treeToArr


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        """
        Return the root node of a binary search tree that matches the given preorder traversal.
        (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
        It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

        Arguments:
            preorder {List[int]} -- [description]

        Returns:
            TreeNode -- [description]
        """
        lenList = len(preorder)
        stack = []

        if lenList != 0:
            stack.append(TreeNode(preorder[0]))
            root = stack[0]

        i = 1
        while i < lenList:
            node = TreeNode(preorder[i])
            if preorder[i] < stack[-1].val:
                stack[-1].left = node
                stack.append(node)
            else:
                tempNode = stack.pop()
                while stack and preorder[i] > stack[-1].val:
                    tempNode = stack.pop()

                tempNode.right = node
                stack.append(node)

            i += 1

        return root


def main():
    null = None
    s = Solution()
    traversalArr = [8, 5, 1, 7, 10, 12]
    ans = s.bstFromPreorder(traversalArr)
    print(treeToArr(ans))  # [8,5,10,1,7,null,12]


if __name__ == '__main__':
    main()
