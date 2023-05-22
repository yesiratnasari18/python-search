def binary_search_index(data, key):
    low = 0 
    high = len(data) - 1

    while low <= high:
        mid = (low + high) //2
        if data[mid] == key:
            return mid
        elif data[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1
    
my_list = [3, 6, 9, 12, 15, 18, 21]
key = 12
index = binary_search_index(my_list, key)
if index != -1:
    print(f"index elemen {key} adalah {index}")
else:
    print("Elemen tidak ditemukan.")