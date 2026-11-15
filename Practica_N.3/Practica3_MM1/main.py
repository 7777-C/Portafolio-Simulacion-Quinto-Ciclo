from Controller.controlador_mm1 import ControladorMM1

if __name__ == "__main__":
    app = ControladorMM1()
    app.ejecutar()


'''Primer paso:
sudo apt update
sudo apt install python3-venv -y
'''

"""Segundo paso:
cd ~/Documents/Quinto\ Ciclo/Practica_N.3/Practica3_MM1
/usr/bin/python3 -m venv .venv
source .venv/bin/activate
pip install simpy==4.1.2 matplotlib==3.11.2 numpy==2.5.4
python main.py
"""