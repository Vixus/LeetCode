from PossibleBipartition_DFS import Solution


def test1():
    s = Solution()
    dislikes = [[1, 2], [1, 3], [2, 4]]
    N = 4
    ans = s.possibleBipartition(N, dislikes)
    assert ans == True


def test2():
    s = Solution()
    dislikes = [[1, 2], [1, 3], [2, 3]]
    N = 3
    ans = s.possibleBipartition(N, dislikes)
    assert ans == False


def test3():
    s = Solution()
    dislikes = [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]
    N = 5
    ans = s.possibleBipartition(N, dislikes)
    assert ans == False


def test4():
    s = Solution()
    dislikes = [[4, 7], [4, 8], [5, 6], [1, 6], [3, 7], [2, 5], [5, 8], [1, 2], [4, 9], [6, 10], [8, 10], [
        3, 6], [2, 10], [9, 10], [3, 9], [2, 3], [1, 9], [4, 6], [5, 7], [3, 8], [1, 8], [1, 7], [2, 4]]
    N = 10
    ans = s.possibleBipartition(N, dislikes)
    assert ans == True
