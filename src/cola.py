from picola import PiCola
from typing import TypeVar, Optional, Generic

T = TypeVar("T")


class _Nodo(Generic[T]):

    __slots__ = ("elemento", "siguiente")

    def __init__(self, elemento: T) -> None:
        self.elemento: T = elemento
        self.siguiente: Optional["_Nodo[T]"] = None


class Cola(PiCola[T]):

    def __init__(self) -> None:
        self.__tope: Optional["_Nodo[T]"] = None
        self.__fondo: Optional["_Nodo[T]"] = None
        self.__tamanio = 0

    def meter(self, elemento: T) -> None:
        # TODO: Aquí va tu código.
        pass

    def sacar(self) -> T:
        # TODO: Aquí va tu código.
        pass

    def mira(self) -> T:
        # TODO: Aquí va tu código.
        pass

    def esta_vacia(self) -> bool:
        # TODO: Aquí va tu código.
        pass

    def devolver_tamanio(self) -> int:
        # TODO: Aquí va tu código.
        pass

    def __eq__(self, otro: object) -> bool:
        # TODO: Aquí va tu código.
        pass

    def __str__(self) -> str:
        # TODO: Aquí va tu código.
        pass
