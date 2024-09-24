from IDispositivoElectronico import IDispositivoElectronico
from IConectividad import IConectividad

class ImpresoraWifi(IDispositivoElectronico, IConectividad):
    
    def encender(self):
        print("Se encendió la impresora con Wifi")
    
    def apagar(self):
        print("Se apagó la impresora con Wifi")
    
    def conectar(self):
        print("Conectando a una red wifi ...")