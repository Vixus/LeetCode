from Strings_Valid_Anagram import Solution


def test1():
    s = Solution()
    sStr = 'A man, a plan, a canal: Panama'
    ans = s.isPalindrome(sStr)

    assert ans == True


def test2():
    s = Solution()
    sStr = 'race a car'
    ans = s.isPalindrome(sStr)

    assert ans == False
