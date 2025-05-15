from strategies.netshStrategy import netshStrategy
from utils.exporter import exportToCsv

class wifiAuditor:
    def __init__(self, strategy=None):
        self.strategy = strategy or netshStrategy()
    
    def runAuditor(self, export = False):
        print('starting audit wifi')
        results = self.strategy.getWifiPassword()
        print('Results: ')
        for wifi in results:
            print(f'SSID: {wifi["SSID"]} Contraseña: {wifi["Password"]}')
        
        if export:
            exportToCsv(results)
        return results
    