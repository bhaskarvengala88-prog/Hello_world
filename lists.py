'''
lists store multiple elements or data types in single variable .which are same or different types
'''

# l=[1,2,"msd",'a',23.33,12+0j,True,False,123]
# print(l)

'''' index or position (start with zero and ends length of list-1)
'''
# l1=[20,10,40,50,60,70,80,'a','m','c']
# print(l1[0]) # positive index start from 0 left to right search.
# print(l1[-1]) # negative inex start from -1 right to left search.

# # length of list
# print(len(l1))



'''
 Iterating through the lists using index

 Values are not enough for these cases 

Modifying elements in place

Accessing multiple lists at the same index

Knowing the position of an element
'''

# using index 
# for loop
# l2=[1,2,3,4,5,6,7,8,9,10]
# a=len(l2)
# for i in range(0,a):
#     print(l2[i])


# while loop
# l3=[1,2,3,4,5,6,7,8,8,8]
# a=len(l3)
# b=0
# while b<a:
#     print(l3[b])
#     b=b+1


'''
Iterating through the list using value 

You directly get each element of the list.

simple and more readable

avoids index erros

If our task depends on what the item is, not where it is.

Great for comparisons and conditions.

if we want to perform the arthematic operations on integers on list(we only need result we dont need where int is come from)

'''

# l4=[1,2,3,4,5,56,66]
# # for i in l4:
# #     print(i)


# note= With a while loop, you cannot avoid using an index when iterating over a list.