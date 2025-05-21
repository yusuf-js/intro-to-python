#import	Mengambil library dari luar
#def	Mendefinisikan fungsi
#if / elif / else	Logika untuk pengambilan keputusan
#eval()	Menghitung ekspresi matematika dari string
#entry.insert()	Menambahkan teks ke input
#entry.delete()	Menghapus isi input
#for	Looping (pengulangan)
#lambda	Fungsi kecil tanpa nama, dipakai buat kirim data ke fungsi klik
#tk.Tk()	Membuat jendela utama GUI
#.mainloop()	Jalankan GUI terus-menerusimport tkinter as tk

import tkinter as tk

class Kalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator dengan History")

        self.history = []

        self.entry = tk.Entry(root, width=30, font=("Arial", 16), bd=5, relief=tk.RIDGE, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        self.history_label = tk.Label(root, text="History: ", font=("Arial", 10), anchor='w')
        self.history_label.grid(row=5, column=0, columnspan=4, sticky="w")

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
                      command=lambda t=tombol: self.klik(t)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def klik(self, tombol):
        if tombol == "=":
            try:
                hasil = str(eval(self.entry.get()))
                self.history.append(self.entry.get() + " = " + hasil)
                self.update_history()
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, hasil)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif tombol == "C":
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, tombol)

    def update_history(self):
        self.history_label.config(text="History: " + " | ".join(self.history[-5:]))  # Tampilkan 5 history terakhir

root = tk.Tk()
app = Kalkulator(root)
root.mainloop()

#history
#oop