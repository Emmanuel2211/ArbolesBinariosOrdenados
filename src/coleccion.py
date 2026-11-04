"""
Módulo coleccion
"""

from abc import ABC, abstractmethod
from typing import Generic, Iterator, TypeVar

T = TypeVar("T")


class Coleccion(ABC, Generic[T]):

    @abstractmethod
    def agregar(self, elemento: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def buscar(self, elemento: T) -> bool:
        raise NotImplementedError

    @abstractmethod
    def eliminar(self, elemento: T) -> None:
        raise NotImplementedError

    ## Dunder metodos para la clase Colección

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        """
        Devuelve un iterador sobre los elementos de la colección.
        Permite usar 'for elemento in coleccion: ...'.

        Implementado de forma abstracta. Las colecciones se iteran de forma diferente
        """
        raise NotImplementedError

    def __contains__(self, elemento: T) -> bool:
        """
        Permite usar el operador 'in': 'elemento in coleccion'.

        Ya viene implementado en términos de buscar().
        Cada colección implmenta buscar de forma no abstracta.
        """
        return self.buscar(elemento)
