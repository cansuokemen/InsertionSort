def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1


user_input = input("Please enter numbers (Separate with comma): ")

try:
    user_list = [int(x) for x in user_input.split(",")]
except ValueError:
    print("Please enter integer numbers only.")
    exit()

insertion_sort(user_list)
print("Sorted List:", user_list)
