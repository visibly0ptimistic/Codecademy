# Definition for singly-linked list.
class ListNode(object):
    # define a node
    def __init__(self, val=0, next=None):
        # value of the node
        self.val = val
        # pointer to the next node
        self.next = next

# Iterative solution using 3 pointers to reverse the linked list 
class Solution(object):
    # define a function to reverse the linked list
    def reverseList(self, head):
        # define 3 pointers to keep track of the current, previous and next node
        prev, curr = None, head

        # loop through the linked list
        # while the current node is not None
        while curr:
            # store the next node
            temp = curr.next
            # reverse the current node
            curr.next = prev
            # move the pointers 
            prev = curr
            # move the pointers 
            curr = temp
        # return the reversed linked list
        return prev