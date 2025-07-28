# 快速排序算法实现

def quick_sort(arr: list[int]) -> list[int]:
    """
    使用快速排序算法对整数列表进行排序
    
    参数:
        arr: 需要排序的整数列表
    
    返回:
        排序后的整数列表
    """
    if len(arr) <= 1:
        return arr
    
    # 选择第一个元素作为基准值
    pivot = arr[0]
    
    # 分区过程
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    
    # 递归排序并合并结果
    return quick_sort(left) + [pivot] + quick_sort(right)


# 优化版本：原地快速排序

def quick_sort_in_place(arr: list[int], low: int = 0, high: Optional[int] = None) -> None:
    """
    原地快速排序实现，不创建新列表
    
    参数:
        arr: 需要排序的整数列表
        low: 当前排序区间的起始索引
        high: 当前排序区间的结束索引
    """
    if high is None:
        high = len(arr) - 1
        
    if low < high:
        # 进行分区操作，获取基准值的最终位置
        pivot_index = partition(arr, low, high)
        
        # 递归排序左右子数组
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)


def partition(arr: list[int], low: int, high: int) -> int:
    """
    分区函数，将数组分为两部分并返回基准值的索引
    
    参数:
        arr: 要分区的数组
        low: 分区起始索引
        high: 分区结束索引
    
    返回:
        基准值的最终位置索引
    """
    # 选择最右边的元素作为基准值
    pivot = arr[high]
    
    # i表示小于基准值区域的边界
    i = low - 1
    
    for j in range(low, high):
        # 如果当前元素小于或等于基准值，则扩展小于区域
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # 将基准值放到最终位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# 测试代码
if __name__ == "__main__":
    import random
    from typing import Optional
    
    # 测试基本功能
    test_cases = [
        [],  # 空列表
        [5],  # 单元素
        [3, 1, 4, 1, 5, 9, 2, 6],  # 随机序列
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],  # 逆序
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # 正序
        [5, 3, 5, 1, 5, 9, 5, 6]  # 重复元素
    ]
    
    for i, case in enumerate(test_cases):
        # 测试普通快速排序
        sorted_normal = quick_sort(case.copy())
        # 测试原地快速排序
        case_copy = case.copy()
        quick_sort_in_place(case_copy)
        
        # 验证结果
        assert sorted_normal == sorted(case), f"普通快排测试用例 {i+1} 失败"
        assert case_copy == sorted(case), f"原地快排测试用例 {i+1} 失败"
        
    print("所有测试通过!")
    
    # 性能测试
    large_data = [random.randint(0, 100000) for _ in range(10000)]
    
    # 测试普通快排
    import time
    start = time.time()
    quick_sort(large_data.copy())
    normal_time = time.time() - start
    
    # 测试原地快排
    start = time.time()
    data_copy = large_data.copy()
    quick_sort_in_place(data_copy)
    in_place_time = time.time() - start
    
    print(f"普通快排处理10000个元素耗时: {normal_time:.4f}秒")
    print(f"原地快排处理10000个元素耗时: {in_place_time:.4f}秒")