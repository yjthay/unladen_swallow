__author__ = 'codesse'

from collections import Counter


class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        with open(validwords) as f:
            self.valid_words = f.read().splitlines()
        self.valid_words_set = set(self.valid_words)

        with open(lettervalues) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def score(self, word):
        """
        Scoring function of the word and returns the score of the word in the Scrabble Game
        :param word: string that needs to be validated
        :return: res: integer with the score of the string in the Scrabble Game
        :raises: KeyError if the word is not valid (i.e. not in the wordlist)
        """
        if word.lower() not in self.valid_words_set:
            raise KeyError('Word not in valid wordlist.')
        res = sum([self.letter_values[char.lower()] for char in word])
        return res

    def is_subset(self, superset, subset):
        """
        Return
        :param superset: Dictionary
        :param subset: Dictionary
        :return: boolean where True when subset is in superset and False when subset is not in superset
        """
        if not set(superset.keys()).issuperset(set(subset.keys())):
            return False
        for key in subset:
            if subset[key] > superset[key]:
                return False
        return True

    def sorted_tuples(self, word_score_dict):
        return sorted(word_score_dict.items(), key=lambda item: (-item[1], item[0]))

    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOAD_LENGTH words from the complete set of valid words.
        :return: The list of top words.
        """
        output_dict = {}
        for word in self.valid_words_set:
            if len(word) >= self.MIN_WORD_LENGTH:
                output_dict[word] = self.score(word)
        sorted_tuples = self.sorted_tuples(output_dict)[:self.MAX_LEADERBOARD_LENGTH]
        return list(zip(*sorted_tuples))[0]

    def build_leaderboard_for_letters(self, starting_letters):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters contained in the starting_letters String.
        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are bulx, the word "bull" is NOT valid.
        There is only one l in the starting string but bull contains two l characters.
        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for words which have the same score.
        :param starting_letters: a random string of letters from which to build words that are valid against the contents of the wordlist.txt file
        :return: The list of top buildable words.
        """
        available = Counter(starting_letters)
        output_dict = {}
        for word in self.valid_words_set:
            if len(word) >= self.MIN_WORD_LENGTH and self.is_subset(available, Counter(word)):
                output_dict[word] = self.score(word)
        sorted_tuples = self.sorted_tuples(output_dict)[:self.MAX_LEADERBOARD_LENGTH]
        return list(zip(*sorted_tuples))
