"""
MODELO - Lógica del método de Monte Carlo para estimar π.

Se generan N puntos (x, y) uniformes en el cuadrado [-1, 1] x [-1, 1].
Un punto está dentro del círculo unitario si x² + y² <= 1.

    π ≈ 4 · (Nc / N)
"""
import math

from model.lcg_random import LcgRandom


class MonteCarloModel:
    PI_REAL = math.pi

    @staticmethod
    def contar_puntos_dentro(n: int, semilla: int) -> int:
        rng = LcgRandom(semilla)
        dentro = 0
        for _ in range(n):
            x = 2.0 * rng.next_double() - 1.0
            y = 2.0 * rng.next_double() - 1.0
            if x * x + y * y <= 1.0:
                dentro += 1
        return dentro

    @staticmethod
    def estimar_pi(n: int, puntos_dentro: int) -> float:
        return 4.0 * puntos_dentro / n

    @classmethod
    def error_absoluto(cls, pi_estimado: float) -> float:
        return abs(pi_estimado - cls.PI_REAL)

    @staticmethod
    def generar_puntos(n: int, semilla: int):
        """Devuelve (xs, ys, dentro[]) para visualización (misma secuencia)."""
        rng = LcgRandom(semilla)
        xs, ys, dentro = [], [], []
        for _ in range(n):
            x = 2.0 * rng.next_double() - 1.0
            y = 2.0 * rng.next_double() - 1.0
            xs.append(x)
            ys.append(y)
            dentro.append(x * x + y * y <= 1.0)
        return xs, ys, dentro
