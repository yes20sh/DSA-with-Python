# Remove leading, trailing, and extra spaces in a string.

def clean_spaces(s):
    words = s.strip().split()
    cleaned_string = ' '.join(words)
    return cleaned_string

input_str = "   Hello     world!   This   is   Python.   "
result = clean_spaces(input_str)
print("Cleaned String:", result)
