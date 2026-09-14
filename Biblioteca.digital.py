<<<<<<< HEAD
from libros import lista_libros, consultar_libros, buscar_libro
=======
>>>>>>> 527bff7941f81777148ed36c36077944f951228e
while True:
    print("===BIBLIOTECA DIGITAL===",
          "\n1.-Menu de libros",
          "\n2.-Menu de estudiantes",
          "\n3.-Menu de prestamos",
          "\n4.-Salir")
    try:
        res=int(input("¿Que desea?"))
    except ValueError:
        print("Respuesta no valida")
    else:
        if res==1:
            from libros import menu_libros
            menu_libros()
        elif res==2:
            cantidad=len(lista_libros)
            consultar_libros(cantidad)
        elif res==3:
            busqueda=input("¿Titulo del libro que esta buscando?")
            buscar_libro(busqueda)
        elif res==4:
            break
        else:
            print("Opcion no valida")