import os
import shutil
grub_test_options = ["restore", "shutdown", "shutdown -fr"]

class User:
    def __init__(self,permessi,azioni,var,etc):
        self.permessi = permessi
        self.azioni = azioni
        self.var = var
        self.etc = etc

def rescue(self):
    if FileNotFoundError() is True:
        input("grub rescue ")
    elif input == "restore":
            shutil.rmtree("grub")
    elif input == "shutdown":
        input("attenzione,almeno che questa sia un vm suddetta azione è pericolosa! ")
        if input == "shutdown -fr":
            print("executing shutdown")
            pass
