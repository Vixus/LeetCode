from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Given two arrays, write a function to compute their intersection.

        Arguments:
            nums1 {List[int]} -- [description]
            nums2 {List[int]} -- [description]

        Returns:
            List[int] -- [description]
        """
        cnt1 = Counter(nums1)
        cnt2 = Counter(nums2)

        intersectDict = cnt1 & cnt2
        outputArr = []

        for num, count in intersectDict.items():
            for _ in range(count):
                outputArr.append(num)

        return outputArr


def main():
    s = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    ans = s.intersect(nums1, nums2)
    print(ans)


if __name__ == '__main__':
    main()
