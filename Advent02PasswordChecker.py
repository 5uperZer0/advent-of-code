class password:
    def __init__(self, line):
        self.line = line.split()
        self.nums = self.line[0].split('-')
        self.char = self.line[1][0]
        self.password = self.line[2]

    def check(self):
        if (self.password[int(self.nums[0]) - 1] == self.char) \
           ^ (self.password[int(self.nums[1]) - 1] == self.char):
            return True            

count = 0
lines = open("passwords.txt", mode='r')
for line in lines:
    obj = password(line)
    if obj.check():
        count += 1
print(count)
lines.close()
    
    
        
        
        
