# Insert a character at the first, last, and Kth position in a string.
def insert_char(value, pos, char):
    if pos == 0:
        value = char + value
    elif pos == len(value):
        value = value + char
    elif  pos > 0 and pos < len(value):
        value = value[:pos] + char + value[pos:]
    else:
        value = ""
        print("invalid position")
    return value

value = input("Enter string : ")
char = input("charactor : ")
pos = int(input("Position : "))
print(f"after add : {insert_char(value,pos,char)}")    
        