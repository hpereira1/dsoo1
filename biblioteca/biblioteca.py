from livro import Livro


class Biblioteca:
    def __init__(self):
        self.__livros = []

    @property
    def livros(self):
        return self.__livros

    @livros.setter
    def livros(self, livros):
        if isinstance(livros, list):
            self.__livros = livros

    def incluir_livro(self, livro: Livro):
        if isinstance(livro, Livro) and livro not in self.__livros:
            self.__livros.append(livro)

    def excluir_livro(self, livro: Livro):
        if isinstance(livro, Livro) and livro in self.__livros:
            self.__livros.remove(livro)
