from Strings_Valid_Anagram import Solution


def test1():
    s = Solution()
    sStr = 'anagram'
    tStr = 'nagaram'
    ans = s.isAnagram(sStr, tStr)

    assert ans == True


def test2():
    s = Solution()
    sStr = 'rat'
    tStr = 'car'
    ans = s.isAnagram(sStr, tStr)

    assert ans == False
