from picola import PiCola
from typing import TypeVar, Optional, Generic

T = TypeVar("T")


class _Nodo(Generic[T]):
    """
    Representación de un nodo individual para la estructura de datos Cola.
    Almacena el valor genérico y el puntero al elemento subsecuente en la fila.
    """

    __slots__ = ("elemento", "siguiente")

    def __init__(self, elemento: T) -> None:
        self.elemento: T = elemento
        self.siguiente: Optional[_Nodo[T]] = None


class Cola(PiCola[T]):
    """
    Implementación de una Cola (Queue) basada en el TDA PiCola.
    Esta estructura sigue rigurosamente la política de acceso FIFO
    (First In, First Out), donde las inserciones ocurren en el extremo final
    y las extracciones se despachan desde el frente.
    """

    def __init__(self) -> None:
        self.__frente: Optional[_Nodo[T]] = None
        self.__final: Optional[_Nodo[T]] = None
        self.__tamanio = 0

    def meter(self, elemento: T) -> None:
        """
        Anexa un elemento a la estructura garantizando la política FIFO.
        El nuevo nodo es insertado consistentemente como el último elemento (rabo) de la cola.
        """
        nuevo = _Nodo(elemento)
        if self.esta_vacia():
            self.__frente = nuevo
        else:
            self.__final.siguiente = nuevo

        self.__final = nuevo
        self.__tamanio += 1

    def sacar(self) -> T:
        """
        Retira y devuelve el elemento localizado en el frente de la cola.
        Actualiza el puntero del frente al siguiente nodo disponible.
        Levanta un IndexError en caso de requerir extracciones sobre una cola vacía.
        """
        if self.esta_vacia():
            raise IndexError("La cola está vacía, no es posible sacar elementos.")

        elemento_retirado = self.__frente.elemento
        self.__frente = self.__frente.siguiente
        self.__tamanio -= 1

        if self.esta_vacia():
            self.__final = None

        return elemento_retirado

    def mira(self) -> T:
        """
        Devuelve el valor contenido en el frente de la estructura
        preservando el estado interno de la cola intacto.
        """
        if self.esta_vacia():
            raise IndexError("La cola está vacía, no hay elementos en el frente.")
        return self.__frente.elemento

    def esta_vacia(self) -> bool:
        """
        Determina lógicamente la carencia de elementos en la estructura.
        """
        return self.__tamanio == 0

    def devolver_tamanio(self) -> int:
        """
        Proporciona el número exacto de nodos vigentes en la cola.
        """
        return self.__tamanio

    def __eq__(self, otro: object) -> bool:
        """
        Evalúa la identidad secuencial frente a otra estructura Cola.
        Asegura que el orden de ingreso y los valores mantengan
        una correspondencia uno a uno.
        """
        if not isinstance(otro, Cola):
            return False
        if self.__tamanio != otro.devolver_tamanio():
            return False

        actual_self = self.__frente
        actual_otro = otro._Cola__frente

        while actual_self is not None and actual_otro is not None:
            if actual_self.elemento != actual_otro.elemento:
                return False
            actual_self = actual_self.siguiente
            actual_otro = actual_otro.siguiente

        return True

    def __str__(self) -> str:
        """
        Genera una representación en cadena de la cola respetando el formato:
        | a1 | ->| a2 | ->... ->| an |
        Donde a1 es el frente de la cola (el próximo en salir).
        """
        if self.esta_vacia():
            return "| |"

        elementos = []
        actual = self.__frente
        while actual is not None:
            elementos.append(f"| {actual.elemento} |")
            actual = actual.siguiente

        return " ->".join(elementos)
