from libros import menu_libros
from prestamos import menu_prestamos
from estudiantes import menu_estudiantes
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
            menu_libros()
        elif res==2:
            menu_estudiantes()
        elif res==3:
            from prestamos import menu_prestamos
            menu_prestamos()
        elif res==4:
            break
        else:
            print("Opcion no valida")