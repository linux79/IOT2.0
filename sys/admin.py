import shutil
from curses import is_term_resized
from gnu_packages import install_packages
from obj1 import User as user
class super_user:
        super_user = user("any","any","def_admin","def_admin")
        def run_as_administator():
            if is_term_resized is True:
                while is_term_resized is True:
                    is_term_resized is False
        def delete_a_directory():
            if input() == "delete directory {}":
                shutil.rmtree()
        
                