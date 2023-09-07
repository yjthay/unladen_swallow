import pytest
from highscoringwords import HighScoringWords


def scorer(type):
    if type == 'mini_wordlist':
        return HighScoringWords(validwords='data/mini_wordlist.txt', lettervalues='../letterValues.txt')
    elif type == 'charlist':
        return HighScoringWords(validwords='data/charlist.txt', lettervalues='../letterValues.txt')
    elif type == 'src':
        return HighScoringWords(validwords='../wordlist.txt', lettervalues='../letterValues.txt')


@pytest.mark.parametrize("word, src_mod, score",
                         [('cabbage', scorer('src'), 14),
                          ('abacus', scorer('src'), 10),
                          ('queer', scorer('src'), 14),
                          ('CaBbAgE', scorer('src'), 14),
                          ('aBaCuS', scorer('src'), 10),
                          ('qUEer', scorer('src'), 14),
                          ],
                         )
def test_score(word, src_mod, score):
    assert src_mod.score(word) == score


@pytest.mark.parametrize("word, src_mod",
                         [('cabbbage', scorer('src')),
                          ('abbacus', scorer('src')),
                          ('queeer', scorer('src')),
                          ('CABBBAGE', scorer('src')),
                          ('ABBAcUs', scorer('src')),
                          ('QuEeEr', scorer('src'))
                          ]
                         )
def test_invalid_score(word, src_mod):
    with pytest.raises(KeyError):
        src_mod.score(word)


@pytest.mark.parametrize("src_mod",
                         [scorer('mini_wordlist'),
                          scorer('charlist'),
                          ],
                         ids=['mini_wordlist', 'charlist']
                         )
def test_build_leaderboard_for_word_list(src_mod, data_regression):
    data_regression.check(src_mod.build_leaderboard_for_word_list())
