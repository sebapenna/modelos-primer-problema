# El grado de saturacion es el numero de colores usados en
# los vecinos (prendas incompatibles) del vertice (la prenda)
def _grado_saturacion(lavados, prenda):
    ids_lavados_vecinos = []
    for id_prenda in prenda.ids_prendas_incompatibles:
        for lavado in lavados.values():
            # Verifico que el lavado no haya sido anotado y contenga la prenda
            if lavado.id not in ids_lavados_vecinos and lavado.contiene_id_prenda(id_prenda):
                ids_lavados_vecinos.append(lavado.id)
                break
    return len(ids_lavados_vecinos)


# Devuelve prenda con mayor grado de saturacion
# Si mas de una prenda tiene el mismo grado de saturacion
# entonces se devuelve la que tenga mayor grado
def obtener_prenda_mayor_grado(lavados, prendas_no_lavadas):
    max_grado_saturacion = 0
    prendas_max_grado_saturacion = []
    for prenda in prendas_no_lavadas:
        grado_staturacion_prenda = _grado_saturacion(lavados, prenda)
        if grado_staturacion_prenda > max_grado_saturacion:
            # Nuevo maximo grado saturacion
            prendas_max_grado_saturacion.clear()
            prendas_max_grado_saturacion.append(prenda)
            max_grado_saturacion = grado_staturacion_prenda
        elif grado_staturacion_prenda == max_grado_saturacion:
            # Prenda comparte grado de saturacion con maximo actual
            prendas_max_grado_saturacion.append(prenda)

    # Ordeno prendas con mayor grado de saturacion en base a su grado
    prendas_max_grado_saturacion.sort(key=lambda p: p.cantidad_incompatibles(), reverse=True)

    # Devuelvo primer prenda que tenga mayor grado
    return prendas_max_grado_saturacion[0]
