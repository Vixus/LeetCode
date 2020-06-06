from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Given an array, rotate the array to the right by k steps, where k is non-negative.

        Arguments:
            nums {List[int]} -- [description]
            k {int} -- [description]
        """

        N = len(nums)
        currIndex = 0
        currTemp = nums[0]
        startIndex = currIndex

        for _ in range(N):
            nextIndex = (currIndex+k) % N
            nextTemp = nums[nextIndex]
            nums[nextIndex] = currTemp
            if nextIndex != startIndex:
                currIndex = nextIndex
                currTemp = nextTemp
            else:
                currIndex = (nextIndex+1) % N
                currTemp = nums[currIndex]
                startIndex = currIndex

        return None


def main():
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    k = 3
    s.rotate(nums, k)
    print(nums)


if __name__ == '__main__':
    main()
