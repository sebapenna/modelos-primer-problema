import constantes
from prenda import Prenda


def _cargar_incompatibilidad(prendas, id_prenda1, id_prenda2):
    prenda = prendas.get(id_prenda1)
    if prenda:
        prenda.agregar_incompatibilidad(id_prenda2)
        prendas[id_prenda1] = prenda


def _cargar_costo(prendas, id_prenda, costo):
    prenda = prendas.get(id_prenda)
    if prenda:
        prenda.cargar_costo(costo)
        prendas[id_prenda] = prenda


def _cargar_prendas_no_lavadas(prendas, cant_prendas):
    for id_prenda in range(1, cant_prendas + 1):
        prendas[id_prenda] = Prenda(id_prenda)


# Carga todos los datos de cada prenda y los guarda en el
#   diccionario de prendas
def cargar_prendas(prendas, nombre_archivo):
    with open(nombre_archivo) as archivo:
        for linea in archivo:
            tipo_dato = linea[constantes.POS_TIPO_DATO]

            # Ignorar comentarios
            if tipo_dato == constantes.COMENTARIO:
                continue

            linea = linea.rstrip('\n')  # Quitar caracter nueva linea
            datos = linea.split(constantes.DATOS_SEP)

            if tipo_dato == constantes.FORMATO_PROBLEMA:
                _cargar_prendas_no_lavadas(
                    prendas,
                    int(datos[constantes.POS_CANT_PRENDAS])
                )
            elif tipo_dato == constantes.INCOMPATIBILIDAD:
                # Cargar incopatibilidad en ambos sentidos
                _cargar_incompatibilidad(
                    prendas,
                    int(datos[constantes.POS_PRENDA_INCOMPATIBLE_1]),
                    int(datos[constantes.POS_PRENDA_INCOMPATIBLE_2])
                )
                _cargar_incompatibilidad(
                    prendas,
                    int(datos[constantes.POS_PRENDA_INCOMPATIBLE_2]),
                    int(datos[constantes.POS_PRENDA_INCOMPATIBLE_1])
                )
            elif tipo_dato == constantes.TIEMPO_LAVADO:
                _cargar_costo(
                    prendas,
                    int(datos[constantes.POS_PRENDA_LAVADO]),
                    int(datos[constantes.POS_TIEMPO_LAVADO])
                )
            else:
                raise Exception("Contenido de linea incorrecto: " + tipo_dato)
