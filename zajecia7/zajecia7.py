#procesy

# import subprocess
#
# out1 = subprocess.call(
#     ["ls"], shell= True)
# out2 = subprocess.check_output(
#     ["ls"], shell= True)
# print out1
# print out2

out2 = ' '

import subprocess
import os
with open(os.devnull, 'w') as devnull:
        out1 = subprocess.call(
            ["ls"], shell= True)
try:
    out2 = subprocess.check_call(
            ["ls"], shell= True)
except subprocess.CalledProcessError as ex:
    print ex
print out1
print out2