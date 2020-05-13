from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if int(len(nums)/2) == 0:
            print("Array length cannot be even!!")
            return -1

        foundSolo = False
        uBound = len(nums)-1
        lBound = 0

        while foundSolo == False:
            print(lBound, uBound)
            mid = int((lBound+uBound)/2)
            mid = int(mid/2)*2

            if uBound == lBound:
                foundSolo = True
                break
            print(mid)
            print(nums[lBound:uBound+1])

            if nums[mid] == nums[mid+1]:
                lBound = mid+2
            else:
                uBound = mid

        return nums[lBound]


s = Solution()
ans = s.singleNonDuplicate([1, 1, 2, 3, 3])
print(ans)
