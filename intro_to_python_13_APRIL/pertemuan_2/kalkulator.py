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

# Buat window utama
root = tk.Tk()
root.title("kalkulator")


# Entry untuk tampilkan input & hasil
entry = tk.Entry(root, width=30, font=("Arial", 16), bd=5, relief=tk.RIDGE, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Tombol-tombol
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

# Jalankan aplikasi
root.mainloop() 
