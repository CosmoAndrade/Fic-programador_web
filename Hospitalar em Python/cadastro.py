from hospital import Hospital,Medico
from tkinter import *

hosp = Hospital(nome='',tipo='',especialidade='',avaliacao='')
app = Tk()
app.geometry('300x300+200+100')

btn_inserir = Button (app,text = 'Inserir', command=hosp.inserir)
btn_inserir.pack()

btn_mostrar = Button (app, text = 'Mostrar', command=hosp.mostrar)
btn_mostrar.pack()



app.mainloop()


