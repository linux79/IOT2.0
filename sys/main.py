from obj1 import User as user
filesystem = ("sbin","var","bin","boot","home","dev")
subfiles = ("opt"," root" , "usr","srv")
class sys_integration:
    def __init__(self,module):
        self.module = module
sys_integration1 = sys_integration("default")
