# for i in range(0,10,2):
#     print(f'perulangan ke-{i}')

# # PERULANGAN UNTUK MENGECEK BILANGAN GENAP GANJIL
# for i in range(0,15):
#     if i % 2 == 0:
#         print(f'{i} - Bilangan Genap')
#     else:
#         print(f'{i} - Bilangan Ganjil')

# # 

# fruits = ['duren','mangga','semangka','apel']

# for i,buah in enumerate (fruits):
#     print(f'Buah ke-{i} : {buah}')

# biodata = {
#     'nama' : 'agus',
#     'nim' : '24090097',
#     'kelas' : '1c',
#     'umur' : 35
# }

# for data in biodata:
#     print(data)

# for data in biodata.values(): 
#     print(data)

# for label,value in biodata.items():
#     print(f'{label} : {value}')

# #BREAK IN CONTINUE
# for i in range(5):
#     if i == 3:
#         break
#     print(i)

for x in range(10):
    if x == 5:
        continue
    print(x)