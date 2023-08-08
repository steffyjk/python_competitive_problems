"""
Problem statement:
    Pattern Chaser
    Have the function PatternChaser(str) take str which will be a string and return the longest pattern within the string.
    A pattern for this challenge will be defined as: if at least 2 or more adjacent characters within the string repeat at least twice.
    So for example "aabecaa" contains the pattern aa, on the other hand "abbbaac" doesn't contain any pattern.
    Your program should return yes/no pattern/null. So if str were "aabejiabkfabed" the output should be yes abe.
    If str were "123224" the output should return no null. The string may either contain all characters (a through z only), integers, or both.
    But the parameter will always be a string type. The maximum length for the string being passed in will be 20 characters. If a string for example is "aa2bbbaacbbb" the pattern is "bbb" and not "aa".
    You must always return the longest pattern possible.
    Examples

    Input: "da2kr32a2"
    Output: yes a2

    Input: "sskfssbbb9bbb"
    Output: yes bbb
"""


def PatternChaser(strParam):
    def is_repeating_pattern(s):
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                pattern = s[i:j]
                count = s.count(pattern)
                pattern_length = len(pattern)

                if count >= 2 and pattern_length > max_length[0]:
                    max_length[0] = pattern_length
                    max_pattern[0] = pattern

    max_pattern = [None]
    max_length = [0]

    is_repeating_pattern(strParam)

    return f"yes {max_pattern[0]}" if max_pattern[0] else "no null"


print(PatternChaser(input()))
