#inisialisasi

makanans = ["Nasi", "Sayur", "Daging", "puding"]
print(f"{makanans}")


numbers = [1, 2, 3]
numbers.extend([12])
print(numbers)

numbers = [1, 2, 3]
numbers.append(12)
print(numbers)


a = [1, 2, 3]
b = [4, 5]

a.append(b)
print(a)

a = [1, 2, 4]
a.extend(b)
print(a)

# Read (R)
# print all
print(f"{makanans}")
# read spesifik
print(f"Isi dari Index ke 1 adalah : {makanans[1]}")
print(f"isi dari index ini : {makanans[-3]}")

# add 
makanans.append("jeli")
print(f"{makanans}")
# delete
makanans.remove("puding")
print(f"{makanans}")
list_2 = ["pisang", "Semangka"]
makanans += list_2 # makanans = makanans + list_2 (incerment)
print(f"{makanans}")