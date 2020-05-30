from typing import List
from collections import defaultdict


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
        (Here, the distance between two points on a plane is the Euclidean distance.)
        You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

        Arguments:
            numCourses {int} -- [description]
            prerequisites {List[List[int]]} -- [description]

        Returns:
            bool -- [description]
        """

        distArr = list(map(lambda x: x[0]**2+x[1]**2, points))
        zipped_lists = zip(distArr, points)
        sorted_pairs = sorted(zipped_lists)
        distArr, points = zip(*sorted_pairs)

        return points[0:K]


def main():
    s = Solution()
    K = 1
    points = [[1, 3], [-2, 2]]
    ans = s.kClosest(points, K)
    print(list(ans))  # [[-2,2]]


if __name__ == '__main__':
    main()
