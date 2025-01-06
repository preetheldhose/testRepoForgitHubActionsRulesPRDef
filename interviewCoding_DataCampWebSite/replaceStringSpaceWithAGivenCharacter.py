#!/usr/local/bin/python3

def str_replace(text, ch):
    result = ''
    for i in text:
        if i == ' ':
            i = ch
        result += i;
    return result


text = "D t C mpBl ckFrid yS le"
ch = "a"

print("Prechange : ", text, ch);
print("Postchange : ", str_replace(text, ch));
# 'DataCampBlackFridaySale'
