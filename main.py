# 1 - chap -> binary search

# import time
#
# index = 0
# index_1 = 0
# start = time.time()
# for number in range(100000000):
#     if number == 99987900:
#         index_1 = index
#     else:
#         index += 1
#
# end = time.time()
#
# print(index_1)
# print(f"Run time 1: {(end - start) * 10 ** 3:.03f}ms")
#
# start = time.time()
#
#
# def binary_search(list, item):
#     low = 0
#     high = len(list) - 1
#
#     while low <= high:
#         mid = (low + high)
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
#
# print(binary_search(range(100000000), 99987900))
# end = time.time()
#
# print(f"Run time 2: {(end - start) * 10 ** 3:.03f}ms")

# 2 - chap -> sort

# def findSmallest(arr):
#     smallest = arr[0]
#     smallest_index = 0
#     for i in range(1, len(arr)):
#         if arr[i] < smallest:
#             smallest = arr[i]
#             smallest_index = i
#     return smallest_index
#
#
# def selectionSort(arr):
#     newArr = []
#     for i in range(len(arr)):
#         smallest = findSmallest(arr)
#         newArr.append(arr.pop(smallest))
#     return newArr
#
#
# print(selectionSort([5, 6, 3, 7, 1]))

# 4  - chap -> quicksort

# def quickSort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array if i > pivot]
#         return quickSort(less) + [pivot] + quickSort(greater)
#
#
# print(quickSort([4, 10, 5, 2, 3]))

# 6 - chap -> breath-first / search

graph = {}

graph['you'] = ['alice', 'bob', 'claire']
