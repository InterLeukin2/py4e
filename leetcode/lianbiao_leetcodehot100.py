#160.相交链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 如果链表为空，直接返回 None
        if not headA or not headB:
            return None

        # 初始化指针 pA 和 pB
        pA, pB = headA, headB

        # 遍历两个链表，直到两个指针相遇或者都为 None
        while pA != pB:
            # 如果 pA 到达链表 A 的末尾，则跳到链表 B 的头部
            pA = pA.next if pA else headB  # 这行代码的逻辑是：如果 pA 不为 None，即 pA 还有下一个节点（pA.next 不是 None），那么 pA = pA.next 就是正常的指针移动。
            # 如果 pB 到达链表 B 的末尾，则跳到链表 A 的头部
            pB = pB.next if pB else headA

        # 如果 pA 和 pB 相遇，则返回相遇节点，否则返回 None
        return pA




"""
206.反转列表：给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
206 关键步骤：
	•	next_node：是指向下一个节点的引用，帮助我们在改变链表链接时不丢失链表的后续部分。
	•	curr.next：是我们反转链表的关键，通过将它指向前一个节点 prev，来达到链表反转的目的。
	•	prev 和 curr：分别保存反转链表过程中当前节点的前一个节点和当前节点。

结论：

每一轮的循环，只会生成 2 个值：
	1.	next_node：保存当前节点的下一个节点，防止反转时丢失链表的其余部分。
	2.	curr.next：将当前节点的 next 指针指向前一个节点，实际反转链表的操作。

curr 和 prev 是用来遍历和反转链表的指针，它们在每一轮循环中都会更新。"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:#Optional 是 Python 标准库 typing 模块的一部分，表示一个值可以是某种类型或 None
        prev = None  # 初始化前驱节点为 None
        curr = head  # 当前节点从头节点开始遍历

        # 遍历链表
        while curr:#好简洁
            next_node = curr.next  # 暂存下一个节点
            curr.next = prev  # 反转当前节点的指针
            prev = curr  # 前驱节点移到当前节点
            curr = next_node  # 当前节点移到下一个节点

        # 最后， prev 会指向新的头节点
        return prev

#234.回文链表
#给你一个单链表的头节点 head ，请你判断该链表是否为回文链表如果是，返回 true ；否则，返回 false 。
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 边界情况：空链表或只有一个节点的链表直接返回 True
        if not head or not head.next:
            return True

        # 步骤 1: 快慢指针找到链表的中点
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 步骤 2: 反转链表的后半部分
        prev = None  # 这里prev是反转后最后一个节点指向的节点，prev最后会变成最后一个节点，因为slow.next会指向none
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # 步骤 3: 比较前半部分和反转后的后半部分
        left, right = head, prev
        while right:  # 只需要比较右半部分，因为如果右半部分都相同，左半部分一定也相同，这个写法比较简洁
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

