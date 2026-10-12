from abc import ABC, abstractmethod


class BaseModel(ABC):

    def __init__(self, p0: float, r: float, tiempo: float):
        self.p0 = p0
        self.r = r
        self.tiempo = tiempo

    @abstractmethod
    def simular(self):
        """Devuelve (tiempo, poblacion)."""
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(p0={self.p0}, r={self.r}, tiempo={self.tiempo})"