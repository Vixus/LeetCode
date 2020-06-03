from MaximumCircularSubArray import Solution


def test1():
    s = Solution()
    ans = s.maxSubarraySumCircular([1, -2, 3, -2])
    assert ans == 3


def test2():
    s = Solution()
    ans = s.maxSubarraySumCircular([5, -3, 5])
    assert ans == 10


def test3():
    s = Solution()
    ans = s.maxSubarraySumCircular([3, -1, 2, -1])
    assert ans == 4


def test4():
    s = Solution()
    ans = s.maxSubarraySumCircular([3, -2, 2, -3])
    assert ans == 3


def test5():
    s = Solution()
    ans = s.maxSubarraySumCircular([-2, -3, -1])
    assert ans == -1


def test6():
    s = Solution()
    ans = s.maxSubarraySumCircular([3, 1, 3, 2, 6])
    assert ans == 15


def test7():
    s = Solution()
    ans = s.maxSubarraySumCircular([-6, 0, -5, 7, 7, -5, 4])
    assert ans == 14
