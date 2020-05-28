import numpy as np
from typing import List
from itertools import product
from collections import defaultdict


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        """
        Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
        Each person may dislike some other people, and they should not go into the same group. 
        Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
        Return true if and only if it is possible to split everyone into two groups in this way.

        Arguments:
            N {int} -- [description]
            dislikes {List[List[int]]} -- [description]

        Returns:
            bool -- [description]
        """
        color = {}

        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(num, c ^ 1) for num in dislikeDict[node])

        dislikeDict = defaultdict(list)

        for x, y in dislikes:
            dislikeDict[x].append(y)
            dislikeDict[y].append(x)

        return all(dfs(num) for num in range(1, N+1) if num not in color)


def main():
    s = Solution()
    dislikes = [[4, 7], [4, 8], [5, 6], [1, 6], [3, 7], [2, 5], [5, 8], [1, 2], [4, 9], [6, 10], [8, 10],
                [3, 6], [2, 10], [9, 10], [3, 9], [2, 3], [1, 9], [4, 6], [5, 7], [3, 8], [1, 8], [1, 7], [2, 4]]
    N = 10
    ans = s.possibleBipartition(N, dislikes)
    print(ans)


if __name__ == '__main__':
    main()
