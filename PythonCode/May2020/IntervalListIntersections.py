import numpy as np
from typing import List
from collections import Counter


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
        Return the intersection of these two interval lists.
        (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

        Arguments:
            A {List[List[int]]} -- [description]
            B {List[List[int]]} -- [description]

        Returns:
            List[List[int]] -- [description]
        """
        indexA = 0
        indexB = 0
        intersectArr = []
        start = end = -1

        if len(A) == 0 or len(B) == 0:
            return intersectArr

        while indexB < len(B) and indexA < len(A):
            if A[indexA][0] > B[indexB][1]:
                indexB += 1
            elif A[indexA][1] < B[indexB][0]:
                indexA += 1
            else:
                if A[indexA][0] > B[indexB][0]:
                    start = A[indexA][0]
                else:
                    start = B[indexB][0]

                if A[indexA][1] == B[indexB][1]:
                    end = B[indexB][1]
                    indexA += 1
                    indexB += 1
                elif A[indexA][1] > B[indexB][1]:
                    end = B[indexB][1]
                    indexB += 1
                else:
                    end = A[indexA][1]
                    indexA += 1
                intersectArr.append([start, end])

        return intersectArr


def main():
    s = Solution()
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    ans = s.intervalIntersection(A, B)
    print(ans)  # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


if __name__ == '__main__':
    main()
