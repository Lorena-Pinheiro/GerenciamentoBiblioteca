from model.Livro import Livro
from model.Usuario import Usuario
from Biblioteca import Biblioteca
from controler.LivroController import LivroController


controladora = LivroController()

livro = Livro("livro","autor","generico", 1234)
#controladora.cadastrarLivro()
controladora.lerLivro()