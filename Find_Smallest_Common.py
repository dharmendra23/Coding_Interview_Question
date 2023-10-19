#Given three integer arrays sorted in ascending order, return the smallest number that is common in all three arrays. Return -1 if there is no common number

def find_smallest_common_number(arr1, arr2, arr3):
    i, j, k = 0, 0, 0  # Initialize pointers for the three arrays

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        num1, num2, num3 = arr1[i], arr2[j], arr3[k]

        if num1 == num2 == num3:
            return num1  # Found a common number
        elif num1 <= num2 and num1 <= num3:
            i += 1
        elif num2 <= num1 and num2 <= num3:
            j += 1
        else:
            k += 1

    return -1  # No common number found

# Example usage:
arr1 = [1, 5, 10, 20]
arr2 = [3, 5, 15]
arr3 = [5, 10, 15, 30]
result = find_smallest_common_number(arr1, arr2, arr3)
if result != -1:
    print("The smallest common number is:", result)
else:
    print("There is no common number.")
