from math import ceil

class boarding:

    all_seats = []
    
    def __init__(self, file):
        self.file = open(file, mode='r')
        self.reader = self.file.readlines()
        self.file.close()

    def find_id(self, code):
        bound1 = 0
        bound2 = 127
        num = 0
        column = 0
        code = code.rstrip('\n')
        for x in code[:7]:
            if x == "F":
                bound2 = (bound2 - bound1)//2 + bound1
            else:
                bound1 += ceil((bound2 - bound1)/ 2)
        num = bound2 if code[7] == "B" else bound1
        bound1 = 0
        bound2 = 7
        
        for y in code[-3:-1]:
            if y == "L":
                bound2 = (bound2 - bound1)//2 + bound1
            else:
                bound1 += ceil((bound2 - bound1)/2)
        column = bound2 if code[-1] == "R" else bound1
        return (num * 8) + column
    
        
    def find_max(self):
        maximum = 0
        for i in self.reader:
            balls = self.find_id(i)
            maximum = balls if balls > maximum else maximum
            boarding.all_seats.append(balls)
        return maximum

    def find_seat(self):
        boarding.all_seats.sort()
        for i in range(len(boarding.all_seats)):
            if boarding.all_seats[i] != (boarding.all_seats[i + 1] - 1):
                return boarding.all_seats[i] + 1
            
        


        
obj = boarding("boarding.txt")
print(obj.find_max())
print(obj.find_seat())
            
