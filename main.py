from models import Bebida, Alimento, ProductoInvalido, Pedido
from cafeteria import Cafeteria

if __name__ == "__main__":
  # Menú de Bebidas (10 opciones)
  bebidas = [
      Bebida("Café Americano", 2500, "grande"),
      Bebida("Café Expreso", 2000, "pequeño"),
      Bebida("Capuchino", 3000, "mediano"),
      Bebida("Latte", 3200, "grande"),
      Bebida("Mocaccino", 3500, "mediano"),
      Bebida("Té Verde", 2000, "mediano"),
      Bebida("Té Negro", 1800, "pequeño"),
      Bebida("Jugo Natural de Naranja", 2800, "grande"),
      Bebida("Jugo de Frutilla", 3000, "mediano"),
      Bebida("Chocolate Caliente", 3200, "grande")
  ]

  # Menú de Alimentos (15 opciones, incluye comida típica de Chile)
  alimentos = [
      Alimento("Empanada de Pino", 2500),
      Alimento("Empanada de Queso", 2000),
      Alimento("Completo Italiano", 3000),
      Alimento("Sopaipilla", 1000, True),
      Alimento("Pastel de Choclo", 5000),
      Alimento("Cazuela de Vacuno", 6000),
      Alimento("Humita", 3500, True),
      Alimento("Ensalada Chilena", 2500, True),
      Alimento("Mote con Huesillo", 2000, True),
      Alimento("Croissant", 3000),
      Alimento("Sandwich Vegano", 4000, True),
      Alimento("Muffin de Chocolate", 2500),
      Alimento("Tarta de Manzana", 3200),
      Alimento("Sándwich Barros Luco", 4500),
      Alimento("Sándwich Chacarero", 4800)
  ]

  cafeteria = Cafeteria()

  while True:
    cliente = input("\nIngrese el nombre del cliente: ")
    pedido = Pedido(cliente)

    # Elegir bebida
    print("\nMenú de Bebidas:")

    for i, b in enumerate(bebidas, start=1):
      print(f"{i}. {b.nombre} - ${b.calcular_precio():.0f}".replace(",", "."))

    try:
      opcion_bebida = int(input("Elija una bebida: "))

      if 1 <= opcion_bebida <= len(bebidas):
        pedido.agregar_producto(bebidas[opcion_bebida - 1])
      else:
        print("Debe seleccionar una opción válida del menú.")

        pedido.agregar_producto(ProductoInvalido())
    except ValueError:
      print("Debe seleccionar una opción válida del menú.")
      pedido.agregar_producto(ProductoInvalido())

    # Elegir alimento
    print("\nMenú de Alimentos:")

    for i, a in enumerate(alimentos, start=1):
      print(f"{i}. {a.nombre} - ${a.calcular_precio():.0f}".replace(",", "."))

    try:
      opcion_alimento = int(input("Elija un alimento: "))

      if 1 <= opcion_alimento <= len(alimentos):
        pedido.agregar_producto(alimentos[opcion_alimento - 1])
      else:
        print("Debe seleccionar una opción válida del menú.")

        pedido.agregar_producto(ProductoInvalido())
    except ValueError:
      print("Debe seleccionar una opción válida del menú.")
      pedido.agregar_producto(ProductoInvalido())

    cafeteria.registrar_pedido(pedido)

    # Preguntar si desea otro pedido
    otro = input("\n¿Desea realizar otro pedido? (si/no): ").lower()

    if otro != "si":
      break

  # Procesar pedidos en paralelo
  cafeteria.procesar_pedidos_concurrentes()
