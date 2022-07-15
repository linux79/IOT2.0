from curses import is_term_resized
from logging import shutdown
import shutil
grub_test_options = {"shutdown -fr"}
class User:
        
        def __init__(self,user_class):
            self.user_class = user_class
        def rescue(self):
            
            if FileNotFoundError("grub") is True:
                input("grub rescue ")
            
            elif input == "restore":
                shutil.rmtree("grub")
   
            elif input == "":
                input("warning,dangerius attencin ")
        def ls(self):
            print(User.__dict__)
        def shutdown(self):
                print("executing shutdown")
                shutdown
class term_resized_user:
        def __init__(self,additional_restrictions):
            self.additional_restrictions = additional_restrictions
        def term_resized_user(self,**kwargs):
            is_term_resized is True    
            
            if User == input(grub_test_options):
                User == input(shutdown)
            InterruptedError() is True
            
            while is_term_resized is True:
                input() is not "{}".format
default_restricted_user = term_resized_user("default_restrictions")