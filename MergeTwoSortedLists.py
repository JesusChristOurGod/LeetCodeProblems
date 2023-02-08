"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
def merge_two_lists(list1, list2):
    while True:
        if not(list1):
            return list2
        if len(list2)==0 and len(list1)>0:
            return list1
        a= list2.pop(0)
        for i in range (1,len(list1)):
            if list1[i-1]<=a<=list1[i]:
                list1.insert(i, a)
                break

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a=ListNode()
print(merge_two_lists(list1 = [], list2 = []))