"""Modelo: Generador Congruencial Lineal (LCG).

X(n+1) = (a * X(n) + c) mod m      U(n+1) = X(n+1) / m
"""


class GeneradorLCG:
    def __init__(self, semilla: int, a: int, c: int, m: int, nombre: str = "LCG"):
        self.nombre = nombre
        self.semilla = semilla
        self.a = a
        self.c = c
        self.m = m
        self._x = semilla

    def reiniciar(self) -> None:
        self._x = self.semilla

    def siguiente(self) -> float:
        """Devuelve el siguiente número pseudoaleatorio en [0,1)."""
        self._x = (self.a * self._x + self.c) % self.m
        return self._x / self.m

    def generar(self, n: int) -> list[float]:
        """Genera n números desde la semilla (reinicia el generador)."""
        self.reiniciar()
        return [self.siguiente() for _ in range(n)]

    def descripcion(self) -> str:
        return (f"{self.nombre}: semilla={self.semilla}, a={self.a}, "
                f"c={self.c}, m={self.m}")
