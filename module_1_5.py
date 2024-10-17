immutable_var = (1 , 2 , 'd' , 'gena')
print('Immutable tuple:', immutable_var)
try:
      immutable_var[0] = 10
except TypeError as e:
 print('error: ', e)
mutable_list=[1 , 2 , 'd' , 'gena']
mutable_list[2]='modified'
print('mutable_list: ' , mutable_list)
