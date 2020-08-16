from H_Index import Solution


def test1():
    s = Solution()
    citations = [3, 0, 6, 1, 5]
    ans = s.hIndex(citations)
    assert ans == 3


def test2():
    s = Solution()
    citations = [0]
    ans = s.hIndex(citations)
    assert ans == 0


def test3():
    s = Solution()
    citations = [11, 15]
    ans = s.hIndex(citations)
    assert ans == 2
