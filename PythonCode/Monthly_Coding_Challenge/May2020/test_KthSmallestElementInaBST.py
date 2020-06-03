from KthSmallestElementInaBST import Solution, createTree


def test1():
    s = Solution()
    nodeValArr = [5, 3, 6, 2, 4, None, None, 1]
    root = createTree(nodeValArr)
    ans = s.kthSmallest(root, 3)
    assert ans == 3


def test2():
    s = Solution()
    nodeValArr = [3, 1, 4, None, 2]
    root = createTree(nodeValArr)
    ans = s.kthSmallest(root, 1)
    assert ans == 1
