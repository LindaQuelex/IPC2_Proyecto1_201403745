class NodoCelda():
    def __init__(self, color ):
       
        # self.filacelda = r
        # self.columnacelda = c
        self.colorcelda =color
        self.siguiente = None
        self.anterior = None    

    # def getcodigopatron(self):
    #     return self.codigopatron

    # def setcodigopatron(self, codigopatron):
    #     self.codigopatron = codigopatron

    # def getfilacelda(self):
    #     return self.filacelda

    # def setfilacelda(self, filacelda):
    #     self.filacelda = filacelda

    # def getcolumnacelda(self):
    #     return self.columnacelda

    # def setcolumnacelda(self, columnacelda):
    #     self.columnacelda = columnacelda

    def getcolorcelda(self):
        return self.colorcelda

    def setcolorcelda(self, colorcelda):
        self.colorcelda = colorcelda


    def getanterior(self):
        return self.anterior

    def setanterior(self, nuevacelda):
        self.anterior = nuevacelda
   

    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, nuevacelda):
        self.siguiente = nuevacelda