
import queue

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

        Arguments:
            root {TreeNode} -- [description]
            k {int} -- [description]

        Returns:
            int -- [description]
        """
        stack = [root]

        while stack[-1].left:
            stack.append(stack[-1].left)

        while k > 0:
            node = stack.pop()
            k -= 1

            if node.right:
                stack.append(node.right)
                while stack[-1].left:
                    stack.append(stack[-1].left)

        return node.val


def createTree(nodeValArr):
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


def main():
    s = Solution()
    nodeValArr = [5, 3, 6, 2, 4, None, None, 1]
    root = createTree(nodeValArr)
    ans = s.kthSmallest(root, 3)
    print(ans)


if __name__ == '__main__':
    main()
