from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        """
        Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
        Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
        Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

        Arguments:
            A {List[int]} -- [description]

        Returns:
            int -- [description]
        """

        return nums[lBound]


def main():
    s = Solution()
    ans = s.singleNonDuplicate([1, 1, 2, 3, 3])
    print(ans)


if __name__ == '__main__':
    main()
