"""ESTRELLA MAYRANI DIAZ RODRIGUEZ
MARIA FERNANDA MACIAS ROMO
EDGAR RODRIGUEZ PEREZ"""

from openpyxl import Workbook
import csv
import subprocess
import os

print('Podrás ver el CSV y el Excel en ',os.getcwd())

ps_script = 'monitor_servicios.ps1'
csv_file = 'services.csv'
excel_file = 'services.xlsx'

workbook = Workbook()
worksheet = workbook.active

try:
   execute_script = subprocess.run(['powershell', '-File', ps_script], capture_output=True, text=True, check=True)
except subprocess.CalledProcessError as e:
   print(f"Ocurrió un error al intentar ejecutar el script de PowerShell: \n{e}")
else:
   with open(csv_file, newline = '', encoding = 'UTF-8') as file:
      csv_read = csv.reader(file)
      for i in csv_read:
         worksheet.append(i)

cellsWithData = sum(1 for row in worksheet.iter_rows() for cell in row if cell.value)

if cellsWithData > 0:
   workbook.save(excel_file)
   print("El archivo de Excel se creó.")
else:
   print("No se pudo crear el archivo. No hay datos.")