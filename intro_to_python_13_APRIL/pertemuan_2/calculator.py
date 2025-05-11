#import	Mengambil library dari luar
#def	Mendefinisikan fungsi
#if / elif / else	Logika untuk pengambilan keputusan
#eval()	Menghitung ekspresi matematika dari string
#entry.insert()	Menambahkan teks ke input
#entry.delete()	Menghapus isi input
#for	Looping (pengulangan)
#lambda	Fungsi kecil tanpa nama, dipakai buat kirim data ke fungsi klik
#tk.Tk()	Membuat jendela utama GUI
#.mainloop()	Jalankan GUI terus-menerus

import tkinter as tk

def klik(tombol):
    if tombol == "=":
        try:
            hasil = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, hasil)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error") 
    elif tombol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, tombol)

root = tk.Tk()
root.title("YUSUF KALKULATOR")

entry= tk.Entry(root, width=30, font=("Arial", 16), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

tombol_list = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

row = 1
col = 0
for tombol in tombol_list:
    tk.Button(root, text=tombol, padx=20, pady=20, font=("Arial", 14),
              command=lambda t=tombol: klik(t)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()



