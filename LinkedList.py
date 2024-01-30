class LinkedNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def tail(self):
        current_node = self.head

        if current_node:
            while current_node:
                if current_node.next == None:
                    return current_node
                else:
                    current_node = current_node.next
        else:
            return None
        

    def length(self):
        counter = 0
        current_node = self.head
        
        while current_node != None:
            counter += 1 
            current_node = current_node.next
        
        return counter
    
    
    def append(self, data=None, index=None):
        appended_node = LinkedNode(data)
        current_node = self.head
        position = 0

        if self.head == None:
            self.head=appended_node
            return 
        elif index==None:
            self.tail().next = appended_node
            return 
        elif position==index:
            appended_node.next = self.head
            self.head = appended_node
            return 
        else:
            position = 1

            while current_node:
                if position==index:
                    appended_node.next = current_node.next
                    current_node.next = appended_node
                    return 
                else:
                    position+=1
                    current_node = current_node.next

    
    def pop(self, index=None):
        current_node = self.head
        position = 0

        if not self.head:
            return None
        elif self.length()==1 or position==index:
            popped_node = self.head

            if popped_node.next == None:
                self.head = None
                return popped_node
            else:
                self.head = popped_node.next
                popped_node.next = None
                return popped_node
        
        elif index == None:
            popped_node = self.tail()

            while current_node.next:
                if current_node.next.next==None:
                    current_node.next = None
                else:
                    current_node = current_node.next
            
            return popped_node
        
        else:
            position = 1

            while current_node:
                if position == index and current_node.next:
                    popped_node = current_node.next
                    current_node.next = popped_node.next
                    return popped_node
                else:
                    position +=1 
                    current_node = current_node.next
                
        return 

    
    def __display(self, current_node=None):
        node_table = []

        if current_node==None:
            if self.head==None:
                return 
            else:
                current_node = self.head

        if current_node.next == None:
            node_table.append(current_node.val)
            node_table.append(None)
        else:
            node_table.append(current_node.val)
            node_table.append(self.__display(current_node.next))

        return node_table  
    
    def print(self, current_node=None):
        print(self.__display(current_node))
    
    def get_node(self, index=None):
        current_node = self.head
        position = 0
        
        if self.head==None or index==None:
            return None
        elif position==index:
            return current_node
        else:
            position = 1
            current_node = current_node.next

            while current_node:
                if position==index:
                    return current_node
                else:
                    position+=1
                    current_node=current_node.next
            
            return None
