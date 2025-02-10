class Producto:
    def __init__(self, nombre, sku, fecha_caducidad, proveedor, conteo_inventario):
        self._nombre = nombre
        self._sku = sku
        self._fecha_caducidad = fecha_caducidad
        self._proveedor = proveedor
        self._conteo_inventario = conteo_inventario

    #HACER LAS VARIABLES PRIVADAS?

    #GETTER Y SETTER PARA FUNCIONAMIENTO DE CLASES HIJAS
    def get_nombre(self):
        return self._nombre

    def get_sku(self):
        return self._sku

    def get_fecha_caducidad(self):
        return self._fecha_caducidad

    def get_proveedor(self):
        return self._proveedor

    def get_conteo_inventario(self):
        return self._conteo_inventario

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_sku(self, sku):
        self._sku = sku

    def set_fecha_caducidad(self, fecha_caducidad):
        self._fecha_caducidad = fecha_caducidad

    def set_proveedor(self, proveedor):
        self._proveedor = proveedor

    def set_conteo_inventario(self, conteo):
        self._conteo_inventario = conteo

    #PARA MODIFICAR INVENTARIO
    def agregar_inventario(self, cantidad):
        self._conteo_inventario += cantidad

    def verificar_inventario(self, limite):
        if self._conteo_inventario < limite:
            print(f"¡Alerta! Solicitar producto {self._nombre} a {self._proveedor}. Inventario actual: {self._conteo_inventario}")
