# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def power(n,i,l):
    if 3**i>n:
        return l
    else:
        l.append(3**i)
        i=i+1
        s=power(n,i,l)
    return s
def recursion_powersof3ton(n):
    if n<0:
        return []
    else:
        l=[]
        return power(n,0,l)
