#korzystajac z modulu subporocess napisz program ktory tworzy strukture katalogow podana w formie:

dirStr = '''
K1
    K2
    K3
        K4
K5
    K6
'''

import subprocess

out1 = subprocess.check_call(
    ["mkdir K1"], ["cd K1"], shell = True
)
out2 = subprocess.check_call(
    ["mkdir K2"], shell=True
)
out3 = subprocess.check_call(
    ["mkdir K3"], ["cd K3"], shell=True
)
out4 = subprocess.check_call(
    ["mkdir K4"], shell=True
)
out5 = subprocess.check_call(
    ["cd.."],["cd.."], shell=True
)
out6 = subprocess.check_call(
    ["mkdir K5"],["cd K5"], shell=True
)
out7 = subprocess.check_call(
    ["mkdir K6"], shell=True
)




