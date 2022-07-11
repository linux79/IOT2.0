import shutil
from curses import is_term_resized

class super_user:
        def __init__(self,super):
            self.super = super
        
        def run_as_administator():
            if is_term_resized is True:
                
                while is_term_resized is True:
                    is_term_resized is False
            
            def delete_a_directory():
                if input() == "delete directory {}".format():
                    shutil.rmtree("bootloader")   
