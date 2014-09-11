# Tyson Spoelma
# MTH 325
# Homework 3
# Problem 3

# This program prints out the function H(n)
# where H(n) = n/2 when n is even
# where H(n) = 3n + 1 when n is odd
def problem2(num):
    if num%2==0:
        return(num/2)
    else:
        return(3*num + 1)


def problem2bc(num): 
    list1 = []
    list1.append(num)
    num1 = num
    while(num1!=1):
        num1 = problem2(num1)
        list1.append(num1)
        #print num1
    
    return (list1)

number =raw_input("Type in an integer: ")
integer = int(number)
print '\n'"H(n) = ", problem2(integer)

print '\n',"List of %i, H(%i), H(H(%i)), and so on: " % (integer, integer, integer)
print problem2bc(integer)
