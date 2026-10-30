# models/continuo_euler.py
import numpy as np
from models.base_model import BaseModel


class ModeloContinuoEuler(BaseModel):
    """dP/dt = rP  aproximado con Euler: P(t+dt) = P(t) + dt*r*P(t)."""

    def __init__(self, p0, r, tiempo, dt):
        super().__init__(p0, r, tiempo)
        self.dt = dt

    def simular(self):
        n = int(self.tiempo / self.dt)
        t = np.linspace(0, self.tiempo, n + 1)
        p = np.zeros(n + 1)
        p[0] = self.p0
        for i in range(1, n + 1):
            cambio = self.r * p[i - 1]
            p[i] = p[i - 1] + self.dt * cambio
        return t, p