from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        power2 = 2
        countBitsArr = [0, 1]

        if num == 0:
            return [0]
        elif num == 1:
            return countBitsArr

        for i in range(2, num+1):
            if i >= power2*2:
                power2 *= 2

            countBitsArr.append(countBitsArr[i-power2]+1)

        return countBitsArr


def main():
    s = Solution()
    N = 15
    ans = s.countBits(N)
    print(ans)


if __name__ == '__main__':
    main()
