# Find the difference between the number of consonants and vowels in a string.

value = input()
vowels = consonants = 0
seen = "aeiou"
for i in value:
    if i in seen:
        vowels += 1
    else:
        consonants += 1
print(f" vowels : {vowels} and consonants : {consonants}")
