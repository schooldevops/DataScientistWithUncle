from platform import python_branch
import numpy as np

# 1차원 배열 생성
array_1d = np.array([1, 2, 3, 4, 5])
print(array_1d)

# 출력 결과
# [1 2 3 4 5]

# 2차원 배열 생성
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array_2d)
# Output:
# [[1 2 3]
#  [4 5 6]]

print("Shape of the array:", array_2d.shape)  # Output: (2, 3)
print("Data type of the array:", array_2d.dtype)  # Output: int64 (or similar depending on your system)

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
result = array_a + array_b
print(result)  # Output: [5 7 9]

## 배열과 Scalar 연산하기
scalar = 3
result = array_a * scalar
print(result)  # Output: [3 6 9]

## 배열에 수학함수 적용하기. 
# Finding the mean
mean_value = np.mean(array_a)
print("Mean:", mean_value)  # Output: 2.0

# Finding the standard deviation
std_dev = np.std(array_a)
print("Standard Deviation:", std_dev)  # Output: 0.816496580927726

## 인덱스로 배열값 가져오기 
# Accessing the first element
first_element = array_1d[0]
print("First element:", first_element)  # Output: 1

# Slicing the array
sliced_array = array_1d[1:4]
print("Sliced array:", sliced_array)  # Output: [2 3 4]

## 배열의 차원변경

# Creating a 1D array
array_1d = np.array([1, 2, 3, 4, 5, 6])
# Reshaping to 2D array (2 rows, 3 columns)
array_reshaped = array_1d.reshape(2, 3)
print(array_reshaped)
# Output:
# [[1 2 3]
#  [4 5 6]]

## 배열 간의 결합하기. 

array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])
# Concatenating along the first axis (1D)
combined_array = np.concatenate((array_a, array_b))
print(combined_array)  # Output: [1 2 3 4 5 6]

# 2차원 배열 간의 결합하기. 
array_2d_a = np.array([[1, 2, 3], [4, 5, 6]])
array_2d_b = np.array([[7, 8, 9]])
combined_2d_array = np.concatenate((array_2d_a, array_2d_b), axis=0)
print(combined_2d_array)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

## 배열 분할하기

array = np.array([1, 2, 3, 4, 5, 6])
# Splitting into 3 equal parts
split_arrays = np.split(array, 3)
print(split_arrays)
# Output: [array([1, 2]), array([3, 4]), array([5, 6])]

## 배열의 특정 인덱스값 가져오기
array = np.array([1, 2, 3, 4, 5, 6])
# Selecting elements greater than 3
filtered_array = array[array > 3]
print(filtered_array)  # Output: [4 5 6]

## 브로드캐스팅
array_a = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10
# Adding a scalar to an array
result = array_a + scalar
print(result)
# Output:
# [[11 12 13]
#  [14 15 16]]

## 고급 배열 인덱싱

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Selecting specific elements
selected_elements = array[[0, 1, 2], [0, 1, 2]]  # Diagonal elements
print(selected_elements)  # Output: [1 5 9]

## 배열의 통계적 함수 사용하기. 

array = np.array([1, 2, 3, 4, 5])
# Finding the sum
sum_value = np.sum(array)
print("Sum:", sum_value)  # Output: 15

# Finding the maximum
max_value = np.max(array)
print("Max:", max_value)  # Output: 5

# Finding the minimum
min_value = np.min(array)
print("Min:", min_value)  # Output: 1