#!/usr/bin/python3

"""ESTRELLA MAYRANI DIAZ RODRIGUEZ
MARIA FERNANDA MACIAS ROMO
EDGAR RODRIGUEZ PEREZ"""

import subprocess
import re

try:
   #puertos estándar
   std_ports = [22, 25, 80, 465, 587, 8080]
   conexiones = []

   execute_script = subprocess.run(['bash', 'monitor_conexiones.sh'], capture_output=True, text=True, check=True)
   execute_script.check_returncode()
   result = execute_script.stdout

   for i in result.splitlines():
      #expresión regular para buscar puertos (ej. :22) 
      coincidencia = re.search(r':(\d+)', i)
      if coincidencia:
            #convierte el puerto a número entero para comparar int == int
            port = int(coincidencia.group(1))
            if port not in std_ports:
               conexiones.append(i)

   if conexiones:
      with open('reporte_conexiones.txt', 'w') as file:
            file.write('Conexiones encontradas\n')
            for j in conexiones:
               file.write(j + '\n')
   else:
      with open('reporte_conexiones.txt', 'w') as file:
            file.write('No se encontraron conexiones.')
   
   print("Se creo el reporte txt :D")    
except subprocess.CalledProcessError as err:
   print(f'Falló al ejecutar el script de BASH: código >> {err.returncode}')
   print(f'Ocurrió un error inesperado >> {err.stderr}')