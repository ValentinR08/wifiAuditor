from .facade import wifiAuditor

if __name__ == '__main__':
    auditor = wifiAuditor()
    auditor.runAuditor()