from KClosestPointsToOrigin_Zip import Solution


def test1():
    s = Solution()
    K = 1
    points = [[1, 3], [-2, 2]]
    ans = s.kClosest(points, K)
    correctOutput = [[-2, 2]]
    assert all(x in correctOutput for x in ans)


def test2():
    s = Solution()
    K = 2
    points = [[3, 3], [5, -1], [-2, 4]]
    ans = s.kClosest(points, K)
    correctOutput = [[3, 3], [-2, 4]]
    assert all(x in correctOutput for x in ans)
