def binary_search(data, key):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == key:
            return True
        elif data[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return False

my_list = [2, 4, 6, 8, 10, 12, 14]
key = 6
found = binary_search(my_list, key)
if found:
    print("Elemen ditemukan.")
else:
    print("Elemen tidak ditemukan.")