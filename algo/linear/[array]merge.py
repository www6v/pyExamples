
# 合并两个有序数组
def merge(nums1, m, nums2, n):
    # 初始化三个指针
    i = m - 1  # nums1有效元素末尾
    j = n - 1  # nums2末尾
    k = m + n - 1  # 合并后数组末尾
    
    # 从后向前比较并填充
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    # 处理nums2中剩余元素
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# 测试代码
if __name__ == "__main__":
    # 测试用例1
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge(nums1, m, nums2, n)
    print("合并后的数组:", nums1)  # 应输出 [1,2,2,3,5,6]
    
    # 测试用例2
    nums1 = [4,5,6,0,0,0]
    m = 3
    nums2 = [1,2,3]
    n = 3
    merge(nums1, m, nums2, n)
    print("合并后的数组:", nums1)  # 应输出 [1,2,3,4,5,6]
