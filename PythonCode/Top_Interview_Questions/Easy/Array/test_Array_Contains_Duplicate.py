from Array_Contains_Duplicate import Solution


def test1():
    s = Solution()
    nums = [1, 2, 3, 1]
    ans = s.containsDuplicate(nums)
    assert ans == True


def test2():
    s = Solution()
    nums = [1, 2, 3, 4]
    ans = s.containsDuplicate(nums)
    assert ans == False


def test3():
    s = Solution()
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    ans = s.containsDuplicate(nums)
    assert ans == True
