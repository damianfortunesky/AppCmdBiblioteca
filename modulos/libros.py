ruta_libros = "db/Libros.txt"


def buscar_libro(isbn):
    with open(ruta_libros, "r+") as archivo:
        libros = archivo.readlines()
        for index , libro in enumerate(libros):

            campos = libro.split(",")
            libro_ISBN = campos[0].strip().rstrip('\n')

            if libro_ISBN == str(isbn):
                return [campos[0], campos[1], campos[2], campos[3], campos[4].strip().rstrip('\n')]
    return []
            

def alta_libro(isbn, titulo, autor, estado="Disponible", DNI=0):
    resultado = buscar_libro(isbn)

    if not resultado:

        with open(ruta_libros, 'a') as libros:
            libros.write(
                f"{isbn},{titulo},{autor},{estado},{DNI}\n"
            )
            
        print(f'El libro: "{titulo}" del autor "{autor}" se agregado con exito')
    else:
        print(f"Ya existe un libro con el ISBN: {resultado[0]} ")

    return ''



def baja_libro(isbn):
    with open(ruta_libros, "r") as archivo:
        libros = archivo.readlines()

    libro_encontrado = False
    isbn_econtrado = False

    for indice, libro in enumerate(libros):

        datos = libro.strip().split(",")

        if datos[0] == str(isbn):

            estado = datos[3]
            isbn_econtrado = True

            if estado != "Ocupado":

                del libros[indice]
                libro_encontrado = True                            
                break

    if libro_encontrado:
        with open(ruta_libros, "w") as archivo:
            archivo.writelines(libros)
        
        print("Se borró el libro exitosamente.")
    else:
        if isbn_econtrado:
            print(f"El libro se encuentra ocupado. No se puede eliminar.")
        else:
            print(f"No se encontró ningún libro con ISBN {isbn}. No se puede eliminar.")
            


def modificar_libro(isbn, nombre, autor):
     
    with open(ruta_libros, "r+") as archivo:
        libros = archivo.readlines()

        for indice, libro in enumerate(libros):
            campos = libro.strip().split(',')

            if int(campos[0]) == isbn:
                if campos[3].strip() != "Ocupado":
                    campos[1] = nombre
                    campos[2] = autor

                    libros[indice] = ','.join(campos)

                    archivo.seek(0)
                    archivo.writelines(libros)
                    archivo.truncate()

                    print("Se modificaron los datos exitosamente")
                    return 'OK'
                else:
                    print("El libro está marcado como Ocupado, no se puede modificar")
                    return 'ERROR'

        print(f"No se encontró ningún libro con ISBN {isbn}, no se pudo modificar")
        return ''

def consultar_libro(isbn):
    resultado = buscar_libro(str(isbn))
   
    if resultado:
        print(f"El libro buscado es {resultado[1]} del autor {resultado[2]} y se encuentra {resultado[3]} por el cliente con dni {resultado[4]}.")
    return ''



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
    
    nombre = input("Ingrese el nuevo nombre: ")
    autor = input("Ingrese el nuevo autor: ")
     
    # Llamar a la función con los datos ingresados
    print(modificar_libro(isbn, nombre, autor))



def pedir_datos_consulta_libro():
        flag_dni = True
        
        while flag_dni:
            try:
                isbn = int(input("Ingrese el ISBN del libro: "))
                flag_dni = False
            except ValueError:
                print("El ISBN  debe ser numérico")

        print(consultar_libro(str(isbn)))

        return ''
