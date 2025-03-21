import numpy as np

# 创建一维数组
arr1 = np.array([1, 2, 3, 4])
print(arr1)  # 输出：[1 2 3 4]

# 创建二维数组
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)  
# 输出：
# [[1 2 3]
#  [4 5 6]]


# 示例数组
arr = np.array([[1, 2, 3], [4, 5, 6]])

# 数组的形状（shape）
print(arr.shape)  # 输出：(2, 3)

# 数组的维度（ndim）
print(arr.ndim)   # 输出：2

# 数组的大小（size）
print(arr.size)   # 输出：6

# 数组的数据类型（dtype）
print(arr.dtype)  # 输出：int64（或其他整数类型，取决于系统）

# 三维数组
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3)
# 输出：
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]
