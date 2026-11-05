"""
Módulo Lista Doblemente Ligada
"""

from typing import TypeVar, Iterator, Optional, Generic
from lista import Lista

T = TypeVar("T")


class _Nodo(Generic[T]):
    """Nodo para lista doblemente ligada."""

    __slots__ = ("elemento", "siguiente", "anterior")

    def __init__(self, elemento: T) -> None:
        self.elemento: T = elemento
        self.siguiente: Optional["_Nodo[T]"] = None
        self.anterior: Optional["_Nodo[T]"] = None


class ListaDoblementeLigada(Lista[T]):
    """Implementación del TDA Lista mediante una Lista Doblemente Ligada."""

    def __init__(self) -> None:
        self.__cabeza: Optional[_Nodo[T]] = None
        self.__rabo: Optional[_Nodo[T]] = None
        self.__longitud = 0

    def __iter__(self) -> Iterator[T]:
        """Genera los elementos de la lista desde la cabeza hasta el rabo."""
        actual = self.__cabeza
        while actual is not None:
            yield actual.elemento
            actual = actual.siguiente

    def agregar(self, elemento: T) -> None:
        """Agrega un elemento al inicio de la lista."""
        nuevo_nodo = _Nodo(elemento)
        if self.__cabeza is None:
            self.__cabeza = nuevo_nodo
            self.__rabo = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.__cabeza
            self.__cabeza.anterior = nuevo_nodo
            self.__cabeza = nuevo_nodo
        self.__longitud += 1

    def buscar(self, elemento: T) -> bool:
        """Determina si un elemento se encuentra en la lista."""
        for e in self:
            if e == elemento:
                return True
        return False

    def eliminar(self, elemento: T) -> None:
        """Elimina la primera aparición de un elemento en la lista."""
        actual = self.__cabeza
        while actual is not None:
            if actual.elemento == elemento:
                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.__cabeza = actual.siguiente

                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.__rabo = actual.anterior

                self.__longitud -= 1
                return
            actual = actual.siguiente

    def eliminar_indice(self, indice: int) -> None:
        """Elimina el elemento ubicado en la i-ésima posición."""
        if indice < 0 or indice >= self.__longitud:
            raise IndexError("Índice fuera de rango.")

        nodo_a_eliminar = self.acceder_nodo(indice)

        if nodo_a_eliminar.anterior is not None:
            nodo_a_eliminar.anterior.siguiente = nodo_a_eliminar.siguiente
        else:
            self.__cabeza = nodo_a_eliminar.siguiente

        if nodo_a_eliminar.siguiente is not None:
            nodo_a_eliminar.siguiente.anterior = nodo_a_eliminar.anterior
        else:
            self.__rabo = nodo_a_eliminar.anterior

        self.__longitud -= 1

    def acceder(self, indice: int) -> T:
        """Devuelve el elemento ubicado en la i-ésima posición."""
        return self.acceder_nodo(indice).elemento

    def devolver_indice_elemento(self, elemento: T) -> int:
        """Devuelve el índice de la primera aparición de un elemento."""
        indice = 0
        actual = self.__cabeza
        while actual is not None:
            if actual.elemento == elemento:
                return indice
            actual = actual.siguiente
            indice += 1
        raise ValueError(f"El elemento no se encuentra en la lista.")

    def devolver_longitud(self) -> int:
        """Devuelve la longitud actual de la lista."""
        return self.__longitud

    def agregar_final(self, elemento: T) -> None:
        """Agrega un elemento al final de la lista."""
        nuevo_nodo = _Nodo(elemento)
        if self.__rabo is None:
            self.__cabeza = nuevo_nodo
            self.__rabo = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.__rabo
            self.__rabo.siguiente = nuevo_nodo
            self.__rabo = nuevo_nodo
        self.__longitud += 1

    def reversa(self) -> "ListaDoblementeLigada[T]":
        """Devuelve una nueva lista con los elementos en orden inverso."""
        nueva_lista = ListaDoblementeLigada[T]()
        actual = self.__cabeza

        while actual is not None:
            nueva_lista.agregar(actual.elemento)
            actual = actual.siguiente
        return nueva_lista

    def acceder_nodo(self, indice: int) -> _Nodo[T]:
        """Devuelve el i-ésimo nodo de la lista iterando desde el punto más cercano."""
        if indice < 0 or indice >= self.__longitud:
            raise IndexError("Índice fuera de rango.")

        if indice < self.__longitud // 2:
            actual = self.__cabeza
            for _ in range(indice):
                assert actual is not None
                actual = actual.siguiente
        else:
            actual = self.__rabo
            for _ in range(self.__longitud - 1 - indice):
                assert actual is not None
                actual = actual.anterior

        assert actual is not None
        return actual

    def __str__(self) -> str:
        """Devuelve la representación en cadena con formato a_1 <-> a_2 <-> ... <-> a_n."""
        if self.__longitud == 0:
            return ""
        return " <-> ".join(str(elemento) for elemento in self)
