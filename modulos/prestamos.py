
ruta_libros ="db\\Libros.txt"
ruta_clientes ="db\\Clientes.txt"

def libros_disponibles():
    print("Libros disponibles: ")
    print("")

    libros_disponibles = False

    with open(ruta_libros, 'r') as archivo_libros:
        for linea in archivo_libros:

            libro_info = linea.strip().split(',')  
            estado_libro = libro_info[3].strip()

            if estado_libro == 'Disponible':  

                libros_disponibles = True

                isbn = libro_info[0].strip()  
                titulo = libro_info[1].strip()  
                autor = libro_info[2].strip()  
                print(f"{isbn} - {titulo} - {autor}")

    if not libros_disponibles:
        print("No hay libros disponibles.")



def registro_prestamo(isbn, dni):

    dni_existe = False

    with open(ruta_clientes, 'r') as archivo:
       
        for linea in archivo:
            cliente_info = linea.strip().split(',')
            dni_db = cliente_info[0].strip()
            
            if dni_db == dni:
                dni_existe = True
                break

    if not dni_existe:
        print("El DNI ingresado no existe en la base de datos.")
        return 'ERROR'


    isbn_existe = False

    with open(ruta_libros, 'r') as archivo:

        for linea in archivo:

            libro_info = linea.strip().split(',')
            isbn_db = libro_info[0].strip()

            if isbn_db == isbn:
                isbn_existe = True
                break

    if not isbn_existe:
        print("El ISBN ingresado no existe en la base de datos.")
        return 'ERROR 404'


    with open(ruta_libros, 'r') as archivo:
        lineas = archivo.readlines()

    with open(ruta_libros, 'w') as archivo:
        for linea in lineas:
            libro_info = linea.strip().split(',')
            isbn_db = libro_info[0].strip()

            if isbn_db == isbn:
                archivo.write(f"{isbn},{libro_info[1]},{libro_info[2]},Ocupado,{dni}\n")
            else:
                archivo.write(linea)


    with open(ruta_clientes, 'r') as archivo:
        lineas = archivo.readlines()

    with open(ruta_clientes, 'w') as archivo:
        for linea in lineas:
            cliente_info = linea.strip().split(',')
            dni_db = cliente_info[0].strip()
            if dni_db == dni:
                archivo.write(f"{dni},{cliente_info[1]},{cliente_info[2]},{cliente_info[3]},{cliente_info[4]},{cliente_info[5]},{cliente_info[6]},{isbn},{cliente_info[8]}\n")
            else:
                archivo.write(linea)

    print("Préstamo registrado con éxito.")
    return ''



def devolver_libro(isbn, dni):
    
    libro_encontrado = False
    cliente_encontrado = False
    nuevos_libros = []

    with open(ruta_libros, 'r') as archivo:
        libros = archivo.readlines()

    for registro in libros:
        libro_info = registro.strip().split(',')

        if libro_info[0].strip() == str(isbn):

            if libro_info[3].strip()=='Ocupado':

                libro_encontrado = True

                libro_info[3] = "Disponible"
                libro_info[4] = "0"
                
            registro_actualizado = ','.join(libro_info)
            nuevos_libros.append(registro_actualizado + '\n')
        else:
            nuevos_libros.append(registro)

    if not libro_encontrado:
        print("El libro no se encontró o no está prestado.")
        return
    
    with open(ruta_clientes, 'r') as archivo:
        clientes = archivo.readlines()

    nuevos_clientes = []

    for cliente in clientes:

        cliente_info = cliente.strip().split(',')
        dni_db = cliente_info[0].strip()
        isbn_cliente = cliente_info[7].strip()

        if dni_db == str(dni):

            if isbn_cliente == str(isbn):
                cliente_encontrado = True
                cliente_info[7] = "NULL"

        nuevo_cliente = ','.join(cliente_info)
        nuevos_clientes.append(nuevo_cliente + '\n')

    if not cliente_encontrado:
        print("Cliente no encontrado o sin préstamo adjudicado.")
        return

    with open(ruta_libros, 'w') as archivo:
        archivo.writelines(nuevos_libros)

    with open(ruta_clientes, 'w') as archivo:
        archivo.writelines(nuevos_clientes)

    print("Libro devuelto correctamente.")
    return ''


# ------------------------------------------------------------------------- CONTROLADORES ------------------------------------------------------------------------------ #


def pedir_datos_alta_prestamo():
    flag_isbn = True
   
    while flag_isbn:
        try:
            isbn = int(input("Ingrese el ISBN del libro: "))
            flag_isbn = False
        except ValueError:
            print("El ISBN debe ser numérico")

    flag_dni = True
    while flag_dni:
        try:
            dni = int(input("Ingrese el DNI: "))
            flag_dni = False
        except ValueError:
            print("El ISBN debe ser numérico")

    print(registro_prestamo(str(isbn), str(dni)))



def pedir_datos_devolucion_prestamo():
    flag_isbn = True
   
    while flag_isbn:
        try:
            isbn = int(input("Ingrese el ISBN del libro: "))
            flag_isbn = False
        except ValueError:
            print("El ISBN debe ser numérico")

    flag_dni = True
    while flag_dni:
        try:
            dni = int(input("Ingrese el DNI: "))
            flag_dni = False
        except ValueError:
            print("El ISBN debe ser numérico")

    print(devolver_libro(isbn, dni))















