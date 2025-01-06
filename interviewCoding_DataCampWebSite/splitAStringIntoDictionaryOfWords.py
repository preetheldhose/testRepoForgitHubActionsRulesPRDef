#!/usr/local/bin/python3

test_string0 = "This is the world";
string0 = test_string0.strip();
pairs0 = string0.split();
print(pairs0)


def can_split_into_dict_words(s: str, wordDict: set) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: empty string can always be segmented

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[n]


# Example usage
wordDict = {"apple", "pen", "applepen", "pine", "pineapple"}
s1 = "pineapplepenapple"
s2 = "catsandog"

print(can_split_into_dict_words(s1, wordDict))  # Output: True
print(can_split_into_dict_words(s2, wordDict))  # Output: False


def str_to_dict(string):
    # remove the curly braces from the string
    string = string.strip('{}')

    # split the string into key-value pairs
    pairs = string.split(', ')

    # use a dictionary comprehension to create
    # the dictionary, converting the values to
    # integers and removing the quotes from the keys
    return {key[1:-2]: int(value) for key, value in (pair.split(': ') for pair in pairs)}


# test the function
test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'
print("The original string : " + str(test_string))
print("The converted dictionary : " + str(
    str_to_dict(test_string)))
