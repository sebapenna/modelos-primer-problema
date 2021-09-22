class Prenda:
    def __init__(self, id):
        self.id = id
        self.costo = 0
        self.ids_prendas_incompatibles = []

    def cargar_costo(self, costo):
        self.costo = costo

    def agregar_incompatibilidad(self, id_incomp):
        self.ids_prendas_incompatibles.append(id_incomp)
