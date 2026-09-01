def merge_sort(numbers):
    """Return the numbers sorted in ascending order using merge sort."""
    if len(numbers) <= 1:
        return numbers.copy()

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])

    sorted_numbers = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_numbers.append(left[left_index])
            left_index += 1
        else:
            sorted_numbers.append(right[right_index])
            right_index += 1

    sorted_numbers.extend(left[left_index:])
    sorted_numbers.extend(right[right_index:])
    return sorted_numbers


if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    try:
        numbers = list(map(int, user_input.split()))
        print("Original list:", numbers)
        print("Sorted list:", merge_sort(numbers))
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")