import sqlite3

conn == sqlite3.connect("todo-app.db")

def criar_tabela_todo():
    #cria tabela caso nao exista
    cursor = conn.cursor()
    conn.execute("""
    create table if not exists tarefa (
        cd_tarefa integer primary key autoincrement,
        tarefa text,
        concluido integer
    )
    """)

def add_tarefa():
    conn.execute("insert into tarefa(tarefa, concluido) values (?, 0)", (tarefa, ))
    conn.commit()

def remover_tarefa():
    conn.execute("delete from tabela where cd_tarefa = ?", (cd_tarefa, ))
    conn.commit()

def concluir_tarefa(cd_tarefa):
    conn.execute("update tarefa set concluido = 1 where cd_tarefa = ?", (cd_tarefa, ))
    conn.commit()

def get_tarefas():
    return conn.execute("select cd_tarefa, tarefa, concluido from tarefa")