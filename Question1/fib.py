def fibonacci_series():
    print("Name : Udbhaw Anand")
    print("Roll No : 2302901520186\n")
    
    n = int(input("Enter the number of terms: "))
    t1, t2 = 0, 1
    
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci Series:", end=" ")
        for i in range(n):
            print(t1, end=", ")
            nth = t1 + t2
            t1 = t2
            t2 = nth
        print()

fibonacci_series()
