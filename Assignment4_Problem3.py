#%md
#Problem 3a
#Write a funtion called "is_reflexive" that takes in a dictionary as input (that represents a relation) and returns True if the relation is reflexive and False otherwise.

def is_reflexive(dictionary):
    length = len(dictionary)
    #print length
    count = 0
    # For each key in the given dictionary
    for key in dictionary:
        #print key
        # see if the key's list contains the key element
        if(key in dictionary[key]):
            count = count + 1

    # See if the number of keys equals the number of reflexive elements
    # if they equal, then the dictionary is reflexive
    if (count == length):
        return True
    else:
        return False

dictionary1 = {1:[2],2:[3],3:[5,6]}
dictionary2 = {1:[1,2],2:[2,3],3:[3,5,6]}
print 'Is the dictionary1 reflexive?: ',is_reflexive(dictionary1)
print 'Is the dictionary2 reflexive?: ',is_reflexive(dictionary2)

#%md
#Problem 3b
#Write a function "is_symmetric" that takes in a dictionary as input (that represents a relation) and returns True if the relation is symmectric and False otherwise.

def is_symmetric(dictionary):
    if (len(dictionary) == 0):
        return True

    # For each key in the given dictionary
    for key in dictionary:
        #print 'key: ',key
        # For each element in the key's list
        for target in dictionary[key]:
            #print 'target: ',target
            # prepare for an error...
            try:
                # see if the original key is found in the
                # element's key list
                if (key in dictionary[target]):
                    if(key == target):
                        continue
                    else:
                        return True
            except KeyError:
                # there is no key in the dictionary that is the same as
                # the element in the target's list.
                continue

    # if there is no symmetric relation seen yet, then the dictionary is
    # not symmetric, so return false.
    return False

dictionary1 = {1:[2],2:[3],3:[5,6]}
dictionary2 = {1:[2],2:[3,1],3:[5,6]}
print 'Is the dictionary1 symmectric?: ',is_symmetric(dictionary1)
print 'Is the dictionary2 symmectric?: ',is_symmetric(dictionary2)

#%md
#Problem 3-Bonus

#Write a third function, is_antisymmetric, that takes in a dictionary as input (that represents a relation) a returns True if the relation is antisymmetric and False otherwise.

def is_antisymmetric(dictionary):

    ### Method of attack: count the amount of edges and count the number
    ###                   of keys that are not symmetric to see if
    ###                   the whole relation is antisymmetric

    ####
    # This set up for loop counts the number of edges in the dictionary
    edges = 0
    for key in dictionary:
        edges = len(dictionary[key]) + edges
    ####

    count = 0

    for key in dictionary:
        #print (key)
        for target in dictionary[key]:
            #print(target)
            try:
                if (key in dictionary[target]):
                    if(key != target):
                        return False
                    else:
                        count = count + 1
                else:
                    count = count + 1
            except KeyError:
                count = count + 1
                continue

    #print "Count ", count
    #print "Edges ", edges
    if (count == edges):
        return True
    else:
        return False

dictionary1 = {1:[2],2:[3],3:[5,6]}
dictionary2 = {1:[2],2:[3,1],3:[5,6]}
dictionary3 = {0:[0,1,3],1:[2],2:[],3:[1]}

print 'Is the dictionary1 antisymmetric?: ',is_antisymmetric(dictionary1)
print 'Is the dictionary2 antisymmetric?: ',is_antisymmetric(dictionary2)
print 'Is the dictionary3 antisymmetric?: ',is_antisymmetric(dictionary3)

dictionary4 = {}
dictionary5 = {1:[2],2:[],3:[5,6]}
dictionary6 = {0:[0],1:[1],2:[2],3:[3]}

print 'Is the dictionary4 antisymmetric?: ',is_antisymmetric(dictionary4)
print 'Is the dictionary5 antisymmetric?: ',is_antisymmetric(dictionary5)
print 'Is the dictionary6 antisymmetric?: ',is_antisymmetric(dictionary6)

dictionary7 = {1:[1,2],2:[1,2],3:[3,1,2]}
dictionary8 = {1:[1,3],2:[3,2,1],3:[3]}
dictionary9 = {1:[2,3],2:[],3:[1]}
dictionary10 = {1:[],2:[],3:[]}
dictionary11 = {1:[1,2,3],2:[1,2,3],3:[1,2,3]}
dictionary12 = {1:[1,2,3,4],2:[2,4,3],3:[3],4:[4,3]}
dictionary13 = {1:[2,3,4],2:[2,3,4],3:[4],4:[4,2]}

print 'dictionary7 should not be antisymmetric: ',is_antisymmetric(dictionary7)
print 'dictionary8 should be antisymmetric: ',is_antisymmetric(dictionary8)
print 'dictionary9 should not be antisymmetric: ',is_antisymmetric(dictionary9)
print 'dictionary10 should be antisymmetric: ',is_antisymmetric(dictionary10)
print 'dictionary11 should not be antisymmetric: ',is_antisymmetric(dictionary11)
print 'dictionary12 should be antisymmetric: ',is_antisymmetric(dictionary12)
print 'dictionary13 should not be antisymmetric: ',is_antisymmetric(dictionary13)
#print _count(dictionary)
#print _count(dictionary2)


# FURTHER TESTING of functions

r = {0: [0,1], 1: [1,2], 2:[2,0]}
is_reflexive(r)
is_symmetric(r)

#True
#False

r = {0: [1,2], 1: [0,2], 2:[1,0]}
is_reflexive(r)
is_symmetric(r)
#False
#True

r = {0: [1], 1: [1,2], 2:[2,0]}
is_reflexive(r)
is_symmetric(r)
#False
#False

# "Complete" relation on three vertices
r = {0: [0,1,2], 1: [0,1,2], 2:[2,1,0]}
is_reflexive(r)
is_symmetric(r)
#True
#True

# Empty relation
r = { }
is_reflexive(r)
is_symmetric(r)
#True
#True
