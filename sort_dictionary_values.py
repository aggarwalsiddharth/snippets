# sorting dictionary with:
d = {'a':1,'b':2,'c':3}
sorted(d) 
# op: ['a','b','c']
# this returns only the keys of the dictionary

sorted(d,reverse = True)
# op: ['c','b','a']

# To sort by values in this case (where only the keys are returned)
d = sorted(d, key = lambda x:d[x])

## To also see values in this dict:
sorted(d.items())
# op: [('a',1),('b',2),('c',3)]


# To sort by values in this case (where values are also needed)
sorted(d.items(), key = lambda x:x[1], reverse = True)
# op: [('c':3,),('b':2),('a':1)]


