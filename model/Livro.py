class Livro():
    def __init__(self, titulo, autor, genero, cod_livro):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cod_livro = cod_livro

        self.status = True

    
    def create(self):
        return f'insert into livro (titulo, autor, genero, cod_livro) values ("{self.titulo}", "{self.autor}", "{self.genero}", {self.cod_livro});'
    
    def read(self):
        return f'select * from livro where cod_livro = {self.cod_livro};'
    
    def upadate(self):
        return f'update livro set titulo = "{self.titulo}", autor = "{self.autor}", genero = "{self.genero}" where cod_livro = {self.cod_livro};'
    
    def delete(self):
        return f'delete from livro where cod_livro = {self.cod_livro};'