# Tyson Spoelma
# MTH 325
# Homework 5


def is_function(dictionary):
    for key in dictionary:
        if(len(dictionary[key]) != 1):
           return False
    return True

def is_injective(dictionary):
    if(is_function(dictionary) == True):
        for key in dictionary:
            # no collisions = one to one relation
            # if 1 points to A, then 2 does not point to A
            # given the dictionary is a function, then it only has one value
            value = dictionary[key]
            for keyNext in dictionary:
                if(keyNext != key and dictionary[keyNext] == value):
                    return False
        return True
                
    else:
        return False

def is_surjective(dictionary):
    # dictionary keys should be 0-9
    # dictionary codomain is 0-9
    # every codomain is being pointed to
    # idea: make a boolean array? and then declare if all are true,
    #                                    then it is surjective?

    boolArray = [False, # 0
                 False, # 1
                 False, # 2
                 False, # 3
                 False, # 4
                 False, # 5
                 False, # 6
                 False, # 7
                 False, # 8
                 False] # 9
    
    if(is_function(dictionary) == True):
        for key1 in dictionary:
            #print 'key for key1:', key1 
            if (key1 not in range(0,10)):
                return False
        for key2 in dictionary:
            try:
                val = dictionary[key2][0]
                #print 'value in key2: ',val
                if(int(val) in range(0,10)):
                    boolArray[val] = True
                #    print boolArray[val] , val
            except:
                print 'error with ',val
        for index in range(0,10):
            #print 'key3: ', index
            #print 'val in boolArray: ',boolArray[index]
            if(True != boolArray[index]):
                #print 'Printing false'
                return False
        return True
    else:
        return False

def is_bijective(dictionary):
    if(is_surjective(dictionary)==True and is_injective(dictionary)==True):
        return True
    else:
        return False


d1 = {1:[0],2:[1],3:[2],4:[3]}
d2 = {1:[0],2:[1],3:[2],4:[2]}
d3 = {0:[0],1:[1],2:[2],3:[3],4:[4],5:[5],6:[6],7:[7],8:[8],9:[9]}

print 'Is the dictionary1 a function? ',is_function(d1)
print 'Is the dictionary1 injective?',is_injective(d1)
print 'Is the dictionary1 surjective?',is_surjective(d1)
print 'Is the dictionary1 bijective?',is_bijective(d1)

print 'Is the dictionary2 a function? ',is_function(d2)
print 'Is the dictionary2 injective?',is_injective(d2)
print 'Is the dictionary2 surjective?',is_surjective(d2)
print 'Is the dictionary2 bijective?',is_bijective(d2)

print 'Is the dictionary3 a function? ',is_function(d3)
print 'Is the dictionary3 injective?',is_injective(d3)
print 'Is the dictionary3 surjective?',is_surjective(d3)
print 'Is the dictionary3 bijective?',is_bijective(d3)



/
