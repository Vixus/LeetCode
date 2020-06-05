from Array_Two_Sum import Solution


def test1():
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    ans = s.twoSum(nums, target)

    assert ans == [0, 1]


def test2():
    s = Solution()
    nums = [3, 3]
    target = 6
    ans = s.twoSum(nums, target)

    assert ans == [0, 1]


def test3():
    s = Solution()
    nums = [3, 2, 4]
    target = 6
    ans = s.twoSum(nums, target)

    assert ans == [1, 2]
