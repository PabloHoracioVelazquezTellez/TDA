from administrador import Producto
class Inventario:
    def __init__(self):
        self._productos={}  # DICCIONARIO PARA ALMACENAR LISTAS, CUMPLIENDO FUNCION DE ARREGLO DE ARREGLOS

    def agregar_producto(self):
        nombre=input("Nombre del producto: ")
        sku=input("SKU: ")
        fecha_caducidad=input("Fecha de caducidad (YYYY-MM-DD): ")
        proveedor=input("Proveedor: ")
        conteo=int(input("Cantidad en inventario: "))

        if sku in self._productos:
            print("Error: SKU ya existe en el inventario.")
        else:
            producto=Producto(nombre, sku, fecha_caducidad, proveedor, conteo)
            self._productos[sku] = producto  #PARA GENERAR LA LISTA CON DATOS DEL PRODUCTO Y GUARDARLA EN EL DICCIONARIO
            print("Producto agregado correctamente.")#DEBUGGEAR

    def mostrar_productos(self):
        if not self._productos:
            print("El inventario está vacío.")
        else:
            print("\nLista de productos en inventario:")
            for sku, producto in self._productos.items():
                print(f"Producto: {producto.get_nombre()} | SKU: {sku} | Fecha de caducidad: {producto.get_fecha_caducidad()} | Proveedor: {producto.get_proveedor()} | Inventario: {producto.get_conteo_inventario()}")

    def actualizar_inventario(self):
        self.mostrar_productos()
        if self._productos:
            sku=input("Ingrese el SKU del producto a actualizar: ")
            if sku in self._productos:
                cantidad=int(input("Cantidad a agregar: "))
                self._productos[sku].agregar_inventario(cantidad)
                print("Inventario actualizado.")
            else:
                print("SKU no encontrado.")

    def verificar_inventario(self):
        limite=int(input("Ingrese inventario minimo para alertas: "))
        for producto in self._productos.values():
            producto.verificar_inventario(limite)

    def eliminar_producto(self):
        self.mostrar_productos()
        if self._productos:
            sku=input("Ingrese el SKU del producto a eliminar: ")
            if sku in self._productos:
                del self._productos[sku]
                print("Producto eliminado.")
            else:
                print("SKU no encontrado.")
