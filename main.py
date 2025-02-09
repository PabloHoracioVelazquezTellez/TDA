from administrador import Producto
inventario = []

def agregar_producto():
    nombre = input("Nombre del producto: ")
    sku = input("SKU: ")
    fecha_caducidad = input("Fecha de caducidad (YYYY-MM-DD): ")
    proveedor = input("Proveedor: ")
    conteo = int(input("Cantidad en inventario: "))
    producto = Producto(nombre, sku, fecha_caducidad, proveedor, conteo)
    inventario.append(producto)
    print("Producto agregado correctamente.")

def mostrar_productos():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("\nLista de productos en inventario:")
        for i, producto in enumerate(inventario):
            print(f"{i + 1}. {producto.get_nombre()} | SKU: {producto.get_sku()} | Inventario: {producto.get_conteo_inventario()}")

def actualizar_inventario():
    mostrar_productos()
    if inventario:
        index = int(input("Seleccione el número del producto a actualizar: ")) - 1
        if 0 <= index < len(inventario):
            cantidad = int(input("Cantidad a agregar: "))
            inventario[index].agregar_inventario(cantidad)
            print("Inventario actualizado.")
        else:
            print("Selección no válida.")

def verificar_inventario():
    limite = int(input("Ingrese el límite de inventario para alertas: "))
    for producto in inventario:
        producto.verificar_inventario(limite)

def eliminar_producto():
    mostrar_productos()
    if inventario:
        index = int(input("Seleccione el número del producto a eliminar: ")) - 1
        if 0 <= index < len(inventario):
            inventario.pop(index)
            print("Producto eliminado.")
        else:
            print("Selección no válida.")
#PLANTEAR LO ANTERIOR EN OTRA CLASE PARA MEJORAR LA ESTRUCTURACION


while True:
    print("\n--- MENÚ INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Actualizar inventario")
    print("4. Verificar inventario")
    print("5. Eliminar producto")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        actualizar_inventario()
    elif opcion == "4":
        verificar_inventario()
    elif opcion == "5":
        eliminar_producto()
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")

#SEPARAR EL MENU EN OTRA CLASE PARA DEJAR LIMPIO EL CODIGO MAIN