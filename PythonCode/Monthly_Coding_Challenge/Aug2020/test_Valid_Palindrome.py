from Valid_Palindrome import Solution


def test1():
    s = Solution()
    wordstr = 'A man, a plan, a canal: Panama'
    ans = s.isPalindrome(wordstr)
    assert ans == True


def test2():
    s = Solution()
    word = 'race a car'
    ans = s.isPalindrome(word)
    assert ans == False
