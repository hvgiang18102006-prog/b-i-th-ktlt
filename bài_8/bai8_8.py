# Hoàng Văn Giang, mssv 245752021610114
import tkinter as tk

root = tk.Tk()
root.title("Thông tin cá nhân")
root.geometry("400x200")
tk.Label(root, text="Họ tên: Hoàng Văn Giang", font=("Arial", 12)).pack(anchor="w")
tk.Label(root, text="Ngày sinh: 18/10/2006", font=("Arial", 12)).pack(anchor="w")
tk.Label(root, text="MSSV: 245752021610114", font=("Arial", 12)).pack(anchor="w")
tk.Label(root, text="Ngành học: Điều khiển kỹ thuật và tự động hóa", font=("Arial", 12)).pack(anchor="w")

root.mainloop()

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Radio Button Demo")
root.geometry("300x200")

v = tk.IntVar()
v.set(1) 


tk.Radiobutton(root, text="Lựa chọn 1", variable=v, value=1).pack(anchor="w")
tk.Radiobutton(root, text="Lựa chọn 2", variable=v, value=2).pack(anchor="w")
tk.Radiobutton(root, text="Lựa chọn 3", variable=v, value=3).pack(anchor="w")

def show_choice():
    messagebox.showinfo("Thông báo", f"Bạn đã chọn: {v.get()}")

btn = tk.Button(root, text="Click Me", command=show_choice)
btn.pack(pady=10)

root.mainloop()
