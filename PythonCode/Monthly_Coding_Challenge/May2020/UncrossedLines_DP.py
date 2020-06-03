import numpy as np
from typing import List
from itertools import product
from collections import defaultdict


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        m = len(B)
        dp_matrix = defaultdict(int)

        for a, b in product(range(n), range(m)):
            if A[a] == B[b]:
                dp_matrix[a, b] = dp_matrix[a-1, b-1]+1
            else:
                dp_matrix[a, b] = max(dp_matrix[a-1, b], dp_matrix[a, b-1])

        return dp_matrix[n-1, m-1]


def main():
    null = None
    s = Solution()
    A = [2, 5, 1, 2, 5]
    B = [10, 5, 2, 1, 5, 2]
    ans = s.maxUncrossedLines(A, B)
    print(ans)


if __name__ == '__main__':
    main()
