from libros import lista_libros
lista_disponibles = lista_libros.copy()
lista_prestamos=[]
def registrar_prestamo():
    estudiante = input('Estudiante que realizara el prestamo\n')
    if estudiante in lista_estudiantes:
        libro = input('Libro que se va a prestar: \n')
        for i in lista_disponibles:
            if libro == lista_disponibles[i]:
                lista_prestamos[i]=lista_disponibles[i]
                lista_disponibles.pop(i)
            else:
                print('Libro no existente o mal escrito, revisar lista de libros')
                break
    else:
        print('Estudiante no encontrado, revisar lista de estudiantes')
def devolver_prestamo():
    libro=input('Libro que desea devolver: \n')
    for i in lista_prestamos:
        if libro in lista_prestamos[i]:
            lista_disponibles[i] = lista_prestamos[i]
            lista_prestamos.pop(i)
            break
    print('Libro no encontrado')
def imprimir_prestamos():
    print('\t --- Lista de prestamos ---')
    for i in lista_prestamos:
        print(lista_prestamos[i])
def menu():
    print("\t===MENU PRESTAMOS===",
          "\n1.-Realizar un prestamo",
          "\n2.-Devolver prestamo",
          "\n3.-Mostrar todos los prestamos",
          "\n4.-Salir")