class MyList:
    def __init__(self,a=None):
        if a==None:
            #create an empty List
        elif isinstance(a, list):
            #if array is given
        elif isinstance(a, MyList):
            #if MyList type of data is given
        else:
            print("Wrong datatype passed in the constructor so creating an empty MyList")
            #create an empty List

#Testing the constructors
lst = MyList()
lst = MyList([5,6,7])
lst_1 = MyList(lst)
