import subprocess
import re
from .baseStrategy import wifiStrategy

class netshStrategy(wifiStrategy):
    def getWifiPassword(self):
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], encoding='utf-8', errors='ignore')
        profile_names = re.findall(r"Perfil de todos los usuarios\s*:\s(.*)", data)
        
        results = []
        for name in profile_names:
            name = name.strip().replace('"', '')
            try:
                result = subprocess.check_output(
                    ['netsh', 'wlan', 'show', 'profile', name, 'key=clear'],
                    encoding='utf-8', errors='ignore'
                )
                password_match = re.search(r"Contenido de la clave\s*:\s(.*)", result)
                password = password_match.group(1).strip() if password_match else "No founded"
                results.append({'SSID': name, 'Password': password})
            except subprocess.CalledProcessError:
                results.append({'SSID': name, 'Password': 'Error to get password'})
        
        return results