package LinkedListLab;

/**
 * Class representing a node in the singly linked list.
 * Note: This class is assumed to be defined elsewhere or nested, 
 * but since it's used in the code, I'm including a placeholder 
 * for completeness based on its usage (LLnode.data, LLnode.next).
 */
class LLnode {
    public int data;
    public LLnode next;

    public LLnode(int data) {
        this.data = data;
        this.next = null;
    }
}

public class linkedlist {
    public LLnode head;   
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

  
    // CONSTRUCTORS
    public linkedlist() { // Changed from LinkedListLab() to linkedlist() to match class name
        head = null;
    }
    
    //----------isEmpty----------
    public boolean isEmpty() {
        
        return head == null;
    }
    
    //----------search----------
    public boolean search(int data) {
        LLnode helpPtr=head;
        while (helpPtr != null){
            if(helpPtr.data==data)
                return true;
            helpPtr= helpPtr.next;
        }
        return false;
    }
    
    //----------printList----------
    public void printList() {
        // We need to traverse...so we need a help ptr
        LLnode helpPtr = head;
 // Traverse to correct insertion point
 while (helpPtr != null) {
            // Print the data value of the node
            System.out.print(helpPtr.data + ", ");
            // Step one node over
            helpPtr = helpPtr.next;
 }
 System.out.println();
    }
    
    //----------insert----------
    // Note: This implements an insertion that maintains sorted order
    public void insert(int data) {
        //create new node
        LLnode a = new LLnode(data);
        // IF there is no list, newNode will be the first node, so just return it
        if (head == null || head.data > data) {
            a.next=head;
            head = a;
        }  
        // ELSE, we have a list. Insert the new node at the correct location
        else {
            // We need to traverse to the correct insertion location...so we need a help ptr
            LLnode helpPtr = head;
            // Traverse to correct insertion point
            while (helpPtr.next != null) {
                if (helpPtr.next.data > data)
                    break; // we found our spot and should break out of the while loop
                helpPtr = helpPtr.next;
            }
            // Now make the new node. Set its next to point to the successor node.
            // And then make the predecessor node point to the new node
            a.next=helpPtr.next;
            helpPtr.next=a;
        }
    }
    
    //----------delete----------
    public boolean delete(int data) {
        // We can only delete if the list has nodes (is not empty)
        if (!isEmpty()) {
            // IF the first node (at the head) has the data value we are wanting to delete
            // we found it. Delete by skipping the node and making head point to the next node.
            if (head.data == data) {
                head = head.next;
                return true;
            }
            
            // ELSE, the data is perhaps somewhere else in the list...so we must traverse and look for it
            else {
                // We need to traverse to find the data we want to delete...so we need a help ptr
                LLnode helpPtr = head;
  // Traverse to correct deletion point
  while (helpPtr.next != null) {
                    if (helpPtr.next.data == data) {
                        helpPtr.next=helpPtr.next.next;
                        return true; // we deleted the value and should break out of the while loop and return true
                    }
                    helpPtr = helpPtr.next;
                }
            }  
        }
        // return false if the list is empty or the data is not found
        return false;
    }

    //----------sum----------
    public int sumNodes() {
        
        return 0;
    }
    
    //----------largestNode----------
    public int largestNode() {
        
        return 0;  
    }
    
    //----------secondNode----------
    public void secondNode() {
           
    }
    
    //----------secondLastNode----------
    public void secondLastNode() {
    }
    
    //----------Odd2Even2Odd----------
    public boolean Odd2Even2Odd() {
        
        return true; 
    }
    
    //----------countEvenOdd----------
    public void countEvenOdd() {
        
    }
    
    //----------swapFirstLast----------
    public boolean swapFirstLast() {     
            
        return true;                  
    }
    
    //----------addNodeAfter----------
    public boolean addNodeAfter(int newValue, int oldValue) { 
        
        return false;   
    }
    
    //----------deleteNodeAfter----------
    public boolean deleteNodeAfter(int value) {
         
        return false;
    } 
     
}