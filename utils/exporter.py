import csv
from datetime import datetime

def exportToCsv(results, fileName = None):
    fileName =  fileName or f"wifi_passwords_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(fileName,mode='w',newline='',encoding='utf-8') as file:
        fieldNames = ['SSID', 'Password']
        writer = csv.DictWriter(file,fieldnames=fieldNames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
        print(f'Exported to {fileName}')