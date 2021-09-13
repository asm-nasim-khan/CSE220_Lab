package lab2;
//######################### Tester class that contains Main method
public class MyTester {
    public static void main(String[] args) {
        int[] a = {5,4,3,2,1};
        int[] b = {5,4,3,2,1,10};
        int[] c = {1,2,5,3,8};
        //task 2.1(b)
        MyList list1 = new MyList(a);
        MyList list2 = new MyList(b);
        MyList list3 = new MyList(c);
        //task 2.1(c)
        MyList list4 = new MyList(list3);
        list4.showList();
        
        //task 2.2
        list1.showList();
        //task 2.3
        System.out.println(list1.isEmpty());
        //task 2.4
        list1.clear();
        list1.showList();
        //task2.5
        Node n2 = new Node(3,null);
        list2.insert(n2);
        list2.showList();
        //task 2.6
        list2.insert(7,3);
        list2.showList();
        //task 2.7
        Node r = list2.remove(3);
        System.out.println("removed key element is: "+r.element);
        list2.showList();
        
        //Task 3.1
        list1.evenList();
        //task 3.2
        list1.isThere(2);
        //task 3.3
         list3.reverse();
        //task3.4
        list3.sort();
        list3.showList();
        //Task 3.5
        list3.sumOfList();
        //Task 3.6
        list2.showList();
        list2.rotate("left",2);
        list2.rotate("right",2);
    }
}
//============================Creating Linked list Abstract Data Type
// Task 1(ii)
class MyList{ 
    Node head;
    //Task 2.1(A)
    MyList(){
        Node head = null; 
    }
    //Task 2.1(B)
    MyList(int[] a){
        head  = new Node(a[0],null);
        Node temp = head;
         for (int i = 1; i <len(a); i++) {
            temp.next = new Node(a[i],null);
            temp = temp.next;
         }
    }
    //Task 2.1(C)
    MyList(MyList Newlist){
        head = new Node(Newlist.head.element,null);
        Node newhead = head;
        for (Node n = Newlist.head.next; n != null; n = n.next) {
            newhead.next = new Node(n.element,null);
            newhead = newhead.next;
        }
    }
  
    //Task 2.2
    void showList(){
        if(head == null){
            System.out.println("Empty List");
        }
        else{
            for (Node n = head; n != null; n = n.next) {
                if(n == head){
                    if(n.next == null){
                        System.out.print("["+n.element+"]"); //when the list has only one element
                    }
                    else{
                        System.out.print("["+n.element+",");
                    }
                }
                else if (n.next == null){
                    System.out.print(n.element+"]");
                }
                else{
                    System.out.print(n.element+",");
                }
            }
        }
        System.out.println(""); // Just for decoration
    }
    void showList(Node h){ //showList function with parameter 
        
        for (Node n = h; n != null; n = n.next) {
            if(n == h){
                if(n.next == null){
                    System.out.print("["+n.element+"]"); //when the list has only one element
                }
                else{
                    System.out.print("["+n.element+",");
                }
            }
            else if (n.next == null){
                System.out.print(n.element+"]");
            }
            else{
                System.out.print(n.element+",");
            }
        }
        System.out.println(""); // Just for decoration
    }
    //Task 2.3
    boolean isEmpty(){
        return head == null;
    }
    //Task 2.4
    void clear(){
        head = null;
    }
    //Task 2.5
    void insert(Node newElement){
        if(NodeAt(newElement) == -1){
            for (Node n = head; n != null; n = n.next) {
                if (n.next == null){
                    n.next = newElement;
                    break;
                }
            }
        }
        else{
            System.out.println("the key already exists At index: "+NodeAt(newElement));
        }
    }
    //Task 2.6
    void insert(int newElement, int index){
        if(index < 0 || index>=listSize(head)){
            throw new IndexOutOfBoundsException();
        }
        Node temp = new Node(newElement,null);
        int count = 0;
        for (Node n = this.head; n != null; n = n.next) {
            if(index == count){
                Node pred = NodeOfIndex(index-1);
                temp.next = pred.next;
                pred.next = temp;
            }
            count++;
        }
    }
    // Task 2.7
    Node remove(int delKey){
        if(this.isEmpty()){
            System.out.println("The list is empty");
            return null;
        }
        Node del = NodeOfKey(delKey);
        int delKeyindex  = NodeAt(del);
        Node pred = NodeOfIndex(delKeyindex -1);
        int count=0;
        for (Node n = head; n != null; n = n.next) {
            if(delKeyindex == count){
                pred.next = n.next;
            }
            count++;
        }
        return del;
    }
    
