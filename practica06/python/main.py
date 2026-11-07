"""Práctica 06 - Validación estadística de números pseudoaleatorios (Python)."""
from controlador.controlador import Controlador
from vista.vista_consola import VistaConsola

if __name__ == "__main__":
    Controlador(VistaConsola()).ejecutar_todo()
