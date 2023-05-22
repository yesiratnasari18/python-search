def binary_search_insert_position(data, target):
    left= 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target :
            left = mid + 1
        else: 
            right = mid - 1
    return left

my_list = [2, 4, 6, 8, 10, 12, 14]
target = 7
index= binary_search_insert_position(my_list, target)
print(f"Elemen {target} dapat disisipkan pada index {index} untuk menjaga daftar tetp terurut.")