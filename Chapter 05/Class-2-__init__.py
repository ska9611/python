class 계산:
    def __init__(self,first,second): 
        self.first = first
        self.second = second
    
    
    def Add(self):
        result = self.first + self.second
        return result
    
    def Times(self):
        result = self.first * self.second
        return result
    
    def Minus(self):
        result = self.first - self.second
        return result

    def Division(self):
        result = self.first / self.second
        return result
    
    
    
obj_a = 계산(10,78)
print(obj_a.Add())

obj_b = 계산(87,65)
print(obj_b.Times())

obj_c = 계산(84,53)
print(obj_c.Minus())

obj_d = 계산(98,2)
print(obj_d.Division())

        
    
