import subprocess
import os
from time import time, sleep

folder = ''

print('''
 /$$$$$$$$        /$$       /$$$$$$$           /$$             /$$    
| $$_____/       | $$      | $$__  $$         |__/            | $$    
| $$     /$$$$$$ | $$   /$$| $$  \ $$ /$$$$$$  /$$ /$$$$$$$  /$$$$$$  
| $$$$$ /$$__  $$| $$  /$$/| $$$$$$$//$$__  $$| $$| $$__  $$|_  $$_/  
| $$__/| $$  \ $$| $$$$$$/ | $$____/| $$  \__/| $$| $$  \ $$  | $$    
| $$   | $$  | $$| $$_  $$ | $$     | $$      | $$| $$  | $$  | $$ /$$
| $$   |  $$$$$$/| $$ \  $$| $$     | $$      | $$| $$  | $$  |  $$$$/
|__/    \______/ |__/  \__/|__/     |__/      |__/|__/  |__/   \___/                                                                                                         
''')

print("Bienvenue sur le service d'impression de PDF by JA !")
print(f"Chaque PDF fourni dans le dossier '{folder}' sera imprimé sur l'imprimante par défaut (macOS) puis supprimé du dossier.")
def imprimer(file, filename):
    print(f"Impression de {filename} !")
    printer = subprocess.getoutput("lpstat -d").split(": ")[1]
    print_cmd = 'lpr -P %s %s'
    os.system(print_cmd % (printer, file))

while True:
    sleep(60 - time() % 60)
    for file in os.listdir(folder):
        f = os.path.join(folder, file)
        if os.path.isfile(f):
            filename = str(f[44:])
            if f[-4:] == '.pdf':
                imprimer(f, filename)
                os.remove(f)