'''
以下是常见的排序算法的大纲总结：

1. 交换排序（Exchange Sort）

	•	冒泡排序（Bubble Sort）
	•	快速排序（Quick Sort）

2. 选择排序（Selection Sort）

	•	简单选择排序（Simple Selection Sort）

3. 插入排序（Insertion Sort）

	•	直接插入排序（Direct Insertion Sort）
	•	二分插入排序（Binary Insertion Sort）

4. 合并排序（Merge Sort）

	•	自顶向下合并排序（Top-down Merge Sort）
	•	自底向上合并排序（Bottom-up Merge Sort）

5. 分配排序（Distribution Sort）

	•	计数排序（Counting Sort）
	•	基数排序（Radix Sort）
	•	桶排序（Bucket Sort）

6. 堆排序（Heap Sort）

	•	最大堆排序（Max Heap Sort）
	•	最小堆排序（Min Heap Sort）

7. 希尔排序（Shell Sort）

	•	希尔增量排序（Shell’s Increment Sort）

8. Tim Sort
'''

#1.1冒泡排序
def bubble_sort(arr:list[int]) -> list[int]:
    breakpoint()
    n = len(arr) #n是int，不是index
    for i in range(n):#i 的作用其实是为了缩短比较长度，因为最大的在最后不用比较了
        for j in range(0, n - i - 1):  # 每轮缩短比较长度
            if arr[j] > arr[j + 1]:    # 如果左边比右边大，交换
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 测试
arr = [5, 2, 9, 1, 5, 6]
print("冒泡排序结果:", bubble_sort(arr))

#1.2 快速排序
def quick_sort(arr:list[int]) -> list[int]:
    # 如果列表为空或仅包含一个元素，则直接返回
    if len(arr) <= 1:
        return arr
    else:
        # 选择一个基准元素，通常选择第一个元素
        pivot = arr[0]
        # 分别创建小于基准、大于基准的子列表
        less_than_pivot = [x for x in arr[1:] if x <= pivot]  #语法结构：[expression for item in iterable if condition]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        # 递归地排序两个子列表，并将结果合并
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# 示例
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted Array:", sorted_arr)

#2.选择排序（Selection Sort）
