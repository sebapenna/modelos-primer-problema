class Prenda:
    def __init__(self, id):
        self.id = id
        self.costo = 0
        self.ids_prendas_incompatibles = []

    def cargar_costo(self, costo):
        self.costo = costo

    def agregar_incompatibilidad(self, id_incomp):
        # Solo agregar incompatibilidad si id no fue cargado previamente
        if id_incomp not in self.ids_prendas_incompatibles:
            self.ids_prendas_incompatibles.append(id_incomp)

    def cantidad_incompatibles(self):
        return len(self.ids_prendas_incompatibles)
