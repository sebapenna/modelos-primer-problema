class Lavado:
    def __init__(self, id, prenda):
        self.id = id
        self.prendas = []
        self.ids_prendas_incompatibles = []
        self._agregar_prenda(prenda)

    def _agregar_prenda(self, prenda):
        if prenda not in self.prendas:
            # Cargar nueva prenda
            self.prendas.append(prenda)

            # Cargar nuevas prendas incompatibles
            self.ids_prendas_incompatibles.extend(
                prenda.ids_prendas_incompatibles
            )

    def _es_compatible(self, id_prenda):
        return id_prenda not in self.ids_prendas_incompatibles

    # Devuelve verdadero si la prenda era compatible y se agrego al lavado
    # Falso si no se pudo agregar
    def agregar_prenda_si_compatible(self, prenda):
        if self._es_compatible(prenda.id):
            self._agregar_prenda(prenda)
            return True
        return False

    def tiene_prendas(self):
        return self.prendas

    def obtener_ids_prendas(self):
        return map(lambda p: p.id, self.prendas)

    def obtener_costo(self):
        return max(map(lambda p: p.costo, self.prendas))

    def contiene_id_prenda(self, id_prenda):
        return id_prenda in self.obtener_ids_prendas()
