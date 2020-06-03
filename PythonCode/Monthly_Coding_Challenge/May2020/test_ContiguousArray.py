from ContiguousArray import Solution


def test1():
    s = Solution()
    nums = [0, 1]
    ans = s.findMaxLength(nums)
    assert ans == 2


def test2():
    s = Solution()
    nums = [0, 1, 0]
    ans = s.findMaxLength(nums)
    assert ans == 2
