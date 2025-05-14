from abc import ABC, abstractmethod

class wifiStrategy(ABC):
    @abstractmethod
    def getWifiPassword(self):
        pass