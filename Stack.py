class Stack:
    def __init__(self, max_size=None):
        self.stack = []
        self.max = max_size

    def append(self, val):
        if self.max == None:
            self.stack.append(val)
        else:
            if len(self.stack) == self.max:
                return None
            else:
                self.stack.append(val)
                return None
    
    def pop(self):
        return self.stack.pop()
        
    def peak(self):
        return self.stack[-1]
    
    def print(self):
        print(self.stack) 
    
    def length(self):
        return len(self.stack)
    
def stackify(_list, max_size=None):
    if max_size==None:
        s = Stack()
        s.stack = _list
        return s
    else:
        s = Stack(max_size)
        
        if len(_list) <= max_size:
            s.stack = _list
        else:
            s.stack = _list[:max_size]
        
        return s
