class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # 创建一个哑节点作为新链表的头
    dummy = ListNode()
    current = dummy
    
    # 遍历两个链表
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # 将剩余的链表直接链接到新链表的末尾
    if l1:
        current.next = l1
    else:
        current.next = l2
    
    return dummy.next

# 测试代码
if __name__ == "__main__":
    # 创建链表1: 1 -> 2 -> 4
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    
    # 创建链表2: 1 -> 3 -> 4
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    
    # 合并链表
    merged_list = mergeTwoLists(l1, l2)
    
    # 输出合并后的链表
    result = []
    while merged_list:
        result.append(str(merged_list.val))
        merged_list = merged_list.next
    print("合并后的链表:", " -> ".join(result))  # 应输出 1 -> 1 -> 2 -> 3 -> 4 -> 4
