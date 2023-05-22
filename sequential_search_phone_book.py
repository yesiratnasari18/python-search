def is_similar(names1, names2):
    names1 = names1.lower()
    names2 = names2.lower()

    if names1[1] == names2[1]:
        return True
    return False

def sequential_search_phone(phones, name):
    for numbers in phones:
        if is_similar(numbers['names'], name):
            return numbers['number']
        
    return "Nomor tidak ditemukan"

phones = [
    {'names' : 'John Doe', 'number' : '081234567890'},
    {'names' : 'Jane Smith', 'number' : '089876543210'},
    {'names' : 'Michael Johnson', 'number' : '087811223344'},
    {'names' : 'Emily Davis', 'number' : '082122232425'}
]
name = input("Masukan nomor telpon seseorang yang ingin dicari: ")
daftar_nomor = sequential_search_phone(phones, name)
print(daftar_nomor)



