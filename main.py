from parser_problema import cargar_prendas
from lavado import Lavado
from coloracion_grafo import obtener_prenda_mayor_grado
import time


def escribir_solucion(lavados):
    output = open("solucion.txt", "w")
    for lavado in lavados.values():
        for id_prenda in lavado.obtener_ids_prendas():
            output.write(f'{str(id_prenda)} {str(lavado.id)}\n')


# Se arman los lavados aplicando el algoritmo de Brelaz
def armar_lavados(lavados, prendas):
    # Ordenar prendas por cantidad incompatibilidades (mayor a menor)
    prendas_ord_costo_desc = list(prendas.values())
    prendas_ord_costo_desc.sort(key=lambda p: 0.5 * (p.costo + p.cantidad_incompatibles()), reverse=True)

    # Crear lavado con primer prenda
    id_lavado_actual = 1
    nuevo_lavado = Lavado(id_lavado_actual, prendas_ord_costo_desc[0])
    lavados[id_lavado_actual] = nuevo_lavado
    id_lavado_actual += 1

    # Ignorar prenda ya usada en primer lavado
    prendas_no_lavadas = list(map(lambda p: p, prendas_ord_costo_desc[1:]))
    cant_prendas_no_lavadas = len(prendas_no_lavadas)

    while cant_prendas_no_lavadas > 0:
        siguiente_prenda = obtener_prenda_mayor_grado(lavados, prendas_no_lavadas)
        prenda_agregada = False
        # Tratar de agregar prenda a lavado ya existente
        for lavado in lavados.values():
            prenda_agregada = lavado.agregar_prenda_si_compatible(siguiente_prenda)
            if prenda_agregada:
                break

        # Si no se pudo agregar la prenda a ningun lavado creo uno nuevo
        if not prenda_agregada:
            nuevo_lavado = Lavado(id_lavado_actual, siguiente_prenda)
            nuevo_lavado.agregar_prenda_si_compatible(siguiente_prenda)
            lavados[id_lavado_actual] = nuevo_lavado
            id_lavado_actual += 1

        # Como se agrego una nueva prenda se actualizan los valores
        prendas_no_lavadas.remove(siguiente_prenda)
        cant_prendas_no_lavadas -= 1


def main():
    start = time.time()
    prendas = {}    # Dict <id, prenda>
    lavados = {}    # Dict <id, lavado>
    cargar_prendas(prendas, "tercer_problema.txt")
    armar_lavados(lavados, prendas)
    escribir_solucion(lavados)
    end = time.time()

    costo_total = sum(map(lambda l: l.obtener_costo(), list(lavados.values())))
    print("Costo total: " + str(costo_total))
    print("Tiempo ejecución: " + str(end - start) + " segundos")


if __name__ == "__main__":
    main()
