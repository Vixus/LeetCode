from ConstructBinarySearchTreeFromPreorderTraversal import Solution
from Tools.TreeFunctions import treeToArr


def test1():
    null = None
    s = Solution()
    traversalArr = [8, 5, 1, 7, 10, 12]
    ans = s.bstFromPreorder(traversalArr)
    ans = treeToArr(ans)
    assert ans == [8, 5, 10, 1, 7, null, 12]
