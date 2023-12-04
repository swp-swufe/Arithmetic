class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq


class Solution:
    def mergeKLists(self, lists: list) -> [ListNode]:
        '''
        :param lists: List[Optional[ListNode]]
        :return: List[ListNode]
        '''
        heap = []
        heapq.heapify(heap)
        dummy = cur = ListNode(0)

        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i))
        while heap:
            val, i = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(heap, (lists[i].val, i))
        return dummy.next
