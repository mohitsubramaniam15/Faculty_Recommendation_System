import pandas as pd
import time

class Teacher:
    def __init__(self, name, subject, rating, numRatings):
        self.name = name
        self.subject = subject
        self.rating = rating
        self.numRatings = numRatings


def min_run_length(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1

        while j >= left and (
                (arr[j].rating * arr[j].numRatings) < (key.rating * key.numRatings) or
                (arr[j].rating * arr[j].numRatings == key.rating * key.numRatings and
                 arr[j].rating < key.rating)
        ):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


def merge(arr, l, m, r):
    len1 = m - l + 1
    len2 = r - m

    left = [arr[l + i] for i in range(len1)]
    right = [arr[m + 1 + i] for i in range(len2)]

    i = j = 0
    k = l

    while i < len1 and j < len2:
        if (
                (left[i].rating * left[i].numRatings) < (right[j].rating * right[j].numRatings) or
                (left[i].rating * left[i].numRatings == right[j].rating * right[j].numRatings and
                 left[i].rating < right[j].rating)
        ):
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right[j]
        j += 1
        k += 1


def tim_sort(arr):
    n = len(arr)
    min_run = min_run_length(n)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, n - 1))

    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min(left + 2 * size - 1, n - 1)
            merge(arr, left, mid, right)
        size *= 2


def binary_search(arr, subject):
    teachers = []
    for teacher in arr:
        if teacher.subject == subject:
            teachers.append(teacher)
    return teachers


# Read data from Excel file
data_frame = pd.read_excel('teachers_data.xlsx')
data = []
for _, row in data_frame.iterrows():
    teacher = Teacher(row['Name'], row['Subject'], row['Rating'], row['NumRatings'])
    data.append(teacher)

subject = input("Enter the subject you want to search for: ").lower()

# Perform tim_sort and measure the runtime
tim_sort_data = data.copy()
start_time = time.perf_counter()
tim_sort(tim_sort_data)
tim_sort_runtime = time.perf_counter() - start_time

# Perform binary_search and measure the runtime
start_time = time.perf_counter()
results = binary_search(data, subject)
binary_search_runtime = time.perf_counter() - start_time

if results:
    tim_sort(results)

    print("Teachers in {} (Ordered by popularity):".format(subject.capitalize()))
    for i, teacher in enumerate(results, start=1):
        print("{}. {} (Rating: {}, Rated by: {})".format(i, teacher.name, teacher.rating, teacher.numRatings))
else:
    print("No teachers found for {}.".format(subject))

# Print the runtimes with improved precision
print("tim_sort Runtime: {:.6f} seconds".format(tim_sort_runtime))
print("binary_search Runtime: {:.6f} seconds".format(binary_search_runtime))
