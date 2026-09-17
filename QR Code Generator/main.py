import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pyuiWidgets.imageLabel import ImageLabel

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


main = tk.Tk()
main.title("Main Window")
main.config(bg="#E4E2E2")
main.geometry("917x513")
main.update_idletasks()

geometryX = 0
geometryY = 0

main.geometry("+%d+%d"%(geometryX, geometryY))


style = ttk.Style(main)
style.theme_use("clam")

menu = tk.Menu(main)
main.config(menu=menu)
menu_0 = tk.Menu(menu, tearoff=0)
menu_0.add_command(label="New", command=lambda: print("New clicked"))
menu_0.add_command(label="Open", command=lambda: print("Open clicked"))
menu.add_cascade(label="File", menu=menu_0)
menu_1 = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=menu_1)

def generate_QR_Code():
    print("Hello")


# Generate Button
style.configure("label.TLabel", background="#10da32", foreground="#ffffff", anchor="center", command=generate_QR_Code())
label = ttk.Label(master=main, text="Generate", style="label.TLabel")
label.configure(anchor="center")
label.place(x=72, y=273, width=109, height=27)

        #   Input Data
input_data = tk.Text(master=main)
input_data.config(bg="#fff", fg="#000", font=("Arial", 16))
input_data.place(x=161, y=83, width=478, height=57)

style.configure("label1.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
label1 = ttk.Label(master=main, text="Text /  URL", style="label1.TLabel")
label1.configure(anchor="center")
label1.place(x=35, y=93, width=106, height=37)

text = tk.Text(master=main)
text.config(bg="#fff", fg="#000", font=("Arial", 16))
text.place(x=201, y=173, width=142, height=32)

                # Box Size
style.configure("label2.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
label2 = ttk.Label(master=main, text="Box Size (Pixels Per Box):", style="label2.TLabel")
label2.configure(anchor="center")
label2.place(x=39, y=174, width=154, height=32)

                # QR code image
style.configure("qr.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
qr = ImageLabel(master=main, image_path=os.path.join(BASE_DIR, "assets", "images", "Screenshot 2026-09-17 012553.png"), text="", compound=tk.TOP, mode="cover")
qr.configure(anchor="center")
qr.place(x=574, y=269, width=252, height=210)

                # Border 
text1 = tk.Text(master=main)
text1.config(bg="#fff", fg="#000", font=("Arial", 16))
text1.place(x=587, y=178, width=142, height=32)

style.configure("label3.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
label3 = ttk.Label(master=main, text="Border:", style="label3.TLabel")
label3.configure(anchor="center")
label3.place(x=476, y=183, width=77, height=29)

                # Title
style.configure("label4.TLabel", background="#E4E2E2", foreground="#000", anchor="center")
label4 = ttk.Label(master=main, text="Generate QR Code", style="label4.TLabel")
label4.configure(anchor="center")
label4.place(x=102, y=24, width=700, height=30)


main.mainloop()