from obj1 import rescue as rescue
filesystem = ["sbin","var","bin","boot","home","dev"]
subfiles = ["opt"," root" , "usr","srv"]
class sys_needs("operator","requirements need","backend"):
    def ls(self):
        for x in filesystem:
            print(x)
        for x in subfiles:
            print(x)
