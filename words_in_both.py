# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 5/17/2022
# Description: Takes two strings and returns a set of words in both strings.

def words_in_both(sentence_1, sentence_2):
    """Returns the words two strings have in common."""

    split_1 = set(sentence_1.lower().split())
    split_2 = set(sentence_2.lower().split())

    return split_1 & split_2