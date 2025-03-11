class Libro: # Definimos la clase
    def __init__(self, titulo, autor, genero): # Definimos el metodo constructor, que recibira 3 valores
        self._titulo = titulo
        self._autor = autor
        self._genero = genero

# Definimos solo los metodos "get" para leer los valores. No definimos los metodos "set" ya que no vamos a modificarlos.
    def get_titulo(self):
        return self._titulo

    def get_autor(self):
        return self._autor

    def get_genero(self):
        return self._genero