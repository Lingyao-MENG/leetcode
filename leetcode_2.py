class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        def dfs(l, r, i):
            if not l and not r and not i: return None
            s = (l.val if l else 0) + (r.val if r else 0) + i
            node = ListNode(s % 10)
            node.next = dfs(l.next if l else None, r.next if r else None, s // 10)
            return node
        return dfs(l1, l2, 0)


def listtolistlink(list):
    head = ListNode(list[0])
    p = head
    for i in range(1, len(list)):
        p.next = ListNode(list[i])
        p = p.next
    return head


if __name__ == "__main__":
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    l1 = listtolistlink(l1)
    l2 = listtolistlink(l2)
    head = Solution().addTwoNumbers(l1, l2)
    while head:
        print(head.val)
        head = head.next