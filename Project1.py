import CircularLinkedList

def read_circular_linked_list():
    cll = CircularLinkedList.CircularLinkedList()
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        data = int(input("Enter the element: "))
        cll.add_last(data)
    return cll

cll = read_circular_linked_list()

# Find minimum element in a circular linked list and print address of the node
def find_min(cll):
    current = cll.head.next
    min = current.data
    min_element_index = 0
    for i in range(cll.size):
        if current.data < min:
            min = current.data
            min_element_index = i
        current = current.next
    return min, min_element_index

print("min", find_min(cll)[0], "address", find_min(cll)[1])