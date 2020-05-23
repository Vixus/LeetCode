import numpy as np
from typing import List
from collections import Counter


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
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
