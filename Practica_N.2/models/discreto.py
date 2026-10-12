# models/discreto.py
import numpy as np
from models.base_model import BaseModel


class ModeloDiscreto(BaseModel):
    """P(t+1) = P(t) + r*P(t)  — intervalos discretos."""

    def simular(self):
        n = int(self.tiempo)
        t = np.arange(0, n + 1)
        p = np.zeros(n + 1)
        p[0] = self.p0
        for i in range(1, n + 1):
            p[i] = p[i - 1] + self.r * p[i - 1]
        return t, p