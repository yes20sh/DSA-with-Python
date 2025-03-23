# Write a program to input amount from user and print minimum number of notes (Rs. 500, 100, 50, 20, 10, 5, 2, 1) required for the amount.

def notes(amount):
    note500 = note100 = note50 = note20 = note10 = note5 = note2 = note1 = 0
    if amount > 500:
         note500 = int(amount / 500)
         amount -= 500*note500
    if amount  > 100:
         note100 = int(amount / 100)
         amount -=  note100 * 100
    if amount > 50:
         note50 = int(amount / 50)
         amount -= note50 * 50
    if amount > 20:
         note20 = int(amount /20)
         amount -= note20 * 20
    if amount > 10:
         note10 = int(amount /10)
         amount -= note10 * 10
    if amount > 5:
         note5 = int(amount / 5)
         amount -= note5 * 5
    if amount > 2:
         note2 = int(amount /2)         
         amount -= note2 * 2
    if amount > 1:
         note1 =  int(amount / 1)
         amount -= note1 * 1
    
    print(f"500 : {note500}")
    print(f"100 : {note100}")
    print(f"50 : {note50}")
    print(f"20 : {note20}")
    print(f"10 : {note10}")
    print(f"5 : {note5}")
    print(f"2 : {note2}")
    print(f"1 : {note1}")
    

amount = int(input("Enter the amount : "))
notes(amount)