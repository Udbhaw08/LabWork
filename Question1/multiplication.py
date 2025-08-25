# WAP in Python to create a multiplication table for the given number
num = int(input("Enter a number: "))
for i in range(1, 11):
    table = num * i
    print(table)