class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

        Arguments:
            num {str} -- [description]
            k {int} -- [description]

        Returns:
            str -- [description]
        """
        # strNum = ''

        # def findSmallestNum(num, k, strNum):

        #     if k == 0:
        #         return strNum + num
        #     elif len(num) == k:
        #         if strNum == '':
        #             return 0
        #         else:
        #             return strNum
        #     else:
        #         smallestNum = min(num[0:k+1])
        #         smallestIndex = num[0:k+1].index(smallestNum)
        #         remaingNum = num[smallestIndex+1:]
        #         numToRemove = k-smallestIndex
        #         strNum = strNum + smallestNum
        #         strNum = findSmallestNum(remaingNum, numToRemove, strNum)

        #     return strNum

        # return str(int(findSmallestNum(num,k,strNum)))
        strNum = '0'
        totalDigits = len(num)-k

        while k != 0:
            if k == len(num):
                num = ''
                break
            smallestNum = min(num[0:k+1])
            smallestIndex = num[0:k+1].index(smallestNum)
            k = k-(smallestIndex)
            strNum = strNum + smallestNum
            if smallestIndex == len(num)-1:
                num = ''
            else:
                num = num[smallestIndex+1:]

        return str(int(strNum+num))

def main():
    s = Solution()
    ans = s.removeKdigits('10',2)
    print(ans)


if __name__ == '__main__':
    main()
