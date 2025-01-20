import timeit
import random
import matplotlib.pyplot as plt


# Сортування злиттям (Merge sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


# Сортування вставками (Insertion sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def compare_sorts():
    num_elements = [10, 100, 1000, 5000, 10000]
    results = {
        "Merge Sort": [],
        "Insertion Sort": [],
        "Timsort (sorted)": [],
        "Timsort (.sort())": []
    }

    for n in num_elements:
        test_data = [random.randint(0, 10000) for _ in range(n)]

        print(f"\nNumber of elements: {n}")
        
        # Merge Sort
        merge_time = timeit.timeit(lambda: merge_sort(test_data.copy()), number=10)
        results["Merge Sort"].append(merge_time)
        print(f"Merge Sort: {merge_time:.6f} секунд")
        
        # Insertion Sort
        insertion_time = timeit.timeit(lambda: insertion_sort(test_data.copy()), number=10)
        results["Insertion Sort"].append(insertion_time)
        print(f"Insertion Sort: {insertion_time:.6f} секунд")
        
        # Timsort (sorted)
        timsort_time_sorted = timeit.timeit(lambda: sorted(test_data.copy()), number=10)
        results["Timsort (sorted)"].append(timsort_time_sorted)
        print(f"Timsort (sorted): {timsort_time_sorted:.6f} секунд")
        
        # Timsort (.sort())
        timsort_time_sort = timeit.timeit(lambda: test_data.copy().sort(), number=10)
        results["Timsort (.sort())"].append(timsort_time_sort)
        print(f"Timsort (sort): {timsort_time_sort:.6f} секунд")

       
    # Візуалізація результатів
    plt.figure(figsize=(12, 8))

    for sort_type, times in results.items():
        plt.plot(num_elements, times, label=sort_type, marker='o', linewidth=2)

    plt.title("Порівняння алгоритмів сортування", fontsize=16)
    plt.xlabel("Кількість елементів", fontsize=14)
    plt.ylabel("Час виконання (секунди)", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.yscale('log')  # Логарифмічна шкала для кращої візуалізації
    plt.legend(fontsize=12, loc='upper left')
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()


# Запуск порівняння
compare_sorts()