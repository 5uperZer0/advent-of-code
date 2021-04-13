class passports:
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


    def hcl_checker(val):
        for i in range(len(val)):
            if i == 0:
                if val[i] != '#':
                    return 0
            elif not (val[i].isnumeric() or 'a' <= val[i] <= 'f'):
                    return 0
        return 1     
            
    def hgt_checker(val):
        if val[-2:] == 'cm':
            if 150 <= int(val[:-2]) <= 193:
                return 1
            else:
                return 0
        elif val[-2:] =='in':
            if 59 <= int(val[:-2]) <= 76:
                return 1
            else:
                return 0
        else:
            return 0
            
    
    methods = {
            "byr": lambda x: 1 if 1920 <= int(x) <= 2002 else 0,
            "iyr": lambda x: 1 if 2010 <= int(x) <= 2020 else 0,
            "eyr": lambda x: 1 if 2020 <= int(x) <= 2030 else 0,
            "hgt": lambda x: passports.hgt_checker(x),
            "hcl": lambda x: passports.hcl_checker(x),
            "ecl": lambda x: 1 if x in passports.eye_colors else 0,
            "pid": lambda x: 1 if (len(x) == 9 and x.isnumeric()) else 0,
            "cid": lambda x: 1
        }

    
    def __init__(self, file):
        self.file = open(file, mode='r')
        self.reader = self.file.readlines()
        self.file.close()
        self.passport_list = [[],]
            
        
    def parser(self):
        counter = 0
        for i in range(len(self.reader)):
            if self.reader[i] != "\n":
                self.reader[i].rstrip("\n")
                self.passport_list[counter].append(self.reader[i])
            else:
                self.passport_list.append([])
                counter += 1
        for i in range(len(self.passport_list)):
            self.passport_list[i] = " ".join(self.passport_list[i])
            

    def checker(self):
        self.parser()
        req = ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]
        conf = 0
        for i in range(len(self.passport_list)):
            if all(x in self.passport_list[i] for x in req):
                self.passport_list[i] = self.passport_list[i].split()
                if all(self.methods[self.passport_list[i][y][:3]] \
                       (self.passport_list[i][y][4:]) == 1 for y in \
                       range(len(self.passport_list[i]))): 
                        conf += 1
        return conf
        
            
obj = passports("passports.txt")  
print(obj.checker())



                
                
                
            
        
        
