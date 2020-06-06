from Array_Rotate_Array import Solution


def test1():
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    s.rotate(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test2():
    s = Solution()
    nums = [-1, -100, 3, 99]
    k = 2
    s.rotate(nums, k)
    assert nums == [3, 99, -1, -100]
