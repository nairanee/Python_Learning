'''
This script is created to test Tuples, List and Dict
'''
#List sort, reverse , append, pop
mylist = [10,20,30,40,50]

mylist.sort()
print (f'List of numbers skipping 1st value: {mylist[1:]}')
print (f'List of numbers mid 2 value: {mylist[2:4]}')
#reverese list
mylist.reverse()
print (f'reverse list: {mylist}')
#sort list
mylist.sort()
print('Sorted List : {}'.format(mylist))
#append list
mylist.append(92)
print (f'Added 92 to list :{mylist}')
#pop number ie delete from list
mylist.pop()
print ('Number popped is: %s' %(mylist))
