from Strings_Reverse_Integer import Solution


def test1():
    s = Solution()
    x = 123
    ans = s.reverse(x)

    assert ans == 321


def test2():
    s = Solution()
    x = -123
    ans = s.reverse(x)

    assert ans == -321


def test3():
    s = Solution()
    x = 120
    ans = s.reverse(x)

    assert ans == 21


def test4():
    s = Solution()
    x = 1534236469
    ans = s.reverse(x)

    assert ans == 0
