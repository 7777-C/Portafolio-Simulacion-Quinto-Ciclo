"""
MODELO - Generador de números pseudoaleatorios (LCG de 48 bits).

Implementa EXACTAMENTE el mismo algoritmo que java.util.Random y que la clase
LcgRandom.java de este proyecto. Por eso, con la misma semilla, Python y Java
producen la misma secuencia de números (requisito de la sección 6 de la guía).

    X(n+1) = (a * X(n) + c) mod 2^48
    a = 0x5DEECE66D,  c = 0xB,  m = 2^48
"""


class LcgRandom:
    _MULTIPLIER = 0x5DEECE66D
    _ADDEND = 0xB
    _MASK = (1 << 48) - 1

    def __init__(self, seed: int):
        self._seed = (seed ^ self._MULTIPLIER) & self._MASK

    def _next(self, bits: int) -> int:
        self._seed = (self._seed * self._MULTIPLIER + self._ADDEND) & self._MASK
        return self._seed >> (48 - bits)

    def next_double(self) -> float:
        """Número uniforme en [0, 1) con 53 bits de precisión."""
        return ((self._next(26) << 27) + self._next(27)) * (1.0 / (1 << 53))
