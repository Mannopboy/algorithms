# 1 - chap -> binary search

import time

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

#

#
#
#
#
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

# start = time.time()
# print(selectionSort(list_number))
# list_number.sort()
# print(list_number)
# end = time.time()
# print(f"Run time: {(end - start) * 10 ** 3:.03f}ms")

# 3 - chap -> find key in box

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

# 5 - chap -> hash tables

# 6 - chap -> breath-first / search
#
# from collections import deque
#
# graph = {}
#
# graph['you'] = ['alice', 'bob', 'claire']
# graph['bob'] = ['anuj', 'peggy']
# graph['alice'] = ['peggy']
# graph['claire'] = ['thom', 'jonny']
# graph['anuj'] = []
# graph['peggy'] = []
# graph['thom'] = []
# graph['jonny'] = []
#
# search_queue = deque()
# search_queue += graph['you']
#
#
# def person_is_seller(name):
#     return name[-1] == 'm'
#
# while search_queue:
#     person = search_queue.popleft()
#     if person_is_seller(person):
#         print(f'{person} is a mango seller')
#     else:
#         search_queue += graph[person]
#         print(False)
#
#
# def search(name):
#     search_queue = deque()
#     search_queue += graph[name]
#     searched = []
#     while search_queue:
#         person = search_queue.popleft()
#         if person not in searched:
#             if person_is_seller(person):
#                 print(f'{person} is a mango seller')
#                 return True
#             else:
#                 search_queue += graph[person]
#                 searched.append(person)
#     return False
#
#
# search('you')

# 7 - chap -> Dijkstra's algorithm

# infinity = float('inf')
# costs = {}
# costs['a'] = 6
# costs['b'] = 2
# costs['fin'] = infinity
#
# graph = {}
#
# graph['start'] = {}
# graph['start']['a'] = 6
# graph['start']['b'] = 2
#
# graph['a'] = {}
# graph['a']['fin'] = 1
#
# graph['b'] = {}
# graph['b']['a'] = 3
# graph['b']['fin'] = 5
#
# graph['fin'] = {}
#
# parents = {}
# parents['a'] = 'start'
# parents['b'] = 'start'
# parents['fin'] = None
#
# processed = []
#
#
# def find_lowest_cost_node(costs):
#     lowest_cost = float('inf')
#     lowest_cost_node = None
#     for node in costs:
#         cost = costs[node]
#         if cost < lowest_cost and node not in processed:
#             lowest_cost = cost
#             lowest_cost_node = node
#     return lowest_cost_node
#
#
# node = find_lowest_cost_node(costs)
# while node != None:
#     cost = costs[node]
#     neighbors = graph[node]
#     for n in neighbors.keys():
#         new_cost = cost + neighbors[n]
#         if costs[n] > new_cost:
#             costs[n] = new_cost
#             parents[n] = node
#     processed.append(node)
#     node = find_lowest_cost_node(costs)
#
# print(costs['fin'])
# print(parents['fin'])

balance = 0
cost_list = []
income_list = []
while True:
    balance = 0
    method = input('enter method: ')
    if method == 'reg':
        method = input('enter method reg: ')
        if method == 'pay':
            name = input('enter income name: ')
            price = input('enter income price: ')
            info = {
                'name': name,
                'price': int(price)
            }
            income_list.append(info)
        elif method == 'cost':
            name = input('enter cost name: ')
            price = input('enter cost price: ')
            info = {
                'name': name,
                'price': int(price)
            }
            cost_list.append(info)
    elif method == 'del':
        method = input('enter method del: ')
        if method == 'pay':
            name = input('enter income name: ')
            for item in income_list:
                if item['name'] == name:
                    index = income_list.index(item)
                    income_list.pop(index)
        elif method == 'cost':
            name = input('enter cost name: ')
            for item in cost_list:
                if item['name'] == name:
                    index = cost_list.index(item)
                    cost_list.pop(index)
    elif method == 'change':
        method = input('enter method change: ')
        if method == 'pay':
            name = input('enter income name: ')
            for item in income_list:
                if item['name'] == name:
                    new_name = input('enter income new name: ')
                    new_price = input('enter income new price: ')
                    item['name'] = new_name
                    item['price'] = int(new_price)
        elif method == 'cost':
            name = input('enter cost name: ')
            for item in cost_list:
                if item['name'] == name:
                    new_name = input('enter cost new name: ')
                    new_price = input('enter cost new price: ')
                    item['name'] = new_name
                    item['price'] = int(new_price)
    for item in income_list:
        balance += item['price']
    for item in cost_list:
        balance -= item['price']
    print(income_list)
    print(cost_list)
    print(balance)
