# print factorial of a number
#19/08/25
#check on 26/08/25
def calculate_factorial():
    print("Name : Udbhaw Anand")
    print("Roll No : 2302901520186\n")
    
    n = int(input("Enter an integer: "))
    factorial = 1
    
    if n < 0:
        print("Error! Factorial of a negative number doesn't exist.")
    elif n == 0:
        print("Factorial of 0 = 1")
    else:
        for i in range(1, n + 1):
            factorial *= i
        print(f"Factorial of {n} = {factorial}")

calculate_factorial()
