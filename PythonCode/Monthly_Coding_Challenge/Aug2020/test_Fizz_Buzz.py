from Fizz_Buzz import Solution


def test1():
    s = Solution()
    n = 15
    ans = s.fizzBuzz(n)
    assert ans == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ]
