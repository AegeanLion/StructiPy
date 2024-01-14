class DoublyLinkedNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
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
        current_node = self.head
        counter = 0

        while current_node != None:
            current_node = current_node.next
            counter+=1
        
        return counter
    
    def append(self, data=None, index=None):
        appended_node = DoublyLinkedNode(data)
        current_node = self.head
        position = 1

        if self.head == None:
            self.head = appended_node
            return 
        elif index == None:
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
        position =1

        if not self.head:
            return None
        elif self.length()==1 or position==index:
            popped_node = self.head

            if popped_node.next ==None:
                self.head = None
                return popped_node
            else:
                self.head = popped_node.next
                return popped_node
        elif index == None:
            popped_node = self.tail()
            popped_node.prev.next = None
            return popped_node
        else:
            position = 1

            while current_node:
                if position==index and current_node.next:
                    popped_node = current_node.next
                    current_node.next = popped_node.next
                    return popped_node
                else:
                    position+=1
                    current_node = current_node.next
            
    
    def display(self, current_node=None):
        node_table = []
         
        if current_node ==None:
            if self.head ==None:
                return
            else:
                current_node = self.head

        if current_node.next==None:
            node_table.append(current_node.val)
            node_table.append(None)
        else:
            node_table.append(current_node.val)
            node_table.append(self.display(current_node.next))

        return node_table
    
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
                    current_node = current_node.next
                    
            return None

