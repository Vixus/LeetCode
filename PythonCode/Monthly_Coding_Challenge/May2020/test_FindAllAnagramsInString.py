from FindAllAnagramsInString import Solution


def test1():
    s = Solution()
    ans = s.findAnagrams('cbaebabacd', 'abc')
    assert ans == [0, 6]


def test2():
    s = Solution()
    ans = s.findAnagrams('abab', 'ab')
    assert ans == [0, 1, 2]
