# Find the maximum and minimum occurring characters in a string.
value = input()
dic = {}
for i in value:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

maxCharacter = max(dic, key=dic.get)
minCharacter = min(dic, key=dic.get)

print(f"Maximum charactor occurance are {maxCharacter} : {dic[maxCharacter]} times")
print(f"Minimum charactor occurance are {minCharacter} : {dic[minCharacter]} times")
