class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def print_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    print(values)


# Typical test case
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = reverse_list(head)

print("Typical test case:", end=" ")
print_list(result)


# Edge case
head = ListNode(1)

result = reverse_list(head)

print("Edge case:", end=" ")
print_list(result)