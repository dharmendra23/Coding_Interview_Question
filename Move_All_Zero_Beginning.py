#Move All Zeros to the Beginning of the Array

def move_zeros_to_left(arr):
    if len(arr) < 2:
        return arr  # No need to modify if the array has 0 or 1 elements

    read_index = len(arr) - 1
    write_index = len(arr) - 1

    while read_index >= 0:
        if arr[read_index] != 0:
            arr[write_index] = arr[read_index]
            write_index -= 1
        read_index -= 1

    while write_index >= 0:
        arr[write_index] = 0
        write_index -= 1

# Example usage:
my_array = [0, 2, 0, 3, 0, 4, 5, 0]
move_zeros_to_left(my_array)
print(my_array)
