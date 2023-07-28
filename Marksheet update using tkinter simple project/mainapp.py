from tkinter import *
import pandas as pd

def submit_fields():
    path = 'D:\Projects\simple projects\Marksheet update project\Marksheet.xlsx'
    df1 = pd.read_excel(path)
    columns = ['Roll No', 'Name', 'Maths', 'COA', 'DLD', 'FAIDS', 'OOPJ', 'DS']
    data = {col: pd.Series(entry.get()) for col, entry in zip(columns, entries)}

    df2 = df1.append(pd.DataFrame(data), ignore_index=True)
    df2.to_excel(path, index=False)
    clear_entries()

def clear_entries():
    for entry in entries:
        entry.delete(0, END)

app = Tk()
app.title("Marksheet Generator")
app.geometry("900x600")

labels = ['Roll No', 'Name', 'Maths', 'COA', 'DLD', 'FAIDS', 'OOPJ', 'DS']
entries = []

for row, label in enumerate(labels, start=3):
    Label(app, text=label).grid(row=row, column=0, padx=5)
    entry = Entry(app)
    entry.grid(row=row, column=1)
    entries.append(entry)

Button(app, text='Quit', command=app.quit).grid(row=11, column=0, pady=10)
Button(app, text='Submit', command=submit_fields).grid(row=11, column=2, pady=4)

mainloop()
