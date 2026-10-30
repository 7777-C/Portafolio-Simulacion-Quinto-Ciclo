from models.lcg_model import LCGModel
from views.lcg_view import LCGView

class LCGController:
    def __init__(self, seed=12345):
        self.model = LCGModel(seed=seed)
        self.view = LCGView()

    def run_simulation(self, total_samples=10000, table_preview=20):
        raw, norm = self.model.generate_sequence(n=total_samples)
        print(f"--- RESULTADOS LCG (Semilla: {self.model.seed}) ---")
        self.view.print_table(raw, norm, count=table_preview)
        self.view.plot_sequence(norm, title=f"Secuencia LCG - Semilla: {self.model.seed}")
