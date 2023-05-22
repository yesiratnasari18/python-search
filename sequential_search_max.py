def sequential_search_max(data):
    max_index = 0
    for i in range(1, len(data)):
        if data[i] > data[max_index]:
            max_index = i
    return max_index

my_list = [5, 9, 3, 2, 8, 7]
max_index = sequential_search_max(my_list)
print(f"Index elemen maksimum adalah {max_index}")