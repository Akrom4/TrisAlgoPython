# Fabrice Chaplain
# Sorting algorithms plus benchmarking

import random
import time

# Heap sort algorithm (great for space complexity O(1) )
def heapSort(arr):
    n = len(arr)
    # Building a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extracting elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swapping
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left
    # If right child exists and is greater than the root
    if right < n and arr[right] > arr[largest]:
        largest = right
    # If the root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swapping
        heapify(arr, n, largest)

# Merge sort algorithm (great for time complexity O(n log n) but not so great for space complexity O(n))
def mergeSort(arr):
    if len(arr) > 1:
        # Splitting the array in two
        mid = len(arr) // 2
        left = arr[:mid]
        right =arr[mid:]
        mergeSort(left)
        mergeSort(right)
        # Merging the two halves
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        # Copying the remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    # print(arr) # Uncomment to see the steps of the algorithm

# Quicksort algorithm (great for time complexity O(n log n) but not so great for space complexity O(n))
def quicksort(arr):
    quicksortRecursive(arr, 0, len(arr) - 1)

# Splits the array and sorts each part
def quicksortRecursive(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksortRecursive(arr, low, pi - 1)
        quicksortRecursive(arr, pi + 1, high)

# Selects a pivot and partitions the array around it
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Insertion sort algorithm (great for space complexity O(1) but not so great for time complexity O(n^2))
def insertion(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i
        while j > 0 and arr[j - 1] > x:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = x

# Bubble sort algorithm (great for space complexity O(1) but not so great for time complexity O(n^2))
def bubble(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Generates an array of random integers of a given size
def randomTab(n):
    return [random.randint(0, 1000) for _ in range(n)]

# Benchmark utility. Run a sort function a number of times and calculate the total time.
def benchmarkSortFunction(sort_function, array, repetitions):
    totalTime = 0
    for _ in range(repetitions):
        tempArray = array.copy()
        startTime = time.time()
        sort_function(tempArray)
        totalTime += time.time() - startTime
    return totalTime

# Main part of the program
if __name__ == "__main__":
    # Define sizes and associated number of repetitions for benchmarking
    size_repetitions = [(12, 10000), (100, 10000), (1000, 100), (10000, 1)]

    # Printing the header for the output table
    print(f"{'Size':>10} | {'Repetition':>10} | {'Insertion Sort (s)':>20} | {'Bubble Sort (s)':>20} | {'Quicksort (s)':>20} | {'Merge sort (s)':>20} | {'Heapsort (s)':>20}")
    print("-" * 140)


    # Looping through each size and repetition, timing each sorting algorithm
    for size, repetitions in size_repetitions:
        tab = randomTab(size)
        timeInsertion = benchmarkSortFunction(insertion, tab, repetitions)
        timeBubble = benchmarkSortFunction(bubble, tab, repetitions)
        timeQuicksort = benchmarkSortFunction(quicksort, tab, repetitions)
        timeMergeSort = benchmarkSortFunction(mergeSort, tab, repetitions)
        timeHeapSort = benchmarkSortFunction(heapSort, tab, repetitions)
        print(f"{size:>10} | {repetitions:>10} | {timeInsertion:>20.4f} | {timeBubble:>20.4f} | {timeQuicksort:>20.4f} | {timeMergeSort:>20.4f} | {timeHeapSort:>20.4f}")
