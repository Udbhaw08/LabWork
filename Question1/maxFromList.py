def find_max_in_list():
    print("Name : Udbhaw Anand")
    print("Roll No : 2302901520186\n")

    n_str = input("Enter numbers separated by spaces: ")
    numbers = [int(num) for num in n_str.split()]
    
    if not numbers:
        print("The list is empty.")
    else:
        max_element = numbers[0]
        for num in numbers:
            if num > max_element:
                max_element = num
        print(f"Largest element = {max_element}")

find_max_in_list()