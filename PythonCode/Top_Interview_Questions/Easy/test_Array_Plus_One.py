from Array_Plus_One import Solution


def test1():
    s = Solution()
    digits = [1, 2, 3]
    ans = s.plusOne(digits)

    assert ans == [1, 2, 4]


def test2():
    s = Solution()
    digits = [4, 3, 2, 1]
    ans = s.plusOne(digits)

    assert ans == [4, 3, 2, 2]
