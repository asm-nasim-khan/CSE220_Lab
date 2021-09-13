def Arraysize(a):
    count = 0
    for items in a:
        count += 1
    return count
#Task 1.a
def fac(n):
    if n==0: return 1
    return n* fac(n-1)
#Task 1.b
def fibo(n):
    if n == 0: return 0
    elif n == 1: return 1
    return fibo(n-1) + fibo(n-2);
#task 1.c
def PrintList(arr,n):
    if n!= -1:
        PrintList(arr,n-1)
        print(arr[n],end=' ')
#TASK 1.d
def powerN(base,n):
    if n==0:return 1
    return base * powerN(base,n-1)
#Task 2
def DecimalBinary(n):
    if n>0:DecimalBinary(n//2)
    print(n%2,end='')
#Task 3
def hocBuilder(height):
    if height == 0:return 0;
    elif height == 1:return 8;
    return 5 + hocBuilder(height - 1)
#task 5.a
def triangleS(n):
        if n==0:return
        else:
            triangleS(n-1);
            Tprint(n)
            print('')
def Tprint(n):
    if n == 0:return
    else:
        Tprint(n-1);
        print(n,end=' ')
#task 5.b
def ReverseTriangle(height,n):
    if height == 0: return
    else:
        space(height-1)
        Tprint(n-height+1)
        print('')
        ReverseTriangle(height -1,n)
  
def space(i):
    if i == 0: return
    else:
        print(" ",end=" ")
        space(i -1)
# task 6
def clacProfit(invest):
    if invest <= 100000: return (invest-25000) / (1/0.045)
    else:
        return (clacProfit(100000)) + (invest - 100000) / (1/0.08)
 
def Sprint(arr,i):
    if(i<Arraysize(arr)):
        print(f"invest:{arr[i]}Profit : {clacProfit(arr[i])}")
        Sprint(arr,i+1)
#=========
class Node:
    def __init__(self, data=None, next=None):
        self.element = data
        self.next = next

class MyList:
    #Creating Constractor
    def __init__(self,datas=None):
        if datas is None:
            self.head = None
            
        elif isinstance(datas,list):
            self.head = Node(datas[0],None)
            indexnode = self.head
            for data in datas:
                indexnode.next = Node(data,None)
                indexnode = indexnode.next
        else:
            print("Wrong Data Type")
    #Task 2.c
    @classmethod
    def LSum(cls,temp):
        if temp.next == None: return 0
        return (temp.element) + cls.LSum(temp.next)
    #Task 2.d
    def Print(self,head):
        if head.next == None:
            return
        self.Print(head.next)
        print(head.element,end=' ')              
#tester_Class
#Task1.a
print('#Task 1.a')
print(fac(5))
#Task 1.b
print('#Task 1.b')
print(fibo(5))
#Task 1.c
print('#Task 1.c')
A = [1,2,3,4,5]
PrintList(A,Arraysize(A)-1)
print('')
#Task 1.d
print('#Task 1.d')
print(powerN(5,2))
#Task 2.a
print('#Task 2.a')
DecimalBinary(5)
print('')
#Task2.b
print('#Task 2.b')
List1 = MyList([1,2,3,4,5,6])
print(List1.LSum(List1.head))
#task 2.c
print('#Task 2.c')
List1.Print(List1.head)
print('')
#Task 3
print('#Task 3')
print(hocBuilder(3))
#task 5.a
print('#Task 5.a')
triangleS(5)
#Task 5.b
print('#Task 5.b')
ReverseTriangle(5,5)
#task 6
print('#Task 6')
B  = array=[25000,100000,250000,350000]
Sprint(B,0)



