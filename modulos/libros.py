ruta_libros ="db\\Libros.txt"

def buscar_libro(isbn):
    with open(ruta_libros, "r+") as archivo:
        libros = archivo.readlines()
        for i, libro in enumerate(libros):
            indice_inicio_ISBN = libro.index("ISBN:") + len("ISBN: ")
            indice_final_ISBN = libro.index(" |", indice_inicio_ISBN)
            libro_ISBN = libro[indice_inicio_ISBN:indice_final_ISBN].strip()
            if libro_ISBN == isbn:
                return libro, i


def alta_libro(isbn, titulo, autor, estado="L", DNI=0):
    resultado = buscar_libro(isbn)
    if not resultado:
        with open(ruta_libros, 'a') as libros:
            libros.write(
                f"ISBN: {isbn} | Titulo: {titulo} | Autor: {autor} | Estado: {estado} | DNI: {DNI}\n")
        print(f"libro isbn: {isbn} | Titulo: {titulo} | Autor: {autor} | Estado: {estado} | DNI: {DNI} agregado con exito")
    else:
        print(f"ya existe un libro con ese ISBN: {resultado[0]} ")

    return 'OK'



def baja_libro(isbn):
    resultado = buscar_libro(isbn)
    if resultado:
        indice = resultado[1]
        with open(ruta_libros, "r+") as archivo:
            libros = archivo.readlines()
            del libros[indice]
            archivo.seek(0)
            archivo.writelines(libros)
            archivo.truncate()

            print("Se borro el archivo exitosamente")
    else:
        print(f" No se encontro ningun libro con ISBN {isbn}, no se puede eliminar ")

def modificar_libro(isbn, campo, valor):
    resultado = buscar_libro(str(isbn))
    if resultado:
        with open(ruta_libros, "r+") as archivo:
            libros = archivo.readlines()
            libro, indice = resultado

            indice_inicio_campo = libro.index(f"{campo}:") + len(f"{campo}: ")
            indice_final_campo = libro.index(" |", indice_inicio_campo)

            libro_campo = libro[indice_inicio_campo:indice_final_campo]
            libro_modificado = libro.replace(libro_campo, valor)

            libros[indice] = libro_modificado
            archivo.seek(0)
            archivo.writelines(libros)
            archivo.truncate()

            print(f"Se modificaron datos exitosamente")
    else:
        print(f" No se encontro ningun libro con ISBN {isbn}, no se pudo modificar ")

    return 'OK'
    


def consultar_libro(isbn):
    resultado = buscar_libro(str(isbn))
    if resultado:
        libro = resultado[0]  # Suponiendo que el resultado está en la posición 0 de la tupla
        libro = libro.rstrip('\n')
        print(f"El libro buscado es {libro}")
    return 'OK'



# -------------------------------------------- FUNCIONES QUE MANEJAN LAS SOLICITUDES DE LOS USUARIOS, LOS CONTROLADORES -------------------------------------------- #

def pedir_datos_alta_libro(): 
    
    flag_isbn = True

    while flag_isbn:
        try:
            isbn = int(input("Ingrese el ISBN: "))
            flag_isbn = False
        except ValueError:
            print("El ISBN debe ser numérico")
    
    titulo =  input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")

    alta_libro(isbn, titulo, autor)



def pedir_datos_baja_libro():
    flag_isbn = True

    while flag_isbn:
        try:
            isbn = int(input("Ingrese el ISBN: "))
            flag_isbn = False
        except ValueError:
            print("El ISBN debe ser numérico")

    # Llamar a la función con los datos ingresados
    baja_libro(str(isbn))



def pedir_datos_modificacion_libro():
    flag_isbn = True

    while flag_isbn:
        try:
            isbn = int(input("Ingrese el ISBN: "))
            flag_isbn = False
        except ValueError:
            print("El ISBN debe ser numérico")
    
    campo = input("Ingrese el campo a modificar ('Titulo' o 'Autor'): ")
    valor = input("Ingrese el valor del nuevo campo elegido: ")
     
    # Llamar a la función con los datos ingresados
    print(modificar_libro(isbn, campo, valor))



def pedir_datos_consulta_libro():
        flag_dni = True
        
        while flag_dni:
            try:
                isbn = int(input("Ingrese el ISBN del libro: "))
                flag_dni = False
            except ValueError:
                print("El ISBN  debe ser numérico")

        print(consultar_libro(str(isbn)))

        return 'OK'
