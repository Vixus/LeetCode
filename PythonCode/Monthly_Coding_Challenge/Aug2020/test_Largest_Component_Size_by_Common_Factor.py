from Largest_Component_Size_by_Common_Factor import Solution


def test1():
    s = Solution()
    inputArr = [4, 6, 15, 35]
    ans = s.largestComponentSize(inputArr)
    assert ans == 4


def test2():
    s = Solution()
    inputArr = [20, 50, 9, 63]
    ans = s.largestComponentSize(inputArr)
    assert ans == 2


def test3():
    s = Solution()
    inputArr = [2, 3, 6, 7, 4, 12, 21, 39]
    ans = s.largestComponentSize(inputArr)
    assert ans == 8
