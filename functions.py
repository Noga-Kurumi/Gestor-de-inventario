import classesInventory as ci
import os
import re
from colorama import Fore
import datetime as dt

name_regex = r"^[\w\sáéíóúÁÉÍÓÚüÜñÑ.,:;-]+$"  # Validar nombre (letras, espacios y acentos)
price_regex = r"\d+(\.\d{1,2})?" # Validar precio (solo números enteros o decimales)
description_regex = r".*"  # Validar descripción (cualquier caracter)
stock_regex = r"^[0-9]+$"  # Validar stock (solo números enteros)
date_regex = r"^(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[0-2])\/(19\d\d|20\d\d)$" # Validar fechas (DD/MM/AAAA)

products = []
movements = []

def show_error(error):
    print(Fore.RED + error + Fore.WHITE)

def show_success(string):
    print(Fore.GREEN + string + Fore.WHITE)

def show_warning(war):
    print(Fore.YELLOW + war + Fore.WHITE)

def add_product():
    while True:
        name = input(" - AGREGAR PRODUCTO -\n\nIngrese el nombre del producto: ")
        if re.match(name_regex, name):
            os.system("cls")
            break
        else:
            os.system("cls")
            show_error("Porfavor, ingrese un nombre valido!\n")

    while True:
        show_warning(f"Nombre: {name}\n")
        price = input("Ingrese el precio del producto: $")
        if re.match(price_regex, price):
            os.system("cls")
            break
        else:
            os.system("cls")
            show_error("Porfavor, ingrese un precio valido! Ejemplo: $4.99\n")

    while True:
        show_warning(f"Nombre: {name}\n")
        show_warning(f"Precio: {price}\n")
        description = input("Ingrese una descripcion del producto: ")
        if re.match(description_regex, description):
            os.system("cls")
            break
        else:
            os.system("cls")
            show_error("Porfavor, ingrese una descripcion valida!\n")

    while True:
        show_warning(f"Nombre: {name}\n")
        show_warning(f"Precio: ${price}\n")
        show_warning(f"Descripcion: {description}\n")
        stock = input("Ingrese la cantidad de stock entrante: ")
        if re.match(stock_regex, stock):
            os.system("cls")
            break
        else:
            os.system("cls")
            show_error("Porfavor, ingrese una cantidad valida!\n")
    
    new_product = ci.Product(name, price, description, stock) #instanciar un nuevo producto con los datos ingresados
    products.append(new_product) #guardar instancia en la lista de productos
    date = dt.datetime.now()
    movements.append({"Producto":name, "Cantidad":stock, "Fecha":date, "Direccion":"entra"})
    os.system("cls")
    show_success(" - NUEVO PRODUCTO AGREGADO -\n")

def show_products():
    if len(products) > 0:
        for i in products:
            print(f"{i}\n") 
    else:
        show_error("No existen productos para mostrar.\n")
    
    return products

def delete_product():
    if len(products) > 0:
        while True:
            print(" - ELIMINAR PRODUCTO -\n")
            for n, i in enumerate(products):
                print(f"{n}. {i.name}\n")

            option = input("Seleccione en producto que desea eliminar: ")
            if re.match(stock_regex, option):
                option = int(option)
                try:
                    del products[option]
                    os.system("cls")
                    show_success("- PRODUCTO ELIMINADO -\n")
                    break
                except:
                    os.system("cls")
                    show_error("El producto seleccionado no existe!\n")
            else:
                os.system("cls")
                show_error("Porfavor, ingrese un numero valido!\n")
    else:
        show_error("No existen productos para eliminar.\n")

def modify_product():
    if len(products) > 0:
        while True:
            print(" - MODIFICAR PRODUCTO -\n")
            for n, i in enumerate(products):
                print(f"{n}. {i.name}\n")

            option = input("Seleccione en producto que desea modificar: ")
            if re.match(stock_regex, option):
                option = int(option)
                if option >= 0 and option < len(products):
                    
                    os.system("cls")
                    while True:
                        product = products[option]
                        parameters = [product.name, "$" + product.price, product.description, product.stock + "u"]
                        print("1. Nombre | " + Fore.YELLOW + f"Actual: {product.name}" + Fore.WHITE)
                        print("2. Precio | " + Fore.YELLOW + f"Actual: ${product.price}" + Fore.WHITE)
                        print("3. Descripcion | " + Fore.YELLOW + f"Actual: {product.description}" + Fore.WHITE)
                        print("4. Stock | " + Fore.YELLOW + f"Actual: {product.stock}u" + Fore.WHITE)
                        field = input("\nIndique el campo que desea modificar: ")
                        if re.match(stock_regex, field):
                            field = int(field)
                            if field >= 1 and field < 5 :
                                os.system("cls")
                                while True:
                                    fields = ["nombre", "precio", "descripcion", "stock"]
                                    show_warning(f"Modificando {fields[field -1]}...\nIndique el nuevo valor:\n\n")
                                    new_value = input("Valor actual: " + Fore.RED + f"{parameters[field-1]}" + Fore.WHITE + " ==> Nuevo valor: " + Fore.GREEN)
                                    result = modify_class(option, field, new_value)
                                    if result:
                                        os.system("cls")
                                        show_success(" - PRODUCTO MODIFICADO -\n")
                                        break
                                    else:
                                        os.system("cls")
                                        show_error("El nuevo valor es invalido, intente de nuevo!\n")
                                break
                            else:
                                os.system("cls")
                                show_error("Porfavor, seleccione un campo valido!\n")
                        else:
                            os.system("cls")
                            show_error("Porfavor, ingrese un numero valido!\n")
                    break
                else:
                    os.system("cls")
                    show_error("El producto seleccionado no existe!\n")
            else:
                os.system("cls")
                show_error("Porfavor, ingrese un numero valido!\n")
    else:
        show_error("No existen productos para modificar.\n")

