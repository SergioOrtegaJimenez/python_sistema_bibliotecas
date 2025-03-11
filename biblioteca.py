class Biblioteca:
    def __init__(self, nombre): # Definimos el constructor, que recibira el nombre de la biblioteca
        self._nombre = nombre
        self._libros = [] # Creamos lista vacia donde se guardaran los libros (metodo "agregar_libro")

    def get_nombre(self): # Definimos el metodo "get" para leer el valor de nombre
        return self._nombre

    def get_libros(self):
        return self._libros

    def agregar_libro(self, libro): # Definimos este metodo, que recibira un libro
        self._libros.append(libro) # Añadimos el libro a la lista del constructor

    def buscar_libros_autor(self, _autor): # Definimos este metodo, que recibira el autor
        for libro in self._libros: # Recorremos la lista del metodo constructor
            if libro._autor.lower() == _autor.lower(): # Si el autor de la lista del constructor coincide con el autor que recibe el metodo
                self.mostrar_detalle_libro(libro) # Llamada al metodo "mostrar_detalle_libro"

    def buscar_libros_genero(self, _genero): # Definimos este metodo, que recibira el genero
        for libro in self._libros: # Recorremos la lista del metodo constructor
            if libro._genero.lower() == _genero.lower(): # Si el genero de la lista del constructor coincide con el genero que recibe el metodo
                self.mostrar_detalle_libro(libro) # Llamada al metodo "mostrar_detalle_libro"

    def mostrar_todos_libros(self):
        print (f'\nTodos los libros de la {self._nombre}')
        for libro in self._libros: # Recorremos la lista del metodo constructor
            self.mostrar_detalle_libro(libro) # Llamada al metodo "mostrar_detalle_libro"

    def mostrar_detalle_libro(self, libro):
        print (f'Libro -> Titulo: {libro._titulo}, Autor: {libro._autor}, Genero: {libro._genero}')
