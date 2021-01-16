import tkinter as tk
from tkinter import messagebox as mb

def szyfr_motor():
        z = pole_wprowadzenia_wyraz.get()
        l = pole_wprowadzenia_przesuniecie.get()
        for b in range(len(z)):

                if l=="":
                        mb.showwarning("Uwaga","Wprowadz przesuniecie")
                else:
                        p = (ord(z[b]) + int(l))
                        print("".join(chr(p).replace("!", " ")), end="")

def exit():
        tk._exit()

fenster = tk.Tk()
fenster.title("Szyfr Cezara")
fenster.geometry("1600x1000")

label = tk.Label(master=fenster, text=" Wprowadz slowo lub zdanie ", font="Arial 12", width=40, height=6)
label.pack()

pole_wprowadzenia_wyraz = tk.Entry(master=fenster, width=40)
pole_wprowadzenia_wyraz.pack()

label2 = tk.Label(master=fenster, text=" Wprowadz przesuniecie ", font="Arial 12", width=20, height=4)
label2.pack()

pole_wprowadzenia_przesuniecie = tk.Entry(master=fenster, width=10)
pole_wprowadzenia_przesuniecie.pack()

button1 = tk.Button(master=fenster, text="OK", height=1, width=10, bg="pink", command=szyfr_motor)
button1.pack(side="left", padx=300, pady=100)

button_exit = tk.Button(master=fenster, text="END", height=1, width=10, bg="yellow", command=exit)
button_exit.pack(side="right",padx=300, pady=100)

tk.mainloop()






