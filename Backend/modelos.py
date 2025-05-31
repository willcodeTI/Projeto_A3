class Curso:
    def __init__(self, id, codigo, nome):
        self.id = id
        self.codigo = codigo
        self.nome = nome

class Disciplina:
    def __init__(self, id, codigo, nome):
        self.id = id
        self.codigo = codigo
        self.nome = nome

class Professor:
    def __init__(self, matricula, nome, curso_id, disciplina_id):
        self.matricula = matricula
        self.nome = nome
        self.curso_id = curso_id
        self.disciplina_id = disciplina_id

class Aluno:
    def __init__(self, matricula, nome, curso_id):
        self.matricula = matricula
        self.nome = nome
        self.curso_id = curso_id

class Nota:
    def __init__(self, aluno_matricula, disciplina_codigo, nota):
        self.aluno_matricula = aluno_matricula
        self.disciplina_codigo = disciplina_codigo
        self.nota = nota