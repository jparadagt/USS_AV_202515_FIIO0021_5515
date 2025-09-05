from abc import ABC, abstractmethod


# Clase base Producto
class Producto(ABC):

  def __init__(self, nombre: str, precio: float):
    # Se multiplica por 1.5 para aplicar ajuste de precios
    self._nombre = nombre
    self._precio = precio * 1.5

  @property
  def nombre(self):
    return self._nombre

  @abstractmethod
  def calcular_precio(self) -> float:
    pass


# Producto especial para entradas inválidas
class ProductoInvalido(Producto):

  def __init__(self):
    super().__init__("Opción inválida", 0)

  def calcular_precio(self) -> float:
    return 0


# Clase Alimento
class Alimento(Producto):

  def __init__(self, nombre: str, precio: float, es_vegano: bool = False):
    super().__init__(nombre, precio)

    self._es_vegano = es_vegano

  def calcular_precio(self) -> float:
    # Promoción 5% si es vegano
    if self._es_vegano:
      return self._precio * 0.95
    else:
      return self._precio


# Clase Bebida
class Bebida(Producto):

  def __init__(self, nombre: str, precio: float, tamano: str):
    super().__init__(nombre, precio)
    self._tamano = tamano

  def calcular_precio(self) -> float:
    # Descuento 10% en bebidas grandes
    if self._tamano.lower() == "grande":
      return self._precio * 0.9
    return self._precio


class Pedido:

  def __init__(self, cliente: str):
    self._cliente = cliente
    self._productos = []

  def agregar_producto(self, producto: Producto):
    self._productos.append(producto)

  def calcular_total(self) -> float:
    return sum(p.calcular_precio() for p in self._productos)

  def mostrar_detalle(self):
    print(f"\nPedido de {self._cliente}:")

    for p in self._productos:
      print(f"- {p.nombre}: ${p.calcular_precio():.0f}".replace(",", "."))

    print(f"Total: ${self.calcular_total():.0f}".replace(",", "."))
