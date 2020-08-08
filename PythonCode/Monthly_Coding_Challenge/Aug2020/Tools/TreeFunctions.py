import queue
import numpy as np

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def arrToTree(nodeValArr):
    q1 = queue.Queue()
    root = TreeNode(nodeValArr[0])
    q1.put(root)
    len_node = len(nodeValArr)
    i = 1

    while i < len_node:
        if not q1:
            break

        parentNode = q1.get()
        # Left node
        if i < len_node and nodeValArr[i]:
            childNode = TreeNode(nodeValArr[i])
            parentNode.left = childNode
            q1.put(childNode)

        # Right node
        if i+1 < len_node and nodeValArr[i+1]:
            childNode = TreeNode(nodeValArr[i+1])
            parentNode.right = childNode
            q1.put(childNode)

        i = i+2

    return root


def treeToArr(root):
    q1 = queue.Queue()
    q1.put(root)
    treeArr = []
    maxD = maxDepth(root)

    for i in range(sum(2**x for x in range(maxD))):
        node = q1.get()

        if node != None:
            treeArr.append(node.val)
        else:
            treeArr.append(None)

        if node != None and (node.left or node.right):
            if node.left:
                q1.put(node.left)
            else:
                q1.put(None)

            if node.right:
                q1.put(node.right)
            else:
                q1.put(None)
        else:
            q1.put(None)
            q1.put(None)

    # while i in range(-1, -(len(treeArr)+1)):
    #     if treeArr[i] != None:
    #         treeArr = treeArr[0:i]

    return treeArr

# Compute the "maxDepth" of a tree -- the number of nodes
# along the longest path from the root node down to the
# farthest leaf node


def maxDepth(node):
    if node is None:
        return 0

    else:

        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
