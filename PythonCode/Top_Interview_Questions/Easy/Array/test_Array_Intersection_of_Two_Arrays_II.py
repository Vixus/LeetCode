from Array_Intersection_of_Two_Arrays_II import Solution


def test1():
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    ans = s.intersect(nums1, nums2)

    assert ans == [2, 2]


def test2():
    s = Solution()
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    ans = s.intersect(nums1, nums2)
    ans.sort()
    assert ans == [4, 9]
