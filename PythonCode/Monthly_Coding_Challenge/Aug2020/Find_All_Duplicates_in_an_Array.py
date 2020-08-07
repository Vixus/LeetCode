from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
        Find all the elements that appear twice in this array.
        Could you do it without extra space and in O(n) runtime?

        Example:
        Input:
        [4,3,2,7,8,2,3,1]
        Output:
        [2,3]

        Args:
            nums (List[int]): [description]

        Returns:
            List[int]: [description]
        """
        i = 0

        while i < len(nums):
            if nums[i] == i+1 or nums[i] == nums[nums[i]-1]:
                i += 1
            else:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i] # THIS IS NO GOOD. ORDER MATTERS

        return [nums[x] for x in range(len(nums)) if nums[x] != x+1]


def main():
    s = Solution()
    nums = [4, 3, 2, 7, 8, 2, 3, 1, 4]
    ans = s.findDuplicates(nums)
    print(ans)


if __name__ == '__main__':
    main()
