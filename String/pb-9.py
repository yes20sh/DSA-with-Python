# Find the first and last index of occurrence for each character in a string.

value = input()
dic = {}

for index, char in enumerate(value):
    if char not in dic:
        dic[char] = [index, index]
    else:
        dic[char][1] = index

for char, (first_idx, last_idx) in dic.items():
    print(f"Character '{char}' → First Index: {first_idx}, Last Index: {last_idx}")