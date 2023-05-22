def binary_search_rotation(data):
    low = 0
    high = len(data) - 1

    while low < high:
        mid = (low + high) // 2
        if data [mid] > data[high]:
            low = mid + 1
        else:
            high = mid

    return low
my_list = [6, 7, 8, 9, 1, 2, 3, 4, 5]
rotation_index = binary_search_rotation(my_list)
print(f"Index rotasi terkecil adalah {rotation_index}")
