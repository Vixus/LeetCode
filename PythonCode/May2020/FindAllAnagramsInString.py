from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sorted_p = sorted(p)
        # anagramIndexArr = []
        # p_length = len(p)
        # s_length = len(s)

        # for x in range(s_length-p_length+1):
        #     subset_s = s[x:p_length+x]
        #     if all(letter in subset_s for letter in p):
        #         # print(subset_s)
        #         if sorted(subset_s) == sorted_p:
        #             anagramIndexArr.append(x)

        cnt_p = Counter(p)
        anagramIndexArr = []
        p_length = len(p)
        s_length = len(s)

        anagramFound = False
        i = 0
        while i <= s_length-p_length:
            subset_s = s[i:p_length+i]
            if anagramFound == False and Counter(subset_s) == cnt_p:
                anagramFound = True
                anagramIndexArr.append(i)
                i += 1
            elif anagramFound == True:
                if s[i-1] == s[p_length+i-1]:
                    anagramIndexArr.append(i)
                    i += 1
                elif s[p_length+i-1] not in p:
                    anagramFound = False
                    i += p_length
                else:
                    anagramFound = False
                    i += 1
            else:
                i += 1

        return anagramIndexArr


def main():
    s = Solution()
    ans = s.findAnagrams('abacbabc', 'abc')
    print(ans)


if __name__ == '__main__':
    main()
