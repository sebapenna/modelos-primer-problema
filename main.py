import constantes

def escribir_solucion(cantidad_prendas):
    output = open("solucion.txt", "w")
    for i in range(1, cantidad_prendas):
        val = str(i)
        output.write(f'{val} {val}\n')
    val = str(cantidad_prendas)
    output.write(f'{val} {val}')

def main():
    cant_incompatibilidades = 0
    cant_prendas = 0

    with open("primer_problema.txt") as archivo:
        for linea in archivo:
            tipo_dato = linea[constantes.POS_TIPO_DATO]

            if tipo_dato == constantes.COMENTARIO:
                continue

            linea = linea.rstrip('\n')    # Quitar caracter nueva linea
            datos = linea.split(constantes.DATOS_SEP)

            if tipo_dato == constantes.FORMATO_PROBLEMA:
                cant_incompatibilidades = int(datos[constantes.POS_CANT_INCOMPATIBILIDADES])
                cant_prendas = int(datos[constantes.POS_CANT_PRENDAS])
            elif tipo_dato == constantes.INCOMPATIBILIDAD:
                pass # todo: cargar incompatibilidades
            elif tipo_dato == constantes.TIEMPO_LAVADO:
                pass # todo: cargar costos
            else:
                raise Exception("Contenido de linea incorrecto: " + tipo_dato)

    escribir_solucion(cant_prendas)


if __name__ == "__main__":
    main()
