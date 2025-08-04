import tkinter as tk
from tkinter import filedialog

def selecionar_pasta():
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes('-topmost',1)
    pasta = filedialog.askdirectory()
    root.destroy()
    return pasta