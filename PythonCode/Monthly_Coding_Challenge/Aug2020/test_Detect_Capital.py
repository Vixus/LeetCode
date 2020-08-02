from Detect_Capital import Solution


def test1():
    s = Solution()
    word = 'USA'
    ans = s.detectCapitalUse(word)
    assert ans == True


def test2():
    s = Solution()
    word = 'FlaG'
    ans = s.detectCapitalUse(word)
    assert ans == False
