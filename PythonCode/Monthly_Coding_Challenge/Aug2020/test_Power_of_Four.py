from Power_of_Four import Solution


def test1():
    s = Solution()
    num = 16
    ans = s.isPowerOfFour(num)
    assert ans == True


def test2():
    s = Solution()
    num = 5
    ans = s.isPowerOfFour(num)
    assert ans == False


def test3():
    s = Solution()
    num = -10
    ans = s.isPowerOfFour(num)
    assert ans == False
