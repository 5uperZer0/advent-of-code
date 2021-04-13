class declarations:
    def __init__(self, file):
        self.file = open(file, mode='r')
        self.reader = self.file.readlines()
        self.file.close()
        self.elements = [[],]
        self.parser()

    def parser(self):
        counter = 0
        for i in self.reader:
            if i != '\n':
                i = i.rstrip('\n')
                self.elements[counter].append(i)
            else:
                counter += 1
                self.elements.append([])

    def counter(self):
        score = 0
        for i in self.elements:
            for a in i[0]:
                if all(a in x for x in i):
                    score += 1
        return score

obj = declarations("declarations.txt")
print(obj.counter())
