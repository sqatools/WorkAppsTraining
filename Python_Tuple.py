# """
# -> its immutable we can not modify it
# -> it can contain any type of data.
# -> it follows same indexing like string and list
# """
#
# tup1 = (5, 7, 2, 8, 1, 9, 23)
#
# print(tup1[0])  # 5
#
# print(tup1[-2]) # 9
#
# # slicing in tuple
#
# print(tup1[1: 6])  # (7, 2, 8, 1, 9)
# print(tup1[::-1])  # (23, 9, 1, 8, 2, 7, 5)
# print(tup1[-4: -2]) # (8, 1)
#
# # Methods in tuple
#
# print(dir(tup1))
# # 'count', 'index'
#
# tup2 = (
#     23, 9, 1, 8,
#     2, 7, 5, 90,
#     7, 8, 9, 23, 70
# )
#
# # get count of 9
# print(tup2.count(9))  # 2
#
# # Get index of 23
# print(tup2.index(90)) # 7
#
# # reverse the tuple data
# revere_data = reversed(tup2)
# print(revere_data)
# for data in revere_data:
#     print(data, end=" ")
#
# # sort the tuple data
# print()
# sorted_data = sorted(tup2)
# print(sorted_data)
#
#
# # Program :
# tuple1 = ('Python', 'Programming', 'Language', 'Hello', 'h')
# #output = ('PPYTHOnn', 'PPROGRAMMINgg', 'LLANGUAGee', 'HHELLoo')
# output= []
# for data in tuple1:
#     print(data)
#     last_char = data[-3:-1] * 2
#     first_char = data[:2]*2
#     middle_char = data[1:-1].upper()
#     combine_data = f"{first_char}_{middle_char}_{last_char}"
#     output.append(combine_data)
#
# print(tuple(output))
#
#
# from Python_Functions.Python_Functions3 import *
# print(addition(60, 30))
#
s = 'Radar'
print(s.strip('dear'))
