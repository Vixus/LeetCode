from SingleElementInSortedArray import Solution


def test1():
    s = Solution()
    ans = s.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
    assert ans == 2


def test2():
    s = Solution()
    ans = s.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])
    assert ans == 10


def test3():
    s = Solution()
    ans = s.singleNonDuplicate([1, 1, 2, 3, 3])
    assert ans == 2
