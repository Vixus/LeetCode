from PermutationInString_Hash import Solution


def test1():
    s = Solution()
    ans = s.checkInclusion('ab', 'eidbaooo')
    assert ans == True


def test2():
    s = Solution()
    ans = s.checkInclusion('ab', 'eidboaoo')
    assert ans == False
