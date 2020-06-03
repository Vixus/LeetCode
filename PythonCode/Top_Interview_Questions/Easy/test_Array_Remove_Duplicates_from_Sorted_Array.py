from Array_Remove_Duplicates_from_Sorted_Array import Solution


def test1():
    s = Solution()
    nums = [1, 1, 2]
    ans = s.removeDuplicates(nums)
    assert ans == 2
    assert nums[0:ans] == [1, 2]


def test2():
    s = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ans = s.removeDuplicates(nums)
    assert ans == 5
    assert nums[0:ans] == [0, 1, 2, 3, 4]
