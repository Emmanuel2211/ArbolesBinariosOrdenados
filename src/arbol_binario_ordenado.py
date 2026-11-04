from arbol_binario import ArbolBinario, _Vertice
from cola import Cola
from pila import Pila
from typing import TypeVar, Optional, Protocol, Any
from lista_doblemente_ligada import ListaDoblementeLigada


class Comparable(Protocol):
    def __lt__(self, otro: Any) -> bool: ...
    def __le__(self, otro: Any) -> bool: ...
    def __gt__(self, otro: Any) -> bool: ...
    def __ge__(self, otro: Any) -> bool: ...


T = TypeVar("T", bound=Comparable)


class ArbolBinarioOrdenado(ArbolBinario[T]):

    def __init__(self) -> None:
        super().__init__()

    def buscar(self, elemento: T) -> bool:
        # TODO: Aquí va tu código.
        pass

    def eliminar(self, elemento: T) -> None:
        # TODO: Aquí va tu código.
        pass

    def agregar(self, elemento: T) -> None:
        # TODO: Aquí va tu código.
        pass

    def devolver_recorrido(self) -> ListaDoblementeLigada[T]:
        # TODO: Aquí va tu código.
        pass

    def _agregar_aux(self, vertice: Optional["_Vertice[T]"], elemento: T) -> None:
        # TODO: Aquí va tu código.
        pass

    def _eliminar_aux(
        self, vertice: Optional["_Vertice[T]"], elemento: T
    ) -> Optional["_Vertice[T]"]:
        # TODO: Aquí va tu código.
        pass

    def _devolver_minimo(self, vertice: Optional["_Vertice[T]"]) -> T:
        while vertice.izquierdo is not None:
            vertice = vertice.izquierdo
        return vertice

    def _buscar_aux(self, vertice: Optional["_Vertice[T]"], elemento: T) -> bool:
        # TODO: Aquí va tu código.
        pass
