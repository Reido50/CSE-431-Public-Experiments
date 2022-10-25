'''
Reid Harry
Insertion Sort vs Merge Sort
Implementation of the sorting algorithms adapted from geeksforgeeks.org
Merge Sort: https://www.geeksforgeeks.org/python-program-for-merge-sort/
Insertion Sort: https://www.geeksforgeeks.org/python-program-for-insertion-sort/
'''

import timeit
import matplotlib.pyplot as plt

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key


insertion_code = '''
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

insertionSort(arr)
'''

merge_code = '''
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

mergeSort(arr, 0, len(arr) - 1)
'''

setup_code = '''import random
arr_length = x
arr = []
for i in range(arr_length):
    arr.append(i)

random.shuffle(arr)
'''

# Generate Results
insertion_results = {}
merge_results = {}
arr_length = 10
while(True):
    curr_setup = setup_code.replace("x", str(arr_length))

    insertion_results[arr_length] = timeit.timeit(setup=curr_setup, stmt=insertion_code, number=5)
    merge_results[arr_length] = timeit.timeit(setup=curr_setup, stmt=merge_code, number=5)

    if arr_length < 100:
        arr_length += 10
    elif arr_length < 1000:
        arr_length += 100
    elif arr_length < 10000:
        arr_length += 1000
    else:
        break

# Print Results
for length in insertion_results.keys():
    print("Array Length: " + str(length))
    print("\tInsertion Sort Time: " + str(insertion_results[length]))
    print("\tMerge Sort Time: " + str(merge_results[length]))
 
# creating the bar plot for small n
fig = plt.subplots(figsize = (12, 8))
barWidth = 2
arr_lens = list(insertion_results.keys())[0:10]
arr_lens_insert = [x - barWidth/2 for x in arr_lens]
times_insert = list(insertion_results.values())[0:10]
arr_lens_merge = [x + barWidth/2 for x in arr_lens]
times_merge = list(merge_results.values())[0:10]

plt.bar(arr_lens_insert, times_insert, color ='red',
        width = barWidth, edgecolor = "grey", label = "Insertion Sort")
plt.bar(arr_lens_merge, times_merge, color ='blue',
        width = barWidth, edgecolor = "grey", label = "Merge Sort")
 
plt.xlabel("Array Length")
plt.ylabel("Sorting Time")
plt.xticks(arr_lens)
plt.title("Insertion Sort vs Merge Sort (small n's)")
plt.legend()
plt.show()

# creating the bar plot for medium n
fig = plt.subplots(figsize = (12, 8))
barWidth = 20
arr_lens = list(insertion_results.keys())[9:19]
arr_lens_insert = [x - barWidth/2 for x in arr_lens]
times_insert = list(insertion_results.values())[9:19]
arr_lens_merge = [x + barWidth/2 for x in arr_lens]
times_merge = list(merge_results.values())[9:19]

plt.bar(arr_lens_insert, times_insert, color ='red',
        width = barWidth, edgecolor = "grey", label = "Insertion Sort")
plt.bar(arr_lens_merge, times_merge, color ='blue',
        width = barWidth, edgecolor = "grey", label = "Merge Sort")
 
plt.xlabel("Array Length")
plt.ylabel("Sorting Time")
plt.xticks(arr_lens)
plt.title("Insertion Sort vs Merge Sort (medium n's)")
plt.legend()
plt.show()

# creating the bar plot for long n
fig = plt.subplots(figsize = (12, 8))
barWidth = 200
arr_lens = list(insertion_results.keys())[18:30]
arr_lens_insert = [x - barWidth/2 for x in arr_lens]
times_insert = list(insertion_results.values())[18:30]
arr_lens_merge = [x + barWidth/2 for x in arr_lens]
times_merge = list(merge_results.values())[18:30]

plt.bar(arr_lens_insert, times_insert, color ='red',
        width = barWidth, edgecolor = "grey", label = "Insertion Sort")
plt.bar(arr_lens_merge, times_merge, color ='blue',
        width = barWidth, edgecolor = "grey", label = "Merge Sort")
 
plt.xlabel("Array Length")
plt.ylabel("Sorting Time")
plt.xticks(arr_lens)
plt.title("Insertion Sort vs Merge Sort (large n's)")
plt.legend()
plt.show()
