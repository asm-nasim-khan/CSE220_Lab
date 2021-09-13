class Node:
    def __init__(self,elm,ref = None):
        self.element=int(elm)
        self.next=ref
    def __add__(self, other):
        return self.element+ other.element
class MyList:
    def __init__(self,a):
        
        self.head = None
        self.tail = None
        if a==None:
            self.head = None
            pass            
            #if array is given
        elif isinstance(a, list):
            self.head = Node(a[0],None)
            i = 1
            temp = self.head
#            s = Node(a[i],None)
            while i<len(a):
                s = Node(a[i],None)
   #             if i ==1:
  #                  head = s
                temp.next = s
                temp = s
                i+=1
            
            #if MyList type of data is given
        elif isinstance(a, MyList):
            
            self.head = Node(a.head.element,a.head.next)
            newTemp = self.head
            while newTemp is not None:
                newNode = newTemp.next
                newTemp = newNode
            temp = self.head
            print("Wrong datatype passed in the constructor so creating an empty MyList")
            #create an empty List
    

    def showList(self):
        if self.head == None:
            return "Empty"
        else:
            n = self.head
            while(n!=None):
                print(n.element,end=' ')
                n = n.next
            print(" ")
            
    def insert(self,i):
        new_node = Node(i)
        if self.head is None:
             self.head = new_node
             return
 
        last = self.head
        while (last.next):
            last = last.next
        last.next =  new_node       
            
            
    def sum(self, l1,l2,l3): 
       #Compare size 
       #prepend zero to make size same 
      while l1.head and l2.head:
            
            A = l1.head 
            B = l2.head
            S = A+B
            if l3.head == None: 
                       l3.head = Node(S,None) 
            else: 
                        l3.insert(S)

            l1.head = l1.head.next
            l2.head = l2.head.next

      return l3.showList()      

A = [3,2,3] 
B = [3,2,1] 
List3 = MyList(None) 
List3.sum(MyList(A),MyList(B),MyList(None))