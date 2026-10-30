import matplotlib.pyplot as plt

class LCGView:
    @staticmethod
    def print_table(raw_values, norm_values, count=20):
        """Muestra los primeros 'count' elementos en formato de tabla."""
        print(f"\n{'i':<5} | {'X_i (Entero)':<15} | {'U_i (Normalizado)':<20}")
        print("-" * 45)
        for i in range(min(count, len(raw_values))):
            print(f"{i+1:<5} | {raw_values[i]:<15} | {norm_values[i]:<20.8f}")

    @staticmethod
    def plot_sequence(norm_values, title="Secuencia LCG", filename="grafica_lcg.png"):
        """Grafica los valores pseudoaleatorios y guarda la imagen automáticamente."""
        plt.figure(figsize=(10, 5))
        plt.plot(norm_values[:200], marker='o', linestyle='none', markersize=3, alpha=0.7)
        plt.title(title)
        plt.xlabel("Iteración (i)")
        plt.ylabel("Valor Normalizado U(i)")
        plt.grid(True)
        
        # Guardar la imagen en disco antes de mostrarla
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"\n[INFO] Gráfica guardada exitosamente como '{filename}'")
        
        plt.show()