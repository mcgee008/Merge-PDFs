import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess
from pathlib import Path
import datetime
import fitz  # PyMuPDF

def browse_fldr():
    fp = filedialog.askdirectory()
    if fp:
        fp_entry.delete(0, tk.END)
        fp_entry.insert(0, fp)
    
def popup_window(pth):
     result = messagebox.askyesno("Merged!", "Do you want to open file ?")
     print(pth)
     if result:
         if os.path.exists(pth):
            subprocess.Popen(['start', '', pth], shell=True)
     else:
       pass 
     
def mergePDF():
    path = fp_entry.get()
    pdfs = []
    #x = os.listdir(path.resolve())
    today = datetime.date.today()
    today = today.strftime("%Y%m%d")
    now = datetime.datetime.now()
    hr = now.hour
    min = now.minute
    sec = now.second
    
    tm = f"{hr}{min}{sec}"
    output_pdf_path = path + "\merged_output" + "_" + today + "_" + tm+ ".pdf"

    for x in os.listdir(path):
        if x.endswith(".pdf"):
            x = os.path.join(path, x)
            pdfs.append(x)

    merger = fitz.open()

    for x in pdfs:
        pdf_document = fitz.open(x)
        merger.insert_pdf(pdf_document)

    merger.save(output_pdf_path)
    merger.close()
    
    popup_window(output_pdf_path)

root = tk.Tk()
windowWidth = 1000
windowHeight = 700
root.title("PDF Merger")

icon_path = "C:/Python/paperplane.png"
icon = tk.PhotoImage(file=icon_path)
root.iconphoto(True, icon)

img_path = "C:/Python/corgi.png"


bkg_img = tk.PhotoImage(file=img_path)

canvas = tk.Canvas(root, width=bkg_img.width(), height=bkg_img.height())
canvas.grid(row = 1, column = 2)

canvas.create_image(0, 0, anchor=tk.NW, image=bkg_img)
root.geometry(f"{windowWidth}x{windowHeight}")

bold_font = ("Helvetica", 16, "bold")

label = tk.Label(root, text="Select Folder:", font=bold_font)
label.grid(row = 0, column = 0, padx = 15)

fp_entry = tk.Entry(root, width = 50)
fp_entry.grid(row = 0, column = 1, pady = 15)

brws_btn = tk.Button(root, text = "Browse for Folder", command = browse_fldr, font = bold_font)
brws_btn.grid(row=0,column =2, padx=10, pady = 10)

button1 = tk.Button(root, text = "Merge PDF Files", command = mergePDF, font=bold_font)
button1.grid(row = 1, column = 1)

root.mainloop()