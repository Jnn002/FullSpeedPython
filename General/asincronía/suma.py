import asyncio

async def suma(a, b):
    print('Inicio de la suma', a, '+', b)
    await asyncio.sleep(1)
    print('Fin de la suma', a, '+', b)
    return a + b

# evento loop
loop = asyncio.get_event_loop()

# Ejecutar funcion asincrona
resultado = loop.run_until_complete(asyncio.gather(
    suma(5, 4),
    suma(34,2),
    suma(34,19)
    ))
for operacion in resultado:
    print(f'El resultado de la suma es {operacion}')

# cerrar el loop
loop.close()