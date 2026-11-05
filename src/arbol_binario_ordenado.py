from arbol_binario import ArbolBinario, _Vertice
from cola import Cola
from pila import Pila
from lista_doblemente_ligada import ListaDoblementeLigada
from typing import TypeVar, Optional, Protocol, Any


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
        return self._buscar_aux(self._raiz, elemento)

    def _buscar_aux(self, vertice: Optional["_Vertice[T]"], elemento: T) -> bool:
        if vertice is None:
            return False
        if vertice.elemento == elemento:
            return True
        if vertice.elemento <= elemento:
            return self._buscar_aux(vertice.derecho, elemento)
        return self._buscar_aux(vertice.izquierdo, elemento)

    def agregar(self, elemento: T) -> None:
        if elemento is None:
            raise ValueError("No se puede agregar un elemento nulo")
        if self._raiz is None:
            nuevo_vertice = _Vertice(elemento)
            self._raiz = nuevo_vertice
            self._tamanio += 1
            return
        self._agregar_aux(self._raiz, elemento)

    def _agregar_aux(self, vertice: Optional["_Vertice[T]"], elemento: T) -> None:
        if vertice.elemento == elemento:
            return
        if vertice.elemento <= elemento:
            if vertice.derecho is None:
                v_aux = _Vertice(elemento)
                self._tamanio += 1
                vertice.agrega_derecho(v_aux)
            else:
                self._agregar_aux(vertice.derecho, elemento)
        else:
            if vertice.izquierdo is None:
                v_aux = _Vertice(elemento)
                self._tamanio += 1
                vertice.agrega_izquierdo(v_aux)
            else:
                self._agregar_aux(vertice.izquierdo, elemento)

    def eliminar(self, elemento: T) -> None:
        if elemento is None:
            raise ValueError("No se puede eliminar un elemento nulo")
        self._raiz = self._eliminar_aux(self._raiz, elemento)

    def _eliminar_aux(
        self, vertice: Optional["_Vertice[T]"], elemento: T
    ) -> Optional["_Vertice[T]"]:
        if vertice is None:
            return None
        if vertice.elemento > elemento:
            vertice.izquierdo = self._eliminar_aux(vertice.izquierdo, elemento)
            if vertice.izquierdo is not None:
                vertice.izquierdo.padre = vertice
        elif vertice.elemento < elemento:
            vertice.derecho = self._eliminar_aux(vertice.derecho, elemento)
            if vertice.derecho is not None:
                vertice.derecho.padre = vertice
        else:
            if vertice.izquierdo is None and vertice.derecho is None:
                self._tamanio -= 1
                return None
            if vertice.izquierdo is None:
                self._tamanio -= 1
                if vertice.derecho is not None:
                    vertice.derecho.padre = vertice.padre
                return vertice.derecho
            if vertice.derecho is None:
                self._tamanio -= 1
                if vertice.izquierdo is not None:
                    vertice.izquierdo.padre = vertice.padre
                return vertice.izquierdo

            sucesor = self._devolver_minimo(vertice.derecho)
            vertice.elemento = sucesor.elemento
            vertice.derecho = self._eliminar_aux(vertice.derecho, sucesor.elemento)
            if vertice.derecho is not None:
                vertice.derecho.padre = vertice
        return vertice

    def _devolver_minimo(self, vertice: Optional["_Vertice[T]"]) -> Any:
        while vertice.izquierdo is not None:
            vertice = vertice.izquierdo
        return vertice

    def devolver_recorrido(self) -> ListaDoblementeLigada[T]:
        recorrido = ListaDoblementeLigada[T]()
        if self._raiz is None:
            return recorrido

        pila = Pila["_Vertice[T]"]()
        actual = self._raiz

        while actual is not None or not pila.esta_vacia():
            while actual is not None:
                pila.meter(actual)
                actual = actual.izquierdo
            actual = pila.sacar()
            recorrido.agregar_final(actual.elemento)
            actual = actual.derecho
        return recorrido
