from libros import lista_libros
lista_reseñas = []
def registrar_reseña():
    reseña=input("¿Cuál es tu opinion sobre este libro? \n")
    lista_reseñas.append(reseña)
def imprimir_reseñas():
    for i in lista_reseñas:
        print(lista_reseñas[i])