from controllers.lcg_controller import LCGController

if __name__ == "__main__":
    # Inicializar controlador con la semilla predeterminada (12345)
    controller = LCGController(seed=12345)
    controller.run_simulation(total_samples=10000, table_preview=20)
