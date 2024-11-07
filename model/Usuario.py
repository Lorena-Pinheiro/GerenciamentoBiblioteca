class Usuario():
    MAX_EMPRESTIMO = 3

    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.lista_livro = []

    def pegarEmprestado(self,livro):
        if len(self.lista_livro) == self.MAX_EMPRESTIMO:
            return 'Limite de emprestimo atingido'
        
        self.lista_livro.append(livro.titulo)