"""Modelo: estimación de π por Monte Carlo usando pares (x, y) del LCG."""
import math
import time
from dataclasses import dataclass

from .lcg import GeneradorLCG


@dataclass
class ResultadoPi:
    n: int
    pi_estimado: float
    error: float
    tiempo_s: float


def estimar_pi(gen: GeneradorLCG, n: int) -> ResultadoPi:
    """Lanza n puntos (x,y) en el cuadrado unitario; cuenta los que caen
    dentro del cuarto de círculo x²+y² <= 1. π ≈ 4 * aciertos / n."""
    gen.reiniciar()
    inicio = time.perf_counter()
    aciertos = 0
    for _ in range(n):
        x = gen.siguiente()
        y = gen.siguiente()
        if x * x + y * y <= 1.0:
            aciertos += 1
    tiempo = time.perf_counter() - inicio
    pi = 4.0 * aciertos / n
    return ResultadoPi(n, pi, abs(math.pi - pi), tiempo)
