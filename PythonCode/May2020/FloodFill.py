from typing import List


class Solution():
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
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
