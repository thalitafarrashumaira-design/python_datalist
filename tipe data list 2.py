list_buah = [' pisang', 'nanas', 'melon', 'durian', ]

print(list_buah)

# ubah data pertama 
list_buah[0] = 'jeruk'

print(list_buah)

# ubah data terakhir
list_buah[-1] = 'mangga'

print(list_buah)

#ubah data dalam range
list_buah[1:3] = ['naga', 'pepaya']

print(list_buah)

# tambah data di belakang list
list_buah.append('sirsak')
print(list_buah)

# tambah data di awal list
list_buah.insert(0, 'jambu')
print(list_buah)

# tambah data di index mana pun dalam list
list_buah.insert(2, 'imut')
print(list_buah)