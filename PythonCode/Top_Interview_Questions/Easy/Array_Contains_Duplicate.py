from typing import List
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Given an array of integers, find if the array contains any duplicates.
        Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

        Arguments:
            nums {List[int]} -- [description]
            k {int} -- [description]

        Returns:
            [type] -- [description]
        """
        setNums = set(nums)

        return len(setNums) != len(nums)


def main():
    s = Solution()
    nums = [1, 2, 3, 4]
    ans = s.containsDuplicate(nums)
    print(ans)


if __name__ == '__main__':
    main()
