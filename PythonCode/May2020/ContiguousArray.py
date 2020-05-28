import numpy as np
from typing import List
from itertools import product
from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

        Arguments:
            nums {List[int]} -- [description]

        Returns:
            int -- [description]
        """
        refArr = dict()
        refArr[0] = 0
        maxCont = 0
        sum = 0

        if len(nums) <= 1:
            return maxCont

        for i, x in enumerate(nums):
            if x:
                sum += 1
            else:
                sum -= 1

            if sum not in refArr:
                refArr[sum] = i+1

            maxCont = max(maxCont, i+1-refArr[sum])

        return maxCont


def main():
    s = Solution()
    nums = [0, 1, 0, 1, 1, 1, 0]
    ans = s.findMaxLength(nums)
    print(ans)


if __name__ == '__main__':
    main()
