text = "https://github.com/rhboot/grub2"
from sys.obj1 import User as user

filesystem = ["sbin","var","bin","boot","home","dev"]
subfiles = ["opt"," root" , "usr","srv"]

def rescue(self):
    f = open("/home/alessio/coding/GitHub/gnu-murd/sys/main.py")
    content = f.read
    
    if "boot" not in filesystem:
       with open("boot","w") as file:
        file.write(text)       
