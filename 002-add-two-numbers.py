from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = self.node_to_number(l1)
        n2 = self.node_to_number(l2)
        target = n1 + n2

        result = self.number_to_node(target)
        return result

    def node_to_number(self, node):
        """ Return number from node """
        result = 0
        count = 0
        while node:
            result += (node.val * 10 ** count)
            count += 1
            node = node.next
        return result

    def number_to_node(self, number):
        """ Return ListNode from number """
        result = []
        for i in str(number):
            result.append(int(i))

        # reverse result and convert to ListNode
        result = result[::-1]
        node = self.list_to_listnode(result)
        return node

    @staticmethod
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

class Solution:
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