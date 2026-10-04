from abc import ABC, abstractmethod


# ============================================================
# PATRÓN STRATEGY
# ============================================================

class EstrategiaTemperatura(ABC):
    """Interfaz para calcular el factor de temperatura Tf."""

    @abstractmethod
    def calcular(self, temp: float) -> float:
        pass


class TemperaturaInterpolada(EstrategiaTemperatura):
    """Calcula Tf interpolando linealmente entre los valores de la tabla."""

    TABLA = {
        10: 1.00, 12: 0.90, 14: 0.80, 16: 0.70, 18: 0.60,
        20: 0.50, 22: 0.40, 24: 0.30, 26: 0.20, 28: 0.10
    }

    def calcular(self, temp: float) -> float:
        if temp <= 10:
            return 1.00
        if temp >= 28:
            return 0.10

        claves = sorted(self.TABLA.keys())
        for i in range(len(claves) - 1):
            t1, t2 = claves[i], claves[i + 1]
            if t1 <= temp <= t2:
                v1, v2 = self.TABLA[t1], self.TABLA[t2]
                return v1 + (v2 - v1) * (temp - t1) / (t2 - t1)
        return 0.10


class EstrategiaClasificacion(ABC):
    """Interfaz para clasificar el índice I."""

    @abstractmethod
    def clasificar(self, indice: float) -> str:
        pass

    @abstractmethod
    def color(self, indice: float) -> str:
        pass


class ClasificacionEstandar(EstrategiaClasificacion):
    """Reglas definidas en el PDF."""

    def clasificar(self, indice: float) -> str:
        if indice < 0.40:
            return "Sin lluvia"
        elif indice < 0.60:
            return "Baja posibilidad"
        elif indice < 0.75:
            return "Lluvia probable"
        else:
            return "Lluvia"

    def color(self, indice: float) -> str:
        if indice < 0.40:
            return "#4CAF50"
        elif indice < 0.60:
            return "#FFEB3B"
        elif indice < 0.75:
            return "#FF9800"
        else:
            return "#F44336"