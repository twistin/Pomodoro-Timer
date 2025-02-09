"""
This is a setup.py script for building a standalone macOS application using py2app.
"""
from setuptools import setup

# Reemplaza con el nombre de tu archivo principal de Python
APP = ['/Users/sdcarr/Desktop/pomodoro/pomodoro_project/src/pomodoro_timer.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['pygame', 'PIL', 'tkinter'],
    # Especifica un archivo de icono para tu app
    #'iconfile': '"/Users/sdcarr/Desktop/pomodoro/pomodoro_project/resources/images/logo.png",',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
