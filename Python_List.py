list1 = [4, 7, 3, 8, 2, 9, 23, 'Python', 2.3]

#
print(list1[0], list1[-1])

# Slicing examples

print(list1[2:7])  # [3, 8, 2, 9, 23]

print(list1[:8])  # [4, 7, 3, 8, 2, 9, 23, 'Python']

print(list1[-3: -1])  # [23, 'Python']

print(list1[::-1]) # [2.3, 'Python', 23, 9, 2, 8, 3, 7, 4]

#List methods

print(dir(list))
"""
'append', 'clear', 'copy', 'count',
 'extend', 'index', 'insert', 
 'pop', 'remove', 'reverse', 'sort'
"""

######### Adding data to the list #######

# add data at the end of list
# append method: add data at the end of list
list1 = [4, 7, 2, 8]
list1.append(50)
print(list1)

# insert method
list1.insert(2, 100)
print(list1)

list1.insert(2, [4, 7, 2])
print(list1)

# add multiple data to the list
lista = [3, 'a', 'b', 'c', 5, 7, 1]
listb = ['p', 'q', 'r']

"""
lista.extend(listb)
print("lista", lista)
print("listb", listb)
"""

# add two list with plus operator
listc = lista + listb

print("listc :", listc)
print("lista", lista)
print("listb", listb)

########### Remove data from the list ##########

listd = [8, [3, 6, 7], 'python', (4, 2, 7), 'python']

# remove method
"""
listd.remove('python')
print("listd:", listd)
"""

# pop method : pop method remove data with index, by default it takes -1 as default index

output = listd.pop()  # default index -1
print(output)
print("listd:", listd)
print("_"*50)
output2 = listd.pop(3)
print(output2)
print("listd:", listd)


# Remove all the data from list
print("_"*50)
liste = [8, [3, 6, 7], 'python', (4, 2, 7), 'python']
liste.clear()
print(liste)

# Delete entire list from memory
#del liste
#print(liste)

# Get index of any element from the list
print("_"*50)
listf = [8, [3, 6, 7], 'python', (4, 2, 7), 'Python']

output2 = listf.index('python')
print(output2)

for data in listf:
    print(data, ":", listf.index(data))

# get count of list data
print("_"*50)
listh = [5, 7, 2, 8, 2, 4, 1, 7, 2, 4]
print(listh.count(2))

temp = []
for data in listh:
    if data not in temp:
        print(data, ":", listh.count(data))
        temp.append(data)
    else:
        continue

# sort : it will sort the given list and modify inplace
print("_"*50)

listb = [4, 1, 7, 2, 8, 12, 6]

#listb.sort()  #  [1, 2, 4, 6, 7, 8, 12]
listb.sort(reverse=True)  #  [12, 8, 7, 6, 4, 2, 1]

print("listb:", listb)

# sorted method : it sort the list and return the output.

print("_"*50)
listc = [4, 7, 1, 6, 8, 2, 12, 15]
output = sorted(listc)

print(output)
print(listc)

# Reverse the data
# reverse method
print("_"*50)
listd = [5, 8, 9, 2, 8, 1, 15]
listd.reverse()
print("listd:", listd)

# reversed : it reverse the list and does not modify existing data
print("_"*50)

liste = [5, 7, 2, 8, 9]

output = reversed(liste)
print(output)
for data in output:
    print(data, end=" ")

print("liste:", liste)

# write a python program to reverse all the sublist in the given list

list33 = [[6, 8, 2], [5, 2, 6], [5, 1, 7, 8]]
#output = [[2, 8, 6], [6, 2, 5], [8, 7, 1, 5]]

output = []
for sublist in list33:
    print(sublist)
    sublist.reverse()
    output.append(sublist)

print(output)

# practice program
list1 = [5, 7, 8, 2, 9, 1, 4]
list2 = [2, 17, 18, 1, 2, 14, 5]

#output = [[5, 2], [7, 17], [8, 18], [2, 1], [9, 2], [1, 14], [4, 5]]
output = []
for i in range(len(list1)):
    print(i, list1[i], list2[i])
    sub_list = [list1[i], list2[i]]
    output.append(sub_list)

print(output)

##### copy() content from list ########
print("_"*50)
# Shallow Copy
listx = [5, 7, 2, 8, 1]
listy = listx
listz = listy
lista = listz
lista.append(60)

print("listx:", listx, id(listx))
print("listy:", listy, id(listy))
print("listz:", listz, id(listz))
print("lista:", lista, id(lista))



# Deep Copy

listx1 = [5, 17, 12, 8, 1]
listy1 = listx1.copy()
listy1.append(100)
listz1 = listy1.copy()

listz1.append(500)

print("listx1 :", listx1, id(listx1))
print("listy1 :", listy1, id(listy1))
print("listz1 :", listz1, id(listz1))

# get square of all the number from 1 to 10
output = []
for i in range(1, 11):
    print(i**2)
    output.append(i**2)
print(output)

# list comprehension
output2 = [x**2 for x in range(1, 11)]
print(output2)

# Get cube of all off numbers with if condition

output3 = [(x, x**3) for x in range(1, 11) if x%2 != 0]
print(output3)

# Tag all the even odd number with "even" and "odd"

output4 = [("even", x) if x%2 ==0 else ("odd", x) for x in range(1, 11)]
print(output4)

# Nested looping in list comprehension

output5 = [(x,y) for x in range(3) for y in range(4)]
print(output5)




