from IDispositivoElectronico import IDispositivoElectronico

class Escaner(IDispositivoElectronico):
    
    def encender(self):
        print("Se encendió el Escaner")
    
    def apagar(self):
        print("Se apagó el Escaner")