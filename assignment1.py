# -*- coding: utf-8 -*-
"""assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/102VXcXxJv9Gw6ekHWzzwGfOC9l7RzpqQ
"""

''' Q1 .Exercise Question 1: Given a two list. Create a
third list by picking an odd-index element from the first list and even index
elements from the second.'''

#Answer ==>
a=[10,20,30,40,50,60,70,80]
b=[11,22,33,44,55,66,77,88]
c=[]
for element in range (len(a)):
  if element%2 != 0:
    c.append(a[element])
for i in range (len(b)):
  if i%2 == 0:
    c.append(b[i])
print(c)

'''Q2 .Given a number count the total
number of digits in a number'''

#Answer ==> 
no=input("Enter a number :")
x=list(no)
print("Number of digits in list are :",len(x))

'''Q3 .Write a Python program to print the numbers of a
specified list after removing even numbers from it. '''

s=[22,43,6,9,3,57,93,12]
for element in s:
  if element%2==0:
    s.remove(element)
print(s)

'''Q4 .Write a Python program to generate and print a list of
first and last 5 elements where the values are square of numbers between 1 and
30 (both included). '''

f=[]
for i in range (1):
  i+=1
  for j in range (i,31):
    s=j**2
    #print(s)
    f.append(s)
print(f)
print(f[0:5])
print(f[-1:-6:-1])

'''Q5 .Write a Python program to generate all permutations of a list in Python.'''

n=0
p=[3,1,2]
print(p)
p.sort()
print(p)
p.sort(reverse=True)
print(p)

import itertools

list1 = [1, 2, 3]

perm = []

for i in range(1,len(list1)+1):
    perm.extend(list(itertools.permutations(list1, r=i)))
print(perm)

'''Q6 .Write a python program to check whether two lists are
circularly identical.'''

a=[3,4,1,2]
b=[1,2,3,4]
x=0
y=0
while True:
  e=a[0]
  a.pop(0)
  a.append(e)
  d=len(b)
  x+=1
  if a==b:
    print ('identical')
    break
  if x==y:
    print ('not identical')
    break

'''Q7 Write a Python
program to change the position of every n-th value with the (n+1)th in a
list. 
Sample list: [0,1,2,3,4,5]





Expected Output: [1, 0, 3, 2, 5, 4]'''

s=0
list=[]
a=[1,2,3,4,5,6]
for i in a:
  for j in a:
    j=i+1
    list.append(j)
    list.append(i)
    break 
  i=j+1  
print(list)

s=0
list=[]
a=[1,2,3,4,5,6]
for i in range(len(a)):
  i=i+1
  list.append(a[i])
  i=i-1
  list.append(a[i])
  break
for i in range(len(a)):
  i=i+3
  list.insert(2,a[i])
  i=i-1
  list.insert(3,a[i])
  break
for i in range(len(a)):
  i=i+5
  list.insert(4,a[i])
  i=i-1
  list.insert(5,a[i])
  break
print(list)



a=[1,2,3,4,5,6]
list=[]
for i in a:
  if i%2!=0:
    print(i)
    list.append(i)
for i in a:
  if i%2==0:
    print(i)
    list.insert(5,i)
print((list))

'''Q8 .Write a Python program to generate the combinations of n
distinct objects taken from the elements of a given list. Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2
distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]'''

k=[1, 2, 3, 4, 5, 6, 7, 8, 9]
s=[]
for i in k:
  for j in k:
    r=[]
    if (i == j):
      continue
    elif (i != j):
      r.append(i)
      r.append(j)
    s.append(r)
print(s)

'''Q9 .Write
a Python program to iterate over two lists simultaneously.'''

#Write a Python program to iterate over two lists simultaneously.  
a=[8,9,6,5,4,4]
b=[1,4,9,3,7,0,5,3]
c=[]
d=0
for i in a:
    c.append(i)
    c.append(b[d])
    d+=1
print(c)

'''Q10 .Write a Python program to remove duplicates from a list of
lists. 



Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33],
[40]]


New List : [[10, 20], [30, 56, 25], [33], [40]]'''

a = [1,22,22,26,22,65,26,55,45,32,1]
b = []
for i in a:
    if i not in b:
           b.append(i)

print(b)

a = [1,22,22,26,22,65,26,55,45,32,1]
aset=set(a)
aset

