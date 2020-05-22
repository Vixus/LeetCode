from SortCharactersByFrequency import Solution


def test1():
    s = Solution()
    ans = s.frequencySort('tree')
    assert ans == 'eetr'


def test2():
    s = Solution()
    ans = s.frequencySort('cccaaa')
    assert ans == 'cccaaa'


def test3():
    s = Solution()
    ans = s.frequencySort('Aabb')
    assert ans == 'bbAa'
