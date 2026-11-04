"""
Módulo lista
"""

from abc import abstractmethod
from typing import TypeVar

from coleccion import Coleccion

T = TypeVar("T")


class Lista(Coleccion[T]):

    @abstractmethod
    def eliminar_indice(self, indice: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def acceder(self, indice: int) -> T:
        raise NotImplementedError

    @abstractmethod
    def devolver_indice_elemento(self, elemento: T) -> int:
        raise NotImplementedError

    @abstractmethod
    def devolver_longitud(self) -> int:
        raise NotImplementedError

    def __len__(self) -> int:
        """Devuelve la cantidad de elementos en la lista."""
        return self.devolver_longitud()

    def __getitem__(self, indice: int) -> T:
        """
        Permite usar 'mi_lista[indice]'.

        Ya viene implementado en términos de acceder(), no es
        necesario sobreescribirlo.
        """
        return self.acceder(indice)
