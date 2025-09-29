class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # ----------isEmpty----------
    def is_empty(self):
        return self.head is None

    # ----------search----------
    def search(self, data):
        help_ptr = self.head
        while help_ptr is not None:
            if help_ptr.data == data:
                return True
            help_ptr = help_ptr.next
        return False

    # ----------printList----------
    def print_list(self):
        help_ptr = self.head
        while help_ptr is not None:
            print(help_ptr.data, end=", ")
            help_ptr = help_ptr.next
        print()

    # ----------insert----------
    def insert(self, data):
        a = LLNode(data)
        if self.head is None or self.head.data > data:
            a.next = self.head
            self.head = a
        else:
            help_ptr = self.head
            while help_ptr.next is not None:
                if help_ptr.next.data > data:
                    break
                help_ptr = help_ptr.next
            a.next = help_ptr.next
            help_ptr.next = a

    # ----------delete----------
    def delete(self, data):
        if not self.is_empty():
            if self.head.data == data:
                self.head = self.head.next
                return True
            else:
                help_ptr = self.head
                while help_ptr.next is not None:
                    if help_ptr.next.data == data:
                        help_ptr.next = help_ptr.next.next
                        return True
                    help_ptr = help_ptr.next
        return False

    # ----------sum----------
    def sum_nodes(self):
        total = 0
        help_ptr = self.head
        while help_ptr is not None:
            total += help_ptr.data
            help_ptr = help_ptr.next
        return total

    # ----------largestNode----------
    def largest_node(self):
        if self.is_empty():
            return None
        largest = self.head.data
        help_ptr = self.head.next
        while help_ptr is not None:
            if help_ptr.data > largest:
                largest = help_ptr.data
            help_ptr = help_ptr.next
        return largest

    # ----------secondNode----------
    def second_node(self):
        if self.head is None or self.head.next is None:
            return None
        return self.head.next.data

    # ----------secondLastNode----------
    def second_last_node(self):
        if self.head is None or self.head.next is None:
            return None
        help_ptr = self.head
        while help_ptr.next.next is not None:
            help_ptr = help_ptr.next
        return help_ptr.data

    # ----------Odd2Even2Odd----------
    def odd2even2odd(self):
        # placeholder (depends on actual requirement)
        return True

    # ----------countEvenOdd----------
    def count_even_odd(self):
        even_count = 0
        odd_count = 0
        help_ptr = self.head
        while help_ptr is not None:
            if help_ptr.data % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
            help_ptr = help_ptr.next
        return even_count, odd_count

    # ----------swapFirstLast----------
    def swap_first_last(self):
        if self.head is None or self.head.next is None:
            return False
        prev = None
        curr = self.head
        while curr.next is not None:
            prev = curr
            curr = curr.next
        # curr is last node, prev is second last
        curr.data, self.head.data = self.head.data, curr.data
        return True

    # ----------addNodeAfter----------
    def add_node_after(self, new_value, old_value):
        help_ptr = self.head
        while help_ptr is not None:
            if help_ptr.data == old_value:
                new_node = LLNode(new_value)
                new_node.next = help_ptr.next
                help_ptr.next = new_node
                return True
            help_ptr = help_ptr.next
        return False

    # ----------deleteNodeAfter----------
    def delete_node_after(self, value):
        help_ptr = self.head
        while help_ptr is not None and help_ptr.next is not None:
            if help_ptr.data == value:
                help_ptr.next = help_ptr.next.next
                return True
            help_ptr = help_ptr.next
        return False
