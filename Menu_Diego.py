
MENU_CATEGORIAS = [
    {"nombre": "Hamburguesa", "categoria": "Comida", "precio": 8.50},
    {"nombre": "Pizza", "categoria": "Comida", "precio": 12.00},
    {"nombre": "hot dog", "categoria": "Comida", "precio": 10.00},
    {"nombre": "cocacola", "categoria": "bebida", "precio": 7.00},
    {"nombre": "agua", "categoria": "bebida", "precio": 5.00},
    {"nombre": "cerveza", "categoria": "bebida", "precio": 9.00},
    {"nombre": "papas", "categoria": "adicionales", "precio": 6.00},
    {"nombre": "ensalada", "categoria": "adicionales", "precio": 7.50},
    {"nombre": "queso extra", "categoria": "adicionales", "precio": 4.00}
]


def calcular_precio_total(categoria,precio):
    
    categoria_objetivo = ("Comida", "adicionales")
    umbral_descuento = 5.00

    if categoria in categoria_objetivo and precio > umbral_descuento:
        descuento = precio * 0.15
        precio_final = precio - descuento
    else:
        precio_final = precio

    return precio_final

for producto in MENU_CATEGORIAS:
    nombre = producto["nombre"]
    categoria = producto["categoria"]
    precio = producto["precio"]

    precio_final = calcular_precio_total(categoria, precio)

    print(f"Producto: {nombre},\n Precio Original: ${precio:.2f},\n Precio Final: ${precio_final:.2f}")