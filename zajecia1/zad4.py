Lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','y','z']

print Lista

n = input('podaj n ')

for x in range (0,len(Lista),n):
    print Lista[x].lower()