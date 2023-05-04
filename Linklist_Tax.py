from Payer import *
from Node_Tax import Node

class mylist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def __repr__(self):
        current = self.head
        node = []
        while current:
            node.append(current.data)
            current = current.next
        return "None <- " + " <=> ".join(map(str, node)) + " -> None"

    def isempty(self):
        return self.head == None
    
    def add_to_End(self,node:Node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.next=None
            self.tail.next = node
            self.tail = node
        self.size += 1
    
    
    def del_by_Code(self, code):
        if self.head.data.code==code:
            temp=self.head.data
            self.head=self.head.next
            return temp
        if self.size == 1 or self.head == None:
            return
        cur = self.head
        while cur.next!=None:
            if cur.next.data.code==code:
                pre=cur.next.data
                cur.next=cur.next.next
                self.size-=1
                return pre
            cur=cur.next
        
    def sort_by_Code(self):
        cur = self.head
        cur1 = None
        while cur != None:
            cur1 = cur.next
            while cur1 != None:
                if (int(cur.data.code[2:]) > int(cur1.data.code[2:])):
                    temp = cur.data
                    cur.data = cur1.data
                    cur1.data = temp
                cur1 = cur1.next
            cur = cur.next
    
    def add_to_Begin(self,node):
        if self.isempty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
    
    def DelIndex(self, index):
        if index< 0:
            return
        if index == 0:
            self.Delfirst()
            return
        pos = 0
        cur = self.head
        while cur.next != None:
            if index == pos+1:
                break
            pos += 1
            cur = cur.next

        if cur.next == None:
            if index != pos+1:
                return
            else:
                self.Dellast()
        else:
            cur.next = cur.next.next
            self.size -= 1
            print()
            
    
    def addAfterIndex(self,node:Node,index):
        if self.isempty():
            if index < 0:
                return
            if index == 0:
                self.add_to_Begin(node)
                return
        pos = 0
        cur = self.head
        while cur != None and pos<index:
            if pos==index-1:
                if cur.next == None:
                    cur.next = node
                    break
                elif cur.next != None:
                    node.next=cur.next
                    cur.next=node
            if cur.next == None and pos<index-1:
                print("Out of index")
                return
            pos+=1
            cur=cur.next
    
    def Search(self, code):
        cur = self.head
        while cur!= None:
            if cur.data.code==code:
                return cur.data
            cur=cur.next
        return False
    
    def Delfirst(self):
        if self.isempty():
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        self.head = self.head.next
        self.size -= 1

    def Dellast(self):
        if self.isempty():
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
        cur.next = None
        self.tail = cur
        self.size -= 1