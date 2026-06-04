productos = {}


def agregar_producto(productos):
    while True:
        nombre = input("Ingrese nombre del producto: ").strip()

        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
        elif nombre in productos:
            print("Error: el producto ya existe.")
        else:
            break

    while True:
        stock = input("Ingrese stock: ")

        if stock.isdigit():
            stock = int(stock)
            break
        else:
            print("Error: ingrese un número entero mayor o igual a 0.")

    while True:
        precio = input("Ingrese precio: ")

        try:
            precio = float(precio)

            if precio > 0:
                break
            else:
                print("Error: el precio debe ser mayor que 0.")
        except:
            print("Error: ingrese un número válido.")

    productos[nombre] = [stock, precio]
    print("Producto agregado correctamente.")


def mostrar_productos(productos):
    if len(productos) == 0:
        print("No existen productos registrados.")
        return

    print("\n--- LISTA DE PRODUCTOS ---")

    for nombre, datos in productos.items():
        print(f"Producto: {nombre}")
        print(f"Stock: {datos[0]}")
        print(f"Precio: ${datos[1]}")
        print("-------------------------")


def buscar_producto(productos):
    if len(productos) == 0:
        print("No existen productos registrados.")
        return

    nombre = input("Ingrese nombre del producto a buscar: ").strip()

    if nombre in productos:
        print("Producto encontrado.")
        print(f"Stock: {productos[nombre][0]}")
        print(f"Precio: ${productos[nombre][1]}")
    else:
        print("El producto no existe.")


def producto_mas_caro(productos):
    if len(productos) == 0:
        print("No existen productos registrados.")
        return

    nombre_caro = ""
    precio_mayor = 0

    for nombre, datos in productos.items():
        if datos[1] > precio_mayor:
            precio_mayor = datos[1]
            nombre_caro = nombre

    print("\nProducto más caro:")
    print(f"Nombre: {nombre_caro}")
    print(f"Precio: ${precio_mayor}")


while True:
    print("\n===== MENÚ =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Producto más caro")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion.isdigit():
        opcion = int(opcion)

        if opcion >= 1 and opcion <= 5:

            if opcion == 1:
                agregar_producto(productos)

            elif opcion == 2:
                mostrar_productos(productos)

            elif opcion == 3:
                buscar_producto(productos)

            elif opcion == 4:
                producto_mas_caro(productos)

            elif opcion == 5:
                print("Programa finalizado.")
                break

        else:
            print("Error: la opción debe estar entre 1 y 5.")
    else:
        print("Error: ingrese un número válido.")