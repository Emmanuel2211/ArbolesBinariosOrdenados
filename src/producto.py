class Producto:
    def __init__(
        self, nombre: str, precio: float, categoria: str, marca: str, existencia: int
    ):
        self.nombre = nombre.strip()
        self.precio = float(precio)
        self.categoria = categoria.strip()
        self.marca = marca.strip()
        self.existencia = int(existencia)
        # Se genera un código de barras determinista de 8 dígitos a partir del nombre
        self.codigo_barras = abs(hash(self.nombre)) % 90000000 + 10000000

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Producto):
            return False
        return self.nombre == otro.nombre

    def __lt__(self, otro: "Producto") -> bool:
        return self.nombre < otro.nombre

    def __le__(self, otro: "Producto") -> bool:
        return self.nombre <= otro.nombre

    def __gt__(self, otro: "Producto") -> bool:
        return self.nombre > otro.nombre

    def __ge__(self, otro: "Producto") -> bool:
        return self.nombre >= otro.nombre

    def __str__(self) -> str:
        return f"[{self.codigo_barras}] {self.nombre} - ${self.precio} ({self.existencia} en stock)"
