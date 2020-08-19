from Goat_Latin import Solution


def test1():
    s = Solution()
    inputStr = 'I speak Goat Latin'
    ans = s.toGoatLatin(inputStr)
    assert ans == 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'


def test2():
    s = Solution()
    inputStr = 'The quick brown fox jumped over the lazy dog'
    ans = s.toGoatLatin(inputStr)
    assert ans == 'heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa'
