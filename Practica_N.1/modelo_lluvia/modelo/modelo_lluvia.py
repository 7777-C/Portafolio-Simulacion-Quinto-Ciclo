from .estrategias import EstrategiaTemperatura, EstrategiaClasificacion


class ModeloLluvia:

    def __init__(self,
                 estrategia_temp: EstrategiaTemperatura,
                 estrategia_clas: EstrategiaClasificacion):
        self.estrategia_temp = estrategia_temp
        self.estrategia_clas = estrategia_clas

    def calcular_indice(self, humedad, nubosidad, temp):
        H = humedad / 100
        N = nubosidad / 100
        Tf = self.estrategia_temp.calcular(temp)
        I = 0.5 * H + 0.3 * N + 0.2 * Tf
        return I, H, N, Tf

    def procesar(self, horas, humedad, nubosidad, temperatura):
        
        resultados = []
        for i in range(len(horas)):
            I, H, N, Tf = self.calcular_indice(
                humedad[i], nubosidad[i], temperatura[i]
            )
            resultados.append({
                "hora": horas[i],
                "humedad": humedad[i],
                "nubosidad": nubosidad[i],
                "temp": temperatura[i],
                "H": H, "N": N, "Tf": Tf, "I": I,
                "estado": self.estrategia_clas.clasificar(I),
                "color": self.estrategia_clas.color(I)
            })
        return resultados