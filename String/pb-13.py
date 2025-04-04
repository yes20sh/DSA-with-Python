# Find a specific substring within a string.

text = input("Enter the string : ")
subText = input("Enter the substring : ")
index = text.find(subText)

if index != -1:
    print(f"The substring {subText} is founded at {index}")
else:
    print(f" The substring {subText} not founded")
