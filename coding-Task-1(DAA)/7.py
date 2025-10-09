import random
import time
import sys
def bubble_sort(arr):
    ops = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            ops += 1  
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ops += 1  
    return ops
def selection_sort(arr):
    ops = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            ops += 1 
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            ops += 1 
    return ops
def insertion_sort(arr):
    ops = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            ops += 1  
            arr[j+1] = arr[j]
            ops += 1  
            j -= 1
        arr[j+1] = key
        ops += 1 
    return ops
def quick_sort(arr):
    ops = [0]  
    def _quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            _quick_sort(low, pi - 1)
            _quick_sort(pi + 1, high)

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            ops[0] += 1  
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                ops[0] += 1  
        arr[i+1], arr[high] = arr[high], arr[i+1]
        ops[0] += 1  
        return i+1

    _quick_sort(0, len(arr)-1)
    return ops[0]

def merge_sort(arr):
    ops = [0]  

    def _merge_sort(lst):
        if len(lst) > 1:
            mid = len(lst)//2
            L = lst[:mid]
            R = lst[mid:]
            _merge_sort(L)
            _merge_sort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                ops[0] += 1  
                if L[i] < R[j]:
                    lst[k] = L[i]
                    ops[0] += 1 
                    i += 1
                else:
                    lst[k] = R[j]
                    ops[0] += 1  
                    j += 1
                k += 1
            while i < len(L):
                lst[k] = L[i]
                ops[0] += 1
                i += 1
                k += 1
            while j < len(R):
                lst[k] = R[j]
                ops[0] += 1
                j += 1
                k += 1

    _merge_sort(arr)
    return ops[0]

def analyze_sorting_algorithm(sort_func, arr):
    arr_copy = arr.copy()
    start_time = time.time()
    ops = sort_func(arr_copy)
    end_time = time.time()
    memory = sys.getsizeof(arr_copy)
    return round(end_time - start_time, 6), ops, memory

# Generate random array
size = int(input("Enter size of array: "))
arr = [random.randint(1, 1000) for _ in range(size)]

# List of algorithms
algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
    ("Quick Sort", quick_sort),
    ("Merge Sort", merge_sort)
]

# Run empirical analysis
print("\nEmpirical Analysis of Sorting Algorithms")
print("{:<15} {:<12} {:<18} {:<10}".format("Algorithm", "Time(s)", "Operations Count", "Memory(bytes)"))
print("-"*60)
for name, func in algorithms:
    time_taken, ops, memory = analyze_sorting_algorithm(func, arr)
    print("{:<15} {:<12} {:<18} {:<10}".format(name, time_taken, ops, memory))