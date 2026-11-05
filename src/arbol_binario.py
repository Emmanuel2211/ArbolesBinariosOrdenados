from lista_doblemente_ligada import ListaDoblementeLigada
from typing import Iterator, TypeVar, Optional, Generic, List, Tuple
from coleccion import Coleccion
from abc import abstractmethod

T = TypeVar("T")


class _Vertice(Generic[T]):
    """
    Representación de un nodo individual para la estructura de datos Árbol Binario.
    Almacena un elemento de tipo genérico y mantiene referencias a sus posibles
    hijos (izquierdo y derecho) así como a su vértice padre, permitiendo
    recorridos bidireccionales.
    """

    def __init__(self, elemento: T) -> None:
        self.elemento: T = elemento
        self.izquierdo: Optional["_Vertice[T]"] = None
        self.derecho: Optional["_Vertice[T]"] = None
        self.padre: Optional["_Vertice[T]"] = None

    def es_hijo_izquierdo(self) -> bool:
        """
        Verifica la relación de descendencia directa por la rama izquierda.
        Devuelve True si este vértice es el hijo izquierdo de su padre.
        """
        return self.padre is not None and self.padre.izquierdo is self

    def es_hijo_derecho(self) -> bool:
        """
        Verifica la relación de descendencia directa por la rama derecha.
        Devuelve True si este vértice es el hijo derecho de su padre.
        """
        return self.padre is not None and self.padre.derecho is self

    def agrega_izquierdo(self, hijo: Optional["_Vertice[T]"]) -> None:
        """
        Establece una nueva relación de parentesco, asignando el vértice
        proporcionado como el hijo izquierdo del vértice actual y actualizando
        la referencia del padre en el hijo.
        """
        self.izquierdo = hijo
        if hijo is not None:
            hijo.padre = self

    def agrega_derecho(self, hijo: Optional["_Vertice[T]"]) -> None:
        """
        Establece una nueva relación de parentesco, asignando el vértice
        proporcionado como el hijo derecho del vértice actual y actualizando
        la referencia del padre en el hijo.
        """
        self.derecho = hijo
        if hijo is not None:
            hijo.padre = self


class ArbolBinario(Coleccion[T]):
    """
    Clase abstracta que define la estructura y operaciones fundamentales
    del TDA Árbol Binario.
    """

    def __init__(self) -> None:
        self._raiz: Optional["_Vertice[T]"] = None
        self._tamanio = 0

    def acceder(self, i: int) -> T:
        """
        Recupera el elemento ubicado en la i-ésima posición del recorrido
        lineal predeterminado del árbol.
        """
        recorrido = self.devolver_recorrido()
        return recorrido.acceder(i)

    def devolver_tamanio(self) -> int:
        """
        Devuelve la cardinalidad actual del árbol (cantidad total de vértices).
        """
        return self._tamanio

    def esta_vacio(self) -> bool:
        """
        Determina si la estructura carece de elementos.
        """
        return self._tamanio == 0

    @abstractmethod
    def agregar(self, elemento: T) -> None:
        """Agrega un elemento siguiendo las reglas específicas de la subclase."""
        raise NotImplementedError

    @abstractmethod
    def eliminar(self, elemento: T) -> None:
        """Elimina un elemento preservando las propiedades del árbol."""
        raise NotImplementedError

    @abstractmethod
    def buscar(self, elemento: T) -> bool:
        """Determina la existencia de un elemento en la estructura."""
        raise NotImplementedError

    @abstractmethod
    def devolver_recorrido(self) -> ListaDoblementeLigada[T]:
        """Devuelve una lista con el recorrido estandarizado del árbol."""
        raise NotImplementedError

    def __iter__(self) -> Iterator[T]:
        """
        Permite la iteración directa sobre la colección utilizando el
        recorrido por defecto del árbol.
        """
        return self.devolver_recorrido().__iter__()

    def __str__(self) -> str:
        """
        Genera una representación visual del árbol
        """
        if self.esta_vacio():
            return "Árbol vacío"

        lineas, _, _, _ = self._representar(self._raiz)
        return "\n".join(lineas)

    def _representar(self, v: _Vertice[T]) -> Tuple[List[str], int, int, int]:
        """
        Método auxiliar recursivo que construye la matriz de caracteres
        para la representación visual del subárbol inducido por el vértice 'v'.
        Calcula dinámicamente espacios, anchos y compensaciones de altura.
        """
        # Caso 1: el vértice es una hoja.
        if v.izquierdo is None and v.derecho is None:
            linea = str(v.elemento)
            ancho = len(linea)
            altura = 1
            medio = ancho // 2
            return ([linea], ancho, altura, medio)

        # Caso 2: solamente existe el hijo izquierdo.
        if v.derecho is None:
            lineas_izq, n, altura_izq, x = self._representar(v.izquierdo)
            elemento = str(v.elemento)
            u = len(elemento)
            primera = " " * (x + 1) + "_" * (n - x - 1) + elemento
            segunda = " " * x + "/" + " " * (n - x - 1 + u)
            desplazadas = [linea + " " * u for linea in lineas_izq]
            lineas = [primera, segunda] + desplazadas
            return (lineas, n + u, altura_izq + 2, n + (u // 2))

        # Caso 3: solamente existe el hijo derecho.
        if v.izquierdo is None:
            lineas_der, n, altura_der, x = self._representar(v.derecho)
            elemento = str(v.elemento)
            u = len(elemento)
            primera = elemento + "_" * x + " " * (n - x)
            segunda = " " * (u + x) + "\\" + " " * (n - x - 1)
            desplazadas = [" " * u + linea for linea in lineas_der]
            lineas = [primera, segunda] + desplazadas
            return (lineas, n + u, altura_der + 2, u // 2)

        # Caso 4: existen ambos hijos.
        lineas_izq, n, h_i, x = self._representar(v.izquierdo)
        lineas_der, m, h_d, y = self._representar(v.derecho)
        elemento = str(v.elemento)
        u = len(elemento)
        primera = " " * (x + 1) + "_" * (n - x - 1) + elemento + "_" * y + " " * (m - y)
        segunda = " " * x + "/" + " " * (n - x - 1 + u + y) + "\\" + " " * (m - y - 1)

        if h_i < h_d:
            lineas_izq.extend([" " * n] * (h_d - h_i))
        elif h_d < h_i:
            lineas_der.extend([" " * m] * (h_i - h_d))

        lineas = [primera, segunda]
        for a, b in zip(lineas_izq, lineas_der):
            lineas.append(a + " " * u + b)

        return (lineas, n + m + u, max(h_i, h_d) + 2, n + (u // 2))
