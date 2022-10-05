import subprocess
import os
from time import time, sleep
from pushnotifier import PushNotifier as pn

test = True
folder = './toPrint'

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

print("Bienvenue sur le service d'impression de PDF par JA !")
print(f"Chaque PDF fourni dans le dossier '{folder}' sera imprimé sur l'imprimante par défaut (macOS) puis supprimé du dossier.\n")

def crash(arg):
    print('''\n
 ,adPPYba, 8b,dPPYba, 8b,dPPYba,  ,adPPYba,  8b,dPPYba,  
a8P_____88 88P'   "Y8 88P'   "Y8 a8"     "8a 88P'   "Y8  
8PP""""""" 88         88         8b       d8 88          
"8b,   ,aa 88         88         "8a,   ,a8" 88          
 `"Ybbd8"' 88         88          `"YbbdP"'  88          

    ''')
    print(f'Erreur fatale ! Raison : {arg}.\nArrêt du service.')
    usernamepn = ''
    passwordpn = ''
    pnsession = pn.PushNotifier(usernamepn, passwordpn, 'notiflvs.aqua', '6C3VDE7DV75BDE7D696VDE7D8B2D6C3VKFTTFBTTFT')
    pnsession.send_text(f"FokPrint s'est arrêté. Raison : {arg}")
    exit()

def imprimer(file, filename):
    print(f"Impression de {filename} !")
    if not test:
        try:
            printer = subprocess.getoutput("lpstat -d").split(": ")[1]
            print_cmd = 'lpr -P %s %s'
            os.system(print_cmd % (printer, file))
        except:
            crash("Impossible d'imprimer le fichier.")
    try:
        os.remove(file)
        print(f'Le fichier {filename} a bien été supprimé !\n')
    except:
        crash(f'Erreur : Impossible de supprimer le fichier {file}, peut-être est-ce dû à un manque de permissions ?')


while True:
    for file in os.listdir(folder):
        f = os.path.join(folder, file)
        if os.path.isfile(f):
            filename = str(f[len(folder)+1:])
            if f[-4:] == '.pdf':
                imprimer(f, filename)
            else:
                try:
                    os.remove(f)
                    print(f"Fichier non accepté trouvé. Suppression de {filename}.\n")
                except:
                    crash(f"Erreur de suppression d'un fichier non voulu. ({filename})")
    try:
        sleep(60 - time() % 60)
    except KeyboardInterrupt:
        crash('Arrêt volontaire avec ctrl+c')
