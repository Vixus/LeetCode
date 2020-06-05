from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        You are given an n x n 2D matrix representing an image.
        Rotate the image by 90 degrees (clockwise).

        Note:
        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

        Args:
            matrix (List[List[int]]): [description]

        Returns:
            [type]: [description]
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

        return


def main():
    s = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    s.rotate(matrix)
    print(matrix)


if __name__ == '__main__':
    main()
