"""I want to make this again with a recursive function"""

#inp = open("input.txt", mode='rt')

#lst = []
#lst2 = []
#lst3 = []

#for i in inp:
#    lst.append(int(str(i)))
#    lst2.append(int(str(i)))
#    lst3.append(int(str(i)))

#for x in lst:
#    for y in lst2:
#        for z in lst3:
#            if x + y  + z == 2020:
#                cok = x * y * z

#print(cok)

#inp.close()

#Here's the remake

class iterator:
    def __init__(self, file):
        self.file = open("{}".format(file), mode='r')
        self.contents = [int(str(i)) for i in self.file]
        self.file.close()
        
    def iterate(self):
        return (int(str(i)) for i in file)


        
gen1 = iterator("input.txt")
gen2 = iterator("input.txt")
gen3 = iterator("input.txt")



print("all done")            
               




            
            
