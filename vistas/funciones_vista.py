import os

# ------------------------------------------------------------------- ALERTAS  DE LAS VISTAS ------------------------------------------------------------------- #

def mostrar_menu_principal():
    print("                            ")
    print("╔══════════════════════════╗")
    print("║       Bienvenido a       ║")
    print("║    Biblioteca IFTS24     ║")
    print("╠═════════════════════════ ╣")
    print("║ 1. Gestion Clientes      ║")
    print("║ 2. Gestion Libros        ║")
    print("║ 3. Gestion Prestamos     ║")
    print("║ 4. Salir                 ║")
    print("╚══════════════════════════╝")
    print("                            ")

def submenu_clientes():
    print("                                       ") 
    print("╔═════════════════════════════════════╗")
    print("║           Gestion Clientes          ║")
    print("╠═════════════════════════════════════╣")
    print("║ 1. Alta Cliente                     ║")
    print("║ 2. Baja Cliente                     ║")
    print("║ 3. Consultar estado del cliente     ║")
    print("║ 4. Actualizar Datos                 ║")
    print("║ 5. Volver al Menu Principal         ║")
    print("╚═════════════════════════════════════╝")
    print("                                       ")

def submenu_libros():
    print("                                       ") 
    print("╔═════════════════════════════════════╗")
    print("║           Gestion Libros            ║")
    print("╠═════════════════════════════════════╣")
    print("║ 1. Alta libros                      ║")
    print("║ 2. Baja libro                       ║")
    print("║ 3. Modificar libro                  ║")
    print("║ 4. Consultar disponibilidad         ║")
    print("║ 5. Volver al Menu Principal         ║")
    print("╚═════════════════════════════════════╝")
    print("                                       ")


def submenu_prestamos():
    print("                                       ") 
    print("╔═════════════════════════════════════╗")
    print("║           Gestion Prestamos         ║")
    print("╠═════════════════════════════════════╣")
    print("║ 1. Consultar disponibilidad libros  ║")
    print("║ 2. Registrar alta prestamo          ║")
    print("║ 3. Registrar devolucion             ║")
    print("║ 4. Volver al Menu Principal         ║")
    print("╚═════════════════════════════════════╝")
    print("                                       ")

def mostrar_mensaje_error():
    print("                                        ")
    print("╔══════════════════════════════════════╗")
    print("║      Error al ingresar dato          ║")
    print("╠══════════════════════════════════════╣")
    print("║ Debe ingresar un Nº de opción válido ║")
    print("╚══════════════════════════════════════╝")
    print("                                        ")

def mensaje_dato_no_encontrado():
    print("                                        ")
    print("╔══════════════════════════════════════╗")
    print("║           Error de busqueda          ║")
    print("╠══════════════════════════════════════╣")
    print("║         Esa opcion no existe         ║")
    print("╚══════════════════════════════════════╝")
    print("                                        ")

def Salir():
    print("                                        ")
    print("╔══════════════════════════════════════╗")
    print("║                Adios                 ║")
    print("╠══════════════════════════════════════╣")
    print("║            Vuelva Pronto!            ║")
    print("╚══════════════════════════════════════╝")
    print("                                        ")

def limpiar_consola():
    # Diferentes comandos para limpiar la consola en distintos sistemas operativos
    comandos_limpiar = {
        'posix': 'clear',  # Linux y macOS
        'nt': 'cls'  # Windows
    }

    # Obtener el comando correspondiente al sistema operativo actual
    comando = comandos_limpiar.get(os.name)

    # Si no se encuentra el comando correspondiente, se imprime un mensaje
    if comando is None:
        print("No se pudo limpiar la consola. Por favor, borra manualmente.")

    # Ejecutar el comando para limpiar la consola
    os.system(comando)
