lista_libros=[]
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
def eliminar_libro(eliminacion):
    for i in range(len(lista_libros)):
        if lista_libros[i][0]["Titulo"]==eliminacion.upper():
            lista_libros.pop(i)
            print("Libro eliminado")
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
while True:
    print("===BIBLIOTECA DIGITAL===",
          "\n1.-Registrar libros",
          "\n2.-Consultar libros",
          "\n3.-Buscar libro",
          "\n4.-Eliminar libro",
          "\n5.-Ver estadisticas",
          "\n6.-Salir")
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
            eliminacion=input("¿Titulo del libro que desea eliminar?")
            eliminar_libro(eliminacion)
        elif res==5:
            cantidad=len(lista_libros)
            estadisticas(cantidad)
        elif res==6:
            break
        else:
            print("Opcion no valida")