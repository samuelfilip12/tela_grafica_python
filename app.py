from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)
DB_PATH = 'app_database.db'


def conectar():
    conn = sqlite3.connect(DB_PATH)
    return conn


@app.route('/')
def index():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM itens')
    itens = cursor.fetchall()
    conn.close()

    return render_template_string('''
    <html>
    <body>
        <h1>Itens</h1>
        <table border="1">
            <tr>
                <th>ID</th>
                <th>Código</th>
                <th>Descrição</th>
            </tr>
            {% for item in itens %}
            <tr>
                <td>{{ item[0] }}</td>
                <td>{{ item[1] }}</td>
                <td>{{ item[2] }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    ''', itens=itens)


if __name__ == '__main__':
    app.run(debug=True)
