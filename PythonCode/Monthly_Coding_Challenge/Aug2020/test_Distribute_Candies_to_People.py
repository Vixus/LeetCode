from Distribute_Candies_to_People import Solution


def test1():
    s = Solution()
    candies = 7
    num_people = 4
    ans = s.distributeCandies(candies, num_people)
    assert ans == [1, 2, 3, 1]


def test2():
    s = Solution()
    candies = 10
    num_people = 3
    ans = s.distributeCandies(candies, num_people)
    assert ans == [5, 2, 3]
