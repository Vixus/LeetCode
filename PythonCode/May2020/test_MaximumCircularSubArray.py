from SingleElementInSortedArray import Solution


def test1():
    s = Solution()
    ans = s.singleNonDuplicate([1, -2, 3, -2])
    assert ans == 3


def test2():
    s = Solution()
    ans = s.singleNonDuplicate([5, -3, 5])
    assert ans == 10


def test3():
    s = Solution()
    ans = s.singleNonDuplicate([3, -1, 2, -1])
    assert ans == 4


def test4():
    s = Solution()
    ans = s.singleNonDuplicate([3, -2, 2, -3])
    assert ans == 3


def test4():
    s = Solution()
    ans = s.singleNonDuplicate([-2, -3, -1])
    assert ans == -1
