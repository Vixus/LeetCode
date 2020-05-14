class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        strNum = ''

        def findSmallestNum(num, k, strNum):

            if k == 0:
                return strNum + num
            elif len(num) == k:
                if strNum == '':
                    return 0
                else:
                    return strNum
            else:
                smallestNum = min(num[0:k+1])
                smallestIndex = num[0:k+1].index(smallestNum)
                remaingNum = num[smallestIndex+1:]
                numToRemove = k-smallestIndex
                strNum = strNum + smallestNum
                strNum = findSmallestNum(remaingNum, numToRemove, strNum)

            return strNum

        return str(int(findSmallestNum(num,k,strNum)))


def main():
    s = Solution()
    ans = s.removeKdigits('10', 2)
    print(ans)


if __name__ == '__main__':
    main()
