lista_estudiantes = ['Jose Hernandez', 'Sebastian Aldaz', 'Miguel Mendez', 'Gisel Portillo']

def registrar_estudiante(cantidad):
    for i in range(cantidad):
        estudiante = input("Nombre del estudiante: ")
        lista_estudiantes.append(estudiante)

def consultar_estudiantes():
    print("========ESTUDIANTES========")
    for i in range(len(lista_estudiantes)):
        print(lista_estudiantes[i])

def menu_estudiantes():
    while True:
        print("===MENU ESTUDIANTES===",
              "\n1.-Registrar estudiantes",
              "\n2.-Consultar estudiantes",
              "\n3.-Salir")
        try:
            res=int(input("¿Que desea?"))
        except ValueError:
            print("Respuesta no valida")
        else:
            if res==1:
                try:
                    cantidad=int(input("¿Cuantos estudiantes desea registrar?"))
                    registrar_estudiante(cantidad)
                except ValueError:
                    print("Respuesta no valida")
            elif res==2:
                consultar_estudiantes()
            elif res==3:
                break
            else:
                print("Opcion no valida")