import constantes


def escribir_solucion(cantidad_prendas):
    output = open("solucion.txt", "w")
    for i in range(1, cantidad_prendas):
        val = str(i)
        output.write(f'{val} {val}\n')
    val = str(cantidad_prendas)
    output.write(f'{val} {val}')


def cargar_incompatibilidad(incompatibilidades, prenda1, prenda2):
    incomp_prenda1 = incompatibilidades.get(prenda1)
    if incomp_prenda1:
        incomp_prenda1.append(prenda2)
    else:
        incomp_prenda1 = [prenda2]

    incompatibilidades[prenda1] = incomp_prenda1


def cargar_costo(costos, prenda, costo):
    costos[prenda] = costo


def main():
    cant_incompatibilidades = 0
    cant_prendas = 0
    incompatibilidades = {}
    costos = {}

    with open("primer_problema.txt") as archivo:
        for linea in archivo:
            tipo_dato = linea[constantes.POS_TIPO_DATO]

            if tipo_dato == constantes.COMENTARIO:
                continue

            linea = linea.rstrip('\n')  # Quitar caracter nueva linea
            datos = linea.split(constantes.DATOS_SEP)

            if tipo_dato == constantes.FORMATO_PROBLEMA:
                cant_incompatibilidades = int(datos[constantes.POS_CANT_INCOMPATIBILIDADES])
                cant_prendas = int(datos[constantes.POS_CANT_PRENDAS])
            elif tipo_dato == constantes.INCOMPATIBILIDAD:
                cargar_incompatibilidad(
                    incompatibilidades,
                    int(datos[constantes.POS_PRENDA_INCOMPATIBLE_1]),
                    int(datos[constantes.POS_PRENDA_INCOMPATIBLE_2])
                )
            elif tipo_dato == constantes.TIEMPO_LAVADO:
                cargar_costo(
                    costos,
                    int(datos[constantes.POS_PRENDA_LAVADO]),
                    int(datos[constantes.POS_TIEMPO_LAVADO])
                )
            else:
                raise Exception("Contenido de linea incorrecto: " + tipo_dato)

    escribir_solucion(cant_prendas)


if __name__ == "__main__":
    main()
