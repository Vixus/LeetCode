from typing import List


class Solution():
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:    
        """An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
        Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
        To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
        At the end, return the modified image.

        Arguments:
            image {List[List[int]]} -- [description]
            sr {int} -- [description]
            sc {int} -- [description]
            newColor {int} -- [description]

        Returns:
            List[List[int]] -- [description]
        """
        height = len(image)
        width = len(image[0])
        oldColor = image[sr][sc]
        image[sr][sc] = newColor

        def recursive_fill(x, y):
            # Check top
            if x > 0:
                if image[x-1][y] == oldColor:
                    image[x-1][y] = newColor
                    recursive_fill(x-1, y)
            # Check bottom
            if x < height-1:
                if image[x+1][y] == oldColor:
                    image[x+1][y] = newColor
                    recursive_fill(x+1, y)

            # Check left
            if y > 0:
                if image[x][y-1] == oldColor:
                    image[x][y-1] = newColor
                    recursive_fill(x, y-1)

            # Check top
            if y < width-1:
                if image[x][y+1] == oldColor:
                    image[x][y+1] = newColor
                    recursive_fill(x, y+1)

            return

        if newColor != oldColor:
            recursive_fill(sr, sc)

        return image


def main():
    s = Solution()
    ans = s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
    print(ans)


if __name__ == '__main__':
    main()
