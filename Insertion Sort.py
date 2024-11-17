import pandas as pd
import time


class Teacher:
    def __init__(self, name, subject, rating, numRatings):
        self.name = name
        self.subject = subject
        self.rating = rating
        self.numRatings = numRatings


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and (
            (arr[j].rating * arr[j].numRatings) < (key.rating * key.numRatings) or
            (arr[j].rating * arr[j].numRatings == key.rating * key.numRatings and arr[j].rating < key.rating)
        ):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


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

# Perform insertion_sort and measure the runtime
insertion_sort_data = data.copy()
start_time = time.perf_counter()
insertion_sort(insertion_sort_data)
insertion_sort_runtime = time.perf_counter() - start_time

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
print("insertion_sort Runtime: {:.6f} seconds".format(insertion_sort_runtime))
print("binary_search Runtime: {:.6f} seconds".format(binary_search_runtime))
