#This problem is going to be divided into sections
#First we need to multiply out the grid an appropriate number of times
#So the width must equal 3 * height + 1, so that we can traverse to the bottom
class trees:
    def __init__(self, file, step_rate, drop_rate, fname):
        self.fname = fname
        self.drop_rate = drop_rate
        self.step_rate = step_rate
        self.tree_counter = 0
        self.file = open(file, mode = 'r')
        self.reader = self.file.readlines()
        self.file.close()
        self.file_maker()
        
    def file_maker(self):
        for i in range(len(self.reader)):
            ogline = self.reader[i][:-1]
            while not (len(self.reader[i]) >= (len(self.reader) \
                                               * self.step_rate//self.drop_rate + 1)):   
                self.reader[i] = "".join([self.reader[i][:-1] if \
                                             self.reader[i][-1] == "\n" \
                                             else self.reader[i], ogline])
        self.new_file = open(f"{self.fname}.txt", mode="w")
        self.new_file.writelines(self.reader)
        self.new_file.close()

#Then we will iterate through it like a matrix
    def checker(self):
        pointer = self.step_rate
        for i in self.reader[self.drop_rate::self.drop_rate]:
            if i[pointer] == '#':
                self.tree_counter += 1
            pointer += self.step_rate
        return(self.tree_counter)
        


        
obj1 = trees("treesProblem.txt", 1, 1, "file1")
obj2 = trees("treesProblem.txt", 3, 1, "file2")
obj3 = trees("treesProblem.txt", 5, 1, "file3")
obj4 = trees("treesProblem.txt", 7, 1, "file4")
obj5 = trees("treesProblem.txt", 1, 2, "file5")

print(obj1.checker() * 
      obj2.checker() * 
      obj3.checker() * 
      obj4.checker() * 
      obj5.checker())


