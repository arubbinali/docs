public class LinkedList {
    public LLnode head;

    // ----------constructor----------
    public LinkedList() {
        head = null;
    }

    // ----------isEmpty----------
    public boolean isEmpty() {
        return head == null;
    }

    // ----------search----------
    public boolean search(int data) {
        LLnode helpPtr = head;
        while (helpPtr != null) {
            if (helpPtr.data == data)
                return true;
            helpPtr = helpPtr.next;
        }
        return false;
    }

    // ----------printList----------
    public void printList() {
        LLnode helpPtr = head;
        while (helpPtr != null) {
            System.out.print(helpPtr.data + ", ");
            helpPtr = helpPtr.next;
        }
        System.out.println();
    }

    // ----------insert (sorted insert)----------
    public void insert(int data) {
        LLnode a = new LLnode(data);
        if (head == null || head.data > data) {
            a.next = head;
            head = a;
        } else {
            LLnode helpPtr = head;
            while (helpPtr.next != null) {
                if (helpPtr.next.data > data)
                    break;
                helpPtr = helpPtr.next;
            }
            a.next = helpPtr.next;
            helpPtr.next = a;
        }
    }

    // ----------delete----------
    public boolean delete(int data) {
        if (!isEmpty()) {
            if (head.data == data) {
                head = head.next;
                return true;
            } else {
                LLnode helpPtr = head;
                while (helpPtr.next != null) {
                    if (helpPtr.next.data == data) {
                        helpPtr.next = helpPtr.next.next;
                        return true;
                    }
                    helpPtr = helpPtr.next;
                }
            }
        }
        return false;
    }

    // ----------sum----------
    public int sumNodes() {
        int total = 0;
        LLnode helpPtr = head;
        while (helpPtr != null) {
            total += helpPtr.data;
            helpPtr = helpPtr.next;
        }
        return total;
    }

    // ----------largestNode----------
    public int largestNode() {
        if (isEmpty()) return Integer.MIN_VALUE;
        int largest = head.data;
        LLnode helpPtr = head.next;
        while (helpPtr != null) {
            if (helpPtr.data > largest) {
                largest = helpPtr.data;
            }
            helpPtr = helpPtr.next;
        }
        return largest;
    }

    // ----------secondNode----------
    public Integer secondNode() {
        if (head == null || head.next == null) return null;
        return head.next.data;
    }

    // ----------secondLastNode----------
    public Integer secondLastNode() {
        if (head == null || head.next == null) return null;
        LLnode helpPtr = head;
        while (helpPtr.next.next != null) {
            helpPtr = helpPtr.next;
        }
        return helpPtr.data;
    }

    // ----------Odd2Even2Odd----------
    public boolean Odd2Even2Odd() {
        // unclear requirement, returning true as placeholder
        return true;
    }

    // ----------countEvenOdd----------
    public void countEvenOdd() {
        int evenCount = 0;
        int oddCount = 0;
        LLnode helpPtr = head;
        while (helpPtr != null) {
            if (helpPtr.data % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
            helpPtr = helpPtr.next;
        }
        System.out.println("Even count: " + evenCount + ", Odd count: " + oddCount);
    }

    // ----------swapFirstLast----------
    public boolean swapFirstLast() {
        if (head == null || head.next == null) return false;

        LLnode prev = null;
        LLnode curr = head;

        while (curr.next != null) {
            prev = curr;
            curr = curr.next;
        }

        // swap data of head and last
        int temp = head.data;
        head.data = curr.data;
        curr.data = temp;
        return true;
    }

    // ----------addNodeAfter----------
    public boolean addNodeAfter(int newValue, int oldValue) {
        LLnode helpPtr = head;
        while (helpPtr != null) {
            if (helpPtr.data == oldValue) {
                LLnode newNode = new LLnode(newValue);
                newNode.next = helpPtr.next;
                helpPtr.next = newNode;
                return true;
            }
            helpPtr = helpPtr.next;
        }
        return false;
    }

    // ----------deleteNodeAfter----------
    public boolean deleteNodeAfter(int value) {
        LLnode helpPtr = head;
        while (helpPtr != null && helpPtr.next != null) {
            if (helpPtr.data == value) {
                helpPtr.next = helpPtr.next.next;
                return true;
            }
            helpPtr = helpPtr.next;
        }
        return false;
    }
}

// Node class
class LLnode {
    int data;
    LLnode next;

    public LLnode(int data) {
        this.data = data;
        this.next = null;
    }
}