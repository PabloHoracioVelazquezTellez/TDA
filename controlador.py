from inventario import Inventario
class Menu:
    def __init__(self):
        self.inventario=Inventario()

    # PARA GENERAR EL MENU DE CONTROL
    def mostrar_menu(self):
        while True:
            print("\n--- MENÚ INVENTARIO ---")
            print("1. Agregar producto")
            print("2. Mostrar productos")
            print("3. Actualizar inventario")
            print("4. Verificar inventario")
            print("5. Eliminar producto")
            print("6. Salir")

            opcion=input("Seleccione una opción: ")

            if opcion=="1":
                self.inventario.agregar_producto()
            elif opcion=="2":
                self.inventario.mostrar_productos()
            elif opcion=="3":
                self.inventario.actualizar_inventario()
            elif opcion=="4":
                self.inventario.verificar_inventario()
            elif opcion=="5":
                self.inventario.eliminar_producto()
            elif opcion=="6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente de nuevo.")
