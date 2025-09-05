from models import Pedido
import threading
import time


class Cafeteria:

  def __init__(self):
    self._pedidos = []

  def registrar_pedido(self, pedido: Pedido):
    self._pedidos.append(pedido)

  def procesar_pedido(self, pedido: Pedido):
    print(f"\nProcesando pedido de {pedido._cliente}...")

    time.sleep(2)  # Simula tiempo de preparación
    pedido.mostrar_detalle()

    print("Gracias por su compra. ¡Buen día!")

  def procesar_pedidos_concurrentes(self):
    hilos = []

    for pedido in self._pedidos:
      hilo = threading.Thread(target=self.procesar_pedido, args=(pedido, ))

      hilos.append(hilo)
      hilo.start()

    for h in hilos:
      h.join()
