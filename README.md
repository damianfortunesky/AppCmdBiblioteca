# AppCmdBiblioteca

Aplicacion de consola en python. Trabajo Final Algoritmos IFTS24

MAIN.PY

    Este módulo contiene el programa principal que ejecuta la interacción con el usuario a través de menús y opciones. 

    Permite seleccionar diferentes acciones relacionadas con clientes, libros y préstamos.

    Función principal que ejecuta el programa y muestra los menús de opciones al usuario.  -> programa()



MODULO CLIENTES.PY

    Este módulo proporciona funciones para gestionar clientes en un sistema. Permite realizar altas, bajas, consultas de estado y modificaciones de datos de clientes.

    Funciones que manejan el modelo de datos
    
    
        Registra un nuevo cliente en el sistema.            -> alta_cliente(dni, nombre, apellido, telefono, direccion)

        Da de baja a un cliente existente en el sistema.    -> baja_cliente(dni)
   
        Da de baja a un cliente existente en el sistema.    -> consultar_estado_cliente(dni)


    Funciones que manejan las solicitudes

        Solicita al usuario los datos necesarios y realiza el alta de un cliente llamando a la función alta_cliente().  -> pedir_datos_alta_cliente()

        Solicita al usuario el DNI del cliente a dar de baja y llama a la función baja_cliente().                       -> pedir_datos_baja_cliente()

        Consultar y llama a la función consultar_estado_cliente(). Muestra el estado del cliente en la salida.          -> pedir_datos_consulta_estado_cliente()

        Modifica los datos del cliente. Llama a la función modificar_datos_cliente()                                    -> pedir_datos_modificacion_cliente()


MODULO LIBROS.PY
    
    Este módulo proporciona funciones para gestionar libros en un sistema. Permite buscar libros, dar de alta, dar de baja, modificar y consultar libros.

    Funciones que manejan el modelo de datos:

        Busca un libro en el sistema mediante su ISBN.                      -> buscar_libro(isbn)
    
        Da de alta un nuevo libro en el sistema.                            -> alta_libro(isbn, titulo, autor, estado="L", DNI=0)

        Da de baja un libro existente en el sistema.                        -> baja_libro(isbn)
    
        Modifica un campo específico de un libro existente en el sistema.   -> modificar_libro(isbn, campo, valor)


    Funciones que manejan las solicitudes:

        Muestra en pantalla la lista de libros disponibles para préstamo en el sistema. -> libros_disponibles()

        Registra un préstamo de libro en el sistema.                                    -> registro_prestamo(isbn, dni)

        Registra la devolución de un libro prestado en el sistema.                      -> devolver_libro(isbn, dni)




MODULO PRESTAMOS.PY

    Este módulo proporciona funciones para gestionar préstamos de libros en un sistema. 

    Funciones que manejan el modelo de datos:
    
        Registra un préstamo de libro en el sistema.                ->  registro_prestamo(isbn, dni)
    
        Registra la devolución de un libro prestado en el sistema.  -> devolver_libro(isbn, dni)
    

    Funciones que manejan las solicitudes:

        Solicita al usuario el ISBN del libro y el DNI del cliente para registrar un nuevo préstamo.                -> pedir_datos_alta_prestamo()

        Solicita al usuario el ISBN del libro y el DNI del cliente para registrar la devolución de un préstamo.     -> pedir_datos_devolucion_prestamo()



DB

    La base de datos esta simulada con archivos Clientes.txt y Libros.txt en el modulo db. La gestion de prestamos interactua con los registros de ambos archivos.