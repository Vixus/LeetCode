from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
        Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

        Arguments:
            nums {List[int]} -- [description]

        Returns:
            int -- [description]
        """
        currNum = ''
        ptrIndex = -1
        count = 0
        for i, x in enumerate(nums):
            if x != currNum:
                nums[ptrIndex+1] = x
                ptrIndex += 1
                currNum = x
                count += 1

        nums = nums[0:count]
        return count


def main():
    s = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ans = s.removeDuplicates(nums)
    print(ans)
    print(nums[0:ans])


if __name__ == '__main__':
    main()
