from tkinter import *
import pandas as pd

def submit_fields():
    path = 'D:\Projects\simple projects\Marksheet update project\Marksheet.xlsx'
    df1 = pd.read_excel(path)
    SeriesA = df1['Roll No']
    SeriesB = df1['Name']
    SeriesC = df1['Maths']
    SeriesD = df1['COA']
    SeriesE = df1['DLD']
    SeriesF = df1['FAIDS']
    SeriesG = df1['OOPJ']
    SeriesH = df1['DS']
    A = pd.Series(entry1.get())
    B = pd.Series(entry2.get())
    C = pd.Series(entry3.get())
    D = pd.Series(entry4.get())
    F = pd.Series(entry6.get())
    G = pd.Series(entry7.get())
    H = pd.Series(entry8.get())

    SeriesA = SeriesA.append(A)
    SeriesB = SeriesB.append(B)
    SeriesC = SeriesC.append(C)
    SeriesD = SeriesD.append(D)
    SeriesF = SeriesF.append(F)
    SeriesG = SeriesG.append(G)
    SeriesH = SeriesH.append(H)

    df2 = pd.DataFrame({"Roll No":SeriesA, "Name":SeriesB, "Maths":SeriesC, "COA":SeriesD, "DLD":SeriesE, "FAIDS":SeriesF, "OOPJ":SeriesG, "DS":SeriesH })
    df2.to_excel(path, index=False)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    entry8.delete(0, END)


app = Tk()
app.title("Marksheet Generator")
#app.config(bg="#DC143C")
app.geometry("900x600")

Label(app, text="Roll No").grid(row=3)
Label(app, text="Name").grid(row=4)
Label(app, text="Maths").grid(row=5)
Label(app, text="COA").grid(row=6) 
Label(app, text="DLD").grid(row=7)
Label(app, text="FAIDS").grid(row=8)
Label(app, text="OOPJ").grid(row=9)
Label(app, text="DS").grid(row=10)

entry1 = Entry(app)
entry2 = Entry(app)
entry3 = Entry(app)
entry4 = Entry(app)
entry5 = Entry(app)
entry6 = Entry(app)
entry7 = Entry(app)
entry8 = Entry(app)

entry1.grid(row=3, column=1)
entry2.grid(row=4, column=1)
entry3.grid(row=5, column=1)
entry4.grid(row=6, column=1)
entry5.grid(row=7, column=1)
entry6.grid(row=8, column=1)
entry7.grid(row=9, column=1)
entry8.grid(row=10, column=1)



Button(app, text='Quit', command=app.quit).grid(row=11,column=0, pady=10)
Button(app, text='Submit', command=submit_fields).grid(row=11,column=2, pady=4)

mainloop()

