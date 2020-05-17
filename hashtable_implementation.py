class HashHelper():
    def hash(self,string,length):
        hashcode = 0
        for i in string:
            hashcode += ord(i)
        return hashcode%length

class HashTable():
    def __init__(self):
        self.length = 4
        self.array = [None]*self.length
        self.hf = HashHelper()
    
    def __str__(self):
        return str(self.array)

    def add(self,key,val):
        index = self.hf.hash(key,self.length)
        if self.array[index] != None:
            for i in range(len(self.array[index])):
                if self.array[index][i][0] == key:
                    self.array[index][i][1] = val
            self.array[index].append([key,val])
        else:
            self.array[index] = [[key,val]]     

    
    def remove(self,key):
        index = self.hf.hash(key,self.length)
        if self.array[index] == None:
            return "No such key exist"
        else:
            rm = False
            for i in range(len(self.array[index])):
                if self.array[index][i][0] == key:
                    self.array[index].pop(i)
                    rm = True
                    break
            if rm == False:
                return "No such key exist"
            else:
                if self.array[index] == []:
                    self.array[index] = None
        
    def lookup(self,key):
        index = self.hf.hash(key,self.length)
        if self.array[index] == None:
            return "No such key exist"
        else:
            for i in range(len(self.array[index])):
                if self.array[index][i][0] == key:
                    return self.array[index][i][1]
            return "No such key exist"



ht = HashTable()
ht.add('beau', 'person')
ht.add('fido', 'dog')
ht.add('rex', 'dinosour')
ht.add('tux', 'penguin')

