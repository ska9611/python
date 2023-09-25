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
    
    
    
class More계산(계산):
    def pow(self):
        result = self.first ** self.second
        return result
    
a = More계산(3,5)
print(a.pow())


