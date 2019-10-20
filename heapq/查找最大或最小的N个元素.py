#查找最大或最小的N个元素
import heapq
nums = [20, -9, 104, 84, 0.29, 3834, 67, 5, 89, 2, 3]
print(heapq.nlargest(3, nums))   #最大的3个数
print(heapq.nsmallest(3, nums))  #最小的3个数

#heapq.heapify(nums)
#实现堆数据结构
