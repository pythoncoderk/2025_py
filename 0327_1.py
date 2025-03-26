from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        print(i)


if __name__ == "__main__":
    nums = [2, 5, 1, 8, 7, 3]
    bubble_sort(nums)