class Queue:
    def __init__(self, max_size=None):
        self.max = max_size
        self.queue = []
        
    def dequeue(self):
        if len(self.queue) != 0:
            return self.queue.pop(0)
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
                out = self.dequeue()
                self.queue.append(val)
                return out
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

def queueify(_list, max_size=None):
    if max_size == None:
        q = Queue()
        q.queue = _list
        return q
    else:
        q = Queue(max_size)

        if len(_list) <= max_size:
            q.queue = _list
        else:
            q.queue = _list[:max_size]

    return q
