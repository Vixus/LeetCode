from Vertical_Order_Traversal_of_a_Binary_Tree import Solution
from Tools.TreeFunctions import arrToTree


def test1():
    s = Solution()
    root = arrToTree([3, 9, 20, None, None, 15, 7])
    ans = s.verticalTraversal(root)
    assert ans == [[9], [3, 15], [20], [7]]


def test2():
    s = Solution()
    root = arrToTree([1, 2, 3, 4, 5, 6, 7]
    ans=s.verticalTraversal(root)
    assert ans == [[4], [2], [1, 5, 6], [3], [7]]
