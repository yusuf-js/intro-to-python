import random

def random_number_generate(nilai):
    list_data = []
    for i in range(nilai):
        nilai_acak = random.randrange(1, 100)
        list_data.append(nilai_acak)
    return list_data   

def short_bubble(data):
    panjang_data = len(data)

    for i in range(panjang_data):
        for j in range(0,panjang_data-i-1):
            if data [j]> data[j+1]:
                temp = data[j]
                data[j] = data [j+1]
                data[j+1] = temp 


def main():
    banyak_data = int(input("banyak data yang akan dibuat"))
    list_data = random_number_generate(banyak_data)
    print("list data sebelum di urutkan")
    print(list_data)
    input("tekan y untuk melanjutkan tahap")
    short_bubble(list_data)
    print("list data yang sudah diurutkan")
    print(list_data)

if __name__ == "__main__":
    main()