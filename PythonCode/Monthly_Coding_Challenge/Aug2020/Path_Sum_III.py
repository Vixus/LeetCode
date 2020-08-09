from Tools.TreeFunctions import arrToTree
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        cumsumDict = defaultdict(int)
        cumsumDict [0] = 1

        def dfs(root, cumsum):
            if not root:
                return 0

            cumsum += root.val
            pathCount = cumsumDict[cumsum - sum]
            cumsumDict[cumsum] += 1
            pathCount += dfs(root.left, cumsum) + dfs(root.right, cumsum)
            cumsumDict[cumsum] -= 1
            return pathCount

        return dfs(root, 0)


def main():
    s = Solution()
    tree = arrToTree([10,5,-3,3,2,None,11,3,-2,None,1])
    num = 8
    ans = s.pathSum(tree, num)
    print(ans)


if __name__ == '__main__':
    main()
