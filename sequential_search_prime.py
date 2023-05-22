def prima(data):
    if data < 2:
        return False
    for i in range(2, int(data**0.5) + 1):
        if data % i == 0:
            return False
        
    return True

def sequential_search_prime(my_list):
    bil_prima = []
    for angka in my_list:
        if prima(angka):
            bil_prima.append(angka)
    return bil_prima

my_list =[7, 10, 13, 6, 17, 22, 19]


bil_prima = sequential_search_prime(my_list)
print(f"Bilangan prima yang ada di daftar adalah {bil_prima}")