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