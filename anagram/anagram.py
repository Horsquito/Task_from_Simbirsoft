from collections import Counter


def is_anagram(input_one, input_two):
    return Counter(input_one) == Counter(input_two)
