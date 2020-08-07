from Find_All_Duplicates_in_an_Array import Solution


def test1():
    s = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1, 4]
    ans = s.findDuplicates(nums)
    print(ans)
    assert set(ans) == set([2, 3, 4])
