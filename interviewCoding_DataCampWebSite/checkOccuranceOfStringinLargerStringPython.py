#!/usr/local/bin/python3

def cat_hat_equal(str):
    # Count occurrences of "cat" and "hat"
    count_cat = str.count("cat")
    count_hat = str.count("hat")

    # Check if counts are equal
    return count_cat == count_hat


# Example usage
str1 = "cat hat cat hat hat"
str2 = "cat hat cat"
str3 = "hat hat cat"
str4 = "cat hat cat hat"
str5 = "cathatcat"

# print(cat_hat_equal(str1))  # Output: False
# print(cat_hat_equal(str2))  # Output: False
# print(cat_hat_equal(str3))  # Output: False
# print(cat_hat_equal(str4))  # Output: False
# print(cat_hat_equal(str5))  # Output: False

def checkOccurance(strA):
    catCount = strA.count("cat")
    hatCount = strA.count("hat")
    return catCount == hatCount

print(checkOccurance("cathat"))
print(checkOccurance("catjathat"))
print(checkOccurance("catat"))















