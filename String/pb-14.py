# Generate all possible substrings of a string.

def all_substrings(s):
    substrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.append(s[i:j])
    return substrings

input_string = "abc"
result = all_substrings(input_string)
print("All substrings:", result)
