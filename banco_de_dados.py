import sqlite3

# Caminho para o arquivo do banco de dados
DB_PATH = 'app_database.db'

def conectar():
    """Estabelece uma conexão com o banco de dados SQLite e retorna a conexão e o cursor."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    return conn, cursor

def criar_tabela():
    """Cria uma tabela no banco de dados se ela não existir."""
    conn, cursor = conectar()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS itens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo TEXT UNIQUE NOT NULL,
        descricao TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def inserir_item(codigo, descricao):
    """Insere um novo item no banco de dados."""
    conn, cursor = conectar()
    try:
        cursor.execute('INSERT INTO itens (codigo, descricao) VALUES (?, ?)', (codigo, descricao))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f'Item com código {codigo} já existe.')
    conn.close()

def consultar_item(codigo):
    """Consulta um item pelo código e retorna os dados."""
    conn, cursor = conectar()
    cursor.execute('SELECT * FROM itens WHERE codigo = ?', (codigo))
    item = cursor.fetchone()
    conn.close()
    return item

def atualizar_item(codigo, descricao):
    """Atualiza a descrição de um item existente."""
    conn, cursor = conectar()
    cursor.execute('UPDATE itens SET descricao = ? WHERE codigo = ?', (descricao, codigo))
    conn.commit()
    conn.close()

def criar_e_iniciar():
    """Cria a tabela e insere alguns dados iniciais se necessário."""
    criar_tabela()
    # Insira dados iniciais se desejar, por exemplo:
    # inserir_item('001', 'Descrição do item 001')
