'''
Reid Harry
Hybrid Sort
Implementation of the sorting algorithms adapted from geeksforgeeks.org
Merge Sort: https://www.geeksforgeeks.org/python-program-for-merge-sort/
Insertion Sort: https://www.geeksforgeeks.org/python-program-for-insertion-sort/
'''

import timeit
import matplotlib.pyplot as plt

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

tim_code = '''
MIN_MERGE = 32
 
 
def calcMinRun(n):
    """Returns the minimum length of a
    run from 23 - 64 so that
    the len(array)/minrun is less than or
    equal to a power of 2.
 
    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r
 
 
# This function sorts array from left index to
# to right index which is of size atmost RUN
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
 
 
# Merge function merges the sorted runs
def merge(arr, l, m, r):
 
    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
 
    i, j, k = 0, 0, l
 
    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
 
        else:
            arr[k] = right[j]
            j += 1
 
        k += 1
 
    # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
 
    # Copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1
 
 
# Iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)
 
    # Sort individual subarrays of size RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertionSort(arr, start, end)
 
    # Start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = minRun
    while size < n:
 
        # Pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):
 
            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)
 
        size = 2 * size

timSort(arr)
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
tim_results = {}
arr_length = 10
while(True):
    curr_setup = setup_code.replace("x", str(arr_length))

    insertion_results[arr_length] = timeit.timeit(setup=curr_setup, stmt=insertion_code, number=5)
    merge_results[arr_length] = timeit.timeit(setup=curr_setup, stmt=merge_code, number=5)
    tim_results[arr_length] = timeit.timeit(setup=curr_setup, stmt=tim_code, number=5)

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
    print("\Tim Sort Time: " + str(tim_results[length]))

# creating the bar plot for small n
fig = plt.subplots(figsize = (12, 8))
barWidth = 2
arr_lens = list(insertion_results.keys())[0:10]
arr_lens_insert = [x - barWidth for x in arr_lens]
times_insert = list(insertion_results.values())[0:10]
arr_lens_merge = [x for x in arr_lens]
times_merge = list(merge_results.values())[0:10]
arr_lens_tim = [x + barWidth for x in arr_lens]
times_tim = list(tim_results.values())[0:10]

plt.bar(arr_lens_insert, times_insert, color ='red',
        width = barWidth, edgecolor = "grey", label = "Insertion Sort")
plt.bar(arr_lens_merge, times_merge, color ='blue',
        width = barWidth, edgecolor = "grey", label = "Merge Sort")
plt.bar(arr_lens_tim, times_tim, color ='green',
        width = barWidth, edgecolor = "grey", label = "Tim Sort")
 
plt.xlabel("Array Length")
plt.ylabel("Sorting Time")
plt.xticks(arr_lens)
plt.title("Insertion Sort vs Merge Sort (small n's, k = 32)")
plt.legend()
plt.show()

# creating the bar plot for medium n
fig = plt.subplots(figsize = (12, 8))
barWidth = 20
arr_lens = list(insertion_results.keys())[9:19]
arr_lens_insert = [x - barWidth for x in arr_lens]
times_insert = list(insertion_results.values())[9:19]
arr_lens_merge = [x for x in arr_lens]
times_merge = list(merge_results.values())[9:19]
arr_lens_tim = [x + barWidth for x in arr_lens]
times_tim = list(tim_results.values())[9:19]

plt.bar(arr_lens_insert, times_insert, color ='red',
        width = barWidth, edgecolor = "grey", label = "Insertion Sort")
plt.bar(arr_lens_merge, times_merge, color ='blue',
        width = barWidth, edgecolor = "grey", label = "Merge Sort")
plt.bar(arr_lens_tim, times_tim, color ='green',
        width = barWidth, edgecolor = "grey", label = "Tim Sort")
 
plt.xlabel("Array Length")
plt.ylabel("Sorting Time")
plt.xticks(arr_lens)
plt.title("Insertion Sort vs Merge Sort (medium n's, k = 32)")
plt.legend()
plt.show()

# creating the bar plot for long n
fig = plt.subplots(figsize = (12, 8))
barWidth = 200
arr_lens = list(insertion_results.keys())[18:30]
arr_lens_insert = [x - barWidth for x in arr_lens]
times_insert = list(insertion_results.values())[18:30]
arr_lens_merge = [x for x in arr_lens]
times_merge = list(merge_results.values())[18:30]
arr_lens_tim = [x + barWidth for x in arr_lens]
times_tim = list(tim_results.values())[18:30]

plt.bar(arr_lens_insert, times_insert, color ='red',
        width = barWidth, edgecolor = "grey", label = "Insertion Sort")
plt.bar(arr_lens_merge, times_merge, color ='blue',
        width = barWidth, edgecolor = "grey", label = "Merge Sort")
plt.bar(arr_lens_tim, times_tim, color ='green',
        width = barWidth, edgecolor = "grey", label = "Tim Sort")
 
plt.xlabel("Array Length")
plt.ylabel("Sorting Time")
plt.xticks(arr_lens)
plt.title("Insertion Sort vs Merge Sort (large n's, k = 32)")
plt.legend()
plt.show()

