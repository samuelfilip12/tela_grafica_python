from tkinter import *

class TelaCadastro:
    def __init__(self, master):
        self.master = master
        self.fonteRotulo = ("Roboto", "8")

        # Frame principal que conterá os widgets de cadastro
        self.frame = Frame(master)

        self.linha01 = Frame(self.frame)
        self.linha01.pack(anchor='w', padx=20, pady=0)
        self.linha01_1 = Frame(self.frame)
        self.linha01_1.pack(anchor='w', padx=20, pady=0)

        # Label "Código" alinhado à esquerda
        self.lb_cadastro = Label(self.linha01, font=self.fonteRotulo, text="Código", anchor='w')
        self.lb_cadastro.pack(side=LEFT, padx=(0, 5), pady=(2, 0))

        # Campo para Código
        self.txt_cadastro = Entry(self.linha01_1, width=8, font=self.fonteRotulo)
        self.txt_cadastro.pack(side=LEFT, pady=(0, 0))

        # Label "Nome" alinhado à esquerda
        self.lb_nome = Label(self.linha01, font=self.fonteRotulo, text="Nome do Aluno", anchor='w')
        self.lb_nome.pack(side=LEFT, padx=18, pady=(2, 0))

        # Campo para Nome
        self.txt_nome = Entry(self.linha01_1, width=60)
        self.txt_nome.pack(side=LEFT, pady=(0, 0), padx=10)

        # Label "Data de Cadastro" alinhado à esquerda
        self.lb_dataCadastro = Label(self.linha01, font=self.fonteRotulo, text="Data do Cadastro", anchor='w')
        self.lb_dataCadastro.pack(side=LEFT, padx=(268), pady=(2, 0))

        # Campo para Data de Cadastro
        self.txt_dataCadastro = Entry(self.linha01_1, width=18)
        self.txt_dataCadastro.pack(side=LEFT, pady=(0, 0), padx=0)

        

    def mostrar(self):
        self.frame.pack(fill='both', expand=True)

    def esconder(self):
        self.frame.pack_forget()

    def salvar(self):
        codigo = self.txt_cadastro.get()
        descricao = self.txt_nome.get()
        banco_de_dados.inserir_item(codigo, descricao)
        self.txt_cadastro.delete(0, END)
        self.txt_nome.delete(0, END)
