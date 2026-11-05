from picola import PiCola
from typing import TypeVar, Optional, Generic

T = TypeVar("T")


class _Nodo(Generic[T]):
    """
    Representación de un nodo individual para la estructura de datos Pila.
    Almacena un elemento de tipo genérico y una referencia al nodo que le precede
    en la jerarquía de la pila.
    """

    __slots__ = ("elemento", "siguiente")

    def __init__(self, elemento: T) -> None:
        self.elemento: T = elemento
        self.siguiente: Optional[_Nodo[T]] = None


class Pila(PiCola[T]):
    """
    Implementación de una Pila (Stack) basada en el TDA PiCola.
    Esta estructura sigue rigurosamente la política de acceso LIFO
    (Last In, First Out), donde el último elemento insertado es siempre
    el primero en ser retirado, manteniendo acceso únicamente a su 'tope'.
    """

    def __init__(self) -> None:
        self.__tope: Optional[_Nodo[T]] = None
        self.__tamanio = 0

    def meter(self, elemento: T) -> None:
        """
        Inserta un nuevo elemento en la pila.
        El elemento es encapsulado en un nodo y anexado al tope de la estructura,
        actualizando el puntero para convertirlo en el nuevo elemento accesible.
        """
        nuevo = _Nodo(elemento)
        nuevo.siguiente = self.__tope
        self.__tope = nuevo
        self.__tamanio += 1

    def sacar(self) -> T:
        """
        Elimina y devuelve el elemento residente en el tope de la pila.
        Levanta una excepción de tipo IndexError en caso de intentar operar
        sobre una estructura carente de elementos.
        """
        if self.esta_vacia():
            raise IndexError("La pila está vacía, no es posible sacar elementos.")

        elemento_retirado = self.__tope.elemento
        self.__tope = self.__tope.siguiente
        self.__tamanio -= 1
        return elemento_retirado

    def mira(self) -> T:
        """
        Devuelve el valor del elemento situado en el tope de la pila
        sin alterar la estructura ni remover el nodo.
        Levanta una excepción si la pila se encuentra vacía.
        """
        if self.esta_vacia():
            raise IndexError("La pila está vacía, no hay elementos en el tope.")
        return self.__tope.elemento

    def esta_vacia(self) -> bool:
        """
        Evalúa el estado lógico de la pila comprobando su cardinalidad.
        Devuelve True si la estructura no contiene elementos, False en caso contrario.
        """
        return self.__tamanio == 0

    def devolver_tamanio(self) -> int:
        """
        Retorna la cantidad actual de elementos retenidos dentro de la estructura.
        """
        return self.__tamanio

    def __eq__(self, otro: object) -> bool:
        """
        Compara la equivalencia secuencial entre dos estructuras tipo Pila.
        Valida que ambas posean el mismo tamaño y que la correspondencia
        de sus elementos sea idéntica desde el tope hasta la base.
        """
        if not isinstance(otro, Pila):
            return False
        if self.__tamanio != otro.devolver_tamanio():
            return False

        actual_self = self.__tope
        # Utilizamos la convención de acceso a nombres protegidos por encapsulamiento
        # estrictamente para evaluar la igualdad estructural sin destruir la pila 'otro'.
        actual_otro = otro._Pila__tope

        while actual_self is not None and actual_otro is not None:
            if actual_self.elemento != actual_otro.elemento:
                return False
            actual_self = actual_self.siguiente
            actual_otro = actual_otro.siguiente

        return True

    def __str__(self) -> str:
        """
        Genera una representación en cadena de la pila respetando el formato:
        / a1 // a2 / ... / an /
        Donde a1 representa de manera estricta el tope actual de la pila.
        """
        if self.esta_vacia():
            return "/ /"

        elementos = []
        actual = self.__tope
        while actual is not None:
            elementos.append(str(actual.elemento))
            actual = actual.siguiente

        return "/ " + " // ".join(elementos) + " /"
