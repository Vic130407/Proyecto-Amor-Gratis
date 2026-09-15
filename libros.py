lista_libros=[(
        {"Titulo": "CIEN AÑOS DE SOLEDAD", "Autor": "Gabriel Garcia Marquez", "Año": 1967, "Genero": "realismo magico",
        }, ("15", "09", "2026"),),
    (
        {"Titulo": "DON QUIJOTE DE LA MANCHA","Autor": "Miguel De Cervantes","Año": 1605,"Genero": "novela",
        },("15", "09", "2026"),),
    (
        {"Titulo": "1984", "Autor": "George Orwell", "Año": 1949, "Genero": "distopia",
        },("15", "09", "2026"),),
    (
        {"Titulo": "EL PRINCIPITO", "Autor": "Antoine De Saint-Exupery","Año": 1943,"Genero": "fantasia",
        },("15", "09", "2026"),),
    (
        {"Titulo": "Fahrenheit 451".upper(), "Autor": "Ray Bradbury","Año": 1953,"Genero": "distopia",
        }, ("15", "09", "2026"),
    ),]
def registrar_libro(cantidad):
    dia=input("¿Dia en que se realiza el registro?(Solo numero)")
    mes=input("¿Mes en que se realiza el registro?(Solo numero)")
    año=input("¿Año en que se realiza el registro?(Solo numero)")
    fecha=(dia,mes,año)
    for i in range(cantidad):
        nom_libro=input("¿Nombre del libro?")
        nom_autor=input("¿Nombre del autor?")
        año_publicacion=int(input("¿Año de publicacion?"))
        genero_libro=input("¿Genero del libro?")
        libro={"Titulo":nom_libro.upper(),"Autor":nom_autor.title(),"Año":año_publicacion,"Genero":genero_libro.lower()}
        info_libro=(libro,fecha)
        lista_libros.append(info_libro)

def consultar_libros(cantidad):
    print("========BIBLIOTECA========")
    for i in range(cantidad):
        print(lista_libros[i][0]["Titulo"],"---",lista_libros[i][0]["Autor"],"---",lista_libros[i][0]["Año"],"---",lista_libros[i][0]["Genero"])

def buscar_libro(busqueda):
    for i in range(len(lista_libros)):
        if lista_libros[i][0]["Titulo"]==busqueda.upper():
            print(lista_libros[i][0]["Titulo"],"---",lista_libros[i][0]["Autor"],"---",lista_libros[i][0]["Año"],"---",lista_libros[i][0]["Genero"])
            break
        elif i==(len(lista_libros)-1):
            print("Libro no encontrado")

def estadisticas(cantidad):
    autor_mayor=genero_mayor=0
    for i in range(cantidad):
        cantidad_autor=cantidad_genero=0
        autor=lista_libros[i][0]["Autor"]
        genero=lista_libros[i][0]["Genero"]
        for i in range(cantidad):
            if autor==lista_libros[i][0]["Autor"]:
                cantidad_autor+=1
            if genero==lista_libros[i][0]["Genero"]:
                cantidad_genero+=1
        if autor_mayor<cantidad_autor:
            autor_mayor=cantidad_autor
            autorpop=autor
        if genero_mayor<cantidad_genero:
            genero_mayor=cantidad_genero
            generopop=genero
    print("Numero de libros:",len(lista_libros))
    print("Autor con mas publicaciones:",autorpop)
    print("Genero mas frecuente:",generopop)

def menu_libros():
    while True:
        print("===BIBLIOTECA DIGITAL===",
            "\n1.-Registrar libros",
            "\n2.-Consultar libros",
            "\n3.-Buscar libro",
            "\n4.-Ver estadisticas",
            "\n5.-Salir")
        try:
            res=int(input("¿Que desea?"))
        except ValueError:
            print("Respuesta no valida")
        else:
            if res==1:
                try:
                    cantidad=int(input("¿Cuantos libros desea registrar?"))
                    registrar_libro(cantidad)
                except ValueError:
                    print("Respuesta no valida")
                else:
                    continue
            elif res==2:
                cantidad=len(lista_libros)
                consultar_libros(cantidad)
            elif res==3:
                busqueda=input("¿Titulo del libro que esta buscando?")
                buscar_libro(busqueda)
            elif res==4:
                cantidad=len(lista_libros)
                estadisticas(cantidad)
            elif res==5:
                break
            else:
                print("Opcion no valida")