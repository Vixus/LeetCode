from Sort_Array_by_Parity import Solution


def test1():
    s = Solution()
    inputArr = [3, 1, 2, 4]
    ans = s.sortArrayByParity(inputArr)
    assert ans == [2, 4, 1, 3]


def test2():
    s = Solution()
    inputArr = [3]
    ans = s.sortArrayByParity(inputArr)
    assert ans == [3]
