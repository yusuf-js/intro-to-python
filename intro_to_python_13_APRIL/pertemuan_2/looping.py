# while
# while jika kamu tahu kapan berenti tapi kapan prosesnya dan di check di pertama kali
# format
# while syarat_berhenti:
    # apa yang akan di ulang

print("==========while=============")
index = 0
while index <= 200:
    print(f"index of value {index}")
    index += 1

    print("==========for=============")
for index in range (1,201):
    print(f"index of value {index}")

makanan = ["baso","mie","sayur","daging"]
for value in makanan:
    print(f"{value}")

# break and continue
bilangan = 1
while bilangan <= 100:
    if bilangan % 2 == 0 :
        bilangan += 1 # penjabaran : bilangan = bilangan + 1
        continue # teknik untuk skip 1 putaran
    print(f"{bilangan}")
    bilangan += 1