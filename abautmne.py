import tkinter as tk


root = tk.Tk()
root.title("Мирач")
root.geometry("400x300")  # Размеры окна (ширина x высота)

label = tk.Label(root, text="Привет мир!", font=("Arial", 20))
label.pack(pady=50)  # Размещение метки в окне с отступом


root.mainloop()
