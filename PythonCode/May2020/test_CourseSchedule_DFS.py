from CourseSchedule_DFS import Solution


def test1():
    s = Solution()
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    ans = s.canFinish(numCourses, prerequisites)
    assert ans == False


def test2():
    s = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]
    ans = s.canFinish(numCourses, prerequisites)
    assert ans == True


def test3():
    s = Solution()
    numCourses = 3
    prerequisites = [[0, 1], [0, 2], [1, 2]]
    ans = s.canFinish(numCourses, prerequisites)
    assert ans == True
