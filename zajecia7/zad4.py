# napisz klase implementacje wlasnej obiektowej listy. Program powienien posiadac podstawowe operacje
# takie jak dodawaniem, usuwanie, sortowanie, posiadac przeciazone operatory i zglaszac niezbedne wyjatki

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class List:
    def __init__(self):
        self.head = None

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def remove(self, item):
        p = self.head
        prev = None
        found = False

        while not found:
            try:
                if p.data == item:
                    found = True
                else:
                    prev = p
                    p = p.next
            except Exception as ex:
                return ex
        if prev == None:
            self.head = p.next
        else:
            prev.next = p.next


    def __str__(self):
        s = ""
        p = self.head
        if p != None:
            while p.next != None:
                s += p.data
                p = p.next
            s += p.data
        return s


    def size(self):
        p = self.head
        count = 0
        while p != None:
            count += 1
            p = p.next
        print "Liczba elementow listy: %d" % (count)


l = List()
l.add('a')
l.add('b')
l.size()
print l.remove('d')
l.remove('a')
l.size()
l.add('c')
print l
