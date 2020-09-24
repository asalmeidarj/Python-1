import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.color_background = '#000000'
        self.minsize(300, 200)
        self.maxsize(300, 200)
        self.title("Gráfico")
        self.wm_iconbitmap('python.ico')
        self.configure(backgroun=self.color_background)
        self.initUI()


    def initUI(self):

        self.name1 = StringVar()
        self.name2 = StringVar()

        color_foreground = '#ffffff'
        self.label_inf = Label(self, text='Limite inferior do intervalo: ', font=25)
        self.label_inf.configure(background=self.color_background, foreground=color_foreground)
        self.label_inf.grid(column=0, row=0)
        self.label_sup = Label(self, text='Limite superior do intervalo: ', font=25)
        self.label_sup.configure(background=self.color_background, foreground=color_foreground)
        self.label_sup.grid(column=0, row=1)
        self.textBox1 = Entry(self, width = 10, textvariable=self.name1)
        self.textBox1.config(background='#111111', foreground = '#44D62C', font=25)
        self.textBox1.grid(column=1, row=0)
        self.textBox2 = Entry(self, width=10, textvariable=self.name2)
        self.textBox2.config(background='#111111', foreground='#44D62C', font=25)
        self.textBox2.grid(column=1, row=1)
        self.button = Button(self, text='Gerar Gráfico', command=self.eventclick)
        self.button.grid(column=1, row=2)


    def eventclick(self):
        """Pega os valores dos textBox e passa para função gerargrafico"""
        inf = self.name1.get()
        sup = self.name2.get()
        self.gerargrafico(inf, sup)


    def gerargrafico(self, inf, sup):
        "Função responsável por gerar o gráfico dado o intervalo"
        plt.clf() #limpa o gráfico caso já tenha sido gerado
        inf = float(inf)
        sup = float(sup)
        dominio = np.linspace(inf, sup, 1000)
        imagem = list(map(lambda x: np.sin(pow(x, 2) + np.exp(x)), dominio))

        plt.title('Gerar o gráfico da função f(x) = sin(x^2 + exp(x)) no intervalo dado')
        plt.plot(dominio, imagem)
        """Limpa o TextBox"""
        tam = len(self.textBox1.get())
        self.textBox1.delete(0, tam)
        tam = len(self.textBox2.get())
        self.textBox2.delete(0, tam)
        """Exibi o gráfico"""
        plt.show()


root = Root()
root.mainloop()