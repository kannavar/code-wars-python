class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleLinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return self.head
        temp = self.head
        while(temp.next is not None):
            temp=temp.next
        temp.next=new_node 
        return self.head
    
    def insert_at_start(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return self.head
        else:
            new_node.next=self.head
            self.head=new_node
            return self.head
        
    def delete_node(self,data):
        if not self.head:
            print("List is empty nothing to delete")
        prev=self.head
        temp=self.head
        found=0
        while(temp):
            if(temp.data==data):
                prev.next=temp.next
                found=1
                break
            prev=temp
            temp=temp.next
        if(not found):
             print("No node found with give value")  
        return self.head   
    
    def reverseLL(self):
        
        if not self.head:
            print("Linked List is empty")
            return
        prev=self.head
        curr=self.head

        while(curr):
            temp=curr.next
        return 

    def displayLL(self):
        if not self.head:
            print("Linked List is empty")
            return
        temp=self.head
        print("HEAD=>",end='')
        while(temp.next):
            print(f"{temp.data}=>",end='')
            temp=temp.next
        print(f'{temp.data}=>END')

    

if __name__=='__main__':

    sll=SingleLinkedList()
    sll.insert_at_end(10)
    sll.displayLL()
    sll.insert_at_end(20)
    sll.displayLL()
    sll.insert_at_end(24)
    sll.displayLL()
    sll.delete_node(20)
    sll.displayLL()
    sll.insert_at_start(30)
    sll.displayLL()
    sll.insert_at_end(45)
    sll.displayLL()
    

        


