def obtener_autor(titulo):
    for libro in libros:
        if libro[0] == titulo:
            return libro[1]
    return "Autor no encontrado"


datos_autores = {
    # autor: nacimiento, defuncion, idioma
    'William Shakespeare': [[1564,  4, 26], [1616,  5,  3], 'inglés'],
    'Franz Kafka':         [[1883,  7,  3], [1924,  6,  3], 'alemán'],
    'Marcela Paz':         [[1902,  2, 28], [1985,  6, 12], 'español'],
    'Miguel de Cervantes': [[1547,  9, 29], [1616,  4, 22], 'español']
    # ...}
}

def obtener_idioma(titulo):
    autor = obtener_autor(titulo)

    if autor in datos_autores:
        return datos_autores[autor][2]

    return "Idioma no encontrado"

libros = [
    ['Papelucho programador', 'Marcela Paz', 1983],
    ['Don Python de la Mancha', 'Miguel de Cervantes', 1615],
    ['Raw_input y Julieta', 'William Shakespeare', 1597],
    ['La tuplamorfosis', 'Franz Kafka', 1915]
    # ...]
]

def calcular_anos_antes_de_morir(titulo):
    autor = obtener_autor(titulo)

    if autor in datos_autores:

        fecha_muerte = datos_autores[autor][1]
        anio_muerte = fecha_muerte[0]

        for libro in libros:
            if libro[0] == titulo:
                anio_libro = libro[2]
                return anio_muerte - anio_libro

    return 0

titulo = input('Ingrese titulo del libro: ')
print('El libro fue escrito en', obtener_idioma(titulo))
print('por', obtener_autor(titulo))
print('El autor fallecio', calcular_anos_antes_de_morir(titulo), 'años')
print('después de haber escrito el libro')
