from Path_Sum_III import Solution
from Tools.TreeFunctions import arrToTree


def test1():
    s = Solution()
    tree = arrToTree([10,5,-3,3,2,None,11,3,-2,None,1])
    num = 8
    ans = s.pathSum(tree, num)
    assert ans == 3
