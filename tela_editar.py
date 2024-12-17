from tkinter import *


class TelaEditar:
    def __init__(self, master):
        self.frame = Frame(master)

        Label(self.frame, text="Tela de Edição", font=("Roboto", 14)).pack(pady=10)

        # Exemplo de campo para edição
        Label(self.frame, text="Código para Editar:").pack(anchor='w', padx=20)
        self.editar_entry = Entry(self.frame)
        self.editar_entry.pack(anchor='w', padx=20, pady=5)

        # Botão para confirmar a edição
        self.editar_button = Button(self.frame, text="Editar", command=self.editar)
        self.editar_button.pack(anchor='w', padx=20, pady=5)

        # Área para exibir resultado da edição
        self.resultado_text = Text(self.frame, height=10, width=50)
        self.resultado_text.pack(anchor='w', padx=20, pady=5)

    def mostrar(self):
        self.frame.pack(fill='both', expand=True)

    def esconder(self):
        self.frame.pack_forget()

    def editar(self):
        # Lógica para editar dados e exibir os resultados
        codigo = self.editar_entry.get()
        # Exemplo de resultado fictício
        resultado = f"Edição realizada para o código: {codigo}"
        self.resultado_text.delete(1.0, END)  # Limpa resultados anteriores
        self.resultado_text.insert(END, resultado)  # Insere novo resultado
