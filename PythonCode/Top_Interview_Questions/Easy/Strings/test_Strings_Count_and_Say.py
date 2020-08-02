from Strings_Count_and_Say import Solution


def test1():
    s = Solution()
    n = 1
    ans = s.countAndSay(n)

    assert ans == '1'


def test2():
    s = Solution()
    n = 4
    ans = s.countAndSay(n)

    assert ans == '1211'
