import timeit
import random


def generate_input_array(case):
    if case == "worst":
        # Generate an array sorted in descending order
        arr = list(range(10 ** 4, 0, -1))
    elif case == "average":
        # Generate a random array
        arr = random.sample(range(10 ** 4), 10 ** 4)
    elif case == "best":
        # Generate an array sorted in ascending order
        arr = list(range(10 ** 4))
    else:
        raise ValueError("Invalid case choice. Please choose either 'worst', 'average', or 'best'.")
    return arr


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    stack = [(0, len(arr) - 1)]
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        pivot = arr[start]
        left = start + 1
        right = end

        while left <= right:
            if arr[left] <= pivot:
                left += 1
            elif arr[right] > pivot:
                right -= 1
            else:
                arr[left], arr[right] = arr[right], arr[left]

        arr[start], arr[right] = arr[right], arr[start]
        stack.append((start, right - 1))
        stack.append((right + 1, end))

    return arr


def timsort(arr):
    arr.sort()
    return arr


# Example usage:
case_choice = input("Choose case (worst/average/best): ")

try:
    arr = generate_input_array(case_choice)

    quicksort_runtime = timeit.timeit(lambda: quicksort(arr), number=1)
    timsort_runtime = timeit.timeit(lambda: timsort(arr), number=1)

    print("Quick Sort Runtime: {:.6f} seconds".format(quicksort_runtime))
    print("Tim Sort Runtime: {:.6f} seconds".format(timsort_runtime))

except ValueError as e:
    print(str(e))
