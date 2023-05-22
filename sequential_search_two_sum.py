def sequential_search_two_sum(data, target):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] + data[j] == target:
                return data[i], data[j]
    return None
    
my_list = [2, 7, 11, 15, 5, 9]
target_sum = 16
result = sequential_search_two_sum(my_list, target_sum)
if result:
    print(f"Dua elemen yang jumlahnya sama dengan {target_sum} adalah {result[0]} dan {result[1]}")
else:
    print("Tidak ada dua elemen yang jumlahnya sama dengan target.")    