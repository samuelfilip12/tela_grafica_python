from tkinter import *


class TelaInstrucoes:
    def __init__(self, master):
        self.frame = Frame(master)

        Label(self.frame, text="Instruções de Uso", font=("Roboto", 14)).pack(pady=10)

        instrucoes = (
            "1. Para cadastrar um novo item, selecione a opção 'Cadastrar'.\n"
            "   - Preencha o formulário e clique em 'Salvar'.\n\n"
            "2. Para consultar itens cadastrados, selecione a opção 'Consultar'.\n"
            "   - Digite o código do item e clique em 'Buscar'.\n\n"
            "3. Para editar um item existente, selecione a opção 'Editar'.\n"
            "   - Digite o código do item e clique em 'Editar'.\n\n"
            "4. Utilize o menu para navegar entre as opções."
        )

        texto_instrucoes = Message(self.frame, text=instrucoes, width=400, anchor='w')
        texto_instrucoes.pack(padx=20, pady=10)

    def mostrar(self):
        self.frame.pack(fill='both', expand=True)

    def esconder(self):
        self.frame.pack_forget()