    //Task 3
    //Task 3.1
    void evenList(){
        Node newNodehead = null;
        Node tail= null;
        for (Node n = head; n != null; n = n.next) {
            if(n.element % 2 == 0){
                Node temp = new Node(n.element,null);
                if(newNodehead == null){
                    newNodehead = temp;
                    tail = newNodehead;
                }
                else{
                    tail.next = temp;
                }
            }
        }
        showList(newNodehead);

    }
    //Task 3.2
    void isThere(int key){ //return if a key is present or not
        boolean result = false;
        for (Node n = head; n != null; n = n.next) {
            if(key == n.element){
                result = true;
            }
        }
        if(result){
            System.out.println("True");
        }
        else{
            System.out.println("False");
        }
    }
    //Task 3.3
    void reverse(){ //{3,2,5,1};
        int size  = listSize(head);
        Node prev = null;
        Node current = head;
        Node front = current.next;
        for(int index = 0; index < size; index++) {
            current.next = prev;
            prev = current;
            current = front;
            if(front.next!= null){
                front = front.next;
            }
        }
        head = prev;
    }
    //task 3.4
    void sort(){
        int size = listSize(head);
        for (int count = 0;count<size;count++) {
            Node n = head;
            Node front = n.next;
            for (int index = 0;index < size-1;index++) {
                if(n.element > front.element){
                    int temp = n.element;
                    n.element = front.element;
                    front.element = temp;
                    n=n.next;
                    front=front.next;
                }
                else{
                    n=n.next;
                    front=front.next;
                }
            }
            
        }
        //showList(head);
    }
    //Task 3.5
    void sumOfList(){
        int sum = 0;
        for (Node n = head; n != null; n = n.next) {
            sum += n.element;
        }
        System.out.println("Sum is: "+ sum);
    }
    //Task 3.6
    void rotate(String dir,int k){
        int size = listSize(head);
        for (Node n = head; n != null; n = n.next) {
                if(n.next == null){
                    n.next = head;
                    break;
                }
            }
        if(dir =="left"){
            int count = 0;
            for (Node newN = head; count<k ; newN = newN.next,count++) {
                if(k - 1 == count){
                    head = newN.next;
                    newN.next = null;
                    break;
                }
            }
        }
        else if(dir == "right"){
            int count = 0;
            for (Node newN = head; count <= size - k -1 ; newN = newN.next,count++) {
                if(size - k-1 == count){
                    head = newN.next;
                    newN.next = null;
                    break;
                }
            }
        }
        else{
            System.out.println("Invalid input");
        }

        showList(head);
    }
    //+++++++++++++++ My methods section +++++++++++++
    int NodeAt(Node check){ // return the index of a given Node
        int count = 0;
        for (Node n = head; n != null; n = n.next) {
            if(n.element == check.element){
                return count;
            }
            count++;
        }
        return -1;
    }
    Node NodeOfIndex(int index){ // return the node of given index
        if(index < 0 || index>=listSize(head)){
            throw new IndexOutOfBoundsException();
        }
        int count =0;
        for (Node n = this.head; n != null; n = n.next) {
            if(index == count){
                return n;
            }
            count++;
        }
        return null;
    }
    Node NodeOfKey(int key){ // return the node of given Key
        for (Node n = head; n != null; n = n.next) {
            if(n.element == key){
                return n;
            }
        }
        return null;
    }
    
    int listSize(Node head){ //return the size of the node
        int count = 0;
        for (Node n = head; n != null; n = n.next) {
            count++;
        }
        return count;
    }
    public static int len(int[] a){ // return the length of an array
        int count = 0;
        for (int elements:a ){
           count++;
        }
        return count;
    }
}
//****************************** Creating Node class
//Task 1(i)
class Node{
    int element;
    Node next ;
    Node(int value,Node n){
        element = value;
        next = n;
    }
}