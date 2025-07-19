from abc import ABC, abstractmethod

class GestorBase(ABC):
    @abstractmethod
    def crear(self, db, obj):
        pass

    @abstractmethod
    def obtener(self, db, id):
        pass

    @abstractmethod
    def actualizar(self, db, id, obj):
        pass

    @abstractmethod
    def eliminar(self, db, id):
        pass
