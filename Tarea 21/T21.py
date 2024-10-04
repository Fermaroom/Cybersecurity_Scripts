# Usar la API de Have I been pwn?
import requests
import json
import logging
import os

key = 'ec1e2ebed1754f1b8c00f2b90aa15906'
headers = {}
headers['content-type']= 'application/json'
headers['api-version']= '3'
headers['User-Agent']='python'

#Place that API key here
headers['hibp-api-key']= key

#Preguntar correo a revisar
email = input("Ingrese el correo a investigar: ")#'falso@hotmail.com'

#solicitud
try: 
    url = 'https://haveibeenpwned.com/api/v3/breachedaccount/'+\
            email+'?truncateResponse=false'
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        encontrados = len(data)
        if encontrados > 0:
            print("Los sitios en los que se ha filtrado el correo ",email," son: ")
        else:
            print("El correo ",email," no ha sido filtrado")
        for filtracion in data:
            print(filtracion["Name"])
            print(filtracion['Domain'])
            print(filtracion['BreachDate'])
            print(filtricion['Description'])
            
        msg = email+" Filtraciones encontradas: "+str(encontrados)
        print(msg)
        logging.basicConfig(filename='hibpINFO.log',
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p",
                            level=logging.INFO)
        logging.info(msg)
    else:
        msg = r.text
        print(msg)
        logging.basicConfig(filename='hibpERROR.log',
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %H:%M:%S",
                            level=logging.ERROR)
        logging.error(msg)
except requests.exceptions.RequestsException as er:
    msg = f"Ocurrio un error: {er}"
    print(msg)
    logging.error(msg)
    
print('your logs will be stored in ',os.getcwd())
