"""ESTRELLA MAYRANI DIAZ RODRIGUEZ
MARIA FERNANDA MACIAS ROMO
EDGAR RODRIGUEZ PEREZ"""

import pyautogui
import subprocess
import datetime

#take screenshots and save them as .jpg files
try: 
   ss = pyautogui.screenshot()
except ModuleNotFoundError as merr:
    print(f'Module not found. Cannot take the screenshot: {merr}')
except Exception as err:
    print(f'Sorry, unable to take screenshot: {err}')
else:
   date = datetime.datetime.now()
   imgName = r'screenshot_'
   imgName += str(date.strftime('%Y%m%d_%H%M%S'))
   imgName += '.jpg'
   ss.save(imgName)

#subprocess using powershell commands (Get-Process)
processdate = datetime.datetime.now()
command = 'Get-Process'
try:
    ps = 'PowerShell -ExecutionPolicy ByPass -Command '+ command
except Exception as error:
    print(f"Sorry, unexpected error D: \n{error}")
else:
    rp = subprocess.run(ps, capture_output=True, text=True, shell=True)
    formatLine = rp.stdout.replace('\\n', '\n') #replaces '\\n' text as a real line break

#save Get-Process with subprocess output as .txt file
filename = r'runningProcesses_'
filename += str(processdate.strftime('%Y%m%d_%H%M%S'))
filename += '.txt'
with open(filename, 'a') as file:
   file.write(formatLine)