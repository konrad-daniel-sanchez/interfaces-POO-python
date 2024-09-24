from IDispositivoElectronico import IDispositivoElectronico

class Impresora(IDispositivoElectronico):
    
    def encender(self):
        print("Se encendió la impresora")
    
    def apagar(self):
        print("Se apagó la impresora")