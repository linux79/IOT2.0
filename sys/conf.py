from admin import super_user
import json
json_string = '''
    {"conf_file" : [
                    {
"[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
                    }
    ]
    }
'''

config = json.loads(json_string)
while super_user == True:
    if input() == "emacs conf.sh":
        with open('conf.sh') as file:
            print(file.readlines) 
