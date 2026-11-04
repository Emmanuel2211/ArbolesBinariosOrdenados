from lista_doblemente_ligada import ListaDoblementeLigada
from typing import Iterator, TypeVar, Optional, Generic
from coleccion import Coleccion
from abc import abstractmethod

T = TypeVar("T")


class _Vertice(Generic[T]):

    def __init__(self, elemento: T) -> None:
        self.elemento: T = elemento
        self.izquierdo: Optional["_Vertice[T]"] = None
        self.derecho: Optional["_Vertice[T]"] = None
        self.padre: Optional["_Vertice[T]"] = None

    def es_hijo_izquierdo(self) -> bool:
        # TODO: Aquí va tu código.
        pass

    def es_hijo_derecho(self) -> bool:
        # TODO: Aquí va tu código.
        pass

    def agrega_izquierdo(self, hijo: Optional["_Vertice[T]"]) -> None:
        # TODO: Aquí va tu código.
        pass

    def agrega_derecho(self, hijo: Optional["_Vertice[T]"]) -> None:
        # TODO: Aquí va tu código.
        pass


class ArbolBinario(Coleccion[T]):

    def __init__(self) -> None:
        self._raiz: Optional["_Vertice[T]"] = None
        self._tamanio = 0

    def acceder(self, i: int) -> T:
        # TODO: Aquí va tu código.
        pass

    def devolver_tamanio(self) -> int:
        # TODO: Aquí va tu código.
        pass

    def esta_vacio(self) -> bool:
        # TODO: Aquí va tu código.
        pass

    @abstractmethod
    def agregar(self, elemento: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def eliminar(self, elemento: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def buscar(self, elemento: T) -> bool:
        raise NotImplementedError

    @abstractmethod
    def devolver_recorrido(self) -> ListaDoblementeLigada[T]:
        raise NotImplementedError

    def __iter__(self) -> Iterator[T]:
        return self.devolver_recorrido().__iter__()

    def __str__(self) -> str:
        # TODO: Aquí va tu código.
        pass
