import tkinter as tk

def __init__(self, root):
    self.root = root
    self.root.title("YUSUF KALKULATOR")

    

    self.entry = tk.Entry(root, width=30, bd=5, relief=tk.RIDGE, justify='right')

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

    root.mainloop()