from Stack_Linked_list import StackLinkedList

def check_celebrity(arr):
    s = StackLinkedList()
    for i in range(len(arr)):
        s.push(i)
    print(s.sizeof())

    while s.sizeof() >= 2:
        i = s.pop()
        j = s.pop()
        if arr[i][j] == 1:
            s.push(i)
        else:
            s.push(j)
    celeb = s.pop()
    for i in range(len(arr)):
        if i != celeb:
            if arr[i][celeb] == 0 or arr[celeb][i] == 1:
                print(f"{celeb} Not a Celebrity")
                return
    print(f"{celeb} is celebrity")
    s.clear()
            


cel_arr = [
    [0,0,0,1],
    [1,0,0,0],
    [0,0,0,0],
    [0,0,1,0]
]
check_celebrity(cel_arr)