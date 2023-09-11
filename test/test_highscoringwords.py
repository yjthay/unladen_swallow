import pytest
from highscoringwords import HighScoringWords
from collections import Counter


def scorer(type):
    if type == 'mini_wordlist':
        return HighScoringWords(validwords='data/mini_wordlist.txt', lettervalues='../letterValues.txt')
    elif type == 'charlist':
        return HighScoringWords(validwords='data/charlist.txt', lettervalues='../letterValues.txt')
    elif type == 'charlist_2chars':
        return HighScoringWords(validwords='data/charlist_2chars.txt', lettervalues='../letterValues.txt')
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
                          ('QuEeEr', scorer('src')),
                          ('!:^&**"£$&*(*&^%', scorer('src')),
                          ('\n        ', scorer('src'))
                          ]
                         )
def test_invalid_score(word, src_mod):
    with pytest.raises(KeyError):
        src_mod.score(word)


@pytest.mark.parametrize("superset_dict, subset_dict, expected",
                         [(Counter('bullx'), Counter('bull'), True),
                          (Counter('buxyyy'), Counter('bull'), False),
                          (Counter('random'), Counter('rand'), True),
                          (Counter('rand'), Counter('random'), False),
                          ],
                         )
def test_is_subset(superset_dict, subset_dict, expected):
    src_mod = scorer('src')
    assert src_mod.is_subset(superset_dict, subset_dict) == expected


@pytest.mark.parametrize("src_mod, word_score_dict",
                         [(scorer('src'), {'c': 3, 'a': 3, 'b': 3}),
                          (scorer('src'), {'c': 4, 'a': 3, 'b': 3}),
                          (scorer('src'), {'zz': 4, 'z': 4, 'a': 3, 'b': 3}),
                          (scorer('src'), {'z': 4, 'c': 4, 'a': 3, 'b': 3}),
                          ],
                         ids=['a b c', 'c a b', 'z zz a b', 'c z a b']
                         )
def test_sorted_tuples(src_mod, word_score_dict, data_regression):
    data_regression.check(src_mod.sorted_tuples(word_score_dict))


@pytest.mark.parametrize("src_mod",
                         [scorer('mini_wordlist'),
                          scorer('charlist'),
                          scorer('charlist_2chars'),
                          ],
                         ids=['mini_wordlist', 'charlist', 'charlist_2chars']
                         )
def test_build_leaderboard_for_word_list(src_mod, data_regression):
    data_regression.check(src_mod.build_leaderboard_for_word_list())


@pytest.mark.parametrize("src_mod, string_letter",
                         [(scorer('src'), 'deora'),
                          (scorer('src'), 'taxes'),
                          (scorer('src'), 'cabs')
                          ],
                         ids=['deora', 'taxes', 'cabs']
                         )
def test_build_leaderboard_for_letters(src_mod, string_letter, data_regression):
    data_regression.check(src_mod.build_leaderboard_for_letters(string_letter))