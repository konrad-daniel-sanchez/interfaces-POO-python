from Impresora import Impresora
from Escaner import Escaner
from Celular import Celular
from ImpresoraWifi import ImpresoraWifi

if __name__ == "__main__":
    
    dispositivos = [None] * 10
    
    dispositivos[0] = Impresora()
    dispositivos[1] = Escaner()
    dispositivos[2] = Celular()
    dispositivos[3] = ImpresoraWifi()
    
    for dispositivo in dispositivos:
        if dispositivo is not None:
            dispositivo.encender()
            dispositivo.apagar()
    
    impresoraWifi = ImpresoraWifi()
    impresoraWifi.encender()
    impresoraWifi.conectar()
    impresoraWifi.apagar()