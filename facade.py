from .strategies.netshStrategy import netshStrategy

class wifiAuditor:
    def __init__(self, strategy=None):
        self.strategy = strategy or netshStrategy()
    
    def runAuditor(self):
        print('iniciando la auditoría de wifi')
        results = self.strategy.getWifiPassword()
        print('Resultados: ')
        for wifi in results:
            print(f'SSID: {wifi["SSID"]} Contraseña: {wifi["Password"]}')
        return results