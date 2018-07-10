import re
def spec(s):
    if re.match(r'^[_\W]+$', s):
        print('Valid')
    else:
        print('Invalid')
spec("*&%^$")

