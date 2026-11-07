"""Modelo: funciones especiales para calcular valores p sin librerías externas
(así Python y Java usan exactamente el mismo método numérico)."""
import math


def gamma_q(a: float, x: float) -> float:
    """Gamma incompleta regularizada superior Q(a, x) (Numerical Recipes)."""
    if x <= 0:
        return 1.0
    gln = math.lgamma(a)
    if x < a + 1.0:                       # serie
        ap, suma = a, 1.0 / a
        delta = suma
        for _ in range(1000):
            ap += 1.0
            delta *= x / ap
            suma += delta
            if abs(delta) < abs(suma) * 1e-15:
                break
        return 1.0 - suma * math.exp(-x + a * math.log(x) - gln)
    # fracción continua (Lentz)
    tiny = 1e-300
    b = x + 1.0 - a
    c = 1.0 / tiny
    d = 1.0 / b
    h = d
    for i in range(1, 1000):
        an = -i * (i - a)
        b += 2.0
        d = an * d + b
        if abs(d) < tiny:
            d = tiny
        c = b + an / c
        if abs(c) < tiny:
            c = tiny
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < 1e-15:
            break
    return math.exp(-x + a * math.log(x) - gln) * h


def p_valor_chi2(estadistico: float, gl: int) -> float:
    """P(X >= estadistico) con X ~ Chi-cuadrado(gl)."""
    return gamma_q(gl / 2.0, estadistico / 2.0)


def p_valor_ks(d: float, n: int) -> float:
    """p-valor asintótico de Kolmogorov-Smirnov (corrección de Stephens)."""
    if d <= 0:
        return 1.0
    sq = math.sqrt(n)
    lam = (sq + 0.12 + 0.11 / sq) * d
    suma = 0.0
    for k in range(1, 101):
        termino = 2.0 * (-1) ** (k - 1) * math.exp(-2.0 * k * k * lam * lam)
        suma += termino
        if abs(termino) < 1e-16:
            break
    return min(1.0, max(0.0, suma))
