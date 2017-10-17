l1 = input('l1: ')
l2 = input('l2: ')
l3 = input('l3: ')

if l1 > l2:
    max = l1
    if max > l3:
        max = l1
    else:
        max = l3
else:
    max = l2
    if max > l3:
        max = l2
    else:
        max = l3

print (max)

