class 계산:
    def setdata(self, first, second):
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
    
    
    
obj_a = 계산()
obj_a.setdata(571,74564)
print(obj_a.Add())

obj_b = 계산()
obj_b.setdata(156,87)
print(obj_b.Times())

obj_c = 계산()
obj_c.setdata(432,321)
print(obj_c.Minus())

obj_d = 계산()
obj_d.setdata(55,11)
print(obj_d.Division())

        
    
