from abc import ABC, abstractmethod

class wifiAuditor(ABC):
    @abstractmethod
    def getWifiPassword(self):
        pass