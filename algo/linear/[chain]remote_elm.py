# 请写出python代码
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。    

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head: ListNode, val: int) -> ListNode:
    # 创建一个虚拟头节点，简化边界情况的处理
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    # 遍历链表
    while current.next:
        # 如果下一个节点的值等于目标值，则跳过该节点
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next

# 测试代码
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values) if values else "空链表")

# 测试示例
if __name__ == "__main__":
    # 测试用例 1: [1,2,6,3,4,5,6], val = 6
    test_list1 = create_linked_list([1,2,6,3,4,5,6])
    print("原始链表:")
    print_linked_list(test_list1)
    result1 = removeElements(test_list1, 6)
    print("删除值为6的节点后:")
    print_linked_list(result1)
    
    # 测试用例 2: [], val = 1
    test_list2 = create_linked_list([])
    print("\n原始链表:")
    print_linked_list(test_list2)
    result2 = removeElements(test_list2, 1)
    print("删除值为1的节点后:")
    print_linked_list(result2)
    
    # 测试用例 3: [7,7,7,7], val = 7
    test_list3 = create_linked_list([7,7,7,7])
    print("\n原始链表:")
    print_linked_list(test_list3)
    result3 = removeElements(test_list3, 7)
    print("删除值为7的节点后:")
    print_linked_list(result3)
