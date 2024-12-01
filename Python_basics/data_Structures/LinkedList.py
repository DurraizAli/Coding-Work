class Node:
    def __init__(self, data=None, next=None):
        self.data= data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        node= Node(data,self.head)
        self.head= node
    def print(self):
        if self.head is None:
            print("List is empty")
            return
        itr= self.head
        listr=''
        while itr:
            listr += str(itr.data)+"--->"
            itr= itr.next
        print(listr)

if __name__=='__main__':
    l=linkedlist()
    l.insert_at_begin(88)
    l.insert_at_begin(9)
    l.print()