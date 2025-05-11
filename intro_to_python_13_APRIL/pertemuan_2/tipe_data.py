#tipe data premitif
#integer adalah bilang bulat
x = 23456
print("ini contoh tipe dat integer: {0}".format(x))
#float atau bubble adalah bilangan desimal
print("ini contoh tipe data float: {0}".format (x))
z = 2+3j
print("ini contoh tipe data kompleks: {0}".format(z))

#tipe data text
#char, varchar, karakter adalah satuan huruf A, B, C. D

#tipe data non primitif seperti data jaman sekarang salah satu contoh nya string

#squence type
#list ini bisanya digunakan untuk menampung tipe data yang sama dalam jumlah
a = [24,25,32,20]
print(a)

#true plat
b = (4, 5, 6) #tidak bisa diubah sifatnya
print(b)

#range
e = range (0, 5)
print(e)

#tipe data mapping
#dict kata lainnya vector (c), array (java)

profile = {"nama" : "yusuf", "age" : 19}
print(profile)

#set
#tipe data final atau tak bisa diubah lagi
f = {1, 2, 3}
print(f)

#frozenset
g = frozenset({4,5,6})

#tipe data kondisi
#boolean nilai ada 2 true(1) dan false(0)
kondisi_angka = 1
kondisi_angka_setelah_di_terjemahkan = bool(kondisi_angka)


#binary
i = 0b01000001
desimal = int(i)
ch = chr(desimal)
print(ch)

#bytearray
j = bytearray(a)
print(j)

#memoryview
z = memoryview(j)
print(z)

for i in range(100):
    print(i)