from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjDict = defaultdict(list)
        nodeStatus = defaultdict(int)

        # 0: Unchecked, 1: Checking, 2: Checked
        def DFS(node):
            if nodeStatus[node] == 2:
                return True
            elif nodeStatus[node] == 1:
                return False

            nodeStatus[node] = 1
            x = all([DFS(course) for course in adjDict[node]])

            if x:
                nodeStatus[node] = 2
            return x

        for x, y in prerequisites:
            adjDict[x].append(y)

        return all(DFS(course) for course in range(numCourses) if nodeStatus[course] != 2)


def main():
    s = Solution()
    numCourses = 2
    prerequisites = [[1, 0]]
    ans = s.canFinish(numCourses, prerequisites)
    print(ans)


if __name__ == '__main__':
    main()
