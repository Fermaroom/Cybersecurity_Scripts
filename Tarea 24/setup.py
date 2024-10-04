#Integrantes del equipo:
#ESTRELLA MAYRANI DIAZ RODRIGUEZ
#MARIA FERNANDA MACIAS ROMO
#EDGAR RODRIGUEZ PEREZ

from distutils.core import setup
import py2exe

setup (
    name = 'ExecutePyautogui',
    description = 'Python-based app, uses pyautogui and subprocess.',
    version = '1.0',
    console = ['execute_pyautogui.py']
)