import numpy as np
from models.base_model import BaseModel


class ModeloDeterministico(BaseModel):
    """P(t) = P0 * e^(r*t)  — sin aleatoriedad."""

    def simular(self):
        t = np.linspace(0, self.tiempo, 200)
        p = self.p0 * np.exp(self.r * t)
        return t, p