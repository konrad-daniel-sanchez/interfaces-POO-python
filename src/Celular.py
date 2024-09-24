from IDispositivoElectronico import IDispositivoElectronico

class Celular(IDispositivoElectronico):
    def encender(self):
        print("Se encendió el celular")
    
    def apagar(self):
        print("Se Apagó el celular")