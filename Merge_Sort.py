import pandas as pd
import time


class Teacher:
    def __init__(self, name, subject, rating, numRatings):
        self.name = name
        self.subject = subject
        self.rating = rating
        self.numRatings = numRatings


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if (
            (left[i].rating * left[i].numRatings) < (right[j].rating * right[j].numRatings) or
            (left[i].rating * left[i].numRatings == right[j].rating * right[j].numRatings and
             left[i].rating < right[j].rating)
        ):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def binary_search(arr, subject):
    teachers = []
    for teacher in arr:
        if teacher.subject == subject:
            teachers.append(teacher)
    return teachers


# Read data from Excel file
data_frame = pd.read_excel('teacher_data_live.xlsx')
data = []
for _, row in data_frame.iterrows():
    teacher = Teacher(row['Name'], row['Subject'], row['Rating'], row['NumRatings'])
    data.append(teacher)

subject = input("Enter the subject you want to search for: ").lower()

# Perform merge_sort and measure the runtime
merge_sort_data = data.copy()
start_time = time.perf_counter()
merge_sort_data = merge_sort(merge_sort_data)
merge_sort_runtime = time.perf_counter() - start_time

# Perform binary_search and measure the runtime
start_time = time.perf_counter()
results = binary_search(data, subject)
binary_search_runtime = time.perf_counter() - start_time

if results:
    print("Teachers in {} (Ordered by popularity):".format(subject.capitalize()))
    for i, teacher in enumerate(results, start=1):
        print("{}. {} (Rating: {}, Rated by: {})".format(i, teacher.name, teacher.rating, teacher.numRatings))
else:
    print("No teachers found for {}.".format(subject))

# Print the runtimes with improved precision
print("merge_sort Runtime: {:.6f} seconds".format(merge_sort_runtime))
print("binary_search Runtime: {:.6f} seconds".format(binary_search_runtime))
