from model.Livro import Livro
from model.Usuario import Usuario

class Biblioteca:
    Acervo:list[Livro] = []

    @staticmethod
    def emprestar(Usuario: Usuario, Livro: list[Livro]):

        for item in Livro:
            if len(Usuario.lista_livro) == Usuario.MAX_EMPRESTIMO:
                return
            Usuario.pegar_emprestado(item)
            item.emprestar_livro(Usuario)