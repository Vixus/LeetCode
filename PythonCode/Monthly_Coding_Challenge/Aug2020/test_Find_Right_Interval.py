from Find_Right_Interval import Solution


def test1():
    s = Solution()
    inputArr = [[1, 2]]
    ans = s.findRightInterval(inputArr)
    assert ans == [-1]


def test2():
    s = Solution()
    inputArr = [[3, 4], [2, 3], [1, 2]]
    ans = s.findRightInterval(inputArr)
    assert ans == [-1, 0, 1]


def test3():
    s = Solution()
    inputArr = [[1, 4], [2, 3], [3, 4]]
    ans = s.findRightInterval(inputArr)
    assert ans == [-1, 2, -1]
