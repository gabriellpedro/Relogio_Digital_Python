from tkinter import *
from datetime import datetime
from tkinter import Label

cor1 = "#3d3d3d"  # preto
cor2 = "#fafcff"  # branca
cor3 = "#3080f0"  # azul

#definindo background color e font color
fundo = cor1
cor = cor2

#cria da janela no TK
janela_relogio = Tk()
#define o título como vazio, sem texto
janela_relogio.title("")
#indica as proporções da tela da aplicação
janela_relogio.geometry("440x180")
#dita que a aplicação não poderá ter sua janaela aumentada, ou  diminuída
janela_relogio.resizable(height=FALSE, width=FALSE)
janela_relogio.configure(bg=cor1)

def hora_relogio():
    tempo_relogio = datetime.now()

    hora = tempo_relogio.strftime("%H:%M:%S")
    dia_semana = tempo_relogio.strftime("%A")
    dia = tempo_relogio.day
    mes = tempo_relogio.strftime("%b")
    ano = tempo_relogio.year

    lable1.config(text=hora)
    lable1.after(600, hora_relogio)

    lable2.config(text=dia_semana + " " + str(dia) + "/" + str(mes) + "/" + str(ano))

lable1 = Label(janela_relogio, text="", font=("Arial 80"), bg = fundo, fg= cor)
lable1.grid(row=0, column=0, sticky=NW, padx=5)

lable2 = Label(janela_relogio, text="", font=("Arial 20"), bg=fundo, fg=cor)
lable2.grid(row=1, column=0, sticky=NW, padx=5)

hora_relogio()
janela_relogio.mainloop()