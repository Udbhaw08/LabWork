numbers = input("Enter numbers separated by space: ").split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

print("Maximum number is:", max_num)