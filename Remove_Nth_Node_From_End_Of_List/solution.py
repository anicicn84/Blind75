class Node:
    def __init__(self, value=0, next=None):
       self.value = value
       self.next = next


class Solution:
    def removeNth(self, head, n):
        
        # Step 1 of the explanation
        dummy = Node(0)
        dummy.next = head
        # step 2 of the explanation
        slow = fast = dummy
        # step 3 of the explanation
        for _ in range(n+1):
            fast = fast.next
            
        # step 4 of the explanation
        while fast:
            slow = slow.next
            fast = fast.next
        
        # step 5 of the explanation
        slow.next = slow.next.next
        
        # step 6 of the explanation
        return dummy.next
        
# Helper function to convert python list to linked list
def list_to_linkedlist(elements):
    head = Node(elements[0])
    current = head
    for element in elements[1:]:
        # Make a new node and add it to the head
        current.next = Node(element)
        # Make sure to move the current to the next node
        current = current.next
    return head

def print_linkedlist(head):
    elements = []
    while head:
        elements.append(str(head.value))
        head = head.next
    print(" -> ".join(elements))


sol = Solution()

# Example 1
list1 = list_to_linkedlist([1, 2, 3, 4, 5])
modified_list1 = sol.removeNth(list1, 2)
print_linkedlist(modified_list1)  # Expected: 1 -> 2 -> 3 -> 5

# Example 2
list2 = list_to_linkedlist([10, 20, 30, 40])
modified_list2 = sol.removeNth(list2, 4)
print_linkedlist(modified_list2)  # Expected: 20 -> 30 -> 40

# Example 3
list3 = list_to_linkedlist([7, 14, 21, 28, 35])
modified_list3 = sol.removeNth(list3, 3)
print_linkedlist(modified_list3)  # Expected: 7 -> 14 -> 28 -> 35