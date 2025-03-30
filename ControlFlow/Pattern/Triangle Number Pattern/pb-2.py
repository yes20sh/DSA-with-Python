'''
Pattern  

    1
   22
  333
 4444
55555

'''

n = int(input("Enter the n row : "))
for i in range(1, n +1):
    print(" " * (n -i) + str(i) * i)