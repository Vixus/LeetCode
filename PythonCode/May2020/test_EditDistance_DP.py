from EditDistance_DP import Solution


def test1():
    s = Solution()
    word1 = 'horse'
    word2 = 'ros'
    ans = s.minDistance(word1, word2)
    assert ans == 3


def test2():
    s = Solution()
    word1 = 'intention'
    word2 = 'execution'
    ans = s.minDistance(word1, word2)
    assert ans == 5
