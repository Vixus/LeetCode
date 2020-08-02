from Strings_Implement_strStr import Solution


def test1():
    s = Solution()
    haystack = "hello"
    needle = "ll"
    ans = s.strStr(haystack, needle)

    assert ans == 2


def test2():
    s = Solution()
    haystack = "aaaaa"
    needle = "bba"
    ans = s.strStr(haystack, needle)

    assert ans == -1
