from model.Livro import Livro
from config.Databse import Database

class LivroController:
    def cadastrarLivro(self):
        bd = Database("localhost","root","","biblioteca")
        bd.conectar()

        self.livro = Livro("livro","autor","generico", 1234)
        bd.cursor.execute(self.livro.create())
        bd.conexao.commit()

    def lerLivro(self):
        bd = Database("localhost","root","","biblioteca")
        bd.conectar()

        self.livro = Livro("livro","autor","generico", 1234)
        bd.cursor.execute(self.livro.read())
        bd.conexao.commit()

    def atualizarLivro(self):
        bd = Database("localhost","root","","biblioteca")
        bd.conectar()

        bd.cursor.execute(self.livro.upadate())
        bd.conexao.commit()

    def excluirLivro(self):
        bd = Database("localhost","root","","biblioteca")
        bd.conectar()

        bd.cursor.execute(self.livro.delete())
        bd.conexao.commit()