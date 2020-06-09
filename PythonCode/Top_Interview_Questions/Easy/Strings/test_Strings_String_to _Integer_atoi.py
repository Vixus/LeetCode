from Strings_String_to_Integer_atoi import Solution


def test1():
    s = Solution()
    sStr = '42'
    ans = s.myAtoi(sStr)

    assert ans == 42


def test2():
    s = Solution()
    sStr = '   -42'
    ans = s.myAtoi(sStr)

    assert ans == -42


def test3():
    s = Solution()
    sStr = '4193 with words'
    ans = s.myAtoi(sStr)

    assert ans == 4193


def test4():
    s = Solution()
    sStr = 'words and 987'
    ans = s.myAtoi(sStr)

    assert ans == 0


def test5():
    s = Solution()
    sStr = '-91283472332'
    ans = s.myAtoi(sStr)

    assert ans == -2147483648


def test6():
    s = Solution()
    sStr = '.1'
    ans = s.myAtoi(sStr)

    assert ans == 0


def test7():
    s = Solution()
    sStr = '+'
    ans = s.myAtoi(sStr)

    assert ans == 0


def test8():
    s = Solution()
    sStr = '+-2'
    ans = s.myAtoi(sStr)

    assert ans == 0


def test9():
    s = Solution()
    sStr = '   +0 123'
    ans = s.myAtoi(sStr)

    assert ans == 0


def test10():
    s = Solution()
    sStr = '3.14'
    ans = s.myAtoi(sStr)

    assert ans == 3
