from arbol_binario_ordenado import ArbolBinarioOrdenado
from producto import Producto


class Inventario:
    def __init__(self):
        self.arbol = ArbolBinarioOrdenado[Producto]()

    def cargar_desde_archivo(self, ruta: str) -> None:
        with open(ruta, "r", encoding="utf-8") as f:
            next(f)
            for linea in f:
                if not linea.strip():
                    continue
                datos = linea.strip().split(",")
                if len(datos) == 4 and "14799" in datos[0]:
                    prod = Producto(
                        "Apple iPhone 14", 799.0, datos[1], datos[2], datos[3]
                    )
                    self.agregar_producto(prod)
                elif len(datos) == 5:
                    prod = Producto(datos[0], datos[1], datos[2], datos[3], datos[4])
                    self.agregar_producto(prod)

    def agregar_producto(self, producto: Producto) -> None:
        self.arbol.agregar(producto)

    def buscar_producto(self, nombre: str) -> bool:
        dummy = Producto(nombre, 0, "", "", 0)
        return self.arbol.buscar(dummy)

    def eliminar_producto(self, nombre: str) -> None:
        dummy = Producto(nombre, 0, "", "", 0)
        self.arbol.eliminar(dummy)

    def productos_en_rango_precio(
        self, min_precio: float, max_precio: float
    ) -> list[Producto]:
        recorrido = self.arbol.devolver_recorrido()
        resultados = []
        for producto in recorrido:
            if min_precio <= producto.precio <= max_precio:
                resultados.append(producto)
        return resultados
