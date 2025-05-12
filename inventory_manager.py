
inventory_products = {}

# Función para agregar productos
def add_product(product_name, product_price, product_quantity):
    inventory_products[product_name] = {
        "price": product_price,
        "quantity": product_quantity
    }

# Función para buscar productos
def search_product(product_name):
    if product_name in inventory_products:
        product = inventory_products[product_name]
        print(f"Name: {product_name}, Price: ${product['price']}, Quantity: {product['quantity']}")
    else:
        print("<----¡Error!: Este producto no existe en el inventario.---->")

# Función para actualizar precios
def update_product_price(product_name, new_price):
    if product_name in inventory_products:
        if new_price > 0:
            inventory_products[product_name]["price"] = new_price
            print("<---- ¡El precio del producto ha sido actualizado con éxito! ---->")
        else:
            print("<----¡Error!: El precio del producto debe ser positivo---->")
    else:
        print("<----¡Error!: El producto que desea actualizar no existe en el inventario--->")

# Función para eliminar productos
def delete_product(product_name):
    if product_name in inventory_products:
        del inventory_products[product_name]
        print("<----¡El producto ha sido eliminado con éxito!---->")
    else:
        print("<----Warning: El producto que desea eliminar no existe en el inventario.---->")

# Función para calcular el valor total del inventario
def calculate_total_inventory_value():
    total_value = 0
    for product in inventory_products.values():
        total_value += product["price"] * product["quantity"]
    print(f"Total inventory value: ${total_value:.2f}")

# Agrega productos iniciales
add_product("Apple", 2.500, 500)
add_product("Banana", 1.000, 190)
add_product("Orange", 1.200, 100)
add_product("Milk", 4.500, 90)
add_product("Bread", 3.000, 380)

# Función para mostrar el menú
def show_menu():
    print("""
<----- Welcome -----> 
1. Agregar producto
2. Buscar producto
3. Actualizar precio
4. Eliminar producto
5. Calcular valor total del inventario
6. Salir
""")

# Bucle principal
while True:
    show_menu()
    option = input("<---- Por favor ingrese una opción ---->: ")

    if option == "1":
        name = input("<---- Ingrese el nombre del producto ---->: ")
        try:
            price = float(input("<---- Ingrese el precio del producto ---->: "))
            quantity = int(input("<---- Ingrese la cantidad de productos ---->: "))
            add_product(name, price, quantity)
            print("<---- Producto agregado exitosamente ---->")
        except ValueError:
            print("<---- Por favor ingrese datos válidos ---->")

    elif option == "2":
        name = input("<---- Ingrese el nombre del producto a buscar ---->: ")
        search_product(name)

    elif option == "3":
        name = input("<---- Ingrese el nombre del producto a actualizar ---->: ")
        try:
            new_price = float(input("<---- Ingrese el nuevo precio ---->: "))
            update_product_price(name, new_price)
        except ValueError:
            print("<---- Por favor ingrese un precio válido ---->")

    elif option == "4":
        name = input("<---- Ingrese el nombre del producto a eliminar ---->: ")
        delete_product(name)

    elif option == "5":
        calculate_total_inventory_value()

    elif option == "6":
        print("<---- Gracias por usar el programa ---->")
        break

    else:
        print("<---- Opción no válida, intente nuevamente ---->")
