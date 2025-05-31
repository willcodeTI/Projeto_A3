import sqlite3

def conectar():
    return sqlite3.connect('academico.db')

def menu():
    print("\n--- Sistema Acadêmico ---")
    print("1 - Cadastrar curso")
    print("2 - Listar cursos")
    print("3 - Cadastrar aluno")
    print("4 - Listar alunos")
    print("5 - Cadastrar disciplina")
    print("6 - Listar disciplinas")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def cadastrar_curso():
    codigo = input("Código do curso: ")
    nome = input("Nome do curso: ")
    conn = conectar()
    conn.execute("INSERT INTO cursos (codigo, nome) VALUES (?, ?)", (codigo, nome))
    conn.commit()
    conn.close()
    print("Curso cadastrado com sucesso!")

def listar_cursos():
    conn = conectar()
    cursos = conn.execute("SELECT id, codigo, nome FROM cursos").fetchall()
    for c in cursos:
        print(f"ID: {c[0]}, Código: {c[1]}, Nome: {c[2]}")
    conn.close()

# Implemente funções semelhantes para alunos, disciplinas, etc.

if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao == "1":
            cadastrar_curso()
        elif opcao == "2":
            listar_cursos()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")