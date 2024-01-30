class Queue:
    def __init__(self, max_size=None):
        self.max = max_size
        self.queue = []
        
    def push(self):
        if len(self.queue) != 0:
            return self.queue.push()
        else:
            return None
    
    def append(self, val):
        if self.max == None:
            self.queue.append(val)
        else:
            if len(self.queue) == self.max:
                return None
            else:
                self.queue.append(val)
                return None

    def force_append(self, val):
        if self.max == None:
            self.queue.append(val)
        else:
            if len(self.queue) == self.max:
                self.push()
                self.queue.append(val)
                return None
            else:
                self.queue.append(val)
                return None
    
    def length(self):
        return f"{len(self.stack)}/{self.max}"
    
    def head(self):
        return self.queue[0]
    
    def tail(self):
        return self.queue[-1]
    
    def print(self):
        print(self.queue)
