import time

# Modulos importados
from modulos.clientes import *
from modulos.prestamos import *
from modulos.libros  import *
from vistas.funciones_vista  import * 

# ---------------------------------------------------------------------------- PROGRAMA PRINCIPAL ------------------------------------------------------------------------ #

def programa():
    estado_menu_principal = True

    while estado_menu_principal:
        
        if estado_menu_principal:
            mostrar_menu_principal()        
        try:
            opcion = int(input("Elige el numero de opción deseada: "))
            estado_menu_principal = False
        except ValueError:
            mostrar_mensaje_error()
            continue

        if opcion == 1:
            estado_submenu_clientes = True

            while estado_submenu_clientes:
                limpiar_consola()
                submenu_clientes()

                try:                    
                    opcion_submenu_clientes = int(input("Elige el número de opción deseada: "))
                    estado_submenu_clientes = False 
                except ValueError:
                    mostrar_mensaje_error()
                    continue
                
                if opcion_submenu_clientes == 1:

                    limpiar_consola()
                    pedir_datos_alta_cliente()
                    time.sleep(3.5)                                                        
                    estado_submenu_clientes = True

                elif opcion_submenu_clientes == 2:

                    limpiar_consola()
                    pedir_datos_baja_cliente()
                    time.sleep(3.5)      
                    estado_submenu_clientes = True

                elif opcion_submenu_clientes == 3:

                    limpiar_consola()
                    pedir_datos_consulta_estado_cliente()
                    time.sleep(3.5)                                   
                    estado_submenu_clientes = True

                elif opcion_submenu_clientes == 4:

                    limpiar_consola()
                    pedir_datos_modificacion_cliente()
                    time.sleep(3.5)       
                    estado_submenu_clientes = True

                elif opcion_submenu_clientes == 5:

                    estado_submenu_clientes = False
                    limpiar_consola()
                    estado_menu_principal = True

                else:
                    print("Opción inválida. Por favor, elige una opción válida.")
        elif opcion == 2:
            
            estado_submenu_libros = True

            while estado_submenu_libros:
                limpiar_consola()
                submenu_libros()

                try:
                    opcion_submenu_libros = int(input("Elige el número de opción deseada: "))
                    estado_submenu_libros = False 
                except ValueError:
                    mostrar_mensaje_error()
                    continue
                
                if opcion_submenu_libros == 1:

                    limpiar_consola()
                    pedir_datos_alta_libro()

                    time.sleep(3.5)                                                     
                    estado_submenu_libros = True

                elif opcion_submenu_libros == 2:

                    limpiar_consola()
                    pedir_datos_baja_libro()
                    
                    time.sleep(3.5)      
                    estado_submenu_libros = True

                elif opcion_submenu_libros == 3:

                    limpiar_consola()
                    pedir_datos_modificacion_libro()
                    
                    time.sleep(3.5)                                   
                    estado_submenu_libros = True
                
                elif opcion_submenu_libros == 4:

                    limpiar_consola()

                    pedir_datos_consulta_libro()
                    
                    time.sleep(3.5)                                   
                    estado_submenu_libros = True

                elif opcion_submenu_libros == 5:

                    estado_submenu_libros = False
                    limpiar_consola()
                    estado_menu_principal = True

                else:
                    print("Opción inválida. Por favor, elige una opción válida.")

        elif opcion == 3:

                    estado_submenu_prestamos = True

                    while estado_submenu_prestamos:
                        limpiar_consola()
                        submenu_prestamos()

                        try:
                            opcion_submenu_prestamos = int(input("Elige el número de opción deseada: "))
                            estado_submenu_prestamos = False 
                        except ValueError:
                            mostrar_mensaje_error()
                            continue
                            
                        
                        if opcion_submenu_prestamos == 1:

                            limpiar_consola()

                            libros_disponibles()

                            time.sleep(5)                                                     
                            estado_submenu_prestamos = True

                        elif opcion_submenu_prestamos == 2:

                            limpiar_consola()
                            pedir_datos_alta_prestamo()
                            
                            time.sleep(3.5)      
                            estado_submenu_prestamos = True

                        elif opcion_submenu_prestamos == 3:

                            limpiar_consola()
                            
                            pedir_datos_devolucion_prestamo()
                            
                            time.sleep(3.5)                                   
                            estado_submenu_prestamos = True
                        
                        elif opcion_submenu_prestamos == 4:

                            estado_submenu_prestamos = False
                            limpiar_consola()
                            estado_menu_principal = True

                        else:
                            print("Opción inválida. Por favor, elige una opción válida.")
        elif opcion == 4:
            Salir()
            time.sleep(3.5)  
            limpiar_consola()
            estado_menu_principal = False
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

programa()
