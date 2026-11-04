from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class PiCola(ABC, Generic[T]):

    @abstractmethod
    def meter(self, elemento: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def sacar(self) -> T:
        raise NotImplementedError

    @abstractmethod
    def mira(self) -> T:
        raise NotImplementedError

    @abstractmethod
    def esta_vacia(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def devolver_tamanio(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def __eq__(self, otro: object) -> bool:
        raise NotImplementedError

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError
