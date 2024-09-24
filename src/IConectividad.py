from abc import ABC, abstractmethod

class IConectividad(ABC):
    
    @abstractmethod
    def conectar(self):
        pass