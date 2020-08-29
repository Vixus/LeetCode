from Pancake_Sorting import Solution


def test1():
    s = Solution()
    inputArr = [3, 2, 4, 1]
    ans = s.pancakeSort(inputArr)
    outputArr = inputArr.copy()
    for k in ans:
        outputArr = outputArr[k-1::-1] + outputArr[k:]
    assert sorted(inputArr) == outputArr


def test2():
    s = Solution()
    inputArr = [1, 2, 3]
    ans = s.pancakeSort(inputArr)
    outputArr = inputArr.copy()
    for k in ans:
        outputArr = outputArr[k-1::-1] + outputArr[k:]
    assert sorted(inputArr) == outputArr
