from Sum_of_Left_Leaves import Solution
from Tools.TreeFunctions import arrToTree


def test1():
    s = Solution()
    treeArr = [3, 9, 20, None, None, 15, 7]
    tree = arrToTree(treeArr)
    ans = s.sumOfLeftLeaves(tree)
    assert ans == 24


def test2():
    s = Solution()
    treeArr = [3]
    tree = arrToTree(treeArr)
    ans = s.sumOfLeftLeaves(tree)
    assert ans == 0
