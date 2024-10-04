"""INTEGRANTES DEL EQUIPO:
ESTRELLA MAYRANI DIAZ RODRIGUEZ
MARIA FERNANDA MACIAS ROMO"""
import requests
import json
import logging
import getpass
import re
import os
import six
import argparse
import sys

print('your logs will be stored in ',os.getcwd())
print('script uses python 3 :D')

#current python version
pyver = sys.version.split()[0]

#apikey = 'ec1e2ebed1754f1b8c00f2b90aa15906'
headers = {}
headers['content-type'] = 'application/json'
headers['api-version'] = '3'
headers['User-Agent'] = 'python'

#error logs basic config
logging.basicConfig(filename='hibpERROR.log',
                    format="%(asctime)s %(message)s",
                    datefmt="%m/%d/%Y %H:%M:%S",
                    level=logging.ERROR)

#argparse config
parser = argparse.ArgumentParser('This script checks if your email was filtered; script uses Have I Been Pwned api')
parser.add_argument('-email', dest='email', help='This is the e-mail to be analyzed')
params = parser.parse_args()

#function to request API
def requestToAPI():
    while True:
        apikey = getpass.getpass(prompt = '>> enter hibp apikey: ')

        #validate 'apikey' format
        if re.match(r'^[a-fA-F0-9]{32}$', apikey):
            #add to headers
            headers['hibp-api-key'] = apikey
            break
        else:
            print('ALERT!! your string is not apikey.')

    try:
        #ask e-mail to be analyzed
        email = params.email #'falso@hotmail.com'
        #make the request
        url = 'https://haveibeenpwned.com/api/v3/breachedaccount/'+\
        email+'?truncateResponse=false'
        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            data = r.json()
            found = len(data)
            if found > 0:
                print('websites that ',email,' has been filtered are: ')
            else:
                print(email,' has not been filtered :D')
            
            for filtered in data:
                    print(filtered['Name'])
                    print(filtered['Domain'])
                    print(filtered['BreachDate'])
                    print(filtered['Description'])

                    msg = email + ' found breaches: ' + str(found)
                    print(msg)

                    #create report .log
                    logging.basicConfig(filename = 'hibpINFO.log',
                                        format="%(asctime)s %(message)s",
                                        datefmt="%m/%d/%Y %I:%M:%S %p",
                                        level=logging.INFO)
                    logging.info(msg)
                    print('report successfully created')
        else:
            msg = r.text
            print(msg)
            logging.error(msg)
            print('errors report successfully created')

    except requests.exceptions.HTTPError as herr:
        msg = f"HTTP error: {herr}"
        print(msg)
        logging.error(msg)
        print('errors report successfully created')
    except requests.exceptions.ConnectionError as cerr:
        msg = f"Connection error: {cerr}"
        print(msg)
        logging.error(msg)
        print('errors report successfully created')
    except Exception as err:
        msg = f":O unexpected error: {err}"
        print(msg)
        logging.error(msg)
        print('errors report successfully created')
    finally:
        #terminates logs correctly
        logging.shutdown()
        print('analysis completed...')

        
#check if python version is 3
pyver3 = six.PY3

if pyver3:
    print(f'current python version {pyver}')
    requestToAPI()
else:
    print(f'current python version {pyver}, you need python 3.')
