__author__ = 'codesse'

from collections import Counter
from typing import List, Dict, Tuple
import logging

WordScoreDict = Dict[str, int]


class HighScoringWords:
    MAX_LEADERBOARD_LENGTH: int = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH: int = 3  # words must be at least this many characters long
    letter_values: Dict = {}
    valid_words: List = []

    def __init__(self, validwords: str = 'wordlist.txt', lettervalues: str = 'letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        """
        self.valid_words_fname = validwords
        with open(validwords) as f:
            self.valid_words = f.read().splitlines()
        self.valid_words_set = set(self.valid_words)

        with open(lettervalues) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def score(self, word: str) -> int:
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

    @staticmethod
    def is_subset(superset: Dict[str, int], subset: Dict[str, int]) -> bool:
        """
        Boolean function set to True if subset dictionary is a subset of superset on the conditions of:
        1) All keys in subset are in superset
        2) All values of keys in subset are less than or equal to the corresponding key-values in superset
        :param superset: Dictionary with alphabet as the key and the number of occurrences of that alphabet as value
        :param subset: Dictionary with alphabet as the key and the number of occurrences of that alphabet as value
        :return: Boolean where True when subset is in superset and False when subset is not in superset
        """
        if not set(superset.keys()).issuperset(set(subset.keys())):
            return False
        for key in subset:
            if subset[key] > superset[key]:
                return False
        return True

    @staticmethod
    def sorted_tuples(word_score_dict: WordScoreDict) -> List[Tuple[str, int]]:
        """
        Sort the dictionary to give output in the right order (descending by value then ascending by word)
        :param word_score_dict: Dictionary of string as key and integers as values where score of each words
        :return: A list of tuples of words and scores with all the highest words ordered in descending order with the
        highest scoring first.  If several words have the same score they are ordered alphabetically in the ascending
        order.
        """
        return sorted(word_score_dict.items(), key=lambda item: (-item[1], item[0]))

    def build_leaderboard_for_word_list(self) -> List[str]:
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words from the complete set of valid words.
        :return: The list of top words.
        """
        output_dict = {}
        logging.info(f'Running build_leaderboard_for_word_list on {self.valid_words_fname}')
        for word in self.valid_words_set:
            if len(word) >= self.MIN_WORD_LENGTH:
                score = self.score(word)
                output_dict[word] = score
                logging.debug(f'{word} added to the leaderboard with a score of {score}')
            else:
                logging.debug(f'{word} is less than minimum word length')
        sorted_tuples = self.sorted_tuples(output_dict)[:self.MAX_LEADERBOARD_LENGTH]
        return list(zip(*sorted_tuples))[0]

    def build_leaderboard_for_letters(self, starting_letters: str) -> List[str]:
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
        logging.info(f'Running build_leaderboard_for_letters on "{starting_letters}"')
        for word in self.valid_words_set:
            if len(word) >= self.MIN_WORD_LENGTH and self.is_subset(available, Counter(word)):
                score = self.score(word)
                output_dict[word] = score
                logging.debug(f'{word} added to the leaderboard with a score of {score}')
            else:
                logging.debug(f'{word} is not a subset of {starting_letters} or less than minimum word length')
        sorted_tuples = self.sorted_tuples(output_dict)[:self.MAX_LEADERBOARD_LENGTH]
        return list(zip(*sorted_tuples))[0]
