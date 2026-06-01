from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

folder = filedialog.askdirectory()

print(folder)