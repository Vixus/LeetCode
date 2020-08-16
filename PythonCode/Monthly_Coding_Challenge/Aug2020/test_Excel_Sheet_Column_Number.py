from Excel_Sheet_Column_Number import Solution


def test1():
    s = Solution()
    wordStr = 'A'
    ans = s.titleToNumber(wordStr)
    assert ans == 1


def test2():
    s = Solution()
    wordStr = 'AB'
    ans = s.titleToNumber(wordStr)
    assert ans == 28


def test3():
    s = Solution()
    wordStr = 'ZY'
    ans = s.titleToNumber(wordStr)
    assert ans == 701
