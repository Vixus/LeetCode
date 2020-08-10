from typing import List
from collections import deque
from itertools import product

"""
    In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.
    Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

    Example 1:

    Input: [[2,1,1],[1,1,0],[0,1,1]]
    Output: 4
    Example 2:

    Input: [[2,1,1],[0,1,1],[1,0,1]]
    Output: -1
    Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
    Example 3:

    Input: [[0,2]]
    Output: 0
    Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

    Note:
    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    grid[i][j] is only 0, 1, or 2.
    """


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        freshCount, minuteCount = 0, -1
        rottenQueue = deque()
        dirArr = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for x, y in product(range(m), range(n)):
            if grid[x][y] == 2:
                rottenQueue.append((x, y))
            elif grid[x][y] == 1:
                freshCount += 1

        if freshCount == 0:  # If there are no fresh fruits
            return 0
        elif not rottenQueue:  # If there are fresh fruits but no rotten fruit, then solution is impossible
            return -1

        while rottenQueue:
            minuteCount += 1
            for _ in range(len(rottenQueue)):
                x, y = rottenQueue.popleft()
                for dx, dy in dirArr:
                    if 0 <= x+dx < m and 0 <= y+dy < n and grid[x+dx][y+dy] == 1:
                        freshCount -= 1
                        grid[x+dx][y+dy] = 2
                        rottenQueue.append((x+dx, y+dy))

        if freshCount:
            return -1
        else:
            return minuteCount


def main():
    s = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    # grid = [[0]]
    ans = s.orangesRotting(grid)
    print(ans)


if __name__ == '__main__':
    main()
