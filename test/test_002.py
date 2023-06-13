from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    dummy = ListNode(0)
    curr = dummy
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        carry, sum_val = divmod(val1 + val2 + carry, 10)
        curr.next = ListNode(sum_val)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

def list_to_listnode(input_list):
    """ Build ListNode from list """
    # initialize node, not to be included in the final result
    node = ListNode()
    # keep node at the beginning of the linked list
    temp = node

    if len(input_list) == 1:
        # if single node, return as it is
        node.next = ListNode(val=input_list[0], next=None)
    else:
        for i in input_list:
            current_node = ListNode(val=i)
            # next node is current node
            temp.next = current_node
            # move node to next node to build the linked list
            temp = temp.next
    # exclude the root node
    return node.next
def test_addTwoNumbers():
    list_node_1 = list_to_listnode([2, 4, 3])
    list_node_2 = list_to_listnode([5, 6, 4])

    target_node = list_to_listnode([7, 0, 8])
    assert addTwoNumbers(list_node_1, list_node_2) == target_node

