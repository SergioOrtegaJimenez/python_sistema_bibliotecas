from sistema_biblioteca.biblioteca import Biblioteca
from sistema_biblioteca.libro import Libro

# Definicion de objeto de tipo "Biblioteca"
bibliotecaNacional = Biblioteca('Biblioteca Nacional')
print(f'*** Bienvenidos a la {bibliotecaNacional._nombre} ***\n')

# Definicion de objetos de tipo "Libro"
libro1 = Libro('Fundacion', 'Isaac Asimov', 'Ciencia ficcion')
libro2 = Libro('El Incal', 'Alejandro Jodorowsky', 'Comic')
libro3 = Libro('El Silmarillion', 'JRR Tolkien', 'Fantasia')
libro4 = Libro('El Señor de los Anillos', 'JRR Tolkien', 'Fantasia')
libro5 = Libro('Kingdom Come', 'Alex Ross', 'Comic')

# Agregar los libros a la biblioteca creada
bibliotecaNacional.agregar_libro(libro1)
bibliotecaNacional.agregar_libro(libro2)
bibliotecaNacional.agregar_libro(libro3)
bibliotecaNacional.agregar_libro(libro4)
bibliotecaNacional.agregar_libro(libro5)

# Buscar libros por autor
autor = 'JRR Tolkien'
print(f'Libros del autor {autor}')
bibliotecaNacional.buscar_libros_autor(autor)

# Buscar libros por genero
genero = 'Comic'
print(f'\nLibros del genero {genero}')
bibliotecaNacional.buscar_libros_genero(genero)

# Mostrar todos los libros de la biblioteca nacional
bibliotecaNacional.mostrar_todos_libros()