def modify_class(option, field, newValue):
    product = products[option]
    if field == 1:
        if re.match(name_regex, newValue):
            product.name = newValue
            return True
        else:
            return False
    elif field == 2:
        if re.match(price_regex, newValue):
            product.price = newValue
            return True
        else:
            return False
    elif field == 3:
        if re.match(description_regex, newValue):
            product.description = newValue
            return True
        else:
            return False
    else:
        if re.match(stock_regex, newValue):
            product.stock = newValue
            return True
        else:
            return False

def register_entry():
    if len(products) > 0:
        while True:
            print(" - REGISTRAR ENTRADA -\n")
            for n, i in enumerate(products):
                print(f"{n}. {i.name}\n")

            option = input("Porfavor, seleccione el producto a registar entradas: ")
            if re.match(stock_regex, option):
                option = int(option)
                if option >= 0 and option < len(products):
                    os.system("cls")
                    
                    while True:
                        entry = input("Ingrese la cantidad de producto que entra: ")
                        if re.match(stock_regex, entry):
                            os.system("cls")
                            
                            while True:
                                date = input("Ingrese la fecha de la entrada DD/MM/AAAA: ")
                                if re.match(date_regex, date):
                                    date = dt.datetime.strptime(date, "%d/%m/%Y")
                                    product = products[option]
                                    movements.append({"Producto":product.name, "Cantidad":entry, "Fecha":date, "Direccion":"entra"})
                                    product.stock = int(product.stock) + int(entry)
                                    os.system("cls")
                                    show_success(" - ENTRADA REGISTRADA -\n")
                                    break
                                else:
                                    os.system("cls")
                                    show_error("Ingrese una valida! Ejemplo: 16/03/2004\n")
                            break
                        else:
                            os.system("cls")
                            show_error("Ingrese un valor numerico!\n")
                    break
                else:
                    os.system("cls")
                    show_error("El producto seleccionado no existe!\n")
            else:
                os.system("cls")
                show_error("Porfavor, ingrese un numero valido!\n")
    else:
        show_error("No existen productos para registrar entradas.\n")

def register_exit():
    if len(products) > 0:
        while True:
            print(" - REGISTRAR SALIDA -\n")
            for n, i in enumerate(products):
                print(f"{n}. {i.name}\n")

            option = input("Porfavor, seleccione el producto a registar salidas: ")
            if re.match(stock_regex, option):
                option = int(option)
                if option >= 0 and option < len(products):
                    os.system("cls")
                    
                    while True:
                        product = products[option]
                        entry = input(f"Cantidad actual de {product.name}: {product.stock}u\nIngrese la cantidad de producto que sale: ")
                        if re.match(stock_regex, entry):
                            entry = int(entry)
                            os.system("cls")
                            if entry <= int(product.stock):
                                while True:
                                    date = input("Ingrese la fecha de la salida DD/MM/AAAA: ")
                                    if re.match(date_regex, date):
                                        date = dt.datetime.strptime(date, "%d/%m/%Y")
                                        movements.append({"Producto":product.name, "Cantidad":entry, "Fecha":date, "Direccion":"sale"})
                                        product.stock = int(product.stock) - int(entry)
                                        os.system("cls")
                                        show_success(" - SALIDA REGISTRADA -\n")
                                        break
                                    else:
                                        os.system("cls")
                                        show_error("Ingrese una valida! Ejemplo: 16/03/2004\n")
                                break
                            else:
                                os.system("cls")
                                show_warning("La salida especificada es mayor a la cantidad de stock actual!\n")
                        else:
                            os.system("cls")
                            show_error("Ingrese un valor numerico!\n")
                    break
                else:
                    os.system("cls")
                    show_error("El producto seleccionado no existe!\n")
            else:
                os.system("cls")
                show_error("Porfavor, ingrese un numero valido!\n")
    else:
        show_error("No existen productos para registrar salidas.\n")

def generate_low_stock_report():
    if len(products) > 0:
        show_warning("Los siguientes productos tienen bajo stock:\n")
        for n, i in enumerate(products):
            if int(i.stock) <= 10:
                print(f"{n}. {i.name} - {i.stock}u\n")
    else:
        show_error("No existen productos para reportar.\n")

def generate_movement_history():
    if len(products) > 0:
        print("- HISTORIAL DE MOVIMIENTOS -\n")
        movementsSorted = sorted(movements, key=lambda x: x["Fecha"])
        for i in movementsSorted:
            formated_date = dt.date.strftime(i["Fecha"], "%d/%m/%Y")
            if i["Direccion"] == "entra":
                show_success(f"ENTRA: {i["Producto"]} x{i["Cantidad"]} | {formated_date}\n")
            else:
                show_error(f"SALE: {i["Producto"]} x{i["Cantidad"]} | {formated_date}\n")
    else:
        show_error("No existen productos para generar un historial.\n")