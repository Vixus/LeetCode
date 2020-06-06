from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        Args:
            nums (List[int]): [description]
            target (int): [description]

        Returns:
            List[int]: [description]
        """
        # d = defaultdict(list)
        # for i, x in enumerate(nums):
        #     d[x].append(i)

        # for x in nums:
        #     if d[target-x]:
        #         if x != target/2:
        #             return [d[x][0], d[target-x][0]]
        #         elif len(d[x]) == 2:
        #             return d[x]

        # return []

        d = defaultdict(int)
        for i, x in enumerate(nums):
            if target - x in d:
                return [d[target - x], i]
            d[x] = i


def main():
    s = Solution()
    nums = [3, 3]
    target = 6
    ans = s.twoSum(nums, target)
    print(ans)


if __name__ == '__main__':
    main()
