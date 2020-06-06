from Strings_Reverse_String import Solution


def test1():
    s = Solution()
    input = ["h", "e", "l", "l", "o"]
    s.reverseString(input)

    assert input == ["o", "l", "l", "e", "h"]


def test2():
    s = Solution()
    input = ["H", "a", "n", "n", "a", "h"]
    s.reverseString(input)

    assert input == ["h", "a", "n", "n", "a", "H"]
