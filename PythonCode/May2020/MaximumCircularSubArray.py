from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        """
        Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
        Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)
        Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

        Arguments:
            A {List[int]} -- [description]

        Returns:
            int -- [description]
        """

        n = len(A)

        # Check if single element
        if n == 1:
            return A[0]
        elif all(i>=0 for i in A) or all(i<=0 for i in A): # Check if all numbers are of the same sign
            return max(A)
        
        # Find start index to collapse
        if A[0] >= 0:
            for i in range(-1,-n,-1):
                if A[i] < 0:
                    startIndex = i+1
                    break
        else:
            for i in range(1, n):
                if A[i] >= 0:
                    startIndex = i
                    break

        print(startIndex)
        # Rotate Array
        A = A[startIndex:] + A[0:startIndex]
        print(A)

        # Collapse Array
        collapsedArr = []
        tempSum = A[0]
        for x in A[1:n]:
            if x*tempSum >= 0:
                tempSum += x
            else:
                collapsedArr.append(tempSum)
                tempSum = x
        collapsedArr.append(tempSum)
        print(collapsedArr)


        # Sum in pairs
        pairSumArr = []
        tempMax = -1e5
        for i in range(int(len(collapsedArr)/2)):
            sum = collapsedArr[i*2]+collapsedArr[i*2+1]
            pairSumArr.append(sum)
            if sum >= tempMax:
                tempMax = sum
        print(pairSumArr)

        startIndexArr = [i for i,x in enumerate(pairSumArr) if x == tempMax]
        
        # There could be a tie in starting block
        
        possibleMax = []
        n = len(collapsedArr)
        for i in startIndexArr:
            runningSum = 0
            tempMax = -1e5

            # Rotate Array
            tempArr = collapsedArr[i*2:n] + collapsedArr[0:i*2]
            
            for x in tempArr:
                runningSum +=x
                if runningSum > tempMax:
                    tempMax = runningSum
            
            possibleMax.append(tempMax)
        

        return max(possibleMax)

def main():
    s = Solution()
    ans = s.maxSubarraySumCircular([-1,5,5,-2,-5,-4,-8,9,8,-20,7,6,3])
    print(ans)

    # ans = s.maxSubarraySumCircular([-2,-3,-1])
    # print(ans)


if __name__ == '__main__':
    main()
