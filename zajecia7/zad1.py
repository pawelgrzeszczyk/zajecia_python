#napisz program ktory kompiluje kod c++ a nastepnie uruchamia go i sprawdza czy jego dzialanie
#nie konczy sie bledem

import subprocess


out1 = subprocess.call(
    ["g++ -o main main.cpp"], shell=True
    )
try:
    out2 = subprocess.check_call(
        ["./main"], shell = True
    )

except subprocess.CalledProcessError as ex:
    print ex


