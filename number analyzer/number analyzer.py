def number_analyzer(numbers):
    # Calculate sum
    total = sum(numbers)
    print("Sum:", total)

    # Determine maximum and minimum numbers
    maximum = max(numbers)
    minimum = min(numbers)
    print("Maximum:", maximum)
    print("Minimum:", minimum)

    # Count even and odd numbers
    evens = 0
    odds = 0
    for num in numbers:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    print("Even numbers:", evens)
    print("Odd numbers:", odds)

    # Calculate average
    average = total / len(numbers)
    print("Average:", average)

    # Check if a specific number is present
    target = int(input("Enter a number to check if it is present in the list: "))
    if target in numbers:
        print(target, "is present in the list.")
    else:
        print(target, "is not present in the list.")


# Main program
number_list = input("Enter a list of numbers (separated by spaces): ").split()
number_list = [int(num) for num in number_list]

number_analyzer(number_list)
1212