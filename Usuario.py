class Usuario:

    mensajesTotal = 0
    ubicacion = 0
    salud = 0
    drogas = 0
    sentiment = 0
    detallesPersonales = 0
    insultos = 0
    videos = 0
    malosVideos = 0
    imagenes_blanco = 0
    spam = 0



    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def sumaUbicación(self):
        self.ubicacion += 1

    def sumaSalud(self):
        self.salud += 1

    def sumaDrogas(self):
        self.drogas += 1

    def sumaSentiment(self):
        self.sentiment += 1

    def sumaDetallesPersonales(self):
        self.detallesPersonales += 1

    def sumaInsultos(self):
        self.insultos += 1

    def sumaVideos(self):
        self.videos += 1

    def sumaMalosVideos(self):
        self.malosVideos += 1

    def sumaImagenes(self):
        self.imagenes_blanco += 1

    def sumaSpam(self):
        self.spam += 1

    def sumaTotal(self):
        self.mensajesTotal += 1