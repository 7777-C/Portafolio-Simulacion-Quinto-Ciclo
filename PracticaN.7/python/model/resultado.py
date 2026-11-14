"""MODELO - Estructura de datos con el resultado de un experimento."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Resultado:
    n: int
    pi_estimado: float
    puntos_dentro: int
    error_absoluto: float
    tiempo_ms: float
