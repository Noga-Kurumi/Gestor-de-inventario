import functions as fn
import os
import re
from colorama import Fore

number_valid = r"^[0-9]+$"

os.system("cls")
    
while True:
    print("Menú principal del gestor de inventario " + Fore.BLUE + "Noga Cuck Grooming:\n" + Fore.WHITE)
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Modificar producto")
    print("4. Mostrar productos")
    print("5. Registrar entrada")
    print("6. Registrar salida")
    print("7. Generar reporte de stock bajo")
    print("8. Generar historial de movimientos")
    
    option = input("\nPor favor, seleccione una opcion: ")
    if re.match(number_valid, option): #verificar si se ingreso un numero
        os.system("cls")
        option = int(option)
        if option == 1:
            fn.add_product()
        elif option == 2:
            fn.delete_product()
        elif option == 3:
            fn.modify_product()
        elif option == 4:
            fn.show_products()
        elif option == 5:
            fn.register_entry()
        elif option == 6:
            fn.register_exit()
        elif option == 7:
            fn.generate_low_stock_report()
        elif option == 8:
            fn.generate_movement_history()
        else:
            fn.show_error("Porfavor, seleccione una opciona valida!\n")
    else:
        os.system("cls")
        fn.show_error("Ingrese un numero!\n")