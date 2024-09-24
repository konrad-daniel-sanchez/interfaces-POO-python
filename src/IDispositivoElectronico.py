from abc import ABC, abstractmethod

class IDispositivoElectronico(ABC):
    
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass