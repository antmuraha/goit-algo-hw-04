import random
import timeit
from tabulate import tabulate
import matplotlib.pyplot as plt
from custom_merge_sort import custom_merge_sort as merge_sort
from custom_insertion_sort import custom_insertion_sort as insertion_sort


def run_experiment():
    sizes = [10**2, 10**3, 10**4]
    results = []

    for size in sizes:
        random_data = [random.randint(0, size) for _ in range(size)]
        sorted_data = sorted(random_data)
        reverse_sorted_data = sorted_data[::-1]

        datasets = {
            "Random": random_data,
            "Sorted": sorted_data,
            "Reverse Sorted": reverse_sorted_data,
        }

        for dataset_type, dataset in datasets.items():
            merge_time = timeit.timeit(
                lambda: merge_sort(dataset[:]), number=1)

            insertion_time = timeit.timeit(
                lambda: insertion_sort(dataset[:]), number=1)

            timsort_time = timeit.timeit(lambda: sorted(dataset[:]), number=1)

            results.append([
                size,
                dataset_type,
                merge_time,
                insertion_time,
                timsort_time
            ])

    return results


def plot_results(results):
    sizes = sorted(set([row[0] for row in results]))
    dataset_types = sorted(set([row[1] for row in results]))

    for dataset_type in dataset_types:
        merge_times = [row[2] for row in results if row[1] == dataset_type]
        insertion_times = [row[3] for row in results if row[1] == dataset_type]
        timsort_times = [row[4] for row in results if row[1] == dataset_type]

        plt.figure(figsize=(10, 6))
        plt.plot(sizes, merge_times, label="Custom merge_sort()")
        plt.plot(sizes, insertion_times, label="Custom insertion_sort()")
        plt.plot(sizes, timsort_times, label="Built-in Timsort")

        plt.title(f"Sorting Performance on {dataset_type} Data")
        plt.xlabel("Input Size")
        plt.ylabel("Time (seconds)")
        # plt.yscale('log')
        plt.legend()
        plt.grid(True)
        plt.show()


def main():
    results = run_experiment()
    headers = [
        "Size",
        "Type",
        "custom_merge_sort() (s)",
        "custom_insertion_sort() (s)",
        "Built-in Timsort (s)"
    ]
    print("\nComparison of Sorting Algorithms:\n")
    print(tabulate(results, headers=headers, floatfmt=".6f"))
    plot_results(results)


if __name__ == "__main__":
    main()
