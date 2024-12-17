from tkinter import *
from tela_cadastro import TelaCadastro
from tela_consulta import TelaConsulta
from tela_editar import TelaEditar
from tela_instrucoes import TelaInstrucoes
import banco_de_dados  # Importa o módulo do banco de dados

win_width, win_height = 1024, 768

class App:
    def __init__(self, master=None):
        self.master = master
        self.master.title('Menu de Opções')
        self.master.geometry(f'{win_width}x{win_height}')

        # Criando o menu de opções
        self.menu_bar = Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Adicionando opções diretamente ao menu bar
        self.menu_bar.add_command(label="Instruções", command=self.abrir_instrucoes)
        self.menu_bar.add_command(label="Cadastrar", command=self.abrir_cadastro)
        self.menu_bar.add_command(label="Consultar", command=self.abrir_consulta)
        self.menu_bar.add_command(label="Editar", command=self.abrir_editar)
        self.menu_bar.add_command(label="Sair", command=self.master.quit)

        # Área principal para trocar entre telas
        self.container = Frame(self.master)
        self.container.pack(fill='both', expand=True)

        # Instanciando as telas
        self.instrucoes_tela = TelaInstrucoes(self.container)
        self.cadastro_tela = TelaCadastro(self.container)
        self.consulta_tela = TelaConsulta(self.container)
        self.editar_tela = TelaEditar(self.container)

        # Frames para cada funcionalidade (instâncias das classes)
        self.frames = {
            "Instruções": self.instrucoes_tela,
            "Cadastro": self.cadastro_tela,
            "Consulta": self.consulta_tela,
            "Editar": self.editar_tela
        }

        # Cria a tabela se não existir
        banco_de_dados.criar_e_iniciar()

        # Exibir tela inicial
        self.exibir_tela_inicial()

    def exibir_tela_inicial(self):
        # Exibe uma tela inicial ou a primeira tela que você deseja mostrar
        self.abrir_instrucoes()  # Exibe a tela de instruções por padrão

    def abrir_instrucoes(self):
        self.esconder_frames()
        self.frames["Instruções"].mostrar()

    def abrir_cadastro(self):
        self.esconder_frames()
        self.frames["Cadastro"].mostrar()

    def abrir_consulta(self):
        self.esconder_frames()
        self.frames["Consulta"].mostrar()

    def abrir_editar(self):
        self.esconder_frames()
        self.frames["Editar"].mostrar()

    def esconder_frames(self):
        for frame in self.frames.values():
            frame.esconder()


# Cria a janela principal e inicia o loop da interface gráfica
root = Tk()
app = App(root)
root.mainloop()
