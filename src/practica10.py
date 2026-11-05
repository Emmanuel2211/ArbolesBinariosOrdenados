from arbol_binario_ordenado import ArbolBinarioOrdenado
from inventario import Inventario
from producto import Producto


class MainArbolOrdenado:
    def main(self):
        print("--- PRUEBAS TDA ÁRBOL BINARIO ORDENADO ---")
        arbol = ArbolBinarioOrdenado[int]()
        elementos = [50, 30, 70, 20, 40, 60, 80]
        for e in elementos:
            arbol.agregar(e)

        print("Recorrido in-order:", [x for x in arbol.devolver_recorrido()])
        print("Buscar 40:", arbol.buscar(40))
        print("Buscar 100:", arbol.buscar(100))

        arbol.eliminar(30)
        print("Recorrido tras eliminar 30:", [x for x in arbol.devolver_recorrido()])

        print("\n--- PRUEBAS DEL SISTEMA DE INVENTARIO ---")
        inv = Inventario()
        inv.cargar_desde_archivo("Productos.txt")

        print("Buscar 'Apple iPhone 14':", inv.buscar_producto("Apple iPhone 14"))
        print("Buscar 'Laptop Inexistente':", inv.buscar_producto("Laptop Inexistente"))

        print("\nProductos con precio entre $100 y $300:")
        en_rango = inv.productos_en_rango_precio(100.0, 300.0)
        for p in en_rango:
            print(f" -> {p}")

        print("\nEliminando 'Nike Air Max Sneakers'...")
        inv.eliminar_producto("Nike Air Max Sneakers")
        print(
            "Buscar 'Nike Air Max Sneakers':",
            inv.buscar_producto("Nike Air Max Sneakers"),
        )


if __name__ == "__main__":
    app = MainArbolOrdenado()
    app.main()
