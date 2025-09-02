def multiplication_table():
    print("Name : Udbhaw Anand")
    print("Roll No : 2302901520186\n")
    
    n = int(input("Enter an integer to display its multiplication table: "))
    print(f"Multiplication table of {n}:")
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

multiplication_table()
