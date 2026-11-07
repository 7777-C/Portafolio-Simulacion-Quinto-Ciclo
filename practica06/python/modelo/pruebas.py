"""Modelo: pruebas de bondad de ajuste Chi-cuadrado y Kolmogorov-Smirnov."""
from dataclasses import dataclass, field

from .funciones_especiales import p_valor_chi2, p_valor_ks

ALFA = 0.05


@dataclass
class ResultadoChi2:
    observadas: list[int]
    esperada: float
    estadistico: float
    grados_libertad: int
    p_valor: float
    rechaza_h0: bool


@dataclass
class ResultadoKS:
    d_mas: float
    d_menos: float
    estadistico: float
    p_valor: float
    rechaza_h0: bool
    ordenados: list[float] = field(repr=False, default_factory=list)


def prueba_chi_cuadrado(datos: list[float], k: int = 10, alfa: float = ALFA) -> ResultadoChi2:
    n = len(datos)
    esperada = n / k
    observadas = [0] * k
    for u in datos:
        idx = min(int(u * k), k - 1)
        observadas[idx] += 1
    chi2 = sum((o - esperada) ** 2 / esperada for o in observadas)
    gl = k - 1
    p = p_valor_chi2(chi2, gl)
    return ResultadoChi2(observadas, esperada, chi2, gl, p, p < alfa)


def prueba_ks(datos: list[float], alfa: float = ALFA) -> ResultadoKS:
    ordenados = sorted(datos)
    n = len(ordenados)
    d_mas = 0.0
    d_menos = 0.0
    for i, x in enumerate(ordenados, start=1):
        f_teorica = x                        # F(x) = x en U(0,1)
        d_mas = max(d_mas, i / n - f_teorica)
        d_menos = max(d_menos, f_teorica - (i - 1) / n)
    d = max(d_mas, d_menos)
    p = p_valor_ks(d, n)
    return ResultadoKS(d_mas, d_menos, d, p, p < alfa, ordenados)
