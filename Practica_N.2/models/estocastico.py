# models/estocastico.py
import numpy as np
from models.base_model import BaseModel


class ModeloEstocastico(BaseModel):
    """P(t+1) = P(t) + r*P(t) + ε,  ε ~ N(0, σ²)."""

    def __init__(self, p0, r, tiempo, sigma, semilla=42):
        super().__init__(p0, r, tiempo)
        self.sigma = sigma
        self.semilla = semilla

    def simular(self):
        rng = np.random.default_rng(self.semilla)
        n = int(self.tiempo)
        t = np.arange(0, n + 1)
        p = np.zeros(n + 1)
        p[0] = self.p0
        for i in range(1, n + 1):
            ruido = rng.normal(0, self.sigma)
            nueva = p[i - 1] + self.r * p[i - 1] + ruido
            p[i] = max(nueva, 0)  # No permitir poblaciones negativas
        return t, p