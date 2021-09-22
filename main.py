from parser import cargar_prendas
from lavado import Lavado


def escribir_solucion(lavados):
    output = open("solucion.txt", "w")
    for lavado in lavados.values():
        for id_prenda in lavado.obtener_ids_prendas():
            output.write(f'{str(id_prenda)} {str(lavado.id)}\n')


def armar_lavados(lavados, prendas):
    # Ordenar prendas por cantidad incompatibilidades (mayor a menor)
    prendas_ord_incomp = list(prendas.values())
    prendas_ord_incomp.sort(key=lambda p: p.cantidad_incompatibles(), reverse=True)

    id_lavado_actual = 1
    ids_prendas_no_lavadas = list(map(lambda p: p.id, prendas_ord_incomp))
    for prenda in list(prendas_ord_incomp):
        # Saltear prenda si ya fue lavada
        if prenda.id not in ids_prendas_no_lavadas:
            continue

        nuevo_lavado = Lavado(id_lavado_actual, prenda)

        for id_prenda in ids_prendas_no_lavadas:
            nuevo_lavado.agregar_prenda_si_compatible(prendas[id_prenda])

        for p in nuevo_lavado.obtener_ids_prendas():
            ids_prendas_no_lavadas.remove(p)

        if nuevo_lavado.tiene_prendas():
            lavados[id_lavado_actual] = nuevo_lavado
            id_lavado_actual += 1

        if not ids_prendas_no_lavadas:  # No quedan prendas por lavar
            break


def main():
    prendas = {}    # Dict <id, prenda>
    lavados = {}    # Dict <id, lavado>
    cargar_prendas(prendas, "primer_problema.txt")
    armar_lavados(lavados, prendas)
    escribir_solucion(lavados)

    costo_total = sum(map(lambda l: l.obtener_costo(), list(lavados.values())))
    print("Costo total: " + str(costo_total))


if __name__ == "__main__":
    main()